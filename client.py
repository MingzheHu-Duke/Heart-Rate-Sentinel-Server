import requests

print("Add new attending with phone number not string")
new_attending = {"attending_username": "Everett",
                 "attending_email": "Every@outlook.com",
                 "attending_phone": 9191111110}
r = requests.post("http://127.0.0.1:5000/new_attending", json=new_attending)
print(r.status_code)
print(r.text)


print("Add new patient with str age")
new_patient = {"patient_id": 101, "attending_username": "Everett",
               "patient_age": "18"}
r = requests.post("http://127.0.0.1:5000/new_patient", json=new_patient)
print(r.status_code)
print(r.text)