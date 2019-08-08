import os
import json
import requests

# Authentication for user filing issue (must have read/write access to
# repository to add issue to)
USERNAME = 'YourGitHubHandle'
PASSWORD = os.environ['GITHUB_PASSWORD']

# The repository to add this issue to
REPO_OWNER = 'YourGitHubHandle'
REPO_NAME = 'ca-project'

def make_github_issue(title, body=None, labels=None):
    '''Create an issue on github.com using the given parameters.'''
    # Our url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)
    # Create an authenticated session to create the issue
    session = requests.Session()
    session.auth = (USERNAME, PASSWORD)
    # Create our issue
    issue = {'title': title,
             'body': body,
             'labels': labels}
    # Add the issue to our repository
    r = session.post(url, json.dumps(issue))
    if r.status_code == 201:
        print 'Successfully created Issue "%s"' % title
    else:
        print 'Could not create Issue "%s"' % title
        print 'Response:', r.content

make_github_issue('Investigate Python dependencies', 'Fill out requirements.txt', ['task'])
make_github_issue('Install python dependencies', 'Using pip, may require sudo', ['task'])
make_github_issue('Familiarize yourself with CoDe Chan', '', ['task'])
make_github_issue('Create Dockerfile', 'Create a Dockerfile, based on ubuntu and installing pip, requirements and running the run.py', ['task'])
make_github_issue('Build Docker image', '', ['task'])
make_github_issue('Run the app using the docker container', '', ['task'])
make_github_issue('Create project build in CircleCI', '', ['task'])
make_github_issue('Setup a pipeline for CI', '', ['task'])
make_github_issue('Run the tests in the pipeline', '', ['task'])
make_github_issue('Create a script for local', '', ['task'])
make_github_issue('Augment script to hit multiple deploy targets', '', ['task'])
make_github_issue('Use CircleCI and deploy to testing', '', ['task'])
make_github_issue('Test in testing environment', '', ['task'])
make_github_issue('Display test results in CircleCI', '', ['task'])
make_github_issue('Deploy to production if test passes', '', ['task'])
make_github_issue('Allow rollbacks', '', ['task'])
make_github_issue('Setup ELK for monitoring', '', ['task'])
