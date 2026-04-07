from flask import Flask,redirect,url_for,render_template,request,jsonify,session  # Import core Flask modules for routing, templates, requests, JSON responses, and session handling
import sqlite3  # Used to connect and interact with SQLite database
from werkzeug.security import generate_password_hash,check_password_hash  # Used to hash passwords securely and verify them
from datetime import timedelta  # Used to define token expiration duration
import secrets  # (Not used here) Typically used for generating secure random tokens
from flask_jwt_extended import (JWTManager,
                                create_access_token,
                                jwt_required,
                                get_jwt_identity)  # JWT utilities for authentication and authorization


app = Flask(__name__)  # Create Flask application instance
app.secret_key = "supersecretkey-change-this"  # Secret key for session encryption (used by Flask sessions)

#----------------
#JWT Config
#-----------------
app.config["JWT_SECRET_KEY"]= "jwt-super-secret-chge-this"  # Secret key used to sign JWT tokens
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)  # Set JWT token expiry time (1 hour)

jwt = JWTManager(app)  # Initialize JWT manager with Flask app


DATABASE = "users.db"  # Database file name


#----------------
# DATABASE SETUP
#----------------

def init_db():
    conn =sqlite3.connect(DATABASE)  # Connect to SQLite database
    cursor = conn.cursor()  # Create cursor object to execute SQL queries

    cursor.execute("""  
    CREATE TABLE IF NOT EXISTS users (  
    id INTEGER PRIMARY KEY AUTOINCREMENT,  # Unique ID for each user (auto-incremented)
    first_name TEXT NOT NULL,  # User's first name (required)
    last_name TEXT NOT NULL,  # User's last name (required)
    email TEXT NOT NULL,  # User email (required, should be unique ideally)
    phone TEXT NOT NULL,  # User phone number
    role TEXT NOT NULL,  # User role (e.g., admin, user)
    password TEXT NOT NULL)""")  # Stores hashed password

    conn.commit()  # Save changes to database
    conn.close()  # Close database connection


def get_db_connection():
    conn =sqlite3.connect(DATABASE)  # Open database connection
    conn.row_factory = sqlite3.Row  # Allows accessing columns by name instead of index
    return conn  # Return connection object




#-------------------------
# FRONTEND ROUTES
#-------------------------

@app.route("/")
def home():
    return redirect(url_for("signup_page"))  # Redirect root URL to signup page

@app.route("/signup",methods=["GET"])
def signup_page():
    return render_template("signup.html")  # Render signup HTML page

@app.route("/login",methods=["GET"])
def login_page():
    return render_template("login.html")  # Render login HTML page

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")  # Render dashboard page


#-------------------------------
#API ROUTES
#-------------------------------

@app.route("/api/signup",methods=["POST"])
def signup():
    data = request.form if request.form else request.get_json()  # Accept form data or JSON input

    first_name = data.get("first_name").strip()  # Get and clean first name
    last_name = data.get("last_name").strip()  # Get and clean last name
    email = data.get("email").strip()  # Get and clean email
    phone = data.get("phone").strip()  # Get and clean phone
    role = data.get("role").strip()  # Get and clean role
    password = data.get("password").strip()  # Get and clean password
    confirm_password = data.get("confirm_password")  # Get confirm password


    #validation
    if not all([first_name,last_name,email,phone,role,password,confirm_password]):
        return jsonify({"message ":"All Fields are requied"})  # Ensure all fields are filled

    if password != confirm_password:
        return jsonify({"message ":"Passwords do not match"})  # Check password confirmation

    hashed_password = generate_password_hash(password)  # Hash password before storing

    try:
        conn = sqlite3.connect(DATABASE)  # Connect to database
        cursor = conn.cursor()  # Create cursor
        cursor.execute("""  
            INSERT INTO users (first_name,last_name,email,phone,role,password)  
            VALUES (?,?,?,?,?,?)  
            """,(first_name,last_name,email,phone,role,hashed_password))  # Insert new user record
        conn.commit()  # Save changes
        conn.close()  # Close connection

        return redirect(url_for("login_page"))  # Redirect to login page after signup

    except sqlite3.IntegrityError:
        return jsonify({"message ":"Email already exists"})  # Handle duplicate email error

    except Exception as e:
        return jsonify({"message ":str(e)})  # Catch any unexpected error

@app.route("/api/users",methods=["GET"])
def get_users():
    conn = get_db_connection()  # Get DB connection
    users = conn.execute("SELECT * FROM users").fetchall()  # Fetch all users
    conn.close()  # Close connection

    user_list = [dict(i) for i in users]  # Convert rows to dictionary format
    return jsonify(user_list),200  # Return users as JSON response


#------------------------------------
#Login API with JWT Token
#------------------------------------
@app.route("/api/login",methods=["POST"])
def login():
    data = request.form if request.form else request.get_json()  # Accept form or JSON input

    email = data.get("email").strip()  # Get email
    password = data.get("password").strip()  # Get password

    if not email or not password:
        return jsonify({"message ":"Email or password are required"})  # Validate input

    conn = get_db_connection()  # Connect to DB
    user = conn.execute("SELECT * FROM users WHERE email = ?",(email,)).fetchone()  # Fetch user by email
    conn.close()  # Close connection

    if user and check_password_hash(user["password"],password):  # Verify user exists and password matches
        session["user_email"] = email  # Store user email in session (for session-based tracking)

        access_token = create_access_token(identity=email,  # Create JWT token with user identity
                                           additional_claims={
                                               "role":user["role"],"token_type":"user_jwt"  # Add extra info to token
                                           })

        return jsonify({
            "message":"Login Successful",  # Success message
            "access_token":access_token,  # Return JWT token
            "token_type":"Bearer",  # Token type for authorization header
            "redirect_url":"/dashboard"  # Frontend redirect after login
        })

    return jsonify({"message ":"Invalid credentials"}),401  # Return error if login fails


if __name__ == "__main__":
    init_db()  # Initialize database (create table if not exists)
    app.run(debug=True)  # Run Flask app in debug mode