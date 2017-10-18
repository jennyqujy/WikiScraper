import json
from graph import ActorNode
from graph import FilmNode
from graph import Edge

class InitGraph:

    ## set up all the film/actor nodes as Dictionary:
    ## key: url, value: film/actor node
    ## store the edges as a list with starting node of actor and ending node as movie
    filmNodes = []
    actorNodes = []
    filmNameDict = {}
    actorNameDict = {}
    edges = []
    nodes = {}
    hub = {}

    #parse a json file
    with open('/Users/Jenny/Desktop/cs242/Assignment2.0/Scraper/Scraper/quotes.json','r') as content_file:
        content = content_file.read()
    data = json.loads(content)

    for i in range(len(data)):
        temp = data[i]
        name = None
        edge = None

        ## when we discover the current index of the json file is an actor
        if temp['isActor'] == True:
            node = ActorNode(temp['actorName'], temp['url'], temp['year'])
            nodes[temp['url']] = node
            actorNodes.append(node)
            actorNameDict[temp['actorName']] = []
            for cast in temp['castings']:
                for ch in cast:
                    actorNameDict[temp['actorName']].append(ch)
            for url in temp['films']:
                if nodes.get(url) is not None:
                    edge = Edge(node,nodes.get(url))

        ## when we discover the current index of the json file is a film
        elif temp['isFilm'] == True:
            node = FilmNode(temp['filmName'],temp['url'],temp['year'], temp['filmValue'])
            nodes[temp['url']] = node
            filmNodes.append(node)
            filmNameDict[temp['filmName']] = temp['starrings']
            for url in temp['actors']:
                if nodes.get(url) is not None:
                    edge = Edge(nodes.get(url), node)

        if edge is not None:
            edges.append(edge)



class GraphQuery:
    ## get the oldest actor name from our scraped json file
    def getOldestActor(self,actorNodes):
        maxAge = 0
        act = ''
        for node in actorNodes:
            if (int(ActorNode.getAge(node))>maxAge):
                maxAge = int(ActorNode.getAge(node))
                act = ActorNode.getName(node)
        return act

    ## get film with greatest box office
    def getMaxBoxOfficeFilm(self,filmNodes):
        maxVal = 0
        act = ''
        for node in filmNodes:
            if (float(FilmNode.getValue(node))>maxVal):
                maxVal = float(FilmNode.getValue(node))
                act = FilmNode.getName(node)
        return act

    ## get the starring actors from a film
    def getActorsInFilm(self,filmNameDict,filmName):
        return filmNameDict.get(filmName)

    ## get the casting films for an actor/actress
    def getActorCastings(self,actorNameDict,actorName):
        return actorNameDict.get(actorName)

    ## get the age of an actor
    def getActorAge(self,actorNodes, actorName):
        for node in actorNodes:
            if (ActorNode.getName(node)==actorName):
                if ActorNode.getAge(node) == '2017':
                    return 'Died'
                else:
                    return ActorNode.getAge(node)

    ## get the gross value for a film
    def getFilmValue(self,filmNodes,filmName):
        for node in filmNodes:
            if (FilmNode.getName(node)==filmName):
                return FilmNode.getValue(node)

    ## get all the actor names for a given year
    def getAllActorsInYear(self,actorNodes, year):
        ret = []
        for node in actorNodes:
            if ActorNode.getYear(node)==str(year):
                ret.append(ActorNode.getName(node))
        return ret

    ## get all the film names for a given year
    def getAllFilmsInYear(self,filmNodes, year):
        ret = []
        for node in filmNodes:
            if FilmNode.getYear(node)==str(year):
                ret.append(FilmNode.getName(node))
        return ret

    ## get actors other than the actor provided
    def getOtherActors(self,actorNodes,actorName):
        ret = []
        for node in actorNodes:
            if ActorNode.getName(node).find(actorName)==-1:
                ret.append(ActorNode.getName(node))
        return ret

    ## get films other than the film provided
    def getOtherFilms(self,filmNodes,filmName):
        ret = []
        for node in filmNodes:
            if FilmNode.getName(node).find(filmName)==-1:
                ret.append(FilmNode.getName(node))
        return ret

    ## remove a film
    def removeFilm(self,filmNodes,filmNameDict,filmName):
        for node in filmNodes:
            if FilmNode.getName(node)==filmName:
                filmNodes.remove(node)
                filmNameDict.pop(filmName)

    ## remove an actor
    def removeActor(self,actorNodes,actorNameDict,actorName):
        for node in actorNodes:
            if ActorNode.getName(node)==actorName:
                actorNodes.remove(node)
                actorNameDict.pop(actorName)

    def addActor(self,actorNodes,actorNameDict,actorName, age):
        node = ActorNode(actorName, None, str(2017-age))
        actorNodes.append(node)
        actorNameDict['actorName'] = actorName

    def addFilm(self,filmNodes,filmNameDict,filmName, value):
        node = FilmNode(filmName, None, None, str(value))
        filmNodes.append(node)
        filmNameDict['filmName'] = filmName
