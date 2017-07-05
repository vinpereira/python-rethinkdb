Python code to access RethinkDB
===============================

A simple Python code to access RethinkDB and perform CRUD actions. Also, the code has a 'real-time change feed' to get all changes in database.

Programming Language and libraries used to solve the problems
-------------------------------------------------------------

  - Python v3.6.1

Main libraries:

  - rethinkdb v2.3.0.post6
  
Running the code with RethinkDB in Docker
-----------------------------------------
- Start RethinkDB container with: 
   $ docker run --name rethinkdb -v "$PWD:/data" -p 28015:28015 -d rethinkdb

- Run codes (using Makefile) to create a table/collection, insert documents, select, update, and/or delete them
    - e.g.: make create_db

    - These actions could all be done using RethinkDB Web UI

To access RethinkDB Web UI
--------------------------
- Get Docker container IP to access RethinkDB Web UI:
   $ docker inspect --format '{{ .NetworkSettings.IPAddress }}' rethinkdb

- Access RethinkDB Web UI:
   rethinkdb_ip:8080