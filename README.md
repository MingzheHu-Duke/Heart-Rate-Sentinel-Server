TEAM WORK ASSIGNMENT:
Mingzhe: 
POST /api/new_patient
POST /api/heart_rate
GET /api/heart_rate/<patient_id>
POST /api/heart_rate/interval_average
Ye: 
POST /api/new_attending
GET /api/status/<patient_id>
GET /api/heart_rate/average/<patient_id>
GET /api/patients/<attending_username>


### Routes
* ` POST /new_patient`

  ```python
  {"name": str, "id": int, "blood_type": str}
  ```
  where blood type is one of O+, O-, A+, A-, B+, B-, AB+, AB-.

* `POST /add_test`

  ```python
  {"id": int, "test_name": str, "test_result": int}
  ``` 

* `GET /get_results/<patient_id>`
   
   where `<patient_id>` is an integer: the ID of whichever patient that 
   interested. If the ID is invalid (e.g. not an integer) it returns an
   error to indicate the correct form of URL; if the ID can't match any
   existing patient's ID on the server it returns the searching result;
   otherwise it should returns all the test history of that interested 
   patient.
   
* `GET /compatible/<donor>/<recipient>`
    
    where `<donor>` is the donor id and `<recipient>` is the recipient id.  It
    returns a string of "Compatible" if the donor can safely give blood to the
    recipient.  It returns a string of "Not Compatible" if the donor cannot
    give blood safely to the recipient.
    
    