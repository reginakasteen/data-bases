import psycopg2
import re
from view import View



def connection():
    return psycopg2.connect(
        user="postgres",
        password="ametyst7",
        host="localhost",
        port="5432",
        database="hotel",
    )


def disconnect(connection):
    connection.commit()
    connection.close()

def is_digit(n):
        try:
            int(n)
            return True
        except ValueError:
            return False


def message(text):
    return print(text)


def validtable():
    incorrect = True
    while incorrect:
        table = input('Choose table number => ')
        if table.isdigit():
            table = int(table)
            if 1 <= table <= 9:
                incorrect = False
            else:
                print('Incorrect input, try again.')
        else:
            print('Incorrect input, try again.')
    return table


def validate_input_items(name):
    if name == "price":
        value = View.enter_item("price")
        if value.isdecimal():
            return value
    if name == "salary":
        value = View.enter_item("salary")
        if value.isdecimal():
            return value
    elif name == "iban":
        value = View.enter_item("iban")
        if value.isalnum():
            return value
    elif name == "is_available":
        message("enter true or false")
        value = View.enter_item("is the room available or not")
        #if (value == "true" or value == "false"):
        return value
    elif name == "is_paid":
        message("enter true or false")
        value = View.enter_item("is the order paid or not")
        return value
    elif name == "comment":
        value = View.enter_item("comment")
        return value
    elif name == "rating":
        value = View.enter_item("rate")
        return value
    elif name == "room":
        value = View.enter_item("room number")
        if value.isdecimal():
            return value
        else:
            message("enter 1 <= number <= 999")
            validate_input_items("room number")
    elif name == "order":
        value = View.enter_item("order number")
        if value.isdecimal():
            return value
        else:
            message("enter 1 <= number <= 999")
            validate_input_items("room number")
    elif name == "service_code":
        value = View.enter_item("order number")
        if value.isdecimal():
            return value
        else:
            message("enter 1 <= number <= 999")
            validate_input_items("service code")
    elif name == "number":
        value = View.enter_item("number of places")
        if value.isdecimal():
            return value
    elif name == "rent_id":
        value = View.enter_item("rental/booking ID")
        if (len(value) == 0):
            return value
        else:
            message("enter 1000 <= number <= 9999")
            validate_input_items("rental/booking ID")
    elif name == "name":
        value = View.enter_item("name")
        if (len(value) == 0):
            return validate_input_items(name)
        return value
    elif name == "responsible":
        value = View.enter_item("responsible for the service's quality")
        if (len(value) == 0):
            return validate_input_items(name)
        return value
    elif name == "type":
        value = View.enter_item("type of room")
        if (len(value) == 0):
            return validate_input_items(name)
        return value
    elif name == "position":
        value = View.enter_item("position")
        if (len(value) == 0):
            return validate_input_items(name)
        return value
    elif name == "boss":
        value = View.enter_item("boss position")
        if (len(value) == 0):
            return validate_input_items(name)
        return value
    elif name == "owner":
        value = View.enter_item("room's owner")
        if (len(value) == 0):
            return validate_input_items(name)
        return value
    elif name == "policy":
        value = View.enter_item("policy number")
        if (len(value) != 9):
            print("Enter like in example: A12345678")
            return validate_input_items(name)
        return value
    elif name == "check_in":
        value = View.enter_item("check in date")
        res = re.sub(r"[/\\,.]", "-", re.search(r"(\d+.*?\d+.*?\d+)", value).group(1))
        return res
    elif name == "check_out":
        value = View.enter_item("check out date")
        res = re.sub(r"[/\\.]", "-", re.search(r"(\d+.*?\d+.*?\d+)", value).group(1))
        return res
    elif name == "bonus":
        value = View.enter_item("bonus or fine value")
        return value
    elif name == "phone_number":
        value = View.enter_item("phone number")
        if value.isdigit() is False:
            print("Enter like in example: 998889999")
            return validate_input_items(name)
        else:
            if len(value) != 9:
                print("Phone should have 9 numbers")
                return validate_input_items(name)
            return value
