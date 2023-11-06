import concurrent.futures
import socket
import sys
from datetime import datetime

def worker(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        connection_status = s.connect_ex((target, port))

        if connection_status == 0:
            print(f"Port {port} is open")
        s.close()

    except KeyboardInterrupt:
        print("Keyboard Interrupt\nExiting program...")
        sys.exit()

    except socket.gaierror:
        print("Could not resolve hostname")
        sys.exit()

    except socket.error:
        print("Could not connect to the server")
        sys.exit()

if __name__ == "__main__":
    if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1])
    else:
        print('Invalid Usage')
        print('Syntax: python <shittyportscanner.py directory> <IP Address>')
        sys.exit()

    print('-' * 60)
    print('Portscan began at: ' + str(datetime.now()))

    # Create a thread pool of 20 max workers
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        # Define a list of port ranges to scan
        port_ranges = [(1, 50), (51, 100), (101, 150), (151, 200), (201, 250), (251, 300), (301, 350), (351, 400), (401, 450), (451, 500), (501, 550), (551, 600), (601, 650), (651, 700), (701, 750), (751, 800), (801, 850), (851,900), (901, 950), (951, 1001)]  # Add more ranges as needed

        # Submit tasks for each port in the specified ranges
        for port_range in port_ranges:
            for port in range(port_range[0], port_range[1] + 1):
                executor.submit(worker, port)

    print("Portscan completed at: " + str(datetime.now()))