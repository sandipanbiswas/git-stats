from com.almabase.github.service.GitHubService import GitHubService
class GitManager:
    def topNRepos(self,org,top_repo_count=5):
        topRepos=GitHubService().getTopNReposByOrg(org,top_repo_count)
        if len(topRepos)>0:
            print 'Top '+ str(top_repo_count) + ' repos in order based on fork_count as follows \n'
            for topRepo in topRepos:
                print 'Name : '+ topRepo[1]['name'] + ' url :' + topRepo[1]['url'] + ' fork_count ' + str(topRepo[1]['forks_count'])
        return topRepos

    def topNCommiters(self, org, top_repo_count=5, top_commiter_count=3):
        topNRepos=self.topNRepos(org,top_repo_count)
        for repo in topNRepos:
            topCommiters=GitHubService().getTopNCommittersByRepo(repo,top_commiter_count)
            if (len(topCommiters) > 0):
                print 'for repo ' + repo[1]['name'] + " top " + str(top_commiter_count) + " contributors as follows.. \n"
            for commiter in topCommiters:
                    print commiter['login'] + 'with contributions '+ str(commiter['contributions'])
        print '\n'

    def start(self):
        org = raw_input('Enter name of organisation for which no of top repositories you want to fetch: ') or "google"
        no_of_repos=raw_input('Enter no of top repositories you want to fetch: ') or 5
        no_of_committers=raw_input('Enter no of top committers in each repo you want to fetch: ') or 3
        self.topNCommiters(org, no_of_repos, no_of_committers)


GitManager().start()