"""This script connects to a RethinkDB instance
    and perform some a Delete action"""
import rethinkdb as r

# connection to RethinkDB
r.connect('localhost', 28015).repl()

HEROES = r.db('python_test').table('heroes')

print('Number of documents before delete action: {}'.format(HEROES.count().run()))

# Delete a document given an ID
# HEROES.get("insert a document ID here").delete().run()

# Delete a document given an attribute
HEROES.filter({"hero": "Storm"}).delete().run()

print('Number of documents after delete action: {}'.format(HEROES.count().run()))
