import sys
from controller import Controller
from service import Service
from dao import Dao


# init dependency chain
dao = Dao(ip="127.0.0.1", port="8000")
service = Service(dao)
controller = Controller(service)

# first argument is file name
args = sys.argv[1:]
cmd = args[0]
args = args[1:]
if cmd == "--price":
    controller.price(args)
elif cmd == "--signal":
    controller.signal(args)
elif cmd == "--server_address":
    controller.server_address(args)
elif cmd == "--del_ticker":
    controller.del_ticker(args)
elif cmd == "--add_ticker":
    controller.add_ticker(args)
elif cmd == "--reset":
    raise NotImplementedError
else:
    raise ValueError("Illegal Arguments")
