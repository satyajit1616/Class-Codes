from flask import Flask,redirect,url_for,render_template,request,jsonify,session
import sqlite3
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import timedelta
import secrets
from flask_jwt_extended import (JWTManager,
                                create_access_token,
                                jwt_required,
                                get_jwt_identity)


app = Flask(__name__)
app.secret_key = "supersecretkey-change-this"

#----------------
#JWT Config
#-----------------
app.config["JWT_SECRET_KEY"]= "jwt-super-secret-chge-this"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

jwt = JWTManager(app)


DATABASE = "users.db"


#----------------
# DATABASE SETUP
#----------------

def init_db():
    conn =sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    role TEXT NOT NULL,
    password TEXT NOT NULL)""")

    conn.commit()
    conn.close()


def get_db_connection():
    conn =sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn




#-------------------------
# FRONTEND ROUTES
#-------------------------

@app.route("/")
def home():
    return redirect(url_for("signup_page"))

@app.route("/signup",methods=["GET"])
def signup_page():
    return render_template("signup.html")

@app.route("/login",methods=["GET"])
def login_page():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


#-------------------------------
#API ROUTES
#-------------------------------

@app.route("/api/signup",methods=["POST"])
def signup():
    data = request.form if request.form else request.get_json()

    first_name = data.get("first_name").strip()
    last_name = data.get("last_name").strip()
    email = data.get("email").strip()
    phone = data.get("phone").strip()
    role = data.get("role").strip()
    password = data.get("password").strip()
    confirm_password = data.get("confirm_password")


    #validation
    if not all([first_name,last_name,email,phone,role,password,confirm_password]):
        return jsonify({"message ":"All Fields are requied"})

    if password != confirm_password:
        return jsonify({"message ":"Passwords do not match"})

    hashed_password = generate_password_hash(password)

    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (first_name,last_name,email,phone,role,password) 
            VALUES (?,?,?,?,?,?)
            """,(first_name,last_name,email,phone,role,hashed_password))
        conn.commit()
        conn.close()

        return redirect(url_for("login_page"))

    except sqlite3.IntegrityError:
        return jsonify({"message ":"Email already exists"})

    except Exception as e:
        return jsonify({"message ":str(e)})

@app.route("/api/users",methods=["GET"])
def get_users():
    conn = get_db_connection()
    users = conn.execute("SELECT * FROM users").fetchall()
    conn.close()

    user_list = [dict(i) for i in users]
    return jsonify(user_list),200


#------------------------------------
#Login API with JWT Token
#------------------------------------
@app.route("/api/login",methods=["POST"])
def login():
    data = request.form if request.form else request.get_json()

    email = data.get("email").strip()
    password = data.get("password").strip()

    if not email or not password:
        return jsonify({"message ":"Email or password are required"})

    conn = get_db_connection()
    user = conn.execute("SELECT * FROM users WHERE email = ?",(email,)).fetchone()
    conn.close()

    if user and check_password_hash(user["password"],password):
        session["user_email"] = email

        access_token = create_access_token(identity=email,
                                           additional_claims={
                                               "role":user["role"],"token_type":"user_jwt"
                                           })

        return jsonify({
            "message":"Login Successful",
            "access_token":access_token,
            "token_type":"Bearer",
            "redirect_url":"/dashboard"
        })

    return jsonify({"message ":"Invalid credentials"}),401


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
