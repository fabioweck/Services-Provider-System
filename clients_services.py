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
    
    def print_os(self, order_number):
        
        excel_file = FileHandler()
        excel_file.add_info(self.__client_name, order_number, self.__phone, self.__client_id, self.__services)
        excel_file.convert_to_pdf(self.__client_name)

class Services:

    def __init__(self, qty, service, price) -> None:
        self.service = (qty, service, price)

    def get_services_details(self):
        return self.service