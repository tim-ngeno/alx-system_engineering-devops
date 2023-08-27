# 0x09. Web infrastructure design

## Network Basics and Definition of Terms

A **network** is a collection of interconnected devices that can communicate and share resources. It enables data exchange between computers, servers, and other devices. Networking basics include understanding protocols (like TCP/IP), hardware components (routers, switches), and addressing (IP addresses).

## What is a Server?

A **server** is a computer or software system that provides services or resources to other computers, known as clients, over a network. Servers can be web servers, application servers, database servers, etc. For example, an email server stores and delivers emails to clients.

## What is a Web Server?

A **web server** is a server specifically designed to deliver web content to users' browsers. It receives HTTP requests from clients, retrieves web pages or files, and sends them as responses. For instance, Apache and Nginx are popular web servers.

## DNS

**DNS (Domain Name System)** translates human-readable domain names (like www.example.com) into IP addresses that computers use to locate servers on the internet. It's like a phonebook for the internet. For example, translating 'google.com' to its corresponding IP address.

## Load Balancer

A **load balancer** distributes incoming network traffic across multiple servers to ensure efficient utilization and prevent overload on any single server. This enhances performance and availability. Imagine a restaurant with multiple chefs cooking food for incoming orders.

## Monitoring

**Monitoring** involves observing and tracking system performance, availability, and other key metrics. It helps identify issues and ensure optimal operation. Monitoring tools like Prometheus or Nagios provide real-time insights into server health.

## What is a Database

A **database** is an organized collection of structured information or data, typically stored in digital form. It allows for efficient storage, retrieval, and manipulation of data. Examples include MySQL, PostgreSQL, and MongoDB.

## Web Server vs. App Server

A **web server** serves static content (HTML, CSS, images) to clients. An **app server** handles dynamic processing, executing code and generating content based on user input. Think of a web server as a waiter serving menu pages and an app server as the chef cooking customized dishes.

## DNS Record Types

DNS uses various **record types** to store different types of information. Some common types include:
- **A Record**: Maps a domain to an IPv4 address (e.g., www.example.com → 192.168.1.1).
- **CNAME Record**: Creates an alias for a domain (e.g., blog.example.com → www.example.com).
- **MX Record**: Specifies mail servers for receiving emails (e.g., example.com → mail.example.com).

## Single Point of Failure

A **single point of failure** is a component in a system that, if it fails, can bring down the entire system. For example, if a website's only server crashes, the site becomes inaccessible.

## Avoiding Downtime during Code Deployment

To prevent downtime, practices like **blue-green deployment** (swapping between old and new versions) or using a **rolling deployment** (gradual update of instances) can be employed. This ensures continuous service availability.

## High Availability Cluster

A **high availability cluster** ensures system resilience. In **active-active**, all nodes are actively serving traffic. In **active-passive**, a standby node takes over if the active node fails. This minimizes downtime and provides redundancy.

## What is HTTPS

**HTTPS (Hypertext Transfer Protocol Secure)** is a secure version of HTTP. It encrypts data exchanged between a user's browser and a web server, ensuring confidentiality and integrity. It's symbolized by the padlock icon in the browser's address bar.

## What is a Firewall

A **firewall** is a security device or software that monitors and controls incoming and outgoing network traffic. It establishes a barrier between trusted internal networks and untrusted external networks, safeguarding against unauthorized access and threats.

---