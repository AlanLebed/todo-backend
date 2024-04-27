### Architectural Decisions

In the process of determining the most suitable architectural style for the backend of our Todo List application, I conducted a thorough analysis of the advantages of the different technologies suggested. This research was aimed at understanding which approach would best meet the requirements of this project. 


### Choice of API: REST over GraphQL

Based on various factors, including ease of implementation, scalability, and the nature of operations required for a todo list application, I opted to use a RESTful API. This decision was driven by several key factors:

**Simplicity and Familiarity**
    REST is a well-established and widely understood architectural style in web development. Flask-RESTful also provides straightforward tools and decorators that simplify the routing and request handling, which aligns well with the typical CRUD operations required by a Todo application.

**Resource-based Approach**
    The resource-oriented architecture of REST is a natural fit for our Todo List application. Each todo item can be treated as a resource that can be created, retrieved, updated, or deleted via standard HTTP methods. This maps intuitively to REST's approach of using standard HTTP verbs (GET, POST, PATCH, DELETE) for interacting with resources, making the API design straightforward and predictable.

**Performance and Overhead**
    REST APIs typically send data over HTTP in JSON or XML format, which is efficient for the relatively small scale of data managed in a Todo List application. While GraphQL offers fine-grained data fetching capabilities, the overhead of parsing and resolving GraphQL queries could be unnecessary for this application’s scope, where the data relationships are simple and the additional flexibility of GraphQL wouldn't provide significant benefits.

**Tooling and Support**
    Flask-RESTful is a mature library with robust support for developing REST APIs in Python. It integrates seamlessly with other parts of the Flask ecosystem, such as Flask-SQLAlchemy for database interactions. The abundance of tutorials, documentation, and community support for RESTful APIs in Flask ensures quick problem resolution and ease of use.

**Scalability and Future Proofing**
    Considering the potential future expansion of the application, REST APIs are easy to scale with tools like load balancers and reverse proxies. The stateless nature of RESTful services allows for better scaling and caching possibilities across distributed systems. Although GraphQL provides a powerful querying language for complex systems, the current and foreseeable requirements of the Todo List application do not justify the additional complexity.


In conclusion, the choice to implement a RESTful API using Flask-RESTful was based on the application’s need for a simple, efficient, and easy-to-understand interface for data interactions. This choice ensures that the API is accessible, maintainable, and scalable without the overheads associated with more complex querying languages like GraphQL.    
