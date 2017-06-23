"""This script connects to a RethinkDB instance
    and perform a Create Database and Table/Collection actions"""
import rethinkdb as r

# connection to RethinkDB
r.connect('localhost', 28015).repl()

print(r.db_list().run())

# create a new database
r.db_create('python_test').run()

# create a new table/collection
r.db('python_test').table_create('heroes').run()

print(r.db_list().run())
