from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

patient_db = list()
attending_db = list()


def init_db():
    #   logging.basicConfig(filename="HR_Sentinel.log", filemode='w',
    #                      level=logging.DEBUG)
    add_patient_to_database(100, "Tom", 23)
    Tom_heart_rate = {"heart_rate": 101,
                      "status": "tachycardic",
                      "timestamp": "2018-03-09 11:00:36"}
    patient_db[0]["heart_rate_history"].append(Tom_heart_rate)
    print(patient_db)
    add_attending_to_database("Tom", "tom@gmail.com", "919-865-5674")


def add_patient_to_database(patient_id=None, attending_username=None,
                            patient_age=None):
    new_patient = {"patient_id": patient_id,
                   "attending_username": attending_username,
                   "patient_age": patient_age,
                   "heart_rate_history": list()}
    patient_db.append(new_patient)
    # logging.info("Added patient {}".format(name))
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


def validate_post_input(in_data, expected_key, expected_types):
    for key, v_type in zip(expected_key, expected_types):
        if key not in in_data.keys():
            return "{} key not found in input".format(key)
        if type(in_data[key]) != v_type:
            return "{} key value has wrong variable type".format(key)
    return True


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
    if info_valid is not True:
        return info_valid + "please make sure all your info are " \
                            "in the type of string!", 400
    add_attending_to_database(attending_username=in_data["attending_username"],
                              attending_email=in_data["attending_email"],
                              attending_phone=in_data["attending_phone"])
    return "Attending successfully added", 200


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
def get_get_results(patient_id):
    answer, server_status = get_test(patient_id)
    # return results
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
    return "Please use an integer or a string of an integer containing an ID number", 400


def id_is_int(patient_id):
    try:
        type(patient_id) in [str, int]
        return True
    except ValueError:
        return False


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


# @app.route("/heart_rate/average/<patient_id>", methods=["GET"]) # YT


# @app.route("/heart_rate/interval_average", methods=["POST"]) #Mingzhe


# @app.route("/patients/<attending_username>", methods=["GET"]) #YT


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
