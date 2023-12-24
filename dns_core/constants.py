
"""This module defines project constants"""

# DNS TYPE constants
TYPE_A = 1  # a host address
TYPE_NS = 2  # an authoritative name server
TYPE_MD = 3  # a mail destination (Obsolete - use MX)
TYPE_MF = 4  # a mail forwarder (Obsolete - use MX)
TYPE_CNAME = 5  # the canonical name for an alias
TYPE_SOA = 6  # marks the start of a zone of authority
TYPE_MB = 7  # a mailbox domain name (EXPERIMENTAL)
TYPE_MG = 8  # a mail group member (EXPERIMENTAL)
TYPE_MR = 9  # a mail rename domain name (EXPERIMENTAL)
TYPE_NULL = 10  # a null RR (EXPERIMENTAL)
TYPE_WKS = 11  # a well-known service description
TYPE_PTR = 12  # a domain name pointer
TYPE_HINFO = 13  # host information
TYPE_MINFO = 14  # mailbox or mail list information
TYPE_MX = 15  # mail exchange
TYPE_TXT = 16  # text strings


# DNS CLASS constants
CLASS_IN = 1  # the Internet
CLASS_CS = 2  # the CSNET class (Obsolete - used only for examples in some obsolete RFCs)
CLASS_CH = 3  # the CHAOS class
CLASS_HS = 4  # Hesiod [Dyer 87]
