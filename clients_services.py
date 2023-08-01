class Client:

    def __init__(self, id: int, name: str, phone: str, email: str) -> None:
        self.__client_id = id
        self.__client_name = name
        self.__phone = phone
        self.__email = email
        self.__services = []
        self.__registry = {}

    def get_client_details(self):
        return (self.__client_id, self.__client_name, self.__phone, self.__email,len(self.__services), len(self.__registry))
    
    def get_name(self):
        return self.__client_name
    
    def add_service(self, service):
        self.__services.append(service)

    def add_registry(self, order_number, service):
        self.__registry[order_number] = service

    def get_services(self):
        return self.__services
    
    def get_registry(self):
        return self.__registry

class Services:

    def __init__(self, qty, service, price) -> None:
        self.service = (qty, service, price)

    def get_services_details(self):
        return self.service