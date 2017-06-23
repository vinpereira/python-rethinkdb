"""This script connects to a RethinkDB instance
    and perform some a Change Feeds (Real Time) action"""
import rethinkdb as r

# connection to RethinkDB
r.connect('localhost', 28015).repl()

HEROES = r.db('python_test').table('heroes')

# Realtime feeds
print('Real-time feeds')
CURSOR = HEROES.changes().run()
for hero in CURSOR:
    print(hero)
