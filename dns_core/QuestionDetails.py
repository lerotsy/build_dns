from dataclasses import dataclass
import struct

@dataclass
class QuestionDetails:
    qname: str  # Question Name
    qtype: int  # Question Type (16 bits)
    qclass: int # Question Class (16 bits)

    def __post_init__(self):
        from .MessageFormatter import encode_name
        self.qname = encode_name(self.qname)

    def to_bytes(self) -> bytes:
        return self.qname + struct.pack(">HH", self.qtype, self.qclass)