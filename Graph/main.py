import click
import json
from graph import ActorNode
from graph import FilmNode
from graph import Edge
from initialize import InitGraph
from initialize import GraphQuery
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
from plotly.graph_objs import *
import networkx as nx
import matplotlib.pyplot as plt
import igraph as ig
from networkx.drawing.nx_agraph import graphviz_layout
import pandas as pd
import numpy as np

"""
Main Commands to play with in the console
TODO: TO BE UPDATED!
"""

@click.group()
def main():
    pass

## for getting all the actor starred in a film
@main.command()
@click.argument('film_name')
def get_film_starrings(film_name):
    actors = GraphQuery.getActorsInFilm(GraphQuery(),InitGraph.filmNameDict,film_name)
    if actors is None:
        print ("Invalid Film!")
    else:
        print ('Starrings in:')
        for actor in actors:
            print(actor)

## getting the filmography information for an actor
@main.command()
@click.argument('actor_name')
def get_actor_castings(actor_name):
    films = GraphQuery.getActorCastings(GraphQuery(),InitGraph.actorNameDict,actor_name)
    if films is None:
        print ("Invalid Actor!")
    else:
        print ('Castings in:')
        for film in films:
            print(film)

## getting the age for an actor
@main.command()
@click.argument('actor_name')
def get_actor_age(actor_name):
    age = GraphQuery.getActorAge(GraphQuery(),InitGraph.actorNodes, actor_name)
    if age is None:
        print ("Invalid Actor!")
    else:
        print ('Age: {0:s}'.format(age))

## getting the value for a film
@main.command()
@click.argument('film_name')
def get_film_value(film_name):
    value = GraphQuery.getFilmValue(GraphQuery(),InitGraph.filmNodes, film_name)
    if value is None:
        print ("Invalid Film!")
    else:
        print ('Gross Value: {0:s}'.format(value))

## get the oldest actor
@main.command()
def get_oldest_actor():
    name = GraphQuery.getOldestActor(GraphQuery(),InitGraph.actorNodes)
    if name is None:
        print ("Invalid Actor!")
    else:
        print ('Oldest Actor: {0:s}'.format(name))

## get the most-earning movie
@main.command()
def get_film_most_value():
    name = GraphQuery.getMaxBoxOfficeFilm(GraphQuery(),InitGraph.filmNodes)
    if name is None:
        print ("Invalid Film!")
    else:
        print ('Film with max Box Office: {0:s}'.format(name))

## get all the films according to a public-year
@main.command()
@click.argument('year')
def get_films_in_year(year):
    films = GraphQuery.getAllFilmsInYear(GraphQuery(),InitGraph.filmNodes, year)
    if films is None:
        print ("Invalid Year!")
    else:
        for film in films:
            print(film)

## get all the actors according to a public-year
@main.command()
@click.argument('year')
def get_actors_in_year(year):
    actors = GraphQuery.getAllActorsInYear(GraphQuery(),InitGraph.actorNodes, year)
    if actors is None:
        print ("Invalid Year!")
    else:
        for actor in actors:
            print(actor)

## get all the hub actors: that is the actor with the most connection
@main.command()
def show_hub_actors():
    hub = {}
    for film in InitGraph.filmNameDict.keys():
        if film is not None:
            actors = GraphQuery.getActorsInFilm(GraphQuery(),InitGraph.filmNameDict,film)
            for actor in actors:
                hub[actor] = len(actors)
    labels = list(hub.keys())
    values = list(hub.values())
    trace = go.Pie(labels=labels, values=values)
    py.plot([trace], filename='basic_pie_chart')

"""
TODO: EC
"""
## Show sum of actor earnings for all movies he/she starred in.
@main.command()
def show_actor_earnings():
    ret = {}
    for film in InitGraph.filmNodes:
        if film is not None:
            value = float(FilmNode.getValue(film))
            name = FilmNode.getName(film)
            actors = GraphQuery.getActorsInFilm(GraphQuery(),InitGraph.filmNameDict,name)
            for actor in actors:
                if actor is not None:
                    if ret.get(actor) is None:
                        ret[actor] = 0.0
                    ret[actor] += value

    labels = list(ret.keys())
    values = list(ret.values())
    trace = go.Pie(labels=labels, values=values)
    py.plot([trace], filename='basic_pie_chart')

## show the relationship between age-group of actors and the gross earning for films
@main.command()
def show_age_gross_relation():
    ret = {}
    for film in InitGraph.filmNodes:
        if film is not None:
            value = FilmNode.getValue(film)
            name = FilmNode.getName(film)
            actors = GraphQuery.getActorsInFilm(GraphQuery(),InitGraph.filmNameDict,name)
            for actor in actors:
                if actor is not None:
                    for node in InitGraph.actorNodes:
                        if ActorNode.getName(node)==actor:
                            ret[ActorNode.getAge(node)] = value

    trace = go.Pie(labels=list(ret.keys()), values=list(ret.values()))
    py.plot([trace], filename='basic_pie_chart')

"""
TODO: EC
"""
## visualize the actor-movie relationship as a network
@main.command()
def visualize():
    ## set up G as an networkx graph
    G=nx.Graph()
    for node in InitGraph.nodes.values():
        G.add_node(node)
    for edge in InitGraph.edges:
        G.add_edge(Edge.getStart(edge),Edge.getEnd(edge))
        G.add_edge(Edge.getEnd(edge),Edge.getStart(edge))

    ## some value for the node color
    myvalue = ['123','25','76','12','34']
    plt.title("Network between Movies and Actors")
    nx.draw(G, node_color=myvalue, pos=nx.fruchterman_reingold_layout(G), cmap=plt.cm.Blues)
    plt.show()

if __name__ == "__main__":
    main()
