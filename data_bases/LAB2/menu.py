from model import Model
from view import View
import controller


class Menu:
    @staticmethod
    def menu():
        while True:
            print('''
                Main menu
                0 - Show one table
                1 - Show all tables
                2 - Insert data
                3 - Delete data
                4 - Update data
                5 - Search data
                6 - Exit
                ''')
            choice = input('Choose an option: ')
            if choice == '0':
                View.list()
                table = controller.validtable()
                if table == 1:
                    Model.display_query(Model.show_table("client"),
                                        ["phone_number", "name", "check_in_date", "check_out_date"])
                elif table == 2:
                    Model.display_query(Model.show_table("hotel_management"), ["position", "name", "iban"])
                elif table == 3:
                    Model.display_query(Model.show_table("room"),
                                        ["room_number", "number_of_places", "price", "is_available", "type", "owner"])
                elif table == 4:
                    Model.display_query(Model.show_table("services"), ["service_name", "price", "responsible_for"])
                elif table == 5:
                    Model.display_query(Model.show_table("staff"),
                                        ["policy_number", "name", "position", "salary", "bonus_or_fine", "boss"])
                elif table == 6:
                    Model.display_query(Model.show_table("booking"),
                                        ["booking_id", "room_number", "booker"])
                elif table == 7:
                    Model.display_query(Model.show_table("rental"),
                                        ["order_id", "room_number", "tenant"])
                elif table == 8:
                    Model.display_query(Model.show_table("ordering"),
                                        ["order_id", "service_name", "client_number", "is_paid", "rating", "comment"])
                elif table == 9:
                    Model.display_query(Model.show_table("providers"),
                                        ["service_code", "service_name", "provider"])
            elif choice == '1':
                Model.display_query(Model.show_table("client"),
                                    ["phone_number", "name", "check_in_date", "check_out_date"])
                Model.display_query(Model.show_table("hotel_management"), ["position", "name", "iban"])
                Model.display_query(Model.show_table("room"),
                                    ["room_number", "number_of_places", "price", "is_available", "type", "owner"])
                Model.display_query(Model.show_table("services"), ["service_name", "price", "responsible_for"])
                Model.display_query(Model.show_table("staff"),
                                    ["policy_number", "name", "position", "salary", "bonus_or_fine", "boss"])
                Model.display_query(Model.show_table("booking"),
                                    ["booking_id", "room_number", "booker"])
                Model.display_query(Model.show_table("rental"),
                                    ["order_id", "room_number", "tenant"])
                Model.display_query(Model.show_table("ordering"),
                                    ["order_id", "service_name", "client_number", "is_paid", "rating", "comment"])
                Model.display_query(Model.show_table("providers"),
                                    ["service_code", "service_name", "provider"])

            elif choice == '2':
                end_insert = False
                while not end_insert:
                    Model.insert()
                    incorrect = True
                    while incorrect:
                        answer = input('Continue working with insert? Enter Yes or No ')
                        if answer == 'No':
                            end_insert = True
                            incorrect = False
                        elif answer == 'Yes':
                            incorrect = False
                            pass
                        else:
                            print('Please, enter Yes or No')
            elif choice == '3':
                end_delete = False
                while not end_delete:
                    Model.delete()
                    incorrect = True
                    while incorrect:
                        answer = input('Continue working with delete? Enter Yes or No ')
                        if answer == 'No':
                            end_delete = True
                            incorrect = False
                        elif answer == 'Yes':
                            incorrect = False
                            pass
                        else:
                            print('Please, enter Yes or No ')
            elif choice == '4':
                end_update = False
                while not end_update:
                    Model.update()
                    incorrect = True
                    while incorrect:
                        answer = input('Continue working with update? Enter Yes or No ')
                        if answer == 'No':
                            end_update = True
                            incorrect = False
                        elif answer == 'Yes':
                            incorrect = False
                            pass
                        else:
                            print('Please, enter Yes or No ')
            elif choice == '5':
                end_search = False
                View.search()
                choice = int(input("Select what you want to search: "))
                while not end_search:
                    if choice == 1:
                        Model.display_query(Model.search1(), ["Name", "Number", "Booking"])
                    elif choice == 2:
                        Model.display_query(Model.search2(), ["Name", "Room", "Type"])
                    elif choice == 3:
                        Model.display_query(Model.search3(), ["Price", "Service", "Responsible for"])
                    incorrect = True
                    while incorrect:
                        answer = input('Continue working with search? Enter Yes or No ')
                        if answer == 'No':
                            end_search = True
                            incorrect = False
                        elif answer == 'Yes':
                            incorrect = False
                            pass
                        else:
                            print('Please, enter Yes or No ')
            elif choice == '6':
                break
            else:
                print('Please, enter valid number')
