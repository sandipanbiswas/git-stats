from com.almabase.github.service.GitHubService import GitHubService
class GitManager:
    def topNRepos(self,org,top_repo_count):
        topRepos=GitHubService().getTopNReposByOrg(org,top_repo_count)
        print 'Top '+ str(top_repo_count) + ' repos in order based on fork_count as follows'
        for topRepo in topRepos:
            print topRepo
        return topRepos

    def topNCommiters(self, org, top_repo_count, top_commiter_count):
        topNRepos=self.topNRepos(org,top_repo_count)
        for repo in topNRepos:
            topCommiters=GitHubService().getTopNCommittersByRepo(repo,top_commiter_count)
            print 'for repo ' + repo[1]['name'] +" top "+ str(top_commiter_count) + " contributors as follows.."
            for commiterList in topCommiters:
             for commiter in commiterList:
                print commiter['login'] + 'with contributions '+ str(commiter['contributions'])

GitManager().topNCommiters("google",3,5)