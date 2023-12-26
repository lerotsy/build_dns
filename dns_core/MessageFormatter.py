import struct
from .constants import TYPE_A, CLASS_IN

class MessageFormatter:
    @staticmethod
    def parse_question(question_section: bytes = b''):
        from .QuestionDetails import QuestionDetails
        # hardcoded for now
        return QuestionDetails(qname='codecrafters.io', qtype=TYPE_A, qclass=CLASS_IN )

    @staticmethod
    def parse_header(header: bytes):
        from .HeaderDetails import HeaderDetails
        if len(header) != 12:
            raise ValueError("header must be of length 12")

        id, flags, qdcount, ancount, nscount, arcount = struct.unpack('>HHHHHH', header)
        qr = 1
        opcode = (flags >> 11) & 0b1111
        rd = (flags >> 8) & 0b1
        rcode = 0 if opcode == 0 else 4

        return HeaderDetails(
            id=id,
            qr=qr,
            opcode=opcode,
            rd=rd,
            rcode=rcode,
            qdcount=qdcount,
            ancount=ancount,
            nscount=nscount,
            arcount=arcount
        )

    @staticmethod
    def process(buffer: bytes) -> bytes:
        from .AnswerDetails import AnswerDetails
        header_section = buffer[:12] # header always the first 12 bytes
        header = MessageFormatter.parse_header(header_section)
        question = MessageFormatter.parse_question()
        answer = AnswerDetails(rname='codecrafters.io', rtype=TYPE_A, rttl=60, rclass=CLASS_IN, rdata=b'\x08\x08\x08\x08')
        # breakpoint()
        return (
            header.to_bytes()
            + question.to_bytes()
            + answer.to_bytes()
        )


    
def encode_name(url: str) -> bytes:
    labels = url.split('.')
    encoded_labels = [bytes([len(l)]) + l.encode('utf-8') for l in labels]
    # Add the null terminator at the end
    encoded_labels.append(b'\x00')
    return b''.join(encoded_labels)
