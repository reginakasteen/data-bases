import controller
import time
from view import View
from pandas import DataFrame
from tabulate import tabulate
from numpy import array


tables = {
    1: 'client',
    2: 'hotel management',
    3: 'room',
    4: 'services',
    5: 'staff',
    6: 'booking',
    7: 'rental',
    8: 'ordering',
    9: 'providers',
}


class Model:
    @staticmethod
    def display_query(rows, headers):
        df = DataFrame([array(el) for el in rows], columns=array(headers))
        print(tabulate(df, headers="keys", tablefmt="pretty", showindex=False))

    @staticmethod
    def show_table(table):
        connection = controller.connection()
        cursor = connection.cursor()
        print(f"Request: SELECT * FROM {table}")
        print(f"\033[1m {table} \033[0m")
        cursor.execute(f"""SELECT * from public.{table}""")
        records = cursor.fetchall()
        cursor.close()
        return records

    @staticmethod
    def insert():
        connection = controller.connection()
        cursor = connection.cursor()
        go_on = True
        while go_on:
            View.list()
            table = controller.validtable()
            if table == 1:
                phone_number = controller.validate_input_items("phone_number")
                name = controller.validate_input_items("name")
                check_in = controller.validate_input_items("check_in")
                check_out = controller.validate_input_items("check_out")
                cursor.execute(f"""select * from public.client where "phone_number" = '{phone_number}' """)
                records = cursor.fetchone()
                if records is not None:
                    controller.message("Person already exists")
                else:
                    cursor.execute(f"""INSERT INTO "client" ("phone_number", "name", "check_in_date", "check_out_date") 
                                    VALUES ('{phone_number}', '{name}', '{check_in}', '{check_out}')""")
                    View.complete_message("phone_number", phone_number, "client", "inserted")
                go_on = False
            elif table == 2:
                position = controller.validate_input_items("position")
                name = controller.validate_input_items("name")
                iban = controller.validate_input_items("iban")
                cursor.execute(f"""select * from public.hotel_management where "position" = '{position}' """)
                records = cursor.fetchone()
                if records is not None:
                    controller.message("ID already exists")
                else:
                    cursor.execute(f"""INSERT INTO "hotel_management" ("position", "name", "iban") 
                    VALUES ('{position}', '{name}', '{iban}')""")
                    View.complete_message("position", position, "hotel_management", "inserted")
                go_on = False
            elif table == 3:
                room = controller.validate_input_items("room")
                number_of = controller.validate_input_items("number")
                price = controller.validate_input_items("price")
                is_available = controller.validate_input_items("is_available")
                type = controller.validate_input_items("type")
                owner = controller.validate_input_items("owner")
                cursor.execute(f"""select * from public.room where "room_number" = '{room}' """)
                records = cursor.fetchone()
                if records is not None:
                    controller.message("ID already exists")
                else:
                    cursor.execute(f"""INSERT INTO "room" ("room_number", "number_of_places", "price", "is_available", "type", "owner") 
                    VALUES ('{room}', '{number_of}', '{price}', '{is_available}', '{type}', '{owner}')""")
                    View.complete_message("room", room, "room", "inserted")
                go_on = False
            elif table == 4:
                name = controller.validate_input_items("name")
                responsible = controller.validate_input_items("responsible")
                price = controller.validate_input_items("price")
                cursor.execute(f"""select * from public.services where "service_name" = '{name}' """)
                records = cursor.fetchone()
                if records is not None:
                    controller.message("ID already exists")
                else:
                    cursor.execute(f"""INSERT INTO "services" ("service_name", "price", "responsible_for") 
                                        VALUES ('{name}', '{price}', '{responsible}')""")
                    View.complete_message("phone_id", id, "phone", "inserted")
                go_on = False
            elif table == 5:
                policy = controller.validate_input_items("policy")
                name = controller.validate_input_items("name")
                position = controller.validate_input_items("position")
                salary = controller.validate_input_items("salary")
                bonus = controller.validate_input_items("bonus")
                boss = controller.validate_input_items("boss")
                cursor.execute(f"""select * from public.staff where "policy_number" = '{policy}' """)
                records = cursor.fetchone()
                if records is not None:
                    controller.message("ID already exists")
                else:
                    cursor.execute(f"""INSERT INTO "staff" ("policy_number", "name", "position", "salary", "bonus_or_fine", "boss") 
                                    VALUES ('{policy}', '{name}', '{position}', '{salary}', '{bonus}', '{boss}')""")
                    View.complete_message("policy_number", policy, "staff", "inserted")
                go_on = False
            elif table == 6:
                booking = controller.validate_input_items("rent_id")
                booker = controller.validate_input_items("phone_number")
                room = controller.validate_input_items("room")
                cursor.execute(f"""select * from public.booking where "booking_id" = '{booking}' """)
                records = cursor.fetchone()
                if records is not None:
                    controller.message("ID already exists")
                else:
                    cursor.execute(f"""select * from public.client where "phone_number" = '{booker}' """)
                    records = cursor.fetchone()
                    if records is not None:
                        cursor.execute(f"""select * from public.room where "room_number" = '{room}' """)
                        records = cursor.fetchone()
                        if records is not None:
                            cursor.execute(f"""INSERT INTO "booking" ("booking_id", "booker", "room_number") 
                                                                VALUES ('{booking}', '{booker}', '{room}')""")
                            View.complete_message("booking_ID", booking, "booking", "inserted")
                        else:
                            controller.message("The room with this ID doesn't exist")
                    else:
                        controller.message("The client with this ID doesn't exist")
                go_on = False
            elif table == 7:
                rent = controller.validate_input_items("rent_id")
                tenant = controller.validate_input_items("phone_number")
                room = controller.validate_input_items("room")
                cursor.execute(f"""select * from public.rental where "order_id" = '{rent}' """)
                records = cursor.fetchone()
                if records is not None:
                    controller.message("ID already exists")
                else:
                    cursor.execute(f"""select * from public.client where "phone_number" = '{tenant}' """)
                    records = cursor.fetchone()
                    if records is not None:
                        cursor.execute(f"""select * from public.room where "room_number" = '{room}' """)
                        records = cursor.fetchone()
                        if records is not None:
                            cursor.execute(f"""INSERT INTO "rental" ("order_id", "tenant", "room_number") 
                                                                                VALUES ('{rent}', '{tenant}', '{room}')""")
                            View.complete_message("order_ID", rent, "rental", "inserted")
                        else:
                            controller.message("The room with this ID doesn't exist")
                    else:
                        controller.message("The client with this ID doesn't exist")
                go_on = False
            elif table == 8:
                order = controller.validate_input_items("service_code")
                service = controller.validate_input_items("name")
                client = controller.validate_input_items("phone_number")
                is_paid = controller.validate_input_items("is_paid")
                rating = controller.validate_input_items("reting")
                comment = controller.validate_input_items("comment")
                cursor.execute(f"""select * from public.ordering where "order_id" = '{order}'""")
                records = cursor.fetchone()
                if records is not None:
                    controller.message("ID already exists")
                else:
                    cursor.execute(f"""select * from public.services where "service_name" = '{service}' """)
                    records = cursor.fetchone()
                    if records is not None:
                        cursor.execute(f"""select * from public.client where "phone_number" = '{client}' """)
                        records = cursor.fetchone()
                        if records is not None:
                            cursor.execute(f"""INSERT INTO "ordering" 
                            ("order_id", "service_name", "client_number", "is_paid", "rating", "comment") 
                            VALUES ('{order}', '{service}', '{client}', '{is_paid}', '{rating}', '{comment}')""")
                            View.complete_message("order_ID", order, "ordering", "inserted")
                        else:
                            controller.message("The client with this ID doesn't exist")
                    else:
                        controller.message("The service with this ID doesn't exist")
                go_on = False
            elif table == 9:
                code = controller.validate_input_items("sevice_code")
                service = controller.validate_input_items("name")
                provider = controller.validate_input_items("policy")
                cursor.execute(f"""select * from public.providers where "service_code" = '{code}' """)
                records = cursor.fetchone()
                if records is not None:
                    controller.message("ID already exists")
                else:
                    cursor.execute(f"""select * from public.staff where "policy_number" = '{provider}' """)
                    records = cursor.fetchone()
                    if records is not None:
                        cursor.execute(f"""select * from public.services where "service_name" = '{service}' """)
                        records = cursor.fetchone()
                        if records is not None:
                            cursor.execute(f"""INSERT INTO "providers" ("service_code", "service_name", "provider") 
                                                                VALUES ('{code}', '{service}', '{provider}')""")
                            View.complete_message("service_code", code, "providers", "inserted")
                        else:
                            controller.message("The service with this ID doesn't exist")
                    else:
                        controller.message("The worker with this ID doesn't exist")
                go_on = False
            else:
                print('Please, enter valid value')
        connection.commit()
        cursor.close()
        controller.disconnect(connection)

    @staticmethod
    def delete():
        connection = controller.connection()
        cursor = connection.cursor()
        go_on = True
        while go_on:
            View.list()
            table = controller.validtable()
            if table == 1:
                phone_number = controller.validate_input_items("phone_number")
                cursor.execute(f"""select * from public.client where "phone_number" = '{phone_number}' """)
                records = cursor.fetchone()
                if records is not None:
                    cursor.execute(f"""select * from public.booking where "booker" = '{phone_number}' """)
                    records = cursor.fetchone()
                    if records is not None:
                        cursor.execute(f"""DELETE FROM public.booking WHERE "booker" = '{phone_number}' """)
                        View.complete_message("booker", phone_number, "booking", "deleted")
                    cursor.execute(f"""select * from public.rental where "tenant" = '{phone_number}' """)
                    records = cursor.fetchone()
                    if records is not None:
                        cursor.execute(f"""DELETE FROM public.rental WHERE "tenant" = '{phone_number}' """)
                        View.complete_message("tenant", phone_number, "rental", "deleted")
                    cursor.execute(f"""select * from public.ordering where "client_number" = '{phone_number}' """)
                    records = cursor.fetchone()
                    if records is not None:
                        cursor.execute(f"""DELETE FROM public.ordering WHERE "client_number" = '{phone_number}' """)
                        View.complete_message("client_number", phone_number, "ordering", "deleted")
                    cursor.execute(f"""DELETE FROM public.client WHERE "phone_number" = '{phone_number}'""")
                    View.complete_message("phone_number", phone_number, "client", "deleted")
                else:
                    controller.message("No person found")
                go_on = False
            elif table == 2:
                position = controller.validate_input_items("position")
                cursor.execute(f"""select * from public.hotel_management where "position" = '{position}' """)
                records = cursor.fetchone()
                if records is not None:
                    cursor.execute(f"""select * from public.room where "owner" = '{position}' """)
                    records = cursor.fetchone()
                    if records is not None:
                        cursor.execute(f"""DELETE FROM public.room WHERE "owner" = '{position}'""")
                        View.complete_message("owner", position, "room", "deleted")
                    cursor.execute(f"""select * from public.staff where "boss" = '{position}' """)
                    records = cursor.fetchone()
                    if records is not None:
                        cursor.execute(f"""DELETE FROM public.staff WHERE "boss" = '{position}'""")
                        View.complete_message("boss", position, "staff", "deleted")
                    cursor.execute(f"""DELETE FROM public.hotel_management WHERE "position" = '{position}'""")
                    View.complete_message("position", position, "hotel_management", "deleted")
                else:
                    controller.message("No person found")
                go_on = False
            elif table == 3:
                room = controller.validate_input_items("room")
                cursor.execute(f"""select * from public.room where "room_number" = '{room}' """)
                records = cursor.fetchone()
                if records is not None:
                    cursor.execute(f"""select * from public.booking where "room_number" = '{room}' """)
                    records = cursor.fetchone()
                    if records is not None:
                        cursor.execute(f"""DELETE FROM public.booking WHERE "room_number" = '{room}'""")
                        View.complete_message("roon_number", room, "booking", "deleted")
                    cursor.execute(f"""select * from public.rental where "room_number" = '{room}' """)
                    records = cursor.fetchone()
                    if records is not None:
                        cursor.execute(f"""DELETE FROM public.rental WHERE "room_number" = '{room}'""")
                        View.complete_message("room_number", room, "rental", "deleted")
                    cursor.execute(f"""DELETE FROM public.services WHERE "service_name" = '{room}'""")
                    View.complete_message("room_number", room, "room", "deleted")
                else:
                    controller.message("No room found")
                go_on = False
            elif table == 4:
                name = controller.validate_input_items("name")
                cursor.execute(f"""select * from public.services where "service_name" = '{name}' """)
                records = cursor.fetchone()
                if records is not None:
                    cursor.execute(f"""select * from public.ordering where "service_name" = '{name}' """)
                    records = cursor.fetchone()
                    if records is not None:
                        cursor.execute(f"""DELETE FROM public.ordering WHERE "service_name" = '{name}'""")
                        View.complete_message("service_name", name, "ordering", "deleted")
                    cursor.execute(f"""select * from public.providers where "service_name" = '{name}' """)
                    records = cursor.fetchone()
                    if records is not None:
                        cursor.execute(f"""DELETE FROM public.providers WHERE "service_name" = '{name}'""")
                        View.complete_message("service_name", name, "providers", "deleted")
                    cursor.execute(f"""DELETE FROM public.services WHERE "service_name" = '{name}'""")
                    View.complete_message("service_name", name, "services", "deleted")
                else:
                    controller.message("No service found")
                go_on = False
            elif table == 5:
                policy = controller.validate_input_items("policy")
                cursor.execute(f"""select * from public.staff where "policy_number" = '{policy}' """)
                records = cursor.fetchone()
                if records is not None:
                    cursor.execute(f"""select * from public.providers where "service_name" = '{policy}' """)
                    records = cursor.fetchone()
                    if records is not None:
                        cursor.execute(f"""DELETE FROM public.providers WHERE "service_name" = '{policy}'""")
                        View.complete_message("provider", policy, "providers", "deleted")
                    cursor.execute(f"""DELETE FROM public.staff WHERE "policy_number" = '{policy}'""")
                    View.complete_message("policy_number", policy, "staff", "deleted")
                else:
                    controller.message("No person found")
                go_on = False
            elif table == 6:
                rent_id = controller.validate_input_items("rent_id")
                cursor.execute(f"""select * from public.booking where "booking_id" = '{rent_id}' """)
                records = cursor.fetchone()
                if records is not None:
                    cursor.execute(f"""DELETE FROM public.booking WHERE "booking_id" = '{rent_id}'""")
                    View.complete_message("booking_id", rent_id, "booking", "deleted")
                else:
                    controller.message("No booking found")
                go_on = False
            elif table == 7:
                rent_id = controller.validate_input_items("rent_id")
                cursor.execute(f"""select * from public.rental where "order_id" = '{rent_id}' """)
                records = cursor.fetchone()
                if records is not None:
                    cursor.execute(f"""DELETE FROM public.rental WHERE "order_id" = '{rent_id}'""")
                    View.complete_message("order_id", rent_id, "rental", "deleted")
                else:
                    controller.message("No rent found")
                go_on = False
            elif table == 8:
                order_id = controller.validate_input_items("order")
                cursor.execute(f"""select * from public.ordering where "order_id" = '{order_id}' """)
                records = cursor.fetchone()
                if records is not None:
                    cursor.execute(f"""DELETE FROM public.ordering WHERE "order_id" = '{order_id}'""")
                    View.complete_message("schedule_id", id, "schedule", "deleted")
                else:
                    controller.message("No order found")
                go_on = False
            elif table == 9:
                code = controller.validate_input_items("service_code")
                cursor.execute(f"""select * from public.providers where "service_code" = '{code}' """)
                records = cursor.fetchone()
                if records is not None:
                    cursor.execute(f"""DELETE FROM public.providers WHERE "service_code" = '{code}'""")
                    View.complete_message("service_code", code, "providers", "deleted")
                else:
                    controller.message("No service found")
                go_on = False
            else:
                print("Please, enter valid number")
            connection.commit()
            cursor.close()
            controller.disconnect(connection)
            pass

    @staticmethod
    def update():
        connection = controller.connection()
        cursor = connection.cursor()
        go_on = True
        while go_on:
            View.list()
            table = controller.validtable()
            if table == 1:
                phone_number = controller.validate_input_items("phone_number")
                cursor.execute(f"""select * from public.client where "phone_number" = '{phone_number}' """)
                records = cursor.fetchone()
                continue_update = True
                if records is not None:
                    View.columns(1)
                    while continue_update:
                        attr = input("Choose a number of column to update")
                        if attr == '1':
                            value = controller.validate_input_items("name")
                            attribute = "name"
                            continue_update = False
                        elif attr == '2':
                            value = controller.validate_input_items("check_in")
                            attribute = "check_in_date"
                            continue_update = False
                        elif attr == '3':
                            value = controller.validate_input_items("check_out")
                            attribute = "check_out_date"
                            continue_update = False
                        else:
                            controller.message("Please, enter valid number")
                    cursor.execute(f"""UPDATE public.client set {attribute} = '{value}' where "phone_number" = '{phone_number}' """)
                    View.complete_message("phone_nomber", phone_number, "client", "updated")
                    go_on = False
                else:
                    controller.message("No client with this ID found")
            elif table == 2:
                position = controller.validate_input_items("position")
                cursor.execute(f"""select * from public.hotel_management where "position" = {position} """)
                records = cursor.fetchone()
                if records is not None:
                    View.columns(2)
                    continue_update = True
                    while continue_update:
                        attr = input("Choose a number of column to update")
                        if attr == '1':
                            value = controller.validate_input_items("name")
                            attribute = "name"
                            continue_update = False
                        elif attr == '2':
                            value = controller.validate_input_items("iban")
                            attribute = "iban"
                            continue_update = False
                        else:
                            controller.message("Please, enter valid number")
                    cursor.execute(f"""UPDATE "hotel_management" set {attribute} = '{value}' where "position" = '{id}' """)
                    View.complete_message("position", position, "hotel_management", "updated")
                    go_on = False
                    pass
                else:
                    controller.message("No boss with this ID found")
            elif table == 3:
                room = controller.validate_input_items("room")
                cursor.execute(f"""select * from public.room where "room_number" = {room} """)
                records = cursor.fetchone()
                if records is not None:
                    View.columns(3)
                    continue_update = True
                    while continue_update:
                        attr = input("Choose a number of column to update: ")
                        if attr == '1':
                            value = controller.validate_input_items("number")
                            attribute = "number_of_places"
                            continue_update = False
                        elif attr == '2':
                            value = controller.validate_input_items("price")
                            attribute = "price"
                            continue_update = False
                        elif attr == '3':
                            value = controller.validate_input_items("is_available")
                            attribute = "is_available"
                            continue_update = False
                        elif attr == '4':
                            value = controller.validate_input_items("type")
                            attribute = "type"
                            continue_update = False
                        elif attr == '5':
                            value = controller.validate_input_items("owner")
                            attribute = "owner"
                            continue_update = False
                        else:
                            controller.message("Please, enter valid number")
                    cursor.execute(f"""UPDATE "room" set {attribute} = '{value}' where "room_number" = '{room}' """)
                    View.complete_message("room_number", room, "room", "updated")
                    go_on = False
                    pass
                else:
                    controller.message("No room with this ID found")
            elif table == 4:
                name = controller.validate_input_items("name")
                cursor.execute(f"""select * from public.services where "service_name" = {name} """)
                records = cursor.fetchone()
                if records is not None:
                    View.columns(4)
                    continue_update = True
                    while continue_update:
                        attr = input("Choose a number of column to update: ")
                        if attr == '1':
                            value = controller.validate_input_items("price")
                            attribute = "price"
                            continue_update = False
                        elif attr == '2':
                            value = controller.validate_input_items("responsible")
                            attribute = "responsible_for"
                            continue_update = False
                        else:
                            controller.message("Please, enter valid number: ")
                    cursor.execute(f"""UPDATE "services" set {attribute} = '{value}' where "service_name" = '{name}' """)
                    View.complete_message("service_name", name, "services", "updated")
                    go_on = False
                    pass
                else:
                    controller.message("No service with this ID found")
            elif table == 5:
                policy = controller.validate_input_items("policy")
                cursor.execute(f"""select * from public.staff where "policy_number" = {policy} """)
                records = cursor.fetchone()
                if records is not None:
                    View.columns(5)
                    continue_update = True
                    while continue_update:
                        attr = input("Choose a number of column to update ")
                        if attr == '1':
                            value = controller.validate_input_items("name")
                            attribute = "name"
                            continue_update = False
                        elif attr == '2':
                            value = controller.validate_input_items("position")
                            attribute = "position"
                            continue_update = False
                        elif attr == '3':
                            value = controller.validate_input_items("salary")
                            attribute = "salary"
                            continue_update = False
                        elif attr == '4':
                            value = controller.validate_input_items("bonus")
                            attribute = "bonus_or_fine"
                            continue_update = False
                        elif attr == '5':
                            value = controller.validate_input_items("boss")
                            attribute = "boss"
                            continue_update = False
                        else:
                            controller.message("Please, enter valid number")
                    cursor.execute(f"""UPDATE "staff" set {attribute} = '{value}' where "policy_number" = '{policy}' """)
                    View.complete_message("policy_number", policy, "staff", "updated")
                    go_on = False
                    pass
                else:
                    controller.message("No worker with this ID found")
            elif table == 6:
                rent_id = controller.validate_input_items("rent_id")
                cursor.execute(f"""select * from public.booking where "booking_id" = {rent_id} """)
                records = cursor.fetchone()
                if records is not None:
                    View.columns(6)
                    continue_update = True
                    while continue_update:
                        attr = input("Choose a number of column to update: ")
                        if attr == '1':
                            value = controller.validate_input_items("room")
                            attribute = "room_number"
                            continue_update = False
                        elif attr == '2':
                            value = controller.validate_input_items("phone_number")
                            attribute = "booker"
                            continue_update = False
                        else:
                            controller.message("Please, enter valid number: ")
                    cursor.execute(f"""UPDATE "booking" set {attribute} = '{value}' where "booking_id" = '{rent_id}' """)
                    View.complete_message("booking_id", rent_id, "booking", "updated")
                    go_on = False
                    pass
                else:
                    controller.message("No booking with this ID found")
            elif table == 7:
                rent_id = controller.validate_input_items("rent_id")
                cursor.execute(f"""select * from public.rental where "order_id" = {rent_id} """)
                records = cursor.fetchone()
                if records is not None:
                    View.columns(7)
                    continue_update = True
                    while continue_update:
                        attr = input("Choose a number of column to update: ")
                        if attr == '1':
                            value = controller.validate_input_items("room")
                            attribute = "room_number"
                            continue_update = False
                        elif attr == '2':
                            value = controller.validate_input_items("phone_number")
                            attribute = "tenant"
                            continue_update = False
                        else:
                            controller.message("Please, enter valid number: ")
                    cursor.execute(f"""UPDATE "rental" set {attribute} = '{value}' where "order_id" = '{rent_id}' """)
                    View.complete_message("order_id", rent_id, "rental", "updated")
                    go_on = False
                    pass
                else:
                    controller.message("No rent with this ID found")
            elif table == 8:
                id = controller.validate_input_items("order")
                cursor.execute(f"""select * from public.ordering where "order_id" = {id} """)
                records = cursor.fetchone()
                if records is not None:
                    View.columns(8)
                    continue_update = True
                    while continue_update:
                        attr = input("Choose a number of column to update: ")
                        if attr == '1':
                            value = controller.validate_input_items("name")
                            attribute = "service_name"
                            continue_update = False
                        elif attr == '2':
                            value = controller.validate_input_items("phone_number")
                            attribute = "client_number"
                            continue_update = False
                        elif attr == '3':
                            value = controller.validate_input_items("is_paid")
                            attribute = "is_paid"
                            continue_update = False
                        elif attr == '4':
                            value = controller.validate_input_items("rating")
                            attribute = "rating"
                            continue_update = False
                        elif attr == '5':
                            value = controller.validate_input_items("comment")
                            attribute = "comment"
                            continue_update = False
                        else:
                            controller.message("Please, enter valid number: ")
                    cursor.execute(f"""UPDATE "ordering" set {attribute} = '{value}' where "order_id" = '{id}' """)
                    View.complete_message("order_id", id, "ordering", "updated")
                    go_on = False
                    pass
                else:
                    controller.message("No order with this ID found")
            elif table == 9:
                id = controller.validate_input_items("order")
                cursor.execute(f"""select * from public.providers where "service_code" = {id} """)
                records = cursor.fetchone()
                if records is not None:
                    View.columns(9)
                    continue_update = True
                    while continue_update:
                        attr = input("Choose a number of column to update: ")
                        if attr == '1':
                            value = controller.validate_input_items("name")
                            attribute = "service_name"
                            continue_update = False
                        elif attr == '2':
                            value = controller.validate_input_items("policy")
                            attribute = "provider"
                            continue_update = False
                        else:
                            controller.message("Please, enter valid number: ")
                    cursor.execute(f"""UPDATE "providers" set {attribute} = '{value}' where "service_code" = '{id}' """)
                    View.complete_message("service_code", id, "providers", "updated")
                    go_on = False
                    pass
                else:
                    controller.message("No order with this ID found")
            else:
                controller.message("Please, enter valid number")
        connection.commit()
        cursor.close()
        controller.disconnect(connection)
        pass

    @staticmethod
    def search1():
        connection = controller.connection()
        cursor = connection.cursor()
        name = controller.validate_input_items("name")
        cursor.execute(f"""select * from public.client where "name" = '{name}' """)
        records = cursor.fetchone()
        #if records is not None:
        search = f"""select "name", "phone_number", "booking_id" from (select c."name", c."phone_number", b."booking_id"
            from "client" c left join "booking" b on b."booker" = c."phone_number"
            where c."name" LIKE '{name}' group by c."name", c."phone_number", b."booking_id") as foo"""
        start = int(time.time() * 1000)
        cursor.execute(search)
        print("--- Time of search = {} ms ---".format(int((time.time() * 1000) - start)))
        records = cursor.fetchall()
        cursor.close()
        return records

    @staticmethod
    def search2():
        connection = controller.connection()
        cursor = connection.cursor()
        name = controller.validate_input_items("name")
        cursor.execute(f"""select * from public.hotel_management where "name" = '{name}' """)
        records = cursor.fetchone()
        search = f"""select "name", "room_number", "type" from (select h."name", r."room_number", r."type"
                    from "hotel_management" h left join "room" r on r."owner" = h."position"
                    where h."name" LIKE '{name}' group by h."name", r."room_number", r."type") as foo"""
        start = int(time.time() * 1000)
        cursor.execute(search)
        print("--- Time of search = {} ms ---".format(int((time.time() * 1000) - start)))
        records = cursor.fetchall()
        cursor.close()
        return records


    @staticmethod
    def search3():
        connection = controller.connection()
        cursor = connection.cursor()
        price = controller.validate_input_items("price")
        cursor.execute(f"""select * from public.services where "price" = '{price}' """)
        records = cursor.fetchone()
        search = f"""select "price", "service_name", "name" from (select s."price", s."service_name", h."name"
                            from "services" s left join "hotel_management" h on h."position" = s."responsible_for"
                            where s."price" > '{price}' group by s."price", s."service_name", h."name") as foo"""
        start = int(time.time() * 1000)
        cursor.execute(search)
        print("--- Time of search = {} ms ---".format(int((time.time() * 1000) - start)))
        records = cursor.fetchall()
        cursor.close()
        return records
