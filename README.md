# Milestone 2

##Team
ksant, abambre, vsnarvek

##Code Repo:
--------------------------------------------------------------------------

Application Repository used :  https://github.com/kaustubhsant/saws/

##Test
--------------------------------------------------------------------------

###Goal 1 
*The ability to run unit tests, measure coverage, and report the results.*

1. Running unit test:    
        
        python tests/run_tests.py

    [run_tests.py](https://github.com/kaustubhsant/saws/tree/master/tests/run_tests.py) runs all the files which have unit tests written for this application.

2. Measure code coverage: 

Using python [coverage](https://coverage.readthedocs.org/en/coverage-4.0.1/) module.
    1. Run the code coverage for the all files.
    2. Create coverage report readable by Cobertura jenkins plugin as well as create a html report.

3. Display the report result:

    1. Cobertura jenkins plugin will display the coverage report.

 ![image](/images/cobertura-coverage.png)
    
    2. Post-build shell console output will show the test results.

 ![image](/images/tests-console-output.png)


###Screencast for goal 1

On successful execution of test-cases and coverage.

![image](/images/anim.gif)


###Goal 2
"The ability to improve testing coverage using one of the techniques covered in class: constraint-based test generation, fuzzing, etc."

For this goal, we have written a python parser to parse the code and generate test case. We used the [ast](https://docs.python.org/2/library/ast.html) module in python library to parse the code and generate the abstract syntax tree. The code parses the [saws.py](https://github.com/kaustubhsant/saws/tree/master/saws/saws.py) and finds the default arguments that are passed for the functions. It then creates a class object with default arguments passed to its constructor and passes this new object to other tests to have test cases with default arguments. The test generator code is [here](/scripts/test-generator.py) and the generated test file is [here](/scripts/test_saws2.py)

The coverage report before adding test_saws2.py

![image](/images/coverage-before-html.png)

Coverage report after adding the test_saws2.py

![image](/images/coverage-after-html.png)

The statement in saws.py which was not covered before

![image](/images/coverage-before-saws.png)

The statement is covered after adding test_saws2.py

![image](/images/coverage-after-saws.png)


##Analysis
---------------------------------------------------------------------------

###Goal 3 
"The ability to run an existing static analysis tool on the source code, process its results, and report its findings."

For this goal, we are using

	1. [pylint](http://www.pylint.org/) for static source code analysis  
	2. [Voilations](https://wiki.jenkins-ci.org/display/JENKINS/Violations) plugin in Jenkins to report the results 

We are parsing the results obtained by running pylint on our target project and converting them to a format which the Voilations plugin in Jenkins can read from.
	
	pylint -f parseable -d I0011,R0801 saws | tee pylint.out 

The Voilations plugin reads these results and outputs in Jenkins as shown below.

![image](/images/pylint-voilations.png)

###Goal 4 
"The ability to extend an existing analysis tool with a custom analysis, or implement a new analysis from scratch."

For this goal, we have written a [custom analysis tool](/scripts/custom-analysis.py). This tool parses the python code and checks if all the classes in the files have a *constructor(init)* function defined in them. It outputs the class names in which there is no constructor defined.

###Goal 5
"Using hooks or post-build scripts, have the ability to reject a commit if it fails a minimum testing criteria."

For this goal, we are changing the build status to failure when

	1. any test cases fail
	2. coverage goes below certain threshold

and sending an email notification informing the developer to revert the changes.

####Screencast for Goal 5
![image](/images/M2-test.gif)