class Controller:
    def __init__(self, service):
        self.service = service
    
    def tickers(self, args):
        """
        """
        # args.split(',')
        self.service.tickers

    def port(self, args):
        """
        """
        if len(args) != 1:
            raise ValueError("invalid port number")
        return self.service.port(args[0])

    def reload(self, filename):
        """
        """
        pass

    def minutes(self, t):
        """
        """
        pass