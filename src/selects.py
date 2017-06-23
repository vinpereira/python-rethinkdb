"""This script connects to a RethinkDB instance
    and perform some a Select action"""
import rethinkdb as r

# connection to RethinkDB
r.connect('localhost', 28015).repl()

HEROES = r.db('python_test').table('heroes')

print('Currently number of documents: {}'.format(HEROES.count().run()))

# Fin document by ID
# HEROES.get('insert a document ID here').run()

# Find document by an attribute
print('Find document by an attribute:')
print(HEROES.filter({'name': 'Charles Francis Xavier'}).run())

# Order all documents based on appearances
print('Order documents based on appearances:')
print(HEROES.order_by(r.desc('appearances_count')).pluck('hero', 'appearances_count').run())

# Find a document with a hero which appears more than 90 times
print('Find a hero with more than 90 appearance:')
print(HEROES.filter(r.row['appearances_count'] >= 90)
      .pluck('hero', 'name', 'appearances_count').run())

# Find documents with heroes which appears in a particular magazine
print('Find heroes which appears in a particular magazine:')
print(HEROES.filter(
    r.row['magazine_titles'].filter(
        lambda mag: mag == 'Amazing Spider-Man vs. Wolverine'
    ).count() > 0
).pluck('hero').run())
