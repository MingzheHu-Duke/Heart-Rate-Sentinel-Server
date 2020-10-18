import requests

print("Add new attending with good inputs")
new_attending = {"attending_username": "Everett", "attending_email": "Every@outlook.com", "attending_phone": 919111111}
r = requests.post("http://127.0.0.1:5000/new_attending", json=new_attending)
print(r.status_code)
print(r.text)