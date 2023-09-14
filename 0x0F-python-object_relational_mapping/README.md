# 0x0F. Python - Object-relational mapping: Background Context

In this project, I'm going to dive into the fascinating realms of both Databases and Python, connecting them in a seamless and efficient manner.

## Part One: MySQLdb

In the first part of this project, I'll be harnessing the power of the `MySQLdb` module to establish a connection with a MySQL database and execute SQL queries. This will involve handling raw SQL queries, allowing me to interact with the database efficiently.

## Part Two: SQLAlchemy - The ORM Magic

In the second part, I'll venture into the world of SQLAlchemy, which is an Object Relational Mapper (ORM). Now, you might wonder, "How do I even pronounce SQLAlchemy?" But don't worry about that; we're here to understand how it works.

The significant distinction with SQLAlchemy is that it liberates us from the confines of writing SQL queries. Instead, our primary focus will shift to contemplating what we can do with our Python objects, rather than dwelling on the intricacies of where and how they're stored. SQLAlchemy abstracts the database storage details, making our code independent of the specific database system.

Here's a quick comparison to highlight the power of ORM:

**Without ORM:**

```python
# Traditional SQL query approach
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") 
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

**With SQLAlchemy ORM:**

```python
# ORM approach
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
session.close()
```

## Challenges with ORM

However, the syntax of different ORM libraries can be a bit challenging. While they all share similarities, they also have subtle differences. My strategy for tackling this? Start coding and consult tutorials as needed.

By the end of this project, I'll be able to explain:

**General**
- Why Python programming is awesome.
- How to connect to a MySQL database from a Python script.
- How to SELECT rows in a MySQL table using a Python script.
- How to INSERT rows into a MySQL table from a Python script.
- What ORM (Object-Relational Mapping) means.
- How to map a Python Class to a MySQL table.
- How to create a Python Virtual Environment.

Let's embark on this exciting journey of database connectivity and Python programming together! Feel free to explore the project and learn with me along the way.