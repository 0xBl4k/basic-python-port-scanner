import socket
import time
# testing host is scanme.nmap.org

try:    
    HOST = socket.gethostbyname('scanme.nmap.org')
    print(f"Target: {HOST}")
    print(f"Start Time: {time.strftime("%m/%d/%Y %I:%M %p")}")
    print("-"*40)

    for PORT in range(1, 65535):
            scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            scan.settimeout(1)
            try:
                code = scan.connect_ex((HOST, PORT)) 
                if code ==  0:
                    print(f"Open port at: {PORT}")
            except TimeoutError:
                 pass
            scan.close()

except KeyboardInterrupt:
    print("You Stopped The Program")
except socket.gaierror:
    print("Name or Service not known")
       

