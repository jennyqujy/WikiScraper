#!/usr/bin/env python3
import unittest
import requests
from requests.auth import HTTPBasicAuth

class TestActorAPI(unittest.TestCase):

    ## Test for authentication login
    def test_login(self):
        response = requests.get('http://127.0.0.1:5000/graph/api/actors/Alan%20Rickman')
        self.assertEqual(response.status_code,401)
        response = requests.get('http://127.0.0.1:5000/graph/api/actors/Alan%20Rickman', auth=HTTPBasicAuth('jenny', 'python'))
        self.assertEqual(response.status_code,200)

    ## Test for GET
    def test_get(self):
        response = requests.get('http://127.0.0.1:5000/graph/api/actors/Alan%20Rickman', auth=HTTPBasicAuth('jenny', 'python'))
        self.assertEqual(response.json(), {
    "actors": {
        "actor_age": "71",
        "actor_castings": [
            "Romeo and Juliet",
            "Tybalt",
            "Alvin Rakoff",
            "BBC Television Shakespeare",
            "Shelley",
            "Smiley's People",
            "Simon Langton",
            "The Barchester Chronicles",
            "David Giles",
            "Girls on Top",
            "Die Hard",
            "John McTiernan",
            "The January Man",
            "Pat O'Connor",
            "Quigley Down Under",
            "Simon Wincer",
            "Truly, Madly, Deeply",
            "Anthony Minghella",
            "Closet Land",
            "Radha Bharadwaj",
            "Robin Hood: Prince of Thieves",
            "Sheriff of Nottingham",
            "Kevin Reynolds",
            "Close My Eyes",
            "Stephen Poliakoff",
            "Bob Roberts",
            "Tim Robbins",
            "Fallen Angels",
            "Mesmer",
            "Franz Mesmer",
            "Roger Spottiswoode",
            "An Awfully Big Adventure",
            "Mike Newell",
            "Sense and Sensibility",
            "Colonel Brandon",
            "Ang Lee",
            "Rasputin: Dark Servant of Destiny",
            "Grigori Rasputin",
            "Uli Edel",
            "Michael Collins",
            "Éamon de Valera",
            "Neil Jordan",
            "The Winter Guest",
            "Judas Kiss",
            "Sebastian Gutierrez",
            "Dark Harbor",
            "Adam Coleman Howard",
            "Dogma",
            "Metatron",
            "Kevin Smith",
            "Galaxy Quest",
            "Dean Parisot",
            "Help! I'm a Fish",
            "Blow Dry",
            "Paddy Breathnach",
            "Play",
            "Anthony Minghella",
            "Harry Potter and the Philosopher's Stone",
            "Professor Severus Snape",
            "Chris Columbus",
            "The Search for John Gissing",
            "Mike Binder",
            "King of the Hill",
            "Harry Potter and the Chamber of Secrets",
            "Chris Columbus",
            "Love Actually",
            "Richard Curtis",
            "Something the Lord Made",
            "Dr. Alfred Blalock",
            "Joseph Sargent",
            "Harry Potter and the Prisoner of Azkaban",
            "Alfonso Cuarón",
            "The Hitchhiker's Guide to the Galaxy",
            "Marvin the Paranoid Android",
            "Garth Jennings",
            "Harry Potter and the Goblet of Fire",
            "Mike Newell",
            "Snow Cake",
            "Marc Evans",
            "Perfume: The Story of a Murderer",
            "Tom Tykwer",
            "Nobel Son",
            "Randall Miller",
            "Harry Potter and the Order of the Phoenix",
            "David Yates",
            "Sweeney Todd: The Demon Barber of Fleet Street",
            "Judge Turpin",
            "Tim Burton",
            "Bottle Shock",
            "Steven Spurrier",
            "Randall Miller",
            "Harry Potter and the Half-Blood Prince",
            "David Yates",
            "Alice in Wonderland",
            "Absolem the Caterpillar",
            "Tim Burton",
            "The Song of Lunch",
            "Niall MacCormick",
            "Harry Potter and the Deathly Hallows – Part 1",
            "David Yates",
            "The Wildest Dream",
            "Noel Odell",
            "Harry Potter and the Deathly Hallows – Part 2",
            "David Yates",
            "Gambit",
            "Michael Hoffman",
            "The Butler",
            "Ronald Reagan",
            "Lee Daniels",
            "A Promise",
            "Patrice Leconte",
            "CBGB",
            "Hilly Kristal",
            "Randall Miller",
            "A Little Chaos",
            "King Louis XIV",
            "Eye in the Sky",
            "Gavin Hood",
            "Alice Through the Looking Glass",
            "James Bobin"
        ],
        "actor_name": "Alan Rickman"
    }
})

    ## Test for PUT method
    def test_put(self):
        response = requests.put('http://127.0.0.1:5000/graph/api/actors/Hugh%20Grant', json = {"gross_value":"500000.0"}, auth=HTTPBasicAuth('jenny', 'python'))
        self.assertEqual(response.json(),
{
    "actors": {
        "actor_castings": [],
        "gross_value": "500000.0",
        "actor_age": "57",
        "actor_name": "Hugh Grant"
    }
})

    ## Test for DELETE method
    def test_delete(self):
        response = requests.delete('http://127.0.0.1:5000/graph/api/actors/Liam%20Neeson', auth=HTTPBasicAuth('jenny', 'python'))
        self.assertEqual(response.status_code,200)
        response = requests.get('http://127.0.0.1:5000/graph/api/actors/Liam%20Neeson', auth=HTTPBasicAuth('jenny', 'python'))
        self.assertEqual(response.json(), {
    "actors": {
        "actor_age": None,
        "actor_castings": None,
        "actor_name": "Liam Neeson"
    }
})


class TestFilmAPI(unittest.TestCase):

    ## Test for authentication login
    def test_login(self):
        response = requests.get('http://127.0.0.1:5000/graph/api/actors/Alan%20Rickman')
        self.assertEqual(response.status_code,401)
        response = requests.get('http://127.0.0.1:5000/graph/api/actors/Alan%20Rickman', auth=HTTPBasicAuth('jenny', 'python'))
        self.assertEqual(response.status_code,200)

    ## Test for GET method
    def test_get(self):
        response = requests.get('http://127.0.0.1:5000/graph/api/movies/How%20to%20Deal', auth=HTTPBasicAuth('jenny', 'python'))
        self.assertEqual(response.json(), {
    "films": {
        "film_name": "How to Deal",
        "film_starrings": [
            "Mandy Moore",
            "Allison Janney",
            "Trent Ford"
        ],
        "film_value": "14308132.0"
    }
})

    ## Test for PUT method
    def test_put(self):
        response = requests.put('http://127.0.0.1:5000/graph/api/movies/Century', json = {"year":"1999"}, auth=HTTPBasicAuth('jenny', 'python'))
        self.assertEqual(response.json(),{
    "films": {
        "film_name": "Century",
        "film_starrings": [
            "Charles Dance",
            "Clive Owen",
            "Miranda Richardson",
            "Robert Stephens"
        ],
        "year": "1999",
        "film_value": "0.0"
    }
})

    ## Test for DELETE method
    def test_delete(self):
        response = requests.delete('http://127.0.0.1:5000/graph/api/movies/The%20Eagle', auth=HTTPBasicAuth('jenny', 'python'))
        self.assertEqual(response.status_code,200)
        response = requests.get('http://127.0.0.1:5000/graph/api/movies/The%20Eagle', auth=HTTPBasicAuth('jenny', 'python'))
        self.assertEqual(response.json(), {
    "films": {
        "film_name": "The Eagle",
        "film_starrings": None,
        "film_value": None
    }
})

class TestFilmListAPI(unittest.TestCase):

    ## Test for authentication login
    def test_login(self):
        response = requests.get('http://127.0.0.1:5000/graph/api/actors/Alan%20Rickman')
        self.assertEqual(response.status_code,401)
        response = requests.get('http://127.0.0.1:5000/graph/api/actors/Alan%20Rickman', auth=HTTPBasicAuth('jenny', 'python'))
        self.assertEqual(response.status_code,200)

    ## Test for GET method
    def test_get(self):
        response = requests.get('http://127.0.0.1:5000/graph/api/movies?name=Dave', auth=HTTPBasicAuth('jenny', 'python'))
        self.assertEqual(response.status_code,200)
        ret = True
        for actor in response.json()['films']:
            if actor.find('Dave')!=-1:
                ret = False
        self.assertEqual(ret, True)

    ## Test for POST method
    def test_post(self):
        response = requests.post('http://127.0.0.1:5000/graph/api/movies', json = {"name":"Billy Joe", "value":"100.0"}, auth=HTTPBasicAuth('jenny', 'python'))
        self.assertEqual(response.status_code,200)
        response = requests.get('http://127.0.0.1:5000/graph/api/movies/Billy%20Joe', auth=HTTPBasicAuth('jenny', 'python'))
        self.assertEqual(response.json(), {
    "films": {
        "film_name": "Billy Joe",
        "film_starrings": None,
        "film_value": "100.0"
    }
})

class TestActorListAPI(unittest.TestCase):

    ## Test for authentication login
    def test_login(self):
        response = requests.get('http://127.0.0.1:5000/graph/api/actors/Alan%20Rickman')
        self.assertEqual(response.status_code,401)
        response = requests.get('http://127.0.0.1:5000/graph/api/actors/Alan%20Rickman', auth=HTTPBasicAuth('jenny', 'python'))
        self.assertEqual(response.status_code,200)

    ## Test for GET method
    def test_get(self):
        response = requests.get('http://127.0.0.1:5000/graph/api/actors?name=Angela%20Bassett', auth=HTTPBasicAuth('jenny', 'python'))
        self.assertEqual(response.status_code,200)
        ret = True
        for actor in response.json()['actors']:
            if actor.find('Angela assett')!=-1:
                ret = False
        self.assertEqual(ret, True)

    ## Test for POST method
    def test_post(self):
        response = requests.post('http://127.0.0.1:5000/graph/api/actors', json = {"name":"Billy Joe", "age":"57"}, auth=HTTPBasicAuth('jenny', 'python'))
        self.assertEqual(response.status_code,200)
        response = requests.get('http://127.0.0.1:5000/graph/api/actors/Billy%20Joe', auth=HTTPBasicAuth('jenny', 'python'))
        self.assertEqual(response.json(), {
    "actors": {
        "actor_age": "57",
        "actor_castings": None,
        "actor_name": "Billy Joe"
    }
})


if __name__ == "__main__":
    unittest.main()
