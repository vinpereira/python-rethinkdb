"""This script connects to a RethinkDB instance
    and perform some an Update action"""
import rethinkdb as r

# connection to RethinkDB
r.connect('localhost', 28015).repl()

HEROES = r.db('python_test').table('heroes')

# Update magazine to every documents and add 1 to every hero appearance
HEROES.update({
    'appearances_count': r.row['appearances_count'] + 1,
    'magazine_titles': r.row['magazine_titles'].append('The Fantastic RethinkDB')
}).run()
