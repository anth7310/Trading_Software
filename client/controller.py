class Controller:
    def __init__(self, service):
        """ Controller Object
        """
        self.service = service

    def price(self, args):
        """
        """
        data = self.__validate_date(args)
        return self.service.price(*data)

    def signal(self, args):
        """
        """
        data = self.__validate_date(args)
        return self.service.signal(*data)

    def server_address(self, args):
        """ Connect to a server
        if not specified, default to
        127.0.0.1:8000
        """
        server = args.split(':')
        if len(server) == 2:
            ip, port = server
            return self.service.server_address(ip, port)
        elif len(server) == 1:
            ip = server[0]
            # default port is 8000
            return self.service.server_address(ip, 8000)

    def del_ticker(self, args):
        """ Delete ticker
        """
        ticket = args[0]
        return self.server.del_ticker(ticket)

    def add_ticker(self, args):
        """ Add ticket
        """
        ticket = args[0]
        return self.server.del_ticker(ticket)

    def __validate_date(self, args):
        """ Validate date from CLI
        raise ValueError if invalid
        """
        args = args.split('-')
        if len(args) != 4:
            raise ValueError("Invalid Date")
        year, month, day, t = args
        t = t.split(':')
        if len(t) != 2:
            raise ValueError("Invalid hour-minute")
        hour, minute = t
        return year, month, day, hour, minute
    