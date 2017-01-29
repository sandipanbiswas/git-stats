from com.almabase.github.repo.GithubRepo import GitHubRepo
import json
import heapq
class GitHubService:

    def getTopNReposByOrg(self,org,top):
        heap=[]
        repoList=GitHubRepo().getReposByOrg(org)
        #Using min heap to get n smallest or largest repos by fork count
        for repos in repoList:
            for repo in repos:
                heapq.heappush(heap,(repo['forks_count'],repo))

        return heapq._nlargest(top,heap)

    def getTopNCommittersByRepo(self,repo,top):
        commiterList=GitHubRepo().getCommitersByRepo(repo)
        i=0
        topNCommiters=[]
        #By default the api gives committers list in descending order of contributions. Getting top n committers from
        #list
        for commiter in commiterList:
            topNCommiters.append(commiter)
            i=i+1
            if i >= top:
                break

        return  topNCommiters


