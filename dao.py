import requests

class Dao:
    def __init__(self, ip, port):
        """
        """
        self.ip = ip
        self.port = port

    def price(self, year, month, day, hour, minute):
        """ Send get request to server
        """
        raise NotImplementedError
        # base_url = self.ip + ':' + self.port
        # query = f"year={year}&month={month}&day={day}&hour={hour}&minute={minute}"

        # # request url
        # req = f"{base_url}?{query}"

        # requests.get(req)

    def signal(self, year, month, day, hour, minute):
        raise NotImplementedError

    def server_address(self, ip, port):
        """ Setter function for port and ip
        """
        self.ip = ip
        self.port = port

    def del_ticker(self, ticket_id):
        raise NotImplementedError

    def add_ticker(self, ticket_id):
        raise NotImplementedError