# Keystone project

This project is meant for you to make awesome software, with the skills in your Continuous Delivery and DevOps toolbox.
Have fun, automate and be awesome!

The project can be run by 1-3 people in a team.

## Fork the project

Fork this repository so you can make changes to it:

![Forking project](/docs/images/forking-project.png)

## Enable issues

On your repository, enable issues:

![Enabling issues](/docs/images/enabling-issues.png)

## Welcome to Initrode

Congratulations, you just scored your first job. Fresh out of college.
It pays decently and the interviewers seemed nice. There are all sorts of perks.
It even sounded like you would work with some bleeding edge technologies.

So now you're ready for whatever tasks they'll throw at you.
You started yesterday together with a few college grads.
You spent the day yesterday getting access to the building.
You know now how to both obtain lunch and relieve any pressures such a feast might impose on you.

You've got your state-of-the-art laptop booted and are ready to make the world a better place,
To innovate! To use all the skills you've gathered while studying at the university.

## Speak of the devil

Your project manager calls you for a meeting and let's you in on the details on the first task that you'll complete.

He truly knows that you are very eager to get started and do cool stuff. But unfortunately they have a Python Flask Web application that runs in production at a bunch of customers, and no one quite remembers how it works. _It's called CoDeChan, just like 4chan but for CoDe. You get it, right, don't you? Ahh never mind then...._

The application is _CoDe Chan_ an anonymous posting tool. No one really knows why or for what the customers use it. But none the less, it brings in some cash.

It is obviously important to keep this application running well and good, otherwise Initrode might end up looking very bad indeed.

Congratulations, on your second day you became the proud owner of a piece of **Legacy Code**.

Now, where to start?

## The bare necessities

You've been handed a huge pile of .. Well you do not quite know of what.

You know that you need two things in order for you to be a success.

You need to know what is happening to the code and who is working on what.

The first step is obvious. Put your code under version control and set up a task management system for your project.

### Collaboration with GitHub Projects

The rest of this README contains a lot of individual tasks to complete. Just as with any other project, you will want some way of managing which tasks you are currently working on and what is on you backlog. You could do this with sticky-notes on a wall, but we would recommend you use an actual online task management system instead - especially if you are working as a group.

An easy way to create an agile task management setup for your project is to use GitHub issues together with the GitHub Projects feature found on the `projects` tab. This allows you to have a full swim lane and track your tasks in a nice visual way that is completely integrated with GitHub.

Go over to the `Projects` tab and create your project.

![Create project](/docs/images/create-project.png)

_Consider every step in a task as a story, also created as an issue in your GH repository. Groom them together, breaking down the stories where it makes sense._

It is good practice to always mention which issue you are working on in your commit messages. GitHub will actually use this information to link your issues and commits together in the UI, giving you valuable traceability information. 

The even cooler next step is to use GitHubs build in automation to automatically close issues when you commit the change. See [Closing issues using keywords](https://help.github.com/en/articles/closing-issues-using-keywords).

You can even move beyond this and look at (Automation for project boards)[https://help.github.com/en/articles/about-automation-for-project-boards].

... and now on to the actual project work.

## Bat out of hell

In some ancient documentation you can see that you can run the application with the command `python run.py`.

Try that and see how that flies for you.

Of course dependencies are not explicitly managed, so you can't just start up the application.

Figure out the dependencies, put them in `requirements.txt` so you can install them with `pip install -r requirements.txt`.

Now that you've fixed that hurdle and you've actually got an application running, spend a few minutes familiarizing yourself with it.

### Task

- Investigate dependencies
- Put dependencies in `requirements.txt`
- Install dependencies with `pip install -r requirements.txt`
- Run application with `python run.py`
- Familiarize yourself with the application

## I'll pack my bags and go

You've got your dependencies handled and all is good. Or sort of good. 

It is tedious to set up dependencies on each system that you want to run on.

Luckily you know how to use Docker.

### Task

- Create a `Dockerfile` containing your application code and requirements
- Build the Docker image
- Run the application in Docker with a docker-compose file
- Check Dockerfile and compose file into your repository.

## Testing the waters

The ability to run your project in Docker has made many things easier for you. You even have the ability to track code changes and manage your self-organizing team.
Things are looking up for you.

You keep stepping a bit on each others toes, so of course you look into some sort of automated tests.
Luckily the project was not created by entities of pure evil. There are some tests that can be run. You need to automate them. You can run the current set of tests with `python tests.py`.

Continuous Integration is the goal, and you look to your good old friend Jenkins for some needed support.

### Task

- Setup a Jenkins project
- Setup a Continuous Integration pipeline (the config Jenkins is running) 
- Run the tests in the pipeline
- Make sure you maintain mainline integrity meaning all commits to master needs to be tested by CI before merging.

> Hint: A good starting point could be [GitHub Flow](https://help.github.com/en/articles/github-flow)

## Cut out the boring stuff

Every time that release time comes around, you get uncomfortable. You do not feel safe about deploying to production, and it always seems to be the case that nothing is quite the same from time to time.

It is now time to script your way to deployment.

> Hint: If you want to run a dockerfile on your server, you can ssh into the server from Jenkins, just like you SSH into the server from your machine.

### Task

- Create a script that runs the application on your server. (tip, you can use the ssh key you were given to the cloud instance. Look here fore more guidance: https://www.jenkins.io/blog/2019/02/06/ssh-steps-for-jenkins-pipeline/)
- Augment your script such that you can deploy to multiple targets ( eg. local, staging, production ).
- If you are more people in the team, try to push your code to one of the other servers, using its private IP (You can get that by issuing the command `ifconfig` ).

## A means to an end

You realise that your process is actually quite mature now, but you don't exactly feel you're quite done.

Even though you are testing the internal quality of your code - you do not have any means of functional testing.

You just want the bare minimum test. So you add a test in your pipeline that will deploy your Dockerized application temporarily and test its availability.

Even a very simple thing as being able to reach your server with `curl` or `wget` would be much better than what you have now. Nothing.

### Task

- Use your automated deploy to deploy in testing
- Do functional testing (You know your servers IP)
- Display result in Jenkins
- This might not be a tollgate criteria, but it is important information for you to gain.

## Now we have time for the cool stuff

You've reached a very mature point for your software development.
You have a containerized, automatically testable and deployable application.

You know who is working on what and why. You have full faith that you can refactor your legacy project without destroying anything.

As you dare to change the code, it is no longer legacy, it is _just your software_.

Now it is time to tread new paths.

### Task

The following are suggestions to explorations that you can take.

- Run a linter as part of the pipeline
- Stress the application, using for instance the docker image `rufus/siege-engine` (more info about using the application can be found [here](https://www.linode.com/docs/tools-reference/tools/load-testing-with-siege/))
- Refactor to remove the unused User and login code from the application
- Add another machine as a build node, and make it run some of the steps in the pipeline.
- Deploy to production if functional tests pass
- Add something to do your buildtasks for you. Gradle, Rake, Grunt, Make, etc.
- Allow rollbacks to a previous version
- Setup an ELK-stack for monitoring
- Use for instance HAProxy to have multiple containers running in production, through a single interface
- Use persistent storage for your SQLite database
- Setup a database in a separate Docker container, change application to use it
- Investigate the usage of docker-compose for your multi-container setup
- Investitage the usage of Kubernetes for your multi-container setup
- Do some TDD on the application
  - Make sure that you can't do an empty post
  - Make links in a post clickable
  - Make the layout prettier
  - Add additional pages
  - Add fields to the post
