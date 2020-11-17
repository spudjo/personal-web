from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, jsonify, Flask
)

# from .database.database import Session, engine, Base
# from .database.github_repo import GithubRepo, GithubRepoSchema

bp = Blueprint('github', __name__)

import json
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

APPS = ['Knights-Tour-Problem',
        'mortuary_management_system',
        'personal-web',
        'quick-organizer',
        'Movement_AI']

def get_public_repos(user):
    url = 'https://api.github.com/users/{0}/repos'.format(user)
    response = requests.get(url) # returns response
    decoded = response.content.decode()  # converts response to string of list
    return json.loads(decoded) # converts string to list then returns


def print_json_formatted(data):
    print(json.dumps(data, indent=4, sort_keys=True))


def print_json_list_formatted(data_list):
    for data in data_list:
        print_json_formatted(data)
        print()


def print_key_info(data):
    print('ID: {0}'.format(data['id']))
    print('Name: {0}'.format(data['name']))
    print('Description: {0}'.format(data['description']))
    print('HTML URL: {0}'.format(data['url']))
    print('Created At: {0}'.format(data['created_at']))
    print('Updated At: {0}'.format(data['updated_at']))


def print_key_info_list(data_list):
    for data in data_list:
        print_key_info(data)
        print()

def minimize_repo_list(data_list):
    minimized_list = []

    print()

    for data in data_list:
        
        if (isinstance(data, dict)):

            if data['name'] in APPS:

                readme_url = 'https://raw.githubusercontent.com/x-raph/{0}/master/README.md'.format(data['name']);

                minimized_list.append({
                    'id': data['id'],
                    'name': data['name'],
                    'description': data['description'],
                    'url': data['html_url'],
                    'readme_url': readme_url,
                    'readme_text': get_readme_text(readme_url),
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

def get_readme_text(url):

    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()  # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '<br>'.join(chunk for chunk in chunks if chunk)

    return text


@bp.route('/api/github')
def get_github():

    user = 'spudjo'
    repos = get_public_repos(user)
    minimized_repos = minimize_repo_list(repos)
    sorted_repos = sort_repos(minimized_repos, sort_by='updated_at', direction='desc')  
    # print_key_info_list(sorted_repos)
    return jsonify(sorted_repos)

def get_github_test():
    user = 'spudjo'
    repos = get_public_repos(user)
    minimized_repos = minimize_repo_list(repos)
    sorted_repos = sort_repos(minimized_repos, sort_by='updated_at', direction='desc')
    # print_key_info_list(sorted_repos)