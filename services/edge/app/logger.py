from datetime import datetime
import os

successfulCentralServerHits: int = 0
successfulCacheHits: int = 0

def log(message:str) -> None:
    """
    Logs server events, adding current time and formatting.
    """
    current_time = datetime.now()
    formatted_log_message = f"[{current_time:%Y-%m-%d %H:%M:%S}] {message}"
    print(formatted_log_message)
    with open(f"./logs/{current_time:%Y-%m-%d}.txt", "a") as log_file:
        log_file.write(f"{formatted_log_message} \n")

logDirExists = os.path.exists(r".\\logs\\")

if not logDirExists:
    try:
        os.makedirs(r".\\logs\\")
    except:
        log: function = lambda message: print(message)
        log("Couldn't create log directory; log messages won't be saved.")

def logCentralServerHit() -> None:
    """
    Logs a successful central server hit and counts the number of successful central server hits.
    """
    global successfulCentralServerHits
    successfulCentralServerHits = successfulCentralServerHits + 1
    log(f"Accessed the central server's resouces. Current number of central server hits: {successfulCentralServerHits}")

def logCacheHit() -> None:
    """
    Logs a cache hit.
    """
    global successfulCacheHits
    successfulCacheHits = successfulCacheHits + 1
    log(f"Accessed the cache. Current number of cache hits: {successfulCacheHits}")