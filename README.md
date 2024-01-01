# DNS Server challenge from CodeCrafters
This is a starting point for Python solutions to the
["Build Your Own DNS server" Challenge](https://app.codecrafters.io/courses/dns-server/overview).


This project is my implementation of a DNS server for a coding challenge on the CC platform. Developed using Python 3.11, the server is designed to parse and create DNS packets, respond to DNS queries, and handle various DNS record types, including A, AAAA, and CNAME, among others. While the server has limited functionality and primarily focuses on parsing DNS packets and providing hardcoded responses, it serves as a practical exercise in understanding the DNS protocol, packet format, and the roles of different types of DNS servers.


**Note**: If you're viewing this repo on GitHub, head over to
[codecrafters.io](https://codecrafters.io) to try the challenge.


## Functionality

1. **UDP Socket**: Utilizes a UDP socket to receive DNS queries from clients.

2. **DNS Message Parsing**: Parses the DNS message, which is comprised of five sections:
   - **Header Section**: Extracts metadata from the DNS message.
   - **Question Section**: Interprets query details such as domain name and type.
   - **Answer Section**: Hardcoded for the scope of this project.
   - *Note*: Authority and Additional sections are not used in this project.


## Limitations

This DNS server is a simplified version tailored for the Codecrafters coding challenge. It is not a comprehensive DNS server solution but rather a conceptual tool for educational purposes, focusing on the basics of DNS operation.
