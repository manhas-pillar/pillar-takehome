# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, redirect, flash
import api_manager
from search import RepoSearchForm 
from uuid import uuid4

server = Flask(__name__)
server.secret_key = str(uuid4())

@server.route('/', methods=['GET', 'POST'])
def index():
    search = RepoSearchForm(request.form)
    if request.method == 'POST':
        return repo_search(search)
    
    return render_template('index.html', form=search)

@server.route('/repo_search')
def repo_search(search):
    results = []
    organization = search.data['search']

    repo_list = api_manager.get_repos(organization)

    if repo_list is None:
        flash('We were not able to retrieve data for that organization')
        return redirect('/')

    results = api_manager.build_repo_data(repo_list)

    return render_template('dashboard.html', name=organization, data=results)

if __name__ == '__main__':
    server.run(debug=True)