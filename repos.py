import requests
import json

def getRepos(user):
    url1 = f"https://api.github.com/users/{user}/repos"
    repositories = json.loads(requests.get(url1).text)

    list = []

    for repo in repositories:
        name = repo['name']

        url2 = f"https://api.github.com/repos/{user}/{name}/commits"
        count = len(json.loads(requests.get(url2).text))

        list.append((name, count))

    for repo, commits in getRepos(user):
        return f"Repo: {repo}, Number of commits: {commits}"



