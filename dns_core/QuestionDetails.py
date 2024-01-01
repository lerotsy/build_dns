from dataclasses import dataclass
import struct
from typing import Union

@dataclass
class QuestionDetails:
    qname: Union[str, bytes]  # Question Name
    qtype: int  # Question Type (16 bits)
    qclass: int # Question Class (16 bits)

    def __post_init__(self):
        from .dns_request_handler import encode_name
        # if we pass a string like 'codecracters.io' we need encode it
        if isinstance(self.qname, str):
            self.qname = encode_name(self.qname)

    def to_bytes(self) -> bytes:
        return self.qname + struct.pack(">HH", self.qtype, self.qclass)