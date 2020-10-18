from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

db = list()


def init_db():
    logging.basicConfig(filename="HR_Sentinel.log", filemode='w',
                        level=logging.DEBUG)

# @app.route("/new_patient", methods=["POST"])   # Mingzhe


# @app.route("/new_attending", methods=["POST"]) # YT


# @app.route("/heart_rate", methods=["POST"]) #Mingzhe


# @app.route("/status/<patient_id>", methods=["GET"]) #YT


# @app.route("/heart_rate/<patient_id>", methods=["GET"]) #Mingzhe


# @app.route("/heart_rate/average/<patient_id>", methods=["GET"]) # YT


# @app.route("/heart_rate/interval_average", methods=["POST"]) #Mingzhe


# @app.route("/patients/<attending_username>", methods=["GET"]) #YT


if __name__ == '__main__':
    init_db()
#    app.run()