import requests

print("Add an attending with his phone number is not string")                  # should be 400
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


print("Add an good attending with correct info type")                        # should be 200
new_attending = {"attending_username": "Trump",
                 "attending_email": "DTrump@whitehouse.com",
                 "attending_phone": "100000000"}
r = requests.post("http://127.0.0.1:5000/new_attending", json=new_attending)
print(r.status_code)
print(r.text)


print("Get Tom's latest heart rate info")                        # should be 200
id = "100"
r = requests.get("http://127.0.0.1:5000/status/" + id)
print(r.status_code)
print(r.text)


print("Get the heart rate info from ID:10 which doesn't exist")                        # should be 400
id = "10"
r = requests.get("http://127.0.0.1:5000/status/" + id)
print(r.status_code)
print(r.text)


print("Get Tom's average heart rate (101+104)/2")                        # should be 200
id = "100"
r = requests.get("http://127.0.0.1:5000/heart_rate/average/" + id)
print(r.status_code)
print(r.text)