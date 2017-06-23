"""This script connects to a RethinkDB instance
    and perform some a Create/Insert action"""
import rethinkdb as r

# connection to RethinkDB
r.connect('localhost', 28015).repl()

HEROES = r.db('python_test').table('heroes')

# Single insert
HEROES.insert({
    "hero": "Wolverine",
    "name": "James 'Logan' Howlett",
    "magazine_titles": [
        "Amazing Spider-Man vs. Wolverine",
        "Avengers",
        "X-MEN Unlimited",
        "Magneto War",
        "Prime"
    ],
    "appearances_count": 98
}).run()

# Multiple inserts
HEROES.insert([
    {
        "hero": "Magneto",
        "name": "Max Eisenhardt",
        "aka": [
            "Magnus",
            "Erik Lehnsherr",
            "Lehnsherr"
        ],
        "magazine_titles": [
            "Alpha Flight",
            "Avengers",
            "Avengers West Coast"
        ],
        "appearances_count": 42
    },
    {
        "hero": "Professor Xavier",
        "name": "Charles Francis Xavier",
        "magazine_titles": [
            "Alpha Flight",
            "Avengers",
            "Bishop",
            "Defenders"
        ],
        "appearances_count": 72
    },
    {
        "hero": "Storm",
        "name": "Ororo Monroe",
        "magazine_titles": [
            "Amazing Spider-Man vs. Wolverine",
            "Excalibur",
            "Fantastic Four",
            "Iron Fist"
        ],
        "appearances_count": 72
    }
]).run()
