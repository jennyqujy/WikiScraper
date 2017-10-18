import unittest
import sys
sys.path.insert(0, '/Users/Jenny/Desktop/cs242/Assignment2.0/Scraper/Scraper')
from Graph.initialize import InitGraph
from Graph.initialize import GraphQuery

class TestGraph(unittest.TestCase):

    def test_getOldestActor(self):
        self.assertEqual(GraphQuery.getOldestActor(GraphQuery(),InitGraph.actorNodes),'Grant Mitchell')

    def test_getAllActorsInYear(self):
        self.assertTrue(GraphQuery.getAllActorsInYear(GraphQuery(),InitGraph.actorNodes,1972),['Jude Law','Cameron Diaz'])

    def test_getAllFilmsInYear(self):
        self.assertEqual(GraphQuery.getAllFilmsInYear(GraphQuery(),InitGraph.filmNodes,2013),['Oblivion'])

    def test_getFilmValue(self):
        self.assertEqual(GraphQuery.getFilmValue(GraphQuery(), InitGraph.filmNodes,'Oblivion'),'$286.2 million[5]')

    def test_getActorAge(self):
        self.assertEqual(GraphQuery.getActorAge(GraphQuery(),InitGraph.actorNodes,'Jude Law'),'45')

    def test_getActorsInFilm(self):
        self.assertEqual(GraphQuery.getActorsInFilm(GraphQuery(),InitGraph.filmNameDict,'Oblivion'),['Tom Cruise','Morgan Freeman', 'Olga Kurylenko','Andrea Riseborough','Nikolaj Coster-Waldau','Melissa Leo'])

    def test_getActorCastings(self):
        # self.assertEqual(GraphQuery.getActorCastings(Init.actorNodes,'Jude Law'),'45')
        pass

if __name__ == '__main__':
    unittest.main()
