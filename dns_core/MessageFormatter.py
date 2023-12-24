from .DNSMessage import DNSMessage
import struct

class MessageFormatter:
    @staticmethod
    def pack_dns_message(message: DNSMessage) -> bytes:
        header = MessageFormatter.build_header(message)
        question = MessageFormatter.build_question(message)
        answer = MessageFormatter.build_answer(message)

        return (
            header
            + question
            + answer
        )

    @staticmethod
    def build_header(message: DNSMessage) -> bytes:
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

    @staticmethod
    def build_answer(message: DNSMessage) -> bytes:
        name = message.answer.rname
        type = struct.pack(">H", message.answer.rtype)
        class_value = struct.pack(">H", message.answer.rclass)
        ttl = struct.pack(">I", message.answer.rttl)
        length = struct.pack(">H", message.answer.rlength)
        data = message.answer.rdata
        return name + type + class_value + ttl + length + data

    @staticmethod
    def build_question(message: DNSMessage) -> bytes:
        encoded_question = encode_name(message.qname)
        return encoded_question + struct.pack(">HH", message.qtype, message.qclass)
    
def encode_name(url: str) -> bytes:
    labels = url.split('.')
    encoded_labels = [bytes([len(l)]) + l.encode('utf-8') for l in labels]
    # Add the null terminator at the end
    encoded_labels.append(b'\x00')
    return b''.join(encoded_labels) 