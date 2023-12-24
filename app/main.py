import socket
import struct
from dns_core.DNSMessage import DNSMessage
from dns_core.AnswerDetails import AnswerDetails
from dns_core.MessageFormatter import MessageFormatter
from dns_core.constants import TYPE_A, CLASS_IN


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("127.0.0.1", 2053))
    
    while True:
        try:
            buf, source = udp_socket.recvfrom(512)

            answer = AnswerDetails(rname='codecrafters.io', rtype=TYPE_A, rclass=CLASS_IN, rdata=b'\x08\x08\x08\x08')
            message = DNSMessage(id=1234, qr=1, qdcount=1, qname='codecrafters.io', ancount=1, qtype=TYPE_A, qclass=CLASS_IN, answer=answer)
            response = MessageFormatter.pack_dns_message(message)
            udp_socket.sendto(response, source)
        except Exception as e:
            print(f"Error receiving data: {e}")
            break




if __name__ == "__main__":
    main()
