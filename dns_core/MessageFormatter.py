from .DNSMessage import DNSMessage
import struct

class MessageFormatter:
    @staticmethod
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
        encoded_question = MessageFormatter.encode_labels(message.qname)

        return (
            struct.pack(
                ">HHHHHH",
                message.id,
                flags,
                message.qdcount,
                message.ancount,
                message.nscount,
                message.arcount
            )
            + encoded_question
            + struct.pack(">HH", message.qtype, message.qclass)
        )

    @staticmethod
    def encode_labels(url: str) -> bytes:
        labels = url.split('.')
        encoded_labels = [bytes([len(l)]) + l.encode('utf-8') for l in labels]
        # Add the null terminator at the end
        encoded_labels.append(b'\x00')
        return b''.join(encoded_labels) 