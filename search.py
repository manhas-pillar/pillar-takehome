# search.py

from wtforms import Form, StringField

class RepoSearchForm(Form):
    search = StringField('')