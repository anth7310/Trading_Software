from datetime import datetime

class Service:
    def __init__(self, dao):
        self.dao = dao
    
    def price(self, year, month, day, hour, minute):
        if not self.__validate_dates(year, month, day, hour, minute):
            raise ValueError("Invalid values")
        return self.dao.price(year, month, day, hour, minute)
    
    def signal(self, year, month, day, hour, minute):
        if not self.__validate_dates(year, month, day, hour, minute):
            raise ValueError("Invalid values")
        return self.dao.signal(year, month, day, hour, minute)

    def server_address(self, ip, port):
        if not self.__validate_server_address(ip, port):
            raise ValueError("Invalid input")
        return self.dao.server_address(ip, port)

    def del_ticker(self, ticket_id):
        return self.dao.del_ticket(ticket_id)

    def add_ticker(self, ticket_id):
        return self.dao.add_ticker(ticket_id)

    def __validate_dates(self, year, month, day, hour, minute):
        """ validate datetime
        """
        try:
            datetime(year=year,month=month,day=day,hour=hour, minute=minute)
            return True
        except ValueError:
            return False

    def __validate_server_address(self, ip, port):
        #TODO
        pass

