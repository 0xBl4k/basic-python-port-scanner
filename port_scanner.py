import socket

# testing host is scanme.nmap.org

#HOST = socket.gethostbyname(socket.gethostname())
HOST = 'scanme.nmap.org'
print(f"Target: {HOST}")
print("-"*40)
try:    
    for PORT in range(1, 201):
        scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scan.settimeout(5)
        code = scan.connect_ex((HOST, PORT)) 
        if code ==  0:
            print(f"Port {PORT} is open")
except KeyboardInterrupt:
    print("You Stopped The Program") 
       

