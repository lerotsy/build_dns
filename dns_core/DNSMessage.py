from dataclasses import dataclass
from .AnswerDetails import AnswerDetails
from .HeaderDetails import HeaderDetails
from typing import Optional
@dataclass
class DNSMessage:
    # Question
    qname: str
    qtype: int
    qclass: int
    # Header
    header: HeaderDetails
    # Answer
    answer: Optional[AnswerDetails] = None
