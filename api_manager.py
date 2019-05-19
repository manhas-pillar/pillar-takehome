import json
import requests
import process_data

api_url_base = 'https://api.github.com/'
headers = {'Content-Type': 'application/json',
           'User-Agent': 'Pillar Take Home',
           'Accept': 'application/vnd.github.v3+json'}
github_username = 'manhas-pillar'

#TODO: Use OAuth Instead
#TODO: Tokens and other sensitive information should never be stored in a committed file. Remove
github_basic_token = '7bd420c6982b08073d2f258c6a889690db5419b5'

#TODO: Write unite tests for these functions
def get_repos(organization):
    repos_api_url = '{}orgs/{}/repos'.format(api_url_base, organization)

    response = requests.get(repos_api_url, headers=headers, auth=(github_username, github_basic_token))

    if response.status_code == 200: #TODO: More robust error handling
        repositories = json.loads(response.content.decode('utf-8'))
        return (repositories)
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, repos_api_url))
        return None

#Returns the contributors list for the given url. 
#TODO: there is max of thirty per page so will need to paginate to retrieve full list
def get_contributors(contributors_api_url):
    response = requests.get(contributors_api_url, headers=headers, auth=(github_username, github_basic_token))

    if response.status_code == 200:
        contributors = json.loads(response.content.decode('utf-8'))
        return (contributors)
    elif response.status_code == 204:
        return []
    else:
        print('[!] HTTP {0} calling [{1}]'.format(response.status_code, contributors_api_url))
        return None

#TODO: this can be abstracted to be a function that takes in variable input instead of being restricted to stars, forks, etc
def build_repo_data(repositories_list):
    stars_data = {}
    forks_data = {}
    contributors_data = {}

    for repository in range(len(repositories_list)):
        stars_data[repositories_list[repository]['name']] = repositories_list[repository]['stargazers_count']
        forks_data[repositories_list[repository]['name']] = repositories_list[repository]['forks_count']

        contributors = get_contributors(repositories_list[repository]['contributors_url'])

        if contributors is None:
            contributors_data[repositories_list[repository]['name']] = 0
        else:
            contributors_data[repositories_list[repository]['name']] = len(contributors)

    repo_data_sorted = process_data.sort_repo_data([stars_data, forks_data, contributors_data])

    return repo_data_sorted

