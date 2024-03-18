from datetime import datetime

successfulMemoryHits: int = 0

def log(message:str) -> None:
    """
    Logs server events, adding current time and formatting.
    """
    current_time = datetime.now()
    formatted_log_message = f"[{current_time:%Y-%m-%d %H:%M:%S}] {message}"
    print(formatted_log_message)
    with open(f"./logs/{current_time:%Y-%m-%d}.txt", "a") as log_file:
        log_file.write(f"{formatted_log_message} \n")

def logMemoryHit() -> None:
    """
    Logs a successful memory hit and counts the number of successful memory hits.
    """
    global successfulMemoryHits
    successfulMemoryHits = successfulMemoryHits + 1
    log(f"Accessed the server's resouces. Current number of memory hits: {successfulMemoryHits}")