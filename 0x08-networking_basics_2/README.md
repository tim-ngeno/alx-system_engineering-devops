# Networking Concepts #1

## What is localhost/127.0.0.1

**localhost** or **127.0.0.1** is a special IP address that refers to the loopback network interface on the local machine.

It is used to establish network connections with services running on the same device. When a program or service on the machine communicates with the localhost IP address, it is essentially communicating with itself.

## What is 0.0.0.0

**0.0.0.0** is a reserved IP address that represents an invalid or unknown target. It is used in various network-related contexts, such as in routing tables or when configuring network devices.

In the context of a server or listening service, binding to 0.0.0.0 means that the service is listening on all available network interfaces on the host.

## What is /etc/hosts

**/etc/hosts** is a plain text file on Unix-like operating systems (including Linux and macOS) that maps hostnames to IP addresses. It is used to manually configure the mapping of domain names to specific IP addresses, bypassing the need for DNS resolution. 

Entries in the /etc/hosts file take precedence over DNS lookups for the specified hostnames.

## How to display your machine’s active network interfaces

To display your machine's active network interfaces, you can use various commands depending on your operating system:

### Linux (using ifconfig):
```
ifconfig
```

### Linux (using ip command):
```
ip addr show
```

### macOS (using ifconfig):
```
ifconfig
```

### Windows (using ipconfig):
```
ipconfig
```

These commands will provide information about the active network interfaces on your machine, including their IP addresses, network masks, and other relevant details.

---