from dataclasses import dataclass
import struct
from typing import Union

@dataclass
class AnswerDetails:
    rname: Union[str, bytes]
    rtype: int
    rclass: int
    rttl: int
    rdata: bytes
    rlength: int = 0

    def __post_init__(self):
        from .dns_request_handler import encode_name
        if isinstance(self.rname, str):
            self.rname = encode_name(self.rname)
        self.rlength = len(self.rdata)
    
    def to_bytes(self) -> bytes:
        name = self.rname
        type = struct.pack(">H", self.rtype)
        class_value = struct.pack(">H", self.rclass)
        ttl = struct.pack(">I", self.rttl)
        length = struct.pack(">H", self.rlength)
        data = self.rdata
        return name + type + class_value + ttl + length + data

