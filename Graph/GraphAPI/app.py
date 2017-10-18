#!/usr/bin/env python3

import sys
# Add the ptdraft folder path to the sys.path list
sys.path.append('/Users/Jenny/Desktop/cs242/Assignment2.0/Scraper/Graph')

import pdb
from flask import Flask, jsonify, abort, make_response, request
from flask_restful import Api, Resource, reqparse, fields, marshal
from flask_httpauth import HTTPBasicAuth
from initialize import GraphQuery
from initialize import InitGraph

app = Flask(__name__, static_url_path="")
api = Api(app)
auth = HTTPBasicAuth()


@auth.get_password
def get_password(username):
    if username == 'jenny':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    # return 403 instead of 401 to prevent browsers from displaying the default
    # auth dialog
    return make_response(jsonify({'message': 'Unauthorized access'}), 401)
"""
use field of film/actor to match the returning json
"""
film_field = {
    'film_name': fields.String,
    'film_value': fields.String,
    'film_starrings': fields.List(fields.String)
}

actor_field = {
    'actor_age': fields.String,
    'actor_castings': fields.List(fields.String),
    'actor_name': fields.String
}

"""
Film API for GET PUT and DELETE with '\actors\<string:film_name>'
"""
class FilmAPI(Resource):
    ## login with authentication
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, required=True, help='No film name provided', location='json')
        self.reqparse.add_argument('value', type=float, required=True, location='json')
        super(FilmAPI, self).__init__()

    ## Method for GET
    ## return film item with input name argument
    def get(self, film_name):
        if len(film_name) <= 0:
            abort(400)
        value = GraphQuery.getFilmValue(GraphQuery(),InitGraph.filmNodes, film_name)
        starrings = GraphQuery.getActorsInFilm(GraphQuery(),InitGraph.filmNameDict,film_name)
        data = {'film_name': film_name, 'film_value': value, 'film_starrings':starrings}
        return make_response(jsonify({'films':marshal(data, film_field)}),200)

    ## Method for PUT
    ## return json of updated item
    def put(self,film_name):
        if len(film_name) <= 0:
            abort(400)
        value = GraphQuery.getFilmValue(GraphQuery(),InitGraph.filmNodes, film_name)
        starrings = GraphQuery.getActorsInFilm(GraphQuery(),InitGraph.filmNameDict,film_name)
        data = {'film_name': film_name, 'film_value': value, 'film_starrings':starrings}
        args = request.get_json()
        if args is not None:
            for k, v in args.items():
                if v is not None:
                    data[k] = v
        return {'films':data}

    ## Method for DELETE
    ## return status_code
    def delete(self,film_name):
        if len(film_name) <= 0:
            abort(400)
        GraphQuery.removeFilm(GraphQuery(),InitGraph.filmNodes, InitGraph.filmNameDict, film_name)
        response = make_response(jsonify({'result': True}),200)
        return {'Status':response.status_code}

"""
Actor API for GET PUT and DELETE with '\actors\<string:actor_name>'
"""
class ActorAPI(Resource):
    ## login with authentication
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, location='json')
        self.reqparse.add_argument('age', type=int, location='json')
        super(ActorAPI, self).__init__()

    ## Method for GET
    def get(self, actor_name):
        if len(actor_name) <= 0:
            abort(400)
        age = GraphQuery.getActorAge(GraphQuery(),InitGraph.actorNodes, actor_name)
        castings = GraphQuery.getActorCastings(GraphQuery(),InitGraph.actorNameDict,actor_name)
        data = {'actor_name': actor_name, 'actor_age': age, 'actor_castings':castings}
        return make_response(jsonify({'actors':marshal(data, actor_field)}),200)

    ## Method for PUT
    def put(self,actor_name):
        if len(actor_name) <= 0:
            abort(400)
        age = GraphQuery.getActorAge(GraphQuery(),InitGraph.actorNodes, actor_name)
        castings = GraphQuery.getActorCastings(GraphQuery(),InitGraph.actorNameDict,actor_name)
        data = {'actor_name': actor_name, 'actor_age': age, 'actor_castings':castings}
        args = request.get_json()
        if args is not None:
            for k, v in args.items():
                if v is not None:
                    data[k] = v
        return {'actors':data}

    ## Method for DELETE
    def delete(self,actor_name):
        GraphQuery.removeActor(GraphQuery(),InitGraph.actorNodes, InitGraph.actorNameDict, actor_name)
        response = make_response(jsonify({'result': True}),200)
        return {'Status':response.status_code}
"""
Actor API for GET and POST with '/actors'
"""
class ActorListAPI(Resource):
    ## login with authentication
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, required=True, help='No actor name provided', location='json')
        self.reqparse.add_argument('age', type=int, required=True, location='json')
        super(ActorListAPI, self).__init__()

    ## Method for GET
    def get(self):
        name = request.args.get('name')
        if name is not None and len(name) <= 0:
            abort(400)
        data = GraphQuery.getOtherActors(GraphQuery(),InitGraph.actorNodes, name)
        return {'actors': [act for act in data]}

    ## Method for POST
    def post(self):
        data = self.reqparse.parse_args()
        if len(data['name']) <= 0:
            abort(400)
        GraphQuery.addActor(GraphQuery(),InitGraph.actorNodes, InitGraph.actorNameDict, data['name'], data['age'])
        response = make_response(jsonify(data),200)
        return {'Status':response.status_code}

"""
Film API for GET and POST with '/movies'
"""

class FilmListAPI(Resource):
    ## login with authentication
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, required=True, help='No film name provided', location='json')
        self.reqparse.add_argument('value', type=float, required=True, location='json')
        super(FilmListAPI, self).__init__()

    ## Method for GET
    def get(self):
        name = request.args.get('name')
        if len(name) <= 0:
            abort(400)
        data = GraphQuery.getOtherFilms(GraphQuery(),InitGraph.filmNodes, name)
        return {'films': [film for film in data]}

    ## Method for POST
    def post(self):
        # pdb.set_trace()
        data = self.reqparse.parse_args()
        if len(data['name']) <= 0:
            abort(400)
        GraphQuery.addFilm(GraphQuery(),InitGraph.filmNodes, InitGraph.filmNameDict, data['name'], data['value'])
        response = make_response(jsonify(data),200)
        return {'Status':response.status_code}

"""
Add the above four resource to our api.
"""
if __name__ == '__main__':
    api.add_resource(ActorAPI, '/graph/api/actors/<string:actor_name>', endpoint='actor')
    api.add_resource(ActorListAPI, '/graph/api/actors', endpoint='actor_list')
    api.add_resource(FilmAPI, '/graph/api/movies/<string:film_name>', endpoint='film')
    api.add_resource(FilmListAPI, '/graph/api/movies', endpoint='film_list')
    app.run(debug=True)
