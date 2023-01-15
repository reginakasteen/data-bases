import controller
from menu import Menu


connection = controller.connection()
cursor = connection.cursor()
Menu.menu()
cursor.close()
connection.close()
print("PostgreSQL connection is closed")
