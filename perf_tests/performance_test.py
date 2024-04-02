from time import time as current_time_in_seconds
import test_config
import random
from requests import get
from statistics import mean

get_random_attachment = lambda: random.choice(test_config.available_attachments)

def measureResponseTime(server_address: str) -> int:
    """
    Measures the server's response time in seconds.
    """
    request_url = f"{server_address}/attachment/{get_random_attachment()}"
    request_time = current_time_in_seconds()
    get(request_url)
    response_time = current_time_in_seconds()
    return(response_time - request_time)

def testServerPerformance(server_address: str) -> None:
    """
    Measures server's performance based on its response times.
    """
    response_times = list()
    for request in range(test_config.NUM_REQUESTS_PER_TEST):
        request_response_time = measureResponseTime(server_address)
        response_times.append(request_response_time)
    print(
        f"""
Server performance test results for {test_config.NUM_REQUESTS_PER_TEST} requests:
Average response time: {mean(response_times)}
Longest response time: {max(response_times)}
Shortest response time: {min(response_times)}
""")
    
if __name__ == "__main__":
    print("Running comparative tests for CDN.")
    print("Test for: connection with central server(bypassing the edge server)")
    testServerPerformance(test_config.CENTRAL_SERVER_ADDRESS)
    print("Test for: connection with edge server")
    testServerPerformance(test_config.EDGE_SERVER_ADDRESS)