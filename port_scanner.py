import socket
import time
import concurrent.futures
import argparse
# testing host is scanme.nmap.org

def ThreadTCP():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(TCP_Scan, HOST, PORT) for PORT in range(1, 65535)]

        for f in concurrent.futures.as_completed(results):
            print(f.result()) if f.result() != None else None

def TCP_Scan(HOST, PORT):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scan:
            scan.settimeout(5)
            code = scan.connect_ex((HOST, PORT)) 
            if code ==  0:
                return f"Open port at: {PORT}"
            return None
    except TimeoutError:
            print("Time Out Error")
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="TCP port scanner")
    parser.add_argument("host", type=str, help="The Name of the host, without http protocol")
    args = parser.parse_args()
    try:    
        HOST = args.host
        print(f"Target: {HOST}")
        print(f"Start Time: {time.strftime("%m/%d/%Y %I:%M %p")}")
        print("-"*40)
        HOST = socket.gethostbyname(HOST)
        ThreadTCP()
        start = time.perf_counter
        
        end = time.perf_counter
        print(f"Scanner Finished! in {end-start}")
    except KeyboardInterrupt:
        print("You Stopped The Program")
    except socket.gaierror:
        print("Name or Service not known")
        

