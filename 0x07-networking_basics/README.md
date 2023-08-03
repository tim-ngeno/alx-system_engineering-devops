# Networking Basics #0

## What is OSI Model

The OSI (Open Systems Interconnection) model is a conceptual framework used to understand and describe how different networking protocols interact and communicate with each other. It defines seven distinct layers, each responsible for specific tasks in the data transmission process.

The OSI model consists of seven layers, which are:

1. **Physical Layer**
2. **Data Link Layer**
3. **Network Layer**
4. **Transport Layer**
5. **Session Layer**
6. **Presentation Layer**
7. **Application Layer**

## Organization of the OSI model

The OSI model is organized in a hierarchical manner, with each layer building upon the functionalities of the layers below it. Data is transmitted from the top layer (Application Layer) down to the bottom layer (Physical Layer) and vice versa during the communication process.

## What is a LAN

A LAN (Local Area Network) is a network of interconnected devices within a limited geographical area, such as a home, office, or campus. It allows for the sharing of resources and data between connected devices.

### Typical usage

LANs are commonly used in homes and businesses to facilitate local communication, share files and printers, and access shared resources.

### Typical geographical size

The geographical size of a LAN typically covers a small area, such as a single building or a group of nearby buildings.

## What is a WAN

A WAN (Wide Area Network) is a network that spans a large geographical area, connecting multiple LANs and other networks over long distances.

### Typical usage

WANs are used to establish communication between geographically distant locations, such as connecting offices in different cities or countries.

### Typical geographical size

The geographical size of a WAN can span across cities, countries, or even continents, enabling global connectivity.

## What is the Internet

The Internet is a global network of interconnected computers and servers that allows users to access and share information across the world.

## What is an IP address

An IP address (Internet Protocol address) is a unique numerical label assigned to each device connected to a network. It serves as an identifier for locating and communicating with devices on the Internet.

## Types of IP addresses

There are two types of IP addresses:

1. **IPv4 (Internet Protocol version 4)**: This is the most widely used version of IP addresses, represented in a 32-bit format (e.g., 192.168.0.1).
2. **IPv6 (Internet Protocol version 6)**: This is the newer version of IP addresses, represented in a 128-bit format (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334).

### Why IPv6 was created

IPv6 was created to address the growing shortage of available IPv4 addresses due to the expansion of the Internet. With its larger address space, IPv6 can support a virtually unlimited number of devices and ensure the continued growth of the Internet.

## Public and Private IP address
A public IP address is an IP address that can be accessed over the Internet. Like a postal address used to deliver a postal mail to your home, a public IP address is the globally unique IP address assigned to a computing device

Private IP address, on the other hand, is used to assign computers within your private space without directly exposing them to the Internet.

- In this scenario, your router gets the public IP address, and each of the computers, tablets and smartphones connected to your router (via wired or wifi) gets a private IP address from your router via DHCP protocol.

## What is localhost

"localhost" is a loopback address referring to the current device or computer that a user is working on. It is often represented by the IP address 127.0.0.1 and is used to access the services and resources on the local machine.

## What is a subnet

A subnet is a smaller division of a larger network. It allows network administrators to segment a large network into smaller, more manageable sub-networks, enhancing security and performance.



## TCP/UDP

TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) are two commonly used transport layer protocols in the OSI model.


### Difference between TCP and UDP

The main difference between TCP and UDP is their approach to data transmission:

1. **TCP**: Provides reliable, connection-oriented data transmission. It ensures data delivery by establishing a connection between sender and receiver, guaranteeing that all data packets arrive in the correct order and without errors.
2. **UDP**: Provides unreliable, connectionless data transmission. It does not establish a connection before transmitting data, making it faster but less reliable, as there is no guarantee that all data packets will reach the destination.

## What is a port

A port is a communication endpoint in a networked device, identified by a 16-bit number. It enables multiple applications or services on the same device to establish simultaneous network connections.

### Some common port numbers

- **SSH (Secure Shell)**: Port 22
- **HTTP (Hypertext Transfer Protocol)**: Port 80
- **HTTPS (Hypertext Transfer Protocol Secure)**: Port 443

## Ping
The Ping tool or ICMP (Internet Control Message Protocol) is often used to check if a device is connected to a network. It sends a simple request to the device, and if the device responds, it indicates that the device is reachable and connected to the network.

---