from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

patient_db = list()
attending_db = list()


def init_db():
    #   logging.basicConfig(filename="HR_Sentinel.log", filemode='w',
    #                      level=logging.DEBUG)
    add_patient_to_database(100, "Tom", 23)
    add_attending_to_database("Tom", "tom@gmail.com", "919-865-5674")


def add_patient_to_database(patient_id=None, attending_username=None,
                            patient_age=None):
    new_patient = {"patient_id": patient_id,
                   "attending_username": attending_username,
                   "patient_age": patient_age,
                   "heart_rate_history": list()}
    patient_db.append(new_patient)
    # logging.info("Added patient {}".format(name))
    print(patient_db)


def add_attending_to_database(attending_username, attending_email=None,
                              attending_phone=None):
    new_attending = {"attending_username": attending_username,
                     "attending_email": attending_email,
                     "attending_phone": attending_phone}
    attending_db.append(new_attending)
    # logging.info("Added patient {}".format(name))
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
    parse_phone(in_data, validate_input)
    info_valid = attending_info_detect(in_data)
    if info_valid is not True:
        return info_valid, 400
    add_attending_to_database(attending_username=in_data["attending_username"],
                              attending_email=in_data["attending_email"],
                              attending_phone=in_data["attending_phone"])
    return "Attending successfully added", 200


def parse_phone(in_data, validate_input):
    if validate_input is not True:
        if type(in_data["attending_phone"]) == int:
            in_data["attending_phone"] = str(in_data["attending_phone"])
        else:
            return validate_input, 400


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


# @app.route("/status/<patient_id>", methods=["GET"]) #YT


# @app.route("/heart_rate/<patient_id>", methods=["GET"]) #Mingzhe


# @app.route("/heart_rate/average/<patient_id>", methods=["GET"]) # YT


# @app.route("/heart_rate/interval_average", methods=["POST"]) #Mingzhe


# @app.route("/patients/<attending_username>", methods=["GET"]) #YT


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
