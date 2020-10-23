from server import patient_db, attending_db
from flask import Flask, jsonify, request


def test_add_attending_to_database():
    from server import add_attending_to_database
    add_attending_to_database("Attending1",
                            "attending1@gmail.com",
                            "777888999")
    expected_name = "Attending1"
    assert attending_db[-1]["attending_username"] == expected_name


# def test_add_attending_to_database():


# def test_process_new_patient()


# def test_validate_age


# def test_parse_string


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
    result4 = process_new_attending(in_data3)
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
    assert  result2 == expected2


def test_attending_info_detect():
    from server import attending_info_detect
    in_data =  {"attending_username": "Everett",
                "attending_email": "Evy.com",
                "attending_phone": "666666"}
    expected = "You entered a invalid email address, "
    result = attending_info_detect(in_data)
    assert result == expected


#def test_process_add_heart_rate()


#def test_time_formatter()


#def test_is_tachycardic()


#def test_find_correct_patient


#def test_find_correct_attending


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
                 "status":'not tachycardic',
                 "timestamp":'2059-13-13 11:00:36'}
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


# def test_calculate_interval_average()


# def test_list_average()


# def test_find_interval_rates()


# def test_validate_time_format()


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
