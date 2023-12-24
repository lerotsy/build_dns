from dataclasses import dataclass
import struct

@dataclass
class AnswerDetails:
    rname: str
    rtype: int
    rclass: int
    rttl: int
    rdata: bytes
    rlength: int = 0

    def __post_init__(self):
        from .MessageFormatter import encode_name
        self.rname = encode_name(self.rname)
        self.rlength = len(self.rdata)

