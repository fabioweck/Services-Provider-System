import PySimpleGUI as sg
from clients_services import Services, ListOfClients

class RepairShop:

    def __init__(self) -> None:
        self.shoplist = ListOfClients()

    def register_client(self):
        client = input("Enter client's name: ")
        phone = input("Phone number: ")
        self.shoplist.add_client(client, phone)
        print('\nClient registered.\n')

    def get_clients_list(self):
        return self.shoplist.get_list_of_clients()
    
    def client_details(self, name):
        person = self.shoplist.get_client(name)
        return person
    
    def add_service_to_client(self, name, qty, service, price):
        person = self.shoplist.get_client(name)
        service = Services(qty, service, price)
        person.add_service(service)
    
    def delete_client(self, name):
        self.shoplist.delete_client(name)

    def print_os(self, name):
        person = self.shoplist.get_client(name)
        person.print_os()

golden_strings = RepairShop()

while True:

    print('')
    print("1 - Add client")
    print("2 - Add service to a client")
    print("3 - Check clients list")
    print("4 - Check client details")
    print("5 - Print invoice")
    print("6 - Delete client")
    print("7 - Exit\n")

    option = input('Enter command: \n')

    if option == '1':
        golden_strings.register_client()

    if option == '2':
        name = input('Type a name: ')
        service = input('Type of service: ')
        qty = int(input('Quantity: '))
        price = float(input('Price: '))
        try:
            golden_strings.add_service_to_client(name, qty, service, price)
            print('Service added!\n')
        except:
            print('Something went wrong. Try again.')

    if option == '3':
        list = golden_strings.get_clients_list()
        for person in list:
            print(person.get_client_details())


    if option == '4':
        name = input('Type a name: \n')
        person = golden_strings.client_details(name)
        print(person.get_client_details())
        for service in person.get_services():
            print(service.get_services_details())

    if option == '5':
        name = input('Type a name: \n')
        golden_strings.print_os(name)
    
    if option == '6':
        name = input('Type a name: \n')
        person = golden_strings.client_details(name)
        print(person.get_client_details())
        golden_strings.delete_client(name)
        print('Client deleted')

    if option == '7':
        break