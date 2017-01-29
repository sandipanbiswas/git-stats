import requests
import json
from com.almabase.github.settings import constants
class GitHubRepo:

    def getReposByOrg(self,org):
        page=1
        payload = {'page': page,'client_id':constants.CLIENT_ID,'client_secret':constants.CLIENT_SECRET}
        repos=requests.get(constants.GITHUB_ORG_REPOS_URL, params=payload)
        repo_objs = []
        while len(repos.content)>0 and repos.status_code==200:
            temp_repo_objs = json.loads(repos.content)
            if len(temp_repo_objs) == 0:
                break
            repo_objs.append(temp_repo_objs)
            page = page + 1
            payload = {'page': page}
            repos = requests.get(constants.GITHUB_ORG_REPOS_URL, params=payload)
        if repos.status_code>=400:
            print 'Rate Limit exceeded. Reading from file..'
            with open('../json/repos.json') as data_file:
                repo_objs = json.load(data_file)

        return repo_objs;

    def getCommitersByRepo(self, repo):
        page = 1
        payload = {'page': page,'client_id':constants.CLIENT_ID,'client_secret':constants.CLIENT_SECRET}
        url=constants.GITHUB_REPO_URL+repo[1]['owner']['login']+'/'+repo[1]['name']+'/contributors'
        commiters = requests.get(url, params=payload)
        commiter_objs = []
        while len(commiters.content) > 0 and  commiters.status_code==200:
            temp_repo_objs = json.loads(commiters.content)
            if len(temp_repo_objs) == 0:
                break
            commiter_objs.append(temp_repo_objs)
            page = page + 1
            payload = {'page': page}
            commiters = requests.get(url, params=payload)

        if commiters.status_code >= 400:
            print 'Rate Limit exceeded. Reading from file..'

        return commiter_objs;

