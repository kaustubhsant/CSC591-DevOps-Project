# Milestone 2

##Team:
ksant, abambre, vsnarvek

##Code Repo:
--------------------------------------------------------------------------

Application Repository used :  https://github.com/kaustubhsant/saws/

##Test:
--------------------------------------------------------------------------

###Test Goal 1 :
    
"The ability to run unit tests, measure coverage, and report the results."

1. Running unit test:
    ```
        python tests/run_tests.py
    ```
    'run_tests.py' calls all the unit tests written for this application.

2. Measure code coverage: Using python 'coverage' library,
    1. Run the code coverage for the all files.
    2. Create coverage report for cobertura jenkins plugin as well as create a html report.

3. Display the report result:
    1. Cobertura jenkins plugin will display the coverage report.
    2. post-build shell console output will show the test results.

###Screencast for goal 1:

1. On successfule execution of test-cases and coverage.

![image](/images/anim.gif)


###Test Goal 4 :

"The ability to extend an existing analysis tool or Introduce a data-flow analysis."

In this milestone, we have added data-flow analysis tool 'pyntch' which examines a source code and infers all possible types of variables, attributes, function arguments. Then it detects possible exceptions caused by type mismatch, attribute not found, or other types of exceptions raised from each function.

![image](/images/pytch_error.png)

