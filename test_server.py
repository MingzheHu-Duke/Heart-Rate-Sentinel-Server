from server import patient_db, attending_db
import pytest


def test_process_new_attending():
    from server import process_new_attending
    in_data1 = {"attending_username": "Everett",
                "attending_email": "Every@outlook.com",
                "attending_phone": 919-1111-110}
    result1 = process_new_attending(in_data1)
    expected1 = "attending_phone key value has wrong variable type, " \
                "please make sure all your info are in the type of " \
                "string!", 400
    assert result1 == expected1

    in_data2 = {"name": "Everett",
                "attending_email": "Every@outlook.com",
                "attending_phone": "919 - 1111 - 110"}
    result2 = process_new_attending(in_data2)
    expected2 = "attending_username key not found in input, " \
                "please make sure all your info are in the type of " \
                "string!", 400
    assert result2 == expected2

    in_data3 = {"attending_username": "Everett",
                "attending_email": "Every@outlook.com",
                "attending_phone": "919 - 1111 - 110"}
    result3 = process_new_attending(in_data3)
    expected3 = "Attending:'Everett' successfully added", 200
    assert result3 == expected3

    in_data4 = {"attending_username": "Everett",
                "attending_email": "Ev@.com",
                "attending_phone": "666"}
    result4 = process_new_attending(in_data4)
    expected4 = "The attending already exists in database! Please " \
                "create a non redundant username to write a new " \
                "attending into database", 400
    assert result4 == expected4

    in_data5 = {"attending_username": "Aby",
                "attending_email": "Aby.com",
                "attending_phone": "666666"}
    result5 = process_new_attending(in_data5)
    expected5 = "You entered a invalid email address, please " \
                "make sure you've entered correct info", 400
    assert result5 == expected5


def test_if_attending_exist():
    from server import if_attending_exist
    in_data = {"attending_username": "Everett",
               "attending_email": "Evy.com",
               "attending_phone": "666666"}
    result = if_attending_exist(in_data)
    expected = "The attending already exists in database! "
    assert result == expected


def test_validate_post_input():
    from server import validate_post_input
    expected_key = ["patient_id", "attending_username", "patient_age"]
    expected_types = [int, str, int]

    in_data1 = {"patient_id": "110",
                "attending_username": "Kobe",
                "patient_age": 99}
    expected1 = "patient_id key value has wrong variable type"
    result1 = validate_post_input(in_data1, expected_key, expected_types)
    assert result1 == expected1

    in_data2 = {"id": "110",
                "attending_username": "Kobe",
                "patient_age": 99}
    expected2 = "patient_id key not found in input"
    result2 = validate_post_input(in_data2, expected_key, expected_types)
    assert result2 == expected2


def test_attending_info_detect():
    from server import attending_info_detect
    in_data = {"attending_username": "Everett",
               "attending_email": "Evy.com",
               "attending_phone": "666666"}
    expected = "You entered a invalid email address, "
    result = attending_info_detect(in_data)
    assert result == expected


def test_get_test():
    from server import get_test

    patient_id1 = 500
    expected1 = "This patient doesn't have any heart rate history", 400
    result1 = get_test(patient_id1)
    assert result1 == expected1

    patient_id2 = 50000
    expected2 = "Could not find a matched patient in database", 400
    result2 = get_test(patient_id2)
    assert expected2 == result2

    patient_id3 = "120abcde"
    expected3 = "Please use an integer or a numeric string containing " \
                "an ID number but without any letter", 400
    result3 = get_test(patient_id3)
    assert expected3 == result3


def test_id_is_int():
    from server import id_is_int

    id1 = 10000
    expected1 = True
    result1 = id_is_int(id1)
    assert result1 == expected1

    id2 = "10000abc"
    expected2 = "Please use an integer or a numeric string containing " \
                "an ID number but without any letter"
    result2 = id_is_int(id2)
    assert result2 == expected2


def test_latest_hr():
    from server import latest_hr

    patient1 = {'patient_id': 111111, 'attending_username': 'abcde',
                'patient_age': 999,
                'heart_rate_history': [{'heart_rate': 0.0001,
                                        'status': 'not tachycardic',
                                        'timestamp': '2099-13-13 11:00:36'},
                                       {'heart_rate': 0.01,
                                        'status': 'not tachycardic',
                                        'timestamp': '2059-13-13 11:00:36'}]}
    expected1 = {"heart_rate": 0.01,
                 "status": 'not tachycardic',
                 "timestamp": '2059-13-13 11:00:36'}
    result1 = latest_hr(patient1)
    assert result1 == expected1

    patient2 = {'patient_id': 222222, 'attending_username': 'lol',
                'patient_age': 666,
                'heart_rate_history': []}
    expected2 = False
    result2 = latest_hr(patient2)
    assert result2 == expected2


# def test_get_heart_rate_list()


def test_get_average():
    from server import get_average

    patient_id1 = "666hahaha"
    expected1 = "Please use an integer or a numeric string containing " \
                "an ID number but without any letter", 400
    result1 = get_average(patient_id1)
    assert result1 == expected1

    patient_id2 = 666
    expected2 = "Could not find a matched patient in database", 400
    result2 = get_average(patient_id2)
    assert result2 == expected2

    patient_id3 = 500
    expected3 = "This patient doesn't have any heart rate history", 400
    result3 = get_average(patient_id3)
    assert result3 == expected3


def test_average_hr():
    from server import average_hr

    patient1 = {'patient_id': 222222, 'attending_username': 'lol',
                'patient_age': 666,
                'heart_rate_history': []}
    expected1 = False
    result1 = average_hr(patient1)
    assert result1 == expected1

    patient2 = {'patient_id': 111111, 'attending_username': 'abcde',
                'patient_age': 999,
                'heart_rate_history': [{'heart_rate': 50,
                                        'status': 'not tachycardic',
                                        'timestamp': '2099-13-13 11:00:36'},
                                       {'heart_rate': 70,
                                        'status': 'not tachycardic',
                                        'timestamp': '2059-13-13 11:00:36'}]}
    expected2 = 60
    result2 = average_hr(patient2)
    assert result2 == expected2


def test_all_patients():
    from server import all_patients

    attending_name1 = "hahaha666"
    expected1 = "Please enter a valid username string " \
                "with no numbers!", 400
    result1 = all_patients(attending_name1)
    assert result1 == expected1

    attending_name2 = "Jerry"
    expected2 = "Sorry, this physician attending doesn't have any " \
                "matched patient in the database", 400
    result2 = all_patients(attending_name2)
    assert result2 == expected2


def test_str_username():
    from server import str_username

    name1 = "good"
    expected1 = True
    result1 = str_username(name1)
    assert result1 == expected1

    name2 = "bad2name"
    expected2 = "Please enter a valid username string with no numbers!"
    result2 = str_username(name2)
    assert result2 == expected2


def test_match_username():
    from server import match_username

    name1 = "Tom"
    expected1 = True
    result1 = match_username(name1)
    assert result1 == expected1

    name2 = "Jerry"
    expected2 = "Sorry, this physician attending doesn't have any " \
                "matched patient in the database"
    result2 = match_username(name2)
    assert result2 == expected2


def test_return_data_list():
    from server import return_data_list

    attending_name = "Tom"
    expected = [{"patient_id": 120,
                 "last_heart_rate": 104,
                 "last_time": "2018-03-10 11:00:36",
                 "status": "tachycardic"},
                {"patient_id": 300,
                 "last_heart_rate": 75,
                 "last_time": "2019-10-10 11:00:36",
                 "status": "not tachycardic"},
                {"patient_id": 500,
                 "last_heart_rate": "No heart rate available"}]
    result = return_data_list(attending_name)
    assert result == expected


def test_init_db():
    from server import init_db
    answer1, answer2 = init_db()
    expected1 = [{'patient_id': 120, 'attending_username': 'Tom',
                  'patient_age': 23,
                  'heart_rate_history': [{'heart_rate': 101,
                                          'status': 'tachycardic',
                                          'timestamp': '2018-03-09 11:00:36'},
                                         {'heart_rate': 104,
                                          'status': 'tachycardic',
                                          'timestamp':
                                              '2018-03-10 11:00:36'}]},
                 {'patient_id': 300, 'attending_username': 'Tom',
                  'patient_age': 25,
                  'heart_rate_history': [{'heart_rate': 75,
                                          'status': 'not tachycardic',
                                          'timestamp':
                                              '2019-10-10 11:00:36'}]},
                 {'patient_id': 500, 'attending_username': 'Tom',
                  'patient_age': 29, 'heart_rate_history': []},
                 {'patient_id': 250, 'attending_username': 'Josh',
                  'patient_age': 20, 'heart_rate_history': []}
                 ]
    expected2 = [{'attending_username': 'Tom',
                  'attending_email': 'tom@gmail.com',
                  'attending_phone': '919-865-5674'},
                 {'attending_username': 'Lady',
                  'attending_email': 'Lady@gmail.com',
                  'attending_phone': '919-222-333'}]
    assert expected1 == answer1
    assert expected2 == answer2


def test_ecg_logging():
    from testfixtures import LogCapture
    from server import logging
    with LogCapture() as log_c:
        logging(0, "a log")
    log_c.check(("root", "INFO", "a log"))


def test_add_patient_to_database():
    from server import add_patient_to_database
    patient_id = 999
    attending_username = "Attending1"
    patient_age = 18
    add_patient_to_database(patient_id, attending_username, patient_age)
    last_patient_in_db = patient_db[-1]
    expected = {"patient_id": patient_id,
                "attending_username": attending_username,
                "patient_age": patient_age,
                "heart_rate_history": []}
    assert last_patient_in_db == expected


def test_add_attending_to_database():
    from server import add_attending_to_database
    add_attending_to_database("Attending1",
                              "attending1@gmail.com",
                              "777888999")
    expected_name = "Attending1"
    assert attending_db[-1]["attending_username"] == expected_name


new_attending_test1_patient_id = 998
new_attending_test1_attending_username = "attending2"
new_patient_test1_patient_age = 18

new_attending_test2_patient_id = 997
new_attending_test2_attending_username = "attending3"
new_patient_test2_patient_age = "18"

new_attending_test3_patient_id = 996
new_attending_test3_attending_username = "attending4"
new_patient_test3_patient_age = "an_age"

new_attending_test4_patient_id = 998
new_attending_test4_attending_username = "attending2"
new_patient_test4_patient_age = 800


def test_process_new_patient():
    from server import process_new_patient
    in_data1 = {"patient_id": new_attending_test1_patient_id,
                "attending_username": new_attending_test1_attending_username,
                "patient_age": new_patient_test1_patient_age}
    answer1 = process_new_patient(in_data1)
    expected1 = 'Patient successfully added', 200
    assert answer1 == expected1
    in_data2 = {"patient_id": new_attending_test2_patient_id,
                "attending_username": new_attending_test2_attending_username,
                "patient_age": new_patient_test2_patient_age}
    answer2 = process_new_patient(in_data2)
    expected2 = 'Patient successfully added', 200
    assert answer2 == expected2
    in_data3 = {"patient_id": new_attending_test3_patient_id,
                "attending_username": new_attending_test3_attending_username,
                "patient_age": new_patient_test3_patient_age}
    answer3 = process_new_patient(in_data3)
    expected3 = 'patient_age key value has wrong variable type', 400
    assert answer3 == expected3
    in_data4 = {"patient_id": new_attending_test4_patient_id,
                "attending_username": new_attending_test4_attending_username,
                "patient_age": new_patient_test4_patient_age}
    answer4 = process_new_patient(in_data4)
    expected4 = "Invalid age, human can't live so long!", 400
    assert answer4 == expected4
    answer5 = process_new_patient(in_data1)
    expected5 = 'patient_id is the primary key, should be unique!', 400
    assert answer5 == expected5


def test_validate_age():
    from server import validate_age
    age1 = 18
    age2 = 200
    age3 = -1
    answer1 = validate_age(age1)
    expected1 = True
    assert answer1 == expected1
    answer2 = validate_age(age2)
    expected2 = "Invalid age, human can't live so long!"
    assert answer2 == expected2
    answer3 = validate_age(age3)
    expected3 = "Invalid age, must be greater than 0!"
    assert answer3 == expected3


def test_primary_key():
    from server import primary_key
    answer1 = primary_key(patient_db, "patient_id", 500)
    expected1 = "patient_id is the primary key, should be unique!"
    assert answer1 == expected1
    answer2 = primary_key(patient_db, "patient_id", 400)
    expected2 = True
    assert expected2 == answer2


def test_primary_key_exception():
    from server import primary_key
    with pytest.raises(Exception):
        primary_key(patient_db, "doctor_id", 500)


def test_parse_string():
    from server import parse_string
    in_data1 = {"patient_id": new_attending_test1_patient_id,
                "attending_username": new_attending_test1_attending_username,
                "patient_age": new_patient_test1_patient_age}
    answer1 = parse_string(in_data1,  "patient_age")
    expected1 = "No need to parse."
    assert answer1 == expected1
    in_data2 = {"patient_id": new_attending_test2_patient_id,
                "attending_username": new_attending_test2_attending_username,
                "patient_age": new_patient_test2_patient_age}
    answer2 = parse_string(in_data2, "patient_age")
    expected2 = "Successfully parsed!"
    assert answer2 == expected2
    in_data3 = {"patient_id": new_attending_test3_patient_id,
                "attending_username": new_attending_test3_attending_username,
                "patient_age": new_patient_test3_patient_age}
    answer3 = parse_string(in_data3, "patient_age")
    expected3 = "No need to parse."
    assert answer3 == expected3


def test_add_heart_rate_to_database():
    from server import add_heart_rate_to_database
    test_patient = {'patient_id': 120, 'attending_username': 'Tom',
                    'patient_age': 23,
                    'heart_rate_history': []}
    add_heart_rate_to_database(test_patient, 100, "tachycardia",
                               '2018-03-09 11:00:36')
    answer = test_patient['heart_rate_history'][-1]
    expected = {'heart_rate': 100,
                'status': 'tachycardia',
                'timestamp': '2018-03-09 11:00:36'}
    assert answer == expected


def test_is_tachycardic():
    from server import is_tachycardic
    import datetime
    time = datetime.datetime.now()
    dict_in1 = {"patient_id": 995, "heart_rate": 99}
    patient1 = {"patient_id": 995,
                "attending_username": "attending5",
                "patient_age": 18}
    attending1 = {"attending_username": "attending995",
                  "attending_email": "Every@outlook.com",
                  "attending_phone": 919-1111-110}
    answer1 = is_tachycardic(dict_in1, patient1, attending1, time)
    expected1 = "not tachycardic"
    assert answer1 == expected1
    dict_in2 = {"patient_id": 995, "heart_rate": 110}
    patient2 = {"patient_id": 995,
                "attending_username": "attending5",
                "patient_age": 18}
    attending2 = {"attending_username": "attending995",
                  "attending_email": "Every@outlook.com",
                  "attending_phone": 919-1111-110}
    answer2 = is_tachycardic(dict_in2, patient2, attending2, time)
    expected2 = "tachycardic"
    assert answer2 == expected2
    dict_in3 = {"patient_id": 995, "heart_rate": 110}
    patient3 = {"patient_id": 995,
                "attending_username": "attending5",
                "patient_age": 9}
    attending3 = {"attending_username": "attending995",
                  "attending_email": "Every@outlook.com",
                  "attending_phone": 919-1111-110}
    answer3 = is_tachycardic(dict_in3, patient3, attending3, time)
    expected3 = "not tachycardic"
    assert answer3 == expected3
    dict_in4 = {"patient_id": 995, "heart_rate": 150}
    patient4 = {"patient_id": 995,
                "attending_username": "attending5",
                "patient_age": 9}
    attending4 = {"attending_username": "attending995",
                  "attending_email": "Every@outlook.com",
                  "attending_phone": 919-1111-110}
    answer4 = is_tachycardic(dict_in4, patient4, attending4, time)
    expected4 = "tachycardic"
    assert answer4 == expected4


def test_email_sender():
    from server import email_sender
    answer = email_sender("123@gmail.com", 140, 100, '2019-10-10 11:00:36')
    expected = (200,
                'E-mail sent to 123@gmail.com from sentinel_server@duke.edu',
                {'from_email': 'sentinel_server@duke.edu',
                 'to_email': '123@gmail.com',
                 'subject': 'Tachycardia Detected! Patient ID: 140',
                 'content': 'Warning! The heart rate of patient ID 140'
                            ' is 100 bpm @ 2019-10-10 11:00:36!'
                            'A tachycardia happened!'})
    assert answer == expected


def test_find_correct_patient():
    from server import add_patient_to_database, find_correct_patient
    add_patient_to_database(111, "111", 50)
    answer = find_correct_patient(111)
    expected = {'patient_id': 111,
                'attending_username': '111',
                'patient_age': 50, 'heart_rate_history': []}
    assert answer == expected


def test_find_correct_attending():
    from server import add_attending_to_database, find_correct_attending
    add_attending_to_database("a_name", "a_name@gmail.com", "919-654-9192")
    answer = find_correct_attending("a_name")
    expected = {'attending_username': 'a_name',
                'attending_email': 'a_name@gmail.com',
                'attending_phone': '919-654-9192'}
    assert answer == expected


def test_process_add_heart_rate():
    from server import process_add_heart_rate
    in_data1 = {"patient_id": 500,
                "heart_rate": 100}
    answer = process_add_heart_rate(in_data1)
    expected = 'Heart rate info successfully added', 200
    assert answer == expected
    in_data2 = {"patient_id": 130,
                "heart_rate": 100}
    answer = process_add_heart_rate(in_data2)
    expected = 'Could not find this patient in database', 400
    assert answer == expected
    in_data3 = {"patient_id": 250,
                "heart_rate": 100}
    answer = process_add_heart_rate(in_data3)
    expected = 'Could not find attending of this patient in database', 400
    assert answer == expected
    in_data4 = {"patient_id": "Not a number",
                "heart_rate": 100}
    answer = process_add_heart_rate(in_data4)
    expected = 'patient_id key value has wrong variable type', 400
    assert answer == expected


def test_list_average():
    from server import list_average
    list1 = [1, 3, 2]
    list2 = [-1, 0, 10]
    list3 = [-1, -1, -1]
    answer1 = list_average(list1)
    expected1 = 2
    answer2 = list_average(list2)
    expected2 = 3
    answer3 = list_average(list3)
    expected3 = -1
    assert answer1 == expected1
    assert answer2 == expected2
    assert answer3 == expected3


def test_find_interval_rates():
    from server import find_interval_rates
    in_data1 = {"patient_id": 120,
                "heart_rate_average_since": "2018-03-09 11:00:30"}
    patient1 = {'patient_id': 120,
                'attending_username': 'Tom',
                'patient_age': 23,
                'heart_rate_history': [{'heart_rate': 101,
                                        'status': 'tachycardic',
                                        'timestamp': '2018-03-09 11:00:56'},
                                       {'heart_rate': 99,
                                        'status': 'not tachycardic',
                                        'timestamp': '2018-03-10 15:07:36'},
                                       {'heart_rate': 150,
                                        'status': 'tachycardic',
                                        'timestamp': '2018-03-10 20:00:11'}
                                       ]}
    answer1 = find_interval_rates(in_data1, patient1)
    expected1 = [101, 99, 150]
    assert answer1 == expected1
    in_data2 = {"patient_id": 120,
                "heart_rate_average_since": "2018-03-10 11:00:30"}
    answer2 = find_interval_rates(in_data2, patient1)
    expected2 = [99, 150]
    assert answer2 == expected2
    in_data3 = {"patient_id": 120,
                "heart_rate_average_since": "2019-03-10 11:00:30"}
    answer3 = find_interval_rates(in_data3, patient1)
    expected3 = []
    assert answer3 == expected3


def test_validate_time_format():
    from server import validate_time_format
    time_in1 = {
        "patient_id": 1,
        "heart_rate_average_since": "2018-03-09 11:00:36"
    }
    answer1 = validate_time_format(time_in1)
    assert answer1 is True
    time_in2 = {
        "patient_id": 1,
        "heart_rate_average_since": "2018.03-09 11:00:36.4567"
    }
    answer2 = validate_time_format(time_in2)
    expected2 = "The time in does not satisfy the format," \
                " e.g. '2018-03-09 11:00:36'"
    assert answer2 == expected2
    time_in3 = {
        "patient_id": 1,
        "heart_rate_average_since": "Year:2018-Month:03-Day:09 11:00:36.4567"
    }
    answer3 = validate_time_format(time_in3)
    expected3 = "The time in does not satisfy the format," \
                " e.g. '2018-03-09 11:00:36'"
    assert answer3 == expected3


def test_calculate_interval_average():
    from server import calculate_interval_average
    in_data1 = {
        "patient_id": 1,
        "heart_rate_average_since": "2018-03-09 11:00:36"
    }
    answer1 = calculate_interval_average(in_data1)
    expected1 = 'Could not find patient in database', 400
    assert answer1 == expected1
    in_data2 = {
        "patient_id": 120,
        "heart_rate_average_since": "2018-03-09 11:00:36"
    }
    answer2 = calculate_interval_average(in_data2)
    expected2 = 102, 200
    assert answer2 == expected2
    in_data3 = {
        "patient_id": 120,
        "heart_rate_average_since": "2021-03-09 11:00:36"
    }
    answer3 = calculate_interval_average(in_data3)
    expected3 = 'Could not find heart rate since the given time', 400
    assert answer3 == expected3


def test_get_heart_rate_list():
    from server import get_heart_rate_list
    patient_id = "10000"
    expected = "Could not find patient in database", 400
    result = get_heart_rate_list(patient_id)
    assert result == expected
