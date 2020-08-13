- [Pipeline Handin](#pipeline-handin)
  - [Requirements](#requirements)
  - [Hand in](#hand-in)
- [Links](#links)

# Pipeline Handin

This assignment is more or less the result of [the ca-project](https://github.com/praqma-training/ca-project)
You are welcome to use your own project and set it up with the process described in the project.

## Requirements

- Pipeline should be _as code_ inside the repository on Github
- The pipeline should have at least three different stages
- Two of the stages (e.g. _create artifact_ and _dockerize application_) needs to run in parallel
- You may only checkout the code once during the pipeline
- It should be possible to download the newest artifact from Jenkins job webpage
- If at all possible, you should produce both the binaries (in pythons case, a zip file), as well as a docker image on docker hub
- you should only push to dockerhub if the branch is named 'master'

## Hand in

- (Group) Link to the Jenkins project website
- (Group) Link to the Git repository where the code (and Jenkinsfile) are located
- (Group) Link to the Dockerhub repository where the image is located
- (Individual) A description of your pipeline, and any problems that you run into during development
- (Individual) A description on how you would make sure that master only have commits that have been tested by the CI server


# Links

- Jenkins - <http://104.155.56.49:8080/job/ca-project/>
- GitHub - <https://github.com/mathn16/ca-project>t>
- DockerHub - <https://hub.docker.com/r/mathn16/ca-project> / docker pull mathn16/ca-project