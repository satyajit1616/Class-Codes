import json

def return_test_data():
    actual_cource = []
    with open("test_json_data.json","r") as json_file:
        json_data = json.load(json_file)

    for k,v in json_data.items():
        if k == 'instructor':
            actual_instructor = v
        if k == 'courses':
            for i in v:
                actual_cource.append(i)

    return actual_instructor,actual_cource

