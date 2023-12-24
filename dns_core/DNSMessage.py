from dataclasses import dataclass
from .AnswerDetails import AnswerDetails
from typing import Optional
@dataclass
class DNSMessage:
    #Question
    qname: str
    qtype: int
    qclass: int
    id: int  # 16 bits (Packet Identifier)
    qr: int  # 1 bit (Query/Response Indicator)
    opcode: int = 0  # 4 bits (Operation Code)
    aa: int = 0  # 1 bit (Authoritative Answer)
    tc: int = 0  # 1 bit (Truncation)
    rd: int = 0  # 1 bit (Recursion Desired)
    ra: int = 0  # 1 bit (Recursion Available)
    z: int = 0  # 3 bits (Reserved)
    rcode: int = 0  # 4 bits (Response Code)
    qdcount: int = 0  # 16 bits (Question Count)
    ancount: int = 0  # 16 bits (Answer Record Count)
    nscount: int = 0  # 16 bits (Authority Record Count)
    arcount: int = 0  # 16 bits (Additional Record Count)
    answer: Optional[AnswerDetails] = None
