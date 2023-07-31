from file_handler import FileHandler

class Client:

    def __init__(self, name: str, phone: str, id: int) -> None:
        self.__client_name = name
        self.__phone = phone
        self.__client_id = id
        self.__services = []

    def get_client_details(self):
        return (self.__client_id, self.__client_name, self.__phone, len(self.__services))
    
    def get_name(self):
        return self.__client_name
    
    def add_service(self, service):
        self.__services.append(service)

    def get_services(self):
        return self.__services
    
    def print_os(self):
        
        excel_file = FileHandler()
        excel_file.add_info(self.__client_name, self.__phone, self.__client_id, self.__services)
        excel_file.convert_to_pdf(self.__client_name)

class ListOfClients:

    def __init__(self) -> None:
        self.list = []

    def add_client(self, name: str, phone: str):
        new_client = Client(name, phone, (self.get_number_of_clients()+1))
        self.list.append(new_client)

    def get_number_of_clients(self):
        return len(self.list)
    
    def get_list_of_clients(self):
        return self.list
    
    def get_client(self, name: str):
        for person in self.list:
            if person.get_name() == name:
                return person
            
    def add_service_to_client(self, name: str , service: 'Services'):
        client = self.get_client(name)
        client.add_service(service)
    
    def delete_client(self, name):
        for person in self.list:
            if person.client_name == name:
                self.list.remove(person)
                break

class Services:

    def __init__(self, qty, service, price) -> None:
        self.service = (qty, service, price)

    def get_services_details(self):
        return self.service