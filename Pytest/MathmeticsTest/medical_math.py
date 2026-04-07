def calculate_bmi(weight, height):
    if weight <=0 and height<=0:
        raise ValueError("weight and height cannot be negative")
    return round(weight / (height **2), 2)


def is_fever(temp_celcius):
    return temp_celcius >= 38.0

