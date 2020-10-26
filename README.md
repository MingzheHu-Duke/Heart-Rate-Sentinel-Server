## Grants
Thank you Prof.Ward and TA Evan to view and test our programs. We spent whole two weeks to build and optimize 
the server and its relevant documents. We enjoyed the process of cooperatively working in a team as well
as exploring brand new and pracitcal functionalities. Please feel free to provide any feedback or valueable suggestions
to the authors.

Ye Tian & Mingzhe Hu 

10/2020

# Heart Rate Sentinel Server

Heart Rate Sentinel ServerThis server receives GET and POST requests from mock patient heart rate monitors that contain patient heart rate information over time. 
The server will also have routes that allow physicians to register on the server and provide their contact information.

### Server Construction
According to the program specifications from BME-547 assignment instructions, student Ye Tian(NetID: yt149) and Mingzhe Hu
 cooperatively designed, developed and  tested the server.py program using PyCharm. Also, we attached a corresponding client.py for convenience.

### TEAM WORK ASSIGNMENT:

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
   where `<attending_username>` is a string that indicates the attending of 
   which you want to know patients' heart rate information. If the username 
   is invalid, or it can't match any existing patient in current database,
   server will return an error with status code 400; otherwise the server 
   returns a list that contains of dictionaries, each of which is pre-designed
   to state that attending's every patients' latest heart rate, patient id, time tag and
   the condition that if that heart rate shows tachycardic situation.

### Server Usage:
Please follow the general method of using a server to get access to our server's functionalities.
For example, to get the average value of a patient's all heart rate info, please type in `/api/heart_rate/average/<patient_id>`
either in your program or in the browser to connect and use our server program.

### License
[MIT](https://choosealicense.com/licenses/mit/)