# Milestone 1

##Team:
ksant, abambre, vsnarvek

##Code Repo:
--------------------------------------------------------------------------

Application Repository used :  https://github.com/kaustubhsant/saws/

##Build Section:
--------------------------------------------------------------------------

We are using Jenkin server hosted on EC2 instance, as our continous integration server pipelined with 'Git' a version control system to build the target project.

- We have created integration end-points both at the git repository end by adding webhook for the hosted Jenkin service running on the EC2 instance as well as the at the Jenkin server end where it is listening for the events published by the git repository per associated branch.
- For our python application we are using 'pip' as our package manager to build the given project , triggered through the shell execution. We are using workspace clean plugin in Jenkins to clean up all the environment before the build is executed.
- In Jenkins, successful execution is determined by the status of last successful command executed in the build procedure. In case of the failures in the build, email notification will be sent as part of post-build execution procedure.
- In Jenkins we have configured different jobs associated with the different branches from the git repository.
- Jenkins allows tracking as well as the displaying of past builds through the web interface.

###Screencast Demonstrating Jenkins Setup:
----------------------------------------------------------------------------
1. Launch AWS EC2 instance
2. Install Jenkins
    - Install Jenkins dependency and start Jenkins.
    - Install proxy which can redirect calls to Jenkin Service End points.
    - The jenkins setup script is [here](/scripts/jenkins-build.sh).

![image](/images/jenkins-setup.gif)

###Screencast of Demonstrating Jenkins configuration Setup:
----------------------------------------------------------------------------
1. Set up security and add user
2. Add githib plugin.
3. Setup Email Notification
4. Add workspace clean plugin
5. Create new job for master branch
6. Create new job for develop branch

The jenkins job config xml is [here](/config/config.xml).

![image](/images/config-setup.gif)

###Screencast For Integration with Git Repo:
----------------------------------------------------------------------------
1. Add jenkin-webhook with the github repository.

![image](/images/git-hook-setup.gif)

###Screencast of Demonstarting Jenkins build jobs triggered via Git push:
----------------------------------------------------------------------------
The devops-develop build job is triggered when a git push is done on develop branch.
The deveops-master build job is triggered when a git push is done on master branch.
Email notification is sent on build job success and failure both.
The build script is [here](/scripts/build.sh) and the unittest script to test if all dependencies are installed is [here](/scripts/test_dependencies.py).

![image](/images/M1-buildstart.gif)

###Build History screenshot
----------------------------------------------------------------------------
Build history is displayed in the Jenkins and can be easily tracked.

![iamge](/images/buildhistory.png)

###Contribution
--------------------------------------------------------------------------

-  Jenkins setup on EC2 instance and configuring Git webhook.  - abambre / ksant
-  Handled the jenkins configuration to create build jobs. -  vsnarvek / ksant
-  Handled the build and unittest script and testing the build system.  - ksant /abambre
