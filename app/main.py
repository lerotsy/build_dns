import socket
import struct
from classes.DNSMessage import DNSMessage


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("127.0.0.1", 2053))
    
    while True:
        try:
            buf, source = udp_socket.recvfrom(512)
    
            # print('buffer is {}'.format(buf.decode()))
            message = DNSMessage(id=1234, qr=1)
            response = pack_dns_message(message)
            breakpoint()
            udp_socket.sendto(response, source)
        except Exception as e:
            print(f"Error receiving data: {e}")
            break

def pack_dns_message(message: DNSMessage) -> bytes:
    flags = (
        (message.qr << 15)
        | (message.opcode << 11)
        | (message.aa << 10)
        | (message.tc << 9)
        | (message.rd << 8)
        | (message.ra << 7)
        | (message.z << 4)
        | message.rcode
    )

    return struct.pack(
        ">HHHHHH",
        message.id,
        flags,
        message.qdcount,
        message.ancount,
        message.nscount,
        message.arcount
    )


if __name__ == "__main__":
    main()
