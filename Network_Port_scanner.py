import socket
import threading

# Target IP or hostname
target = input("Enter target IP or hostname: ")
start_port = 1
end_port = 1024

# Lock for synchronized console output
print_lock = threading.Lock()

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            with print_lock:
                print(f"[+] Port {port} is open")
        s.close()
    except:
        pass

def main():
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(port,))
        thread.start()

if __name__ == "__main__":
    main()