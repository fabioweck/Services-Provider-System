from clients_services import Services, Client
import re
from file_handler import FileHandler

class RepairShop:

    def __init__(self) -> None:
        self.shoplist = []
        self.order_number = 0
        self.invoice_number = 0
        self.load_clients()

    def register_client(self):
        name = input("Enter client's name: ")
        if self.client_details(name) != None:
            print('Client already registered!\n')
            return
        phone = input("Phone number: ")
        email = input('E-mail: ')
        id = len(self.shoplist) + 1
        new_client = Client(id, name, phone, email)
        file = FileHandler()
        file.store_client(new_client.get_client_details())
        print('\nClient registered.\n')

    def get_clients_list(self):
        return self.shoplist
    
    def client_details(self, name):
        for client in self.shoplist:
            if client.get_name() == name:
                return client
    
    def add_service_to_client(self, name, qty, service, price):
        person = self.client_details(name)
        service = Services(qty, service, price)
        person.add_service(service)

    def client_registry(self, name):
        client = self.client_details(name)
        return client.get_registry()
    
    def delete_client(self, name):
        client = self.client_details(name)
        self.shoplist.remove(client)

    def print_os(self, name):
        self.order_number += 1
        client = self.client_details(name)
        details = client.get_client_details()
        self.invoice_number += 1
        file = FileHandler()
        file.add_info_to_excel(details[0], details[1], details[2], details[3], self.invoice_number, client.get_services())
        client.add_registry(self.order_number, client.get_services())
        file.convert_to_pdf(client.get_name())
        del file

    def search_client(self, sentence: str):
        for client in self.shoplist:
            if re.search(f'^{sentence}+', client.get_name()):
                return client.get_client_details()


    def load_clients(self):
        file = FileHandler()
        clients = file.load_clients()
        services = file.load_services()

        for client in clients:
            client_to_add = Client(client[0], client[1], client[2], client[3])
            self.shoplist.append(client_to_add)
            for service in services:
                if service[0] == client_to_add.get_client_details()[0]:
                    list_of_services = []
                    for items in service[2:]:
                        list_of_services.append(items)
                    client_to_add.add_registry(service[1], list_of_services)
                    self.invoice_number += 1

        del client_to_add
        del file


    def main(self):

        while True:
            print('')
            print("1 - Add client")
            print("2 - Add service to a client")
            print("3 - Check clients list")
            print("4 - Check client details")
            print("5 - Print invoice")
            print("6 - Delete client")
            print("7 - Search client")
            print("8 - Check client's invoices")
            print("9 - Exit\n")

            option = input('Enter command: \n')
            match option:
                case '1':
                    self.register_client()

                case '2':
                    name = input('Type a name: ')
                    service = input('Type of service: ')
                    qty = int(input('Quantity: '))
                    price = float(input('Price: '))
                    try:
                        self.add_service_to_client(name, qty, service, price)
                        print('Service added!\n')
                    except:
                        print('Something went wrong. Try again.')

                case '3':
                    list = self.get_clients_list()
                    for person in list:
                        print(person.get_client_details())


                case '4':
                    name = input('Type a name: \n')
                    person = self.client_details(name)
                    print(person.get_client_details())

                case '5':
                    name = input('Type a name: \n')
                    self.print_os(name)
            
                case '6':
                    name = input('Type a name: \n')
                    self.delete_client(name)
                    print('Client deleted')

                case '7':
                    name = input('Type a sentence: \n')
                    self.search_client(name)

                case '8':
                    name = input('Type a sentence: \n')
                    invoices = self.client_registry(name)
                    for services in invoices.values():
                        for item in services:
                            if type(item) == str:
                                print(item)

                case '9':
                    break


      
golden_strings = RepairShop()
golden_strings.main()