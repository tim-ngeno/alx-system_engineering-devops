# Web Servers and Configuration of Nginx

A web server can be understood both in terms of hardware and software. In its most basic definition, a web server serves web pages to users' browsers via the internet.

**1. Web Server (Hardware):**
   * **Computer Hardware:** At its core, the hardware of a web server is similar to that of a regular computer. It typically has a processor, RAM, storage devices, and other basic components. However, it is often optimized for tasks related to serving content rather than for tasks such as gaming or word processing.
   * **Network Connection:** A robust and high-speed network connection is crucial for web servers because they need to handle many requests and send data to users across the internet.

**2. Web Server (Software):**
   * **Basic Functionality:** The primary function of web server software is to store, process, and serve web pages to users. When a user requests a page (usually by typing a URL into a browser), the web server locates the page, processes any necessary scripts, and then sends the resulting content back to the user's browser.
   * **Common Web Servers:** Popular web server software includes Apache, Nginx, Microsoft's Internet Information Services (IIS), and LiteSpeed.
   * **HTTP/HTTPS Protocols:** Web servers operate using the Hypertext Transfer Protocol (HTTP) and its secure version HTTPS. These protocols dictate how messages are formulated and transmitted on the web.
   * **Dynamic Content:** Modern web servers often work in conjunction with other software (like database servers or application servers) to produce dynamic content. For example, when you use a search function on a website, the web server might query a database server to get the results and then use an application server to format those results into a web page before finally sending it to your browser.

**3. Components & Features of Web Servers:**
   * **Request Handling:** Web servers can manage and prioritize multiple requests. They can serve multiple clients simultaneously using a mechanism called multi-threading.
   * **Logging:** Servers keep logs for all requests, errors, and other important events. This helps in debugging, analyzing traffic patterns, and monitoring server health.
   * **Security:** Web servers have features to enhance security. This includes the use of Secure Sockets Layer (SSL)/Transport Layer Security (TLS) for encrypted connections, firewalls, and configurations to ward off potential threats.
   * **Static vs. Dynamic Content:** While web servers can deliver static content (like HTML pages, images, CSS, and JavaScript files), they often integrate with other tools and platforms (like PHP, Python, or Node.js) to generate dynamic content based on user input or database interactions.

**4. Working of a Web Server:**
   1. A user enters a URL in their web browser or clicks on a link.
   2. The browser sends an HTTP request to the web server hosting the desired website.
   3. The web server processes the request. If the request is for a static file, it retrieves the file. If the request is for dynamic content, the server might interact with other software to produce the appropriate content.
   4. Once the content is ready, the server sends it back to the user's browser in an HTTP response.
   5. The user's browser displays the content to the user.


Typically, a web server plays a pivotal role in the world of the internet by being the middleman between users and the content they seek online. It handles requests, retrieves or processes content, and ensures that users get the data they've asked for.

## How the Web Works

The web operates on a client-server model where clients request resources, and servers provide them. Communication typically happens over the HTTP or HTTPS protocols.

## Role of a Web Server

The main role of a web server is to store, process, and deliver web pages to users.

## Nginx

Nginx is a high-performance, scalable, and more resource-friendly web server compared to others. It can also act as a reverse proxy server for HTTP, HTTPS, SMTP, POP3, and IMAP protocols.

## Configuring Nginx

To configure Nginx, modify the main configuration file usually located at `/etc/nginx/nginx.conf`. The actual virtual server configurations are typically placed in `/etc/nginx/conf.d/` or `/etc/nginx/sites-available`.

## Child Processes

In computing, a child process is a process that is spawned by another process, which is the parent process.


## Understanding Child Processes

A child process in computing is a process created by another process (its parent). This creation mechanism ensures controlled and hierarchical spawning of processes.

## Parent and Child Processes in Web Servers

Web servers use a primary process to manage settings and configurations and spawn child processes to handle incoming requests. This ensures efficiency and scalability.


## Domains: Root and Subdomains

- **Root Domain**: This refers to the primary domain name without any prefixes. Example: `example.com`.
- **Subdomain**: It's a subset of the main domain, often used to organize and navigate to different sections of the website. Example: `blog.example.com`.

## HTTP Requests and Status Codes

HTTP operates as a request-response protocol. The main types of HTTP requests include GET, POST, PUT, DELETE, etc. Status codes indicate the result of the HTTP request, with common ones being `200 OK`, `404 Not Found`, and `500 Internal Server Error`.



## Main HTTP Requests

The primary HTTP methods or requests are:
- **GET**: Retrieve data
- **POST**: Submit data for processing
- **PUT**: Update existing data
- **DELETE**: Remove data
