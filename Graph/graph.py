""" A Python Class
A simple Python graph class, demonstrating the essential
facts and functionalities of graphs.
"""

"""
Set up Node Class to store the information of json indices.
Including names, valid wiki url, born year of films/actors
"""
class Node(object):
    def __init__(self, name, url, year):
        self.name = name
        self.url = url
        self.year = year

    def getUrl(self):
        return self.url

    def getName(self):
        return self.name

    def getYear(self):
        return self.year

##
## Extends the Node class.
## Extra instance method to retrive age of an actor/actress.
##
class ActorNode(Node):
    def __init__(self, name, url, year):
        Node.__init__(self, name, url, year)

    def getAge(self):
        return str(2017-int(self.year))

    def eq(self, other):
        if other is None:
          return False
        return (self.name, self.url, self.year) == (other.name, other.url, other.year)

##
## Extends the Node class
## Extra variable to store the gross value of a film
##
class FilmNode(Node):
    def __init__(self, name, url, year, value):
        Node.__init__(self, name, url, year)
        self.value = value

    def getValue(self):
        return self.value

    def eq(self, other):
        if other is None:
          return False
        return (self.name, self.url, self.year, self.value) == (other.name, other.url, other.year, other.value)

"""
Set up Edge Class to store the information of json indices.
Including start Node as an Actor, and end Node as a film
"""
class Edge(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def getStart(self):
        return self.start

    def getEnd(self):
        return self.end
