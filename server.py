from flask import Flask, jsonify, request
import logging
import numpy as np
import json

app = Flask(__name__)

patient_db = list()
attending_db = list()


def init_db():
    logging.basicConfig(filename="HR_Sentinel.log", filemode='w',
                         level=logging.DEBUG)
    add_patient_to_database(100, "Tom", 23)                      #patient id 100, corresponding to attending Tom
    patient101_heart_rate1 = {"heart_rate": 101,
                      "status": "tachycardic",
                      "timestamp": "2018-03-09 11:00:36"}
    patient101_heart_rate2 = {"heart_rate": 104,
                       "status": "tachycardic",
                       "timestamp": "2018-03-10 11:00:36"}
    patient_db[0]["heart_rate_history"].append(patient101_heart_rate1)
    patient_db[0]["heart_rate_history"].append(patient101_heart_rate2)

    add_patient_to_database(200, "Tom", 99)                       #patient id 200, corresponding to attending Tom
    patient200_heart_rate1 = {"heart_rate": 75,
                       "status": "not tachycardic",
                       "timestamp": "2019-10-10 11:00:36"}
    patient_db[1]["heart_rate_history"].append(patient200_heart_rate1)

    add_attending_to_database("Tom", "tom@gmail.com", "919-865-5674")


def add_patient_to_database(patient_id=None, attending_username=None,
                            patient_age=None):
    new_patient = {"patient_id": patient_id,
                   "attending_username": attending_username,
                   "patient_age": patient_age,
                   "heart_rate_history": list()}
    patient_db.append(new_patient)
    logging.info("Added patient id: {}".format(patient_id))
    print("patient database:\r")
    print(patient_db)


def add_attending_to_database(attending_username, attending_email=None,
                              attending_phone=None):
    new_attending = {"attending_username": attending_username,
                     "attending_email": attending_email,
                     "attending_phone": attending_phone}
    attending_db.append(new_attending)
    # logging.info("Added patient {}".format(name))
    print("attending database:\r")
    print(attending_db)


@app.route("/new_patient", methods=["POST"])
def post_new_patient():
    # Receive request data
    in_data = request.get_json()
    # Call functions
    answer, server_status = process_new_patient(in_data)
    # Return results
    return answer, server_status


def process_new_patient(in_data):
    expected_key = ["patient_id", "attending_username", "patient_age"]
    expected_types = [int, str, int]
    if type(in_data["patient_id"]) == str:
        in_data["patient_id"] = parse_string(in_data["patient_id"])
    if type(in_data["patient_age"]) == str:
        in_data["patient_age"] = parse_string(in_data["patient_age"])
    validate_input = validate_post_input(in_data, expected_key, expected_types)
    valid_age = validate_age(in_data["patient_age"])
    if validate_input is not True:
        return validate_input, 400
    if valid_age is not True:
        return valid_age, 400
    add_patient_to_database(in_data["patient_id"],
                            in_data["attending_username"],
                            in_data["patient_age"])
    return "Patient successfully added", 200


def validate_age(age):
    if age <= 0:
        return "Invalid age, must be greater than 0!"
    if age >= 150:
        return "Invalid age, human can't live so long!"
    else:
        return True


def parse_string(a_string):
    if a_string.isdigit() is True:
        return int(a_string)
    else:
        return a_string


@app.route("/new_attending", methods=["POST"])  # YT
def post_new_attending():
    in_data = request.get_json()
    answer, server_status = process_new_attending(in_data)
    return answer, server_status


def process_new_attending(in_data):
    expected_key = ["attending_username", "attending_email", "attending_phone"]
    expected_types = [str, str, str]
    validate_input = validate_post_input(in_data, expected_key, expected_types)
    if validate_input is not True:
        return validate_input + ", please make sure all your info are " \
                            "in the type of string!", 400
    info_valid = attending_info_detect(in_data)
    attending_exist = if_attending_exist(in_data)
    if attending_exist is not False:
        return attending_exist + "Please create a nonredundante username to" \
                                 "write a new attending into database", 400
    if info_valid is not True:
        return info_valid + "please make sure you've entered correct info!", 400
    add_attending_to_database(attending_username=in_data["attending_username"],
                              attending_email=in_data["attending_email"],
                              attending_phone=in_data["attending_phone"])
    return "Attending:'{}' successfully added".format(in_data["attending_username"]), 200


def if_attending_exist(in_data):
    attending_username_list = []
    for attending in attending_db:
        attending_username_list.append(attending["attending_username"])
    if in_data["attending_username"] in attending_username_list:
        return "The attending already exists in database! "
    return False


def validate_post_input(in_data, expected_key, expected_types):
    for key, v_type in zip(expected_key, expected_types):
        if key not in in_data.keys():
            return "{} key not found in input".format(key)
        if type(in_data[key]) != v_type:
            return "{} key value has wrong variable type".format(key)
    return True


def attending_info_detect(in_data):
    good_email = "@" in in_data["attending_email"]
    if good_email is not True:
        return "You entered a invalid email address"
    return True


# @app.route("/heart_rate", methods=["POST"]) #Mingzhe
#这里注意，保存heart_rate一定要保存成int, 无论input是str 还是 int
#然后保存的时候每一次heart_rate是一个单独的dictionary，这个dictionary至少要有以下三个key+value pair
#                       {"heart_rate": 101,
#                      "status": "tachycardic" | "not tachycardic",
 #                     "timestamp": "2018-03-09 11:00:36"}
#这样我后面才能用

@app.route("/status/<patient_id>", methods=["GET"]) #YT
def get_latest_result(patient_id):
    answer, server_status = get_test(patient_id)
    return answer, server_status


def get_test(patient_id):
    int_id = id_is_int(patient_id)
    if int_id is True:
        patient = find_id(patient_id)
        if patient is False:
            return "Could not find a matched patient in database", 400
        have_latest_hr = latest_hr(patient)
        if have_latest_hr == False:
           return "This patient doesn't have any heart rate history", 400
        return jsonify(have_latest_hr), 200
    return int_id, 400


def id_is_int(patient_id):
    try:
        int(patient_id)
        return True
    except ValueError:
        return "Please use an integer or a numeric string containing " \
           "an ID number but without any letter"


def find_id(patient_id):
    for patient in patient_db:
        if patient["patient_id"] == int(patient_id):
            return patient
        return False


def latest_hr(patient):
    if len(patient["heart_rate_history"]) == 0:
        return False
    latest_heart_rate = {"heart_rate": patient["heart_rate_history"][-1]["heart_rate"],
                         "status": patient["heart_rate_history"][-1]["status"],
                         "timestamp": patient["heart_rate_history"][-1]["timestamp"]}
    return latest_heart_rate


# @app.route("/heart_rate/<patient_id>", methods=["GET"]) #Mingzhe


@app.route("/heart_rate/average/<patient_id>", methods=["GET"]) # YT
def get_average_results(patient_id):
    answer, server_status = get_average(patient_id)
    return answer, server_status


def get_average(patient_id):
    int_id = id_is_int(patient_id) # function id_is_int() has been defined in Route /status/<patient_id>
    if int_id is True:
        patient = find_id(patient_id)  # function find_id() has been defined in Route /status/<patient_id>
        if patient is False:
            return "Could not find a matched patient in database", 400
        have_average_hr =average_hr(patient)
        if have_average_hr == False:
           return "This patient doesn't have any heart rate history", 400
        return jsonify(have_average_hr), 200
    return "Please use an integer or a numeric string containing " \
           "an ID number but without any letter", 400


def average_hr(patient):
    if len(patient["heart_rate_history"]) == 0:
        return False
    hr_list = []
    for single_hr in patient["heart_rate_history"]:
        hr_list.append(single_hr["heart_rate"])
    avg_hr = int(np.mean(hr_list))
    return avg_hr

# @app.route("/heart_rate/interval_average", methods=["POST"]) #Mingzhe


@app.route("/patients/<attending_username>", methods=["GET"]) #YT
def get_all_patients(attending_username):
    answer, server_status = all_patients(attending_username)
    return answer, server_status


def all_patients(attending_username):
    if_str_username = str_username(attending_username)
    if if_str_username is True:
        if_username_match = match_username(attending_username)
        if if_username_match == True:
            all_patients_data = return_data_list(attending_username)
#           return jsonify({"Attending {}'s all patients' info:".format(attending_username):
#                                all_patients_data}), 200
            return json.dumps(all_patients_data), 200
        return if_username_match, 400
    return if_str_username, 400


def str_username(attending_username):
    import re
    if bool(re.search(r'\d', attending_username)) == False:
        return True
    else:
        return "Please enter a valid username string with no numbers!"


def match_username(attending_username):
    patients_attending_list = []
    for patient in patient_db:
        patients_attending_list.append(patient["attending_username"])
    if attending_username not in patients_attending_list:
        return "Sorry, this physician attending doesn't have any " \
               "matched patient in the database"
    return True


def return_data_list(attending_username):
    data_list = []
    for patient in patient_db:
        if patient["attending_username"] == attending_username:
            dic = {"patient_id": patient["patient_id"],
                   "last_heart_rate": patient["heart_rate_history"][-1]["heart_rate"],
                   "last_time": patient["heart_rate_history"][-1]["timestamp"],
                   "status": patient["heart_rate_history"][-1]["status"]}
            data_list.append(dic)
    return data_list


if __name__ == '__main__':
    print("running")
    init_db()
    app.run(debug=True)
