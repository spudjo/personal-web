from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify, Flask
)

from .database.database import Session, engine, Base
from .database.github_repo import GithubRepo, GithubRepoSchema

bp = Blueprint('github', __name__)

import json
import requests


def get_public_repos(user):
    url = 'https://api.github.com/users/{0}/repos'.format(user)
    request = requests.get(url)
    decoded = request.content.decode()
    return json.loads(decoded)


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True))


def pretty_print_json_list(data_list):
    for data in data_list:
        pretty_print_json(data)
        print()


def print_key_info(data):
    print('ID: {0}'.format(data['id']))
    print('Name: {0}'.format(data['name']))
    print('Description: {0}'.format(data['description']))
    print('HTML URL: {0}'.format(data['html_url']))
    print('Created At: {0}'.format(data['created_at']))
    print('Updated At: {0}'.format(data['updated_at']))
    print()


def print_key_info_list(data_list):
    for data in data_list:
        print_key_info(data)


def minimize_repo_list(data_list):
    minimized_list = []

    for data in data_list:

        minimized_list.append({
            'id': data['id'], 
            'name': data['name'], 
            'description': data['description'], 
            'url': data['html_url'], 
            'created_at': data['created_at'], 
            'updated_at': data['updated_at']
            })

    return minimized_list

    
def sort_repos(data_list, sort_by='id', direction='asc'):

    acceptable_sort_fields = ['id', 'name', 'created_at', 'updated_at']

    if sort_by is not None:
        if sort_by not in acceptable_sort_fields:
            raise ValueError('Valid parameters: id (default), name created_at, updated_at')
            
    if direction is not None:
        if direction != 'asc' and direction != 'desc':
            raise ValueError('Valid parameters: asc (default), desc')
            

    sorted_list = []
    if sort_by:
        if direction == 'desc':
            sorted_list = sorted(data_list, key=lambda i: i[sort_by], reverse=True)
        else:
            sorted_list = sorted(data_list, key=lambda i: i[sort_by])
    else:
        if direction == 'desc':
            sorted_list = sorted(data_list, key=lambda i: i["id"], reverse=True)
        else:
            sorted_list = sorted(data_list, key=lambda i: i["id"])

    return sorted_list


@bp.route('/github')
def get_github():

    user = 'x-raph'
    repos = get_public_repos(user)
    minimized_repos = minimize_repo_list(repos)
    sorted_repos = sort_repos(minimized_repos, sort_by='updated_at', direction='desc')

    return jsonify(sorted_repos)
    # # fetching from the database
    # session = Session()
    # guestbook_objects = session.query(Guestbook).all()

    # # transforming into JSON-serializable objects
    # schema = GuestbookSchema(many=True)
    # guestbook = schema.dump(guestbook_objects)

    # # serializing as JSON
    # session.close()
    # return jsonify(guestbook)


# @bp.route('/github', methods=['POST'])
# def add_github():
#     return
    # # mount exam object
    # new_post = GuestbookSchema(only=('name', 'message')).load(request.get_json())
    # guestbook = Guestbook(**new_post, created_by="HTTP post request")

    # # persist exam
    # session = Session()
    # session.add(guestbook)
    # session.commit()

    # # return created exam
    # new_post = GuestbookSchema().dump(guestbook)
    # session.close()
    # return jsonify(new_post), 201





# user = 'x-raph'
# repos = get_public_repos(user)
# sorted_repos = sort_repos(repos, sort_by='updated_at', direction='desc')
# print_key_info_list(sorted_repos)