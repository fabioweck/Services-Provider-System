from clients_services import Services, Client

class RepairShop:

    def __init__(self) -> None:
        self.shoplist = []
        self.order_number = 0

    def register_client(self):
        name = input("Enter client's name: ")
        phone = input("Phone number: ")
        id = len(self.shoplist) + 1
        new_client = Client(name, phone, id)
        self.shoplist.append(new_client)
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
    
    def delete_client(self, name):
        client = self.client_details(name)
        self.shoplist.remove(client)

    def print_os(self, name):
        self.order_number += 1
        person = self.client_details(name)
        person.print_os(self.order_number)
        

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

    match option:
        case '1':
            golden_strings.register_client()

        case '2':
            name = input('Type a name: ')
            service = input('Type of service: ')
            qty = int(input('Quantity: '))
            price = float(input('Price: '))
            try:
                golden_strings.add_service_to_client(name, qty, service, price)
                print('Service added!\n')
            except:
                print('Something went wrong. Try again.')

        case '3':
            list = golden_strings.get_clients_list()
            for person in list:
                print(person.get_client_details())


        case '4':
            name = input('Type a name: \n')
            person = golden_strings.client_details(name)
            print(person.get_client_details())

        case '5':
            name = input('Type a name: \n')
            golden_strings.print_os(name)
    
        case '6':
            name = input('Type a name: \n')
            golden_strings.delete_client(name)
            print('Client deleted')

        case '7':
            break