from datetime import datetime

def log(message:str) -> None:
    """
    Logs server events, adding current time and formatting.
    """
    current_time = datetime.now()
    formatted_log_message = f"[{current_time:%Y-%m-%d %H:%M:%S}] {message}"
    print(formatted_log_message)