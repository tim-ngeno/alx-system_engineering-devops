
# Application Programming Interfaces (APIs)

# Overview
This provides a comprehensive guide on APIs, related terms, and Pythonic naming conventions.

## Table of Contents

1. [Bash Scripting Limitations](#bash-scripting-limitations)
2. [Introduction to APIs](#introduction-to-apis)
3. [Understanding REST APIs](#understanding-rest-apis)
4. [Microservices Explained](#microservices-explained)
5. [Introduction to CSV](#introduction-to-csv)
6. [Introduction to JSON](#introduction-to-json)
7. [Pythonic Naming Conventions](#pythonic-naming-conventions)
    - [Packages and Modules](#packages-and-modules)
    - [Classes](#classes)
    - [Variables](#variables)
    - [Functions](#functions)
    - [Constants](#constants)
8. [Significance of CapWords or CamelCase in Python](#significance-of-capwords-or-camelcase-in-python)


## Bash Scripting Limitations

While Bash scripting is powerful for quick scripts and automation, there are tasks better suited to other languages or tools. [This article](https://www.turnkeylinux.org/blog/friends-dont-let-friends-program-shell-script) goes in-depth on why you might reconsider using Bash for complex tasks. Key reasons include:
- **Lack of data structures**: Bash lacks native support for common data structures like arrays or dictionaries.
- **Limited error handling**: Without native exceptions or detailed error types, debugging can be complex.
- **Inherent complexity**: As a script grows, maintaining it can become challenging.

## Introduction to APIs

An **API** or **Application Programming Interface** is a set of rules and protocols that allow software applications to communicate.


## Understanding REST APIs

A **REST API** uses HTTP requests for CRUD operations (Create, Read, Update, Delete). 

```http
GET /users          # Retrieve list of users
POST /users         # Create a new user
PUT /users/1        # Update user with ID 1
DELETE /users/1     # Delete user with ID 1
```

## Microservices Explained

In a **Microservices** architecture, each functionality of an application is a separate service. For example, an e-commerce application might have:

- User Service
- Order Service
- Inventory Service

Each communicates via APIs and can be developed, deployed, and scaled independently.

## Introduction to CSV

A **CSV** file might look like:
```
name,age,occupation
Alice,28,Engineer
Bob,22,Designer
```

## Introduction to JSON

JSON is often used for configuration files and data interchange.

```json
{
  "name": "John",
  "age": 30,
  "city": "New York"
}
```

## Pythonic Naming Conventions

### Packages and Modules

```python
# Good module names
import decoder
import html_parser
```

### Classes

```python
# Good class name
class UserAccount:
    pass

# Bad class name
class user_account:
    pass
```

### Variables

```python
# Good variable names
user_name = "John"
word_list = ["apple", "banana"]

# Bad variable names
u = "John"
w = ["apple", "banana"]
```

### Functions

```python
# Good function name
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# Bad function name
def calc_av(nums):
    return sum(nums) / len(nums)
```

### Constants

```python
# Good constant names
PI = 3.14159
MAX_SIZE = 100

# Bad constant name
maxSize = 100
```

## Significance of CapWords or CamelCase in Python

In Python, CapWords or CamelCase helps distinguish between class names and other identifiers.

```python
# Class name in CamelCase
class UserDatabase:
    pass

# Variable name in snake_case
user_database_instance = UserDatabase()
```

---