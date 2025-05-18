# 📘 What is an API?

An **API (Application Programming Interface)** is a set of **rules and protocols** that allows one piece of software (client) to interact with another (server or service).

Think of it as a **waiter in a restaurant**:

* You (client) request a dish.
* The waiter (API) takes your request to the kitchen (server).
* The kitchen prepares it and the waiter brings back the result.



## 🧾 Types of APIs (With Examples)

| API Type               | Description                                                                 | Real-World Example                         |
| ---------------------- | --------------------------------------------------------------------------- | ------------------------------------------ |
| **1. Open/Public API** | Available to anyone, often free or with some limits.                        | Weather API, Google Maps API               |
| **2. Private API**     | Used internally within a company or application.                            | Internal HR or Payroll APIs in a company   |
| **3. Partner API**     | Shared between specific business partners, usually requires authentication. | Payment gateway API (e.g., PayPal API)     |
| **4. Composite API**   | Combines multiple APIs into a single call.                                  | A travel app API fetching flights + hotels |
| **5. REST API**        | Web API using HTTP methods and URLs, responds in JSON/XML.                  | `GET /api/users/`, `POST /api/login/`      |
| **6. SOAP API**        | XML-based protocol, more strict and secure.                                 | Used in banking or enterprise applications |
| **7. GraphQL API**     | Client asks exactly for the data it needs in a single query.                | GitHub GraphQL API                         |



## 🛠️ Key Features of APIs

* Platform-independent communication.
* Uses standardized formats: **JSON**, **XML**, etc.
* Offers **secure**, **scalable**, and **reusable** access to services.
* Often requires **authentication** like API keys or tokens.



## ✅ Real-World Example: REST API

Suppose you’re building a **bookstore app**. Your mobile frontend app interacts with the backend using API:

| Action                  | Endpoint         | HTTP Method | Description               |
| ----------------------- | ---------------- | ----------- | ------------------------- |
| View all books          | `/api/books/`    | `GET`       | Get list of books         |
| Get details of one book | `/api/books/10/` | `GET`       | Get info about book ID 10 |
| Add a new book          | `/api/books/`    | `POST`      | Create a new book         |
| Update book info        | `/api/books/10/` | `PUT`       | Update book with ID 10    |
| Delete a book           | `/api/books/10/` | `DELETE`    | Remove book with ID 10    |

**Request:**

```http
GET /api/books/10/
```

**Response (JSON):**

```json
{
  "id": 10,
  "title": "Django for Beginners",
  "author": "John Smith",
  "price": 19.99
}
```


## 🧠 Summary

* **API** lets different software communicate.
* APIs come in types: **REST, SOAP, GraphQL**, and usage categories: **public, private, partner**.
* Django REST Framework helps you build **REST APIs** to expose backend data to frontend or external apps.





# 🔗 What is Django REST Framework (DRF)?

**Django REST Framework (DRF)** is a powerful and flexible toolkit built on top of Django for building **Web APIs** (Application Programming Interfaces). It allows you to **expose your Django models and data as RESTful APIs**, making it easy for frontend apps, mobile apps, or external systems to interact with your backend.


## ✅ Why Use DRF?

* Easily convert Django models into **JSON data**.
* Handle **HTTP methods** like `GET`, `POST`, `PUT`, `DELETE`.
* Built-in support for **authentication**, **permissions**, **pagination**, and **serializers**.
* Helps create **secure and scalable APIs** without much boilerplate code.



## 🌐 Real-World Example (Without Code):

Suppose you're building a **Blog App** using Django, and you want to allow mobile apps to:

* View all blog posts
* Create new posts
* Edit or delete existing posts

Instead of rendering HTML pages, you use **Django REST Framework** to expose this functionality via APIs:

| Action                 | DRF API Endpoint | Request Type |
| ---------------------- | ---------------- | ------------ |
| Get list of blog posts | `/api/posts/`    | `GET`        |
| View a single post     | `/api/posts/1/`  | `GET`        |
| Create a new post      | `/api/posts/`    | `POST`       |
| Update a post          | `/api/posts/1/`  | `PUT`        |
| Delete a post          | `/api/posts/1/`  | `DELETE`     |

Instead of HTML, these endpoints return **JSON data** such as:

```json
{
  "id": 1,
  "title": "My First Post",
  "content": "Welcome to the blog!"
}
```



## 🔁 Summary of DRF Flow:

```
Client (mobile/web app)
     ↓ API request (JSON)
Django REST Framework (Views, Serializers, Models)
     ↓
Database interaction + JSON response
     ↓
Client renders the data
```





# 🌟 **Core Principles of REST API**

## ✅ 1. **Stateless**

* Each request from the client to the server **must contain all the information** needed to process the request.
* The server does **not store** any session or client context.
* ✔️ Example: You must send authentication credentials (like tokens) with every request.



## ✅ 2. **Client-Server Architecture**

* The client (frontend) and server (backend) are **separated**.
* They communicate only through the API, promoting modularity and independent development.
* ✔️ Example: A React app calls a Django REST API to fetch data.


## ✅ 3. **Uniform Interface**

* Every RESTful service must use a **consistent way** to interact with resources.
* This includes:

  * Using standard **HTTP methods** (`GET`, `POST`, `PUT`, `DELETE`)
  * Proper **URI naming** (`/users/`, `/products/10/`)
  * Consistent **response formats** (usually JSON)



## ✅ 4. **Resource-Based**

* Everything is considered a **resource** (user, book, product), and each resource is identified by a unique URI.
* ✔️ Example: `/api/books/` → list of books, `/api/books/5/` → book with ID 5


## ✅ 5. **Representation via JSON/XML**

* Resources can have different **representations** like JSON, XML, HTML.
* Most modern APIs use **JSON** for easy readability and use.


## ✅ 6. **Cacheable**

* Responses should indicate whether they can be **cached**.
* Helps improve performance by avoiding repeated processing.


## ✅ 7. **Layered System**

* You can have **multiple layers** (authentication, logging, caching) between client and server.
* Each layer works **independently**, improving scalability and flexibility.

## ✅ 8. **Code on Demand (Optional)**

* The server can optionally send **executable code** (like JavaScript) to the client.
* Rarely used in REST, but allowed by design.


## 📌 Summary Table

| Principle         | Description                                |
| ----------------- | ------------------------------------------ |
| Stateless         | No session data stored on the server       |
| Client-Server     | Separation of frontend and backend         |
| Uniform Interface | Standard methods and URI structure         |
| Resource-Based    | Everything treated as a resource (URI)     |
| Representation    | Uses JSON/XML to represent data            |
| Cacheable         | Improve speed by caching responses         |
| Layered System    | Support middleware layers                  |
| Code on Demand    | (Optional) Send code from server to client |


These principles help make REST APIs **scalable, reliable, reusable, and easy to understand**.