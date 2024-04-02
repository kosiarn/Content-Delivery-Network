from os import environ as env_settings

frontend_addresses = [
    "http://localhost:8000"
]
try:
    central_server_address = env_settings["CENTRAL_SERVER_ADDRESS"]
except KeyError:
    central_server_address = "http://localhost:8002"