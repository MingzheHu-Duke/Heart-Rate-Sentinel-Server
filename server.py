from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

db = list()


def init_db():
#   logging.basicConfig(filename="HR_Sentinel.log", filemode='w',
 #                      level=logging.DEBUG)
    add_to_database("Tom",100, 23, "bc@gmail.com", "919600900")

def add_to_database(attending_username, patient_id = None, patient_age = None,
                            attending_email =None, attending_phone = None):
    new_patient = {"patient_id": patient_id,
                   "attending_username": attending_username,
                   "patient_age": patient_age,
                   "attending_email": attending_email,
                   "attending_phone": attending_phone,
                   "heart_rate_history": list()}
    db.append(new_patient)
   #logging.info("Added patient {}".format(name))
    print(db)


# @app.route("/new_patient", methods=["POST"])   # Mingzhe


@app.route("/new_attending", methods=["POST"]) # YT
def post_new_attending():
    in_data = request.get_json()
    answer, server_status = process_new_attending(in_data)
    return answer, server_status


def process_new_attending(in_data):
    expected_key = ["attending_username", "attending_email", "attending_phone"]
    expected_types = [str, str, str]
    validate_input = validate_post_input(in_data, expected_key, expected_types)
    if validate_input is not True:
        return validate_input, 400
    info_valid = attending_info_detect(in_data)
    if info_valid is not True:
        return info_valid, 400
    add_to_database(attending_username = in_data["attending_username"],
                    attending_email = in_data["attending_email"],
                    attending_phone = in_data["attending_phone"])
    return "Attending successfully added", 200


def validate_post_input(in_data, expected_key, expected_types):
    for key, v_type in zip(expected_key, expected_types):
        if key not in in_data.keys():
            return "{} key not found in input".format(key)
        if type(in_data["attending_phone"]) == int:
            in_data["attending_phone"] = str(in_data["attending_phone"])
        if type(in_data[key]) != v_type:
            return "{} key value has the wrong variable type. " \
                   "It should be a string".format(key)
    return True


def attending_info_detect(in_data):
    good_email = "@" in in_data["attending_email"]
    if good_email != True:
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
    app.run()