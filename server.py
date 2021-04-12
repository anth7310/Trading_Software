from config import api_key

import flask
from flask import request
import database as db
import subprocess



app = flask.Flask(__name__)

@app.route('/api/v1/price', methods=['GET'])
def api_price():
    """
    Queries server for latest price available as of the time specified.
    The time query is expected to be in UTC time.
    Example output:
    AAPL    332.50
    MSFT    180.30
    FB      No Data
    """
    queries = ['year', 'month', 'day', 'hour', 'minute']
    data = {}
    for query in queries:
        data[query] = request.args.get(query)
    # TODO: return output
    return data

@app.route('/api/v1/signal', methods=['GET'])
def api_signal():
    """
    Queries server for latest trading signal avaiable as of the tie
    specified. The time queried is expected to be in UTC Time.
    Answer can either be 1, -1, or 0
    1   :   Success
    0   :   Ticket not found
    -1  :   Server Error
    If server has no data outputs:
        Server has no data
    Example output:
    AAPL    1
    MSFT    1
    FB      0
    """
    queries = ['year', 'month', 'day', 'hour', 'minute']
    data = {}
    for query in queries:
        data[query] = request.args.get(query)

@app.route('/api/v1/delete/<ticker>', methods=['DELETE'])
def api_del_ticker(ticker):
    """
    Instruct server to delete a ticker from the server database
    Returns:
        0=success
        1=server error
        2=ticker not found
    """
    #TODO: Delete data from database
    pass

@app.route('/api/v1/add/<ticker>', methods=['POST'])
def api_add_ticker(ticker):
    """
    Instruct server to add a ticker to the server database. Server will
    download historical data for said ticket, and start appending
    on the next pull
    Returns:
        0=success
        1=server error
        2=ticker not found
    """
    #TODO: Run subprocess
    pass

@app.route('/api/v1/reset', methods=['DELETE'])
def api_reset(ticker):
    """ 
    Delete all information on server.
    Client exits with return code
    0=success
    1=failure
    """
    db.delete()



if __name__ == "__main__":
    # run subprocess in background
    # subprocess.Popen(["python3", "./collect.py", ])
    ip = "127.0.0.1"
    port = 8000
    app.run(host=ip, port=port, debug=True)
