import requests
from server import init_db
print("\n")


print("Add an attending with his phone number is not string")
# should be 400
new_attending = {"attending_username": "Everett",
                 "attending_email": "Every@outlook.com",
                 "attending_phone": 9191111110}
r = requests.post("http://127.0.0.1:5000/api/new_attending",
                  json=new_attending)
print(r.status_code)
print(r.text)
print("\n")


print("Add an attending with his phone number is correct string")
# should be 400
new_attending = {"attending_username": "Everett",
                 "attending_email": "Every@outlook.com",
                 "attending_phone": "919-1111-110"}
r = requests.post("http://127.0.0.1:5000/api/new_attending",
                  json=new_attending)
print(r.status_code)
print(r.text)
print("\n")


print("Add new patient 101 with str age")
# Should be 200
new_patient = {"patient_id": 101, "attending_username": "Everett",
               "patient_age": "18"}
r = requests.post("http://127.0.0.1:5000/api/new_patient", json=new_patient)
print(r.status_code)
print(r.text)
print("\n")


print("Add an good attending with correct info type")
# should be 200
new_attending = {"attending_username": "Trump",
                 "attending_email": "DTrump@whitehouse.com",
                 "attending_phone": "100000000"}
r = requests.post("http://127.0.0.1:5000/api/new_attending",
                  json=new_attending)
print(r.status_code)
print(r.text)
print("\n")


print("Add an existed attending though correct info type")
# should be 400
new_attending = {"attending_username": "Trump",
                 "attending_email": "whatever",
                 "attending_phone": "whatever"}
r = requests.post("http://127.0.0.1:5000/api/new_attending",
                  json=new_attending)
print(r.status_code)
print(r.text)
print("\n")


print("Get the heart rate info from ID:10 which doesn't exist")
# should be 400
id = "10"
r = requests.get("http://127.0.0.1:5000/api/status/" + id)
print(r.status_code)
print(r.text)
print("\n")


print("Get patient 120 's latest heart rate info")
# status code should be 200
id = "120"
r = requests.get("http://127.0.0.1:5000/api/status/" + id)
print(r.status_code)
print(r.text)
print("\n")


print("Get patient 500's latest heart rate info, which is empty")
# should be 400
id = "500"
r = requests.get("http://127.0.0.1:5000/api/status/" + id)
print(r.status_code)
print(r.text)
print("\n")


print("Get patient 120 's average heart rate (101+104)/2")
# should be 200
id = "120"
r = requests.get("http://127.0.0.1:5000/api/heart_rate/average/" + id)
print(r.status_code)
print(r.text)
print("\n")
#
#
print("Get a non-existing attending Flora's all patient info list")
# should be 400
attending_username = "Flora"
r = requests.get("http://127.0.0.1:5000/api/patients/" + attending_username)
print(r.status_code)
print(r.text)
print("\n")
#
#
print("Get a invalid attending name Flora666's all patient info list")
# should be 400
attending_username = 'Flora666'
r = requests.get("http://127.0.0.1:5000/api/patients/" + attending_username)
print(r.status_code)
print(r.text)
print("\n")
#

#
print("Get attending Tom's all patient info list")
# should be 200
attending_username = "Tom"
r = requests.get("http://127.0.0.1:5000/api/patients/" + attending_username)
print(r.status_code)
print(r.text)
print("\n")


print("Post heart rate to a patient 101, tachycardic")
# Should be 200
new_patient = {"patient_id": 101, "heart_rate": 101}
r = requests.post("http://127.0.0.1:5000/api/heart_rate", json=new_patient)
print(r.status_code)
print(r.text)
print("\n")


print("Post heart rate to a patient 101, not tachycardic")
# Should be 200
new_patient = {"patient_id": 101, "heart_rate": 99}
r = requests.post("http://127.0.0.1:5000/api/heart_rate", json=new_patient)
print(r.status_code)
print(r.text)
print("\n")


print("Get patient 101's heart rate history list")
# should be 200
patient_id = "101"
r = requests.get("http://127.0.0.1:5000/api/heart_rate/" + patient_id)
print(r.status_code)
print(r.text)
print("\n")


print("Find an average heart rate")
# Should be 200
patient_timesince = {"patient_id": 101,
                     "heart_rate_average_since": "2020-10-22 15:16:42"}
r = requests.post("http://127.0.0.1:5000/api/heart_rate/interval_average",
                  json=patient_timesince)
print(r.status_code)
print(r.text)
