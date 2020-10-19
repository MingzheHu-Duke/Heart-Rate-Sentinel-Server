###TEAM WORK ASSIGNMENT:
Mingzhe: 
*`POST /api/new_patient`
*`POST /api/heart_rate`
*`GET /api/heart_rate/<patient_id>`
*`POST /api/heart_rate/interval_average`


Ye:

*`POST /api/new_attending`
   ```python
  {"attending_usename": str, 
  "attending_email": str, 
  "attending_phone": str}
  ``` 

*`GET /api/status/<patient_id>`

   where `<patient_id>` is an integer: the ID of whichever patient that 
   interested. If the ID is invalid (e.g. not an integer or a numeric 
   string) it returns an error to indicate the correct form of URL; 
   if the ID can't match any existing patient's ID on the server it 
   returns the searching result; otherwise it should returns all the 
   test history of that interested patient.

*`GET /api/heart_rate/average/<patient_id>`
   where `<patient_id>` is an integer: the ID of whichever patient that 
   interested. If the ID is invalid (e.g. not an integer or a numeric 
   string) it returns an error to indicate the correct form of URL; 
   if the ID can't match any existing patient's ID on the server it 
   returns the searching result; otherwise it should returns the 
   average average heart rate, as an integer, of all measurements you 
   have stored for this patient.
   It should be noticed that in your console the first number you see
   is the server status code(e.g. 200) and then the next number is
   the result of average heart rate.

*`GET /api/patients/<attending_username>`
