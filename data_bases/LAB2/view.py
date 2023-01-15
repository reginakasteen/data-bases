
class View:
    def __init__(self, table, records):
        self.table = table
        self.records = records

    @staticmethod
    def complete_message(attribute, value, table, action):
        print(f"The row with '{attribute}' = '{value}' in table '{table}' was {action} successfully.")

    @staticmethod
    def enter_item(item):
        data = input("Enter {}: ".format(item))
        return data

    @staticmethod
    def list():
        print('''
        1 -> client
        2 -> hotel management
        3 -> room
        4 -> services
        5 -> staff
        6 -> booking
        7 -> rental
        8 -> ordering
        9 -> providers
        ''')

    @staticmethod
    def columns(table):
        if table == 1:
            print('''
                1 -> name
                2 -> check in date
                3 -> check out date
            ''')
        elif table == 2:
            print('''
                1 -> name
                2 -> iban
            ''')
        elif table == 3:
            print('''
                1 -> number of places
                2 -> price 
                3 -> is available
                4 -> type 
                5 -> owner
            ''')
        elif table == 4:
            print('''
                1 -> price
                2 -> responsible for
            ''')
        elif table == 5:
            print('''
                1 -> name
                2 -> position
                3 -> salary
                4 -> bonus or fine
                5 -> boss
            ''')
        elif table == 6:
            print('''
                1 -> room number
                2 -> booker
            ''')
        elif table == 7:
            print('''
                1 -> room number
                2 -> tenant
            ''')
        elif table == 8:
            print('''
                1 -> service name
                2 -> client number
                3 -> is paid
                4 -> rating
                5 -> comment
            ''')
        elif table == 9:
            print('''
                1 -> service name
                2 -> provider
            ''')

    @staticmethod
    def search():
        print('''
                1 -> Search phone number and booking orders of the client with name
                2 -> Search rooms of the manager and types of them with the name
                3 -> Search service name and who is responsible for it with service's price
                ''')
