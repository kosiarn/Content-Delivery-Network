from requests import get
from config import central_server_address
from logger import log, logCentralServerHit

central_server_ping = get(f"{central_server_address}/ping")

if central_server_ping.content != "pong!":
    log("Central server unreachable!")

def fetchFromCentralServer(attachment_name):
    """
    Attempts to fetch an attachment from central server.
    """
    request_address = f"{central_server_address}/attachment/{attachment_name}"
    central_server_fetch_request = get(request_address)
    if central_server_fetch_request.status_code == 200:
        logCentralServerHit()
        return central_server_fetch_request.content
    raise FileNotFoundError