# Milestone 2

##Team:
ksant, abambre, vsnarvek

##Code Repo:
--------------------------------------------------------------------------

Application Repository used :  https://github.com/kaustubhsant/saws/

##Test MileStone:
--------------------------------------------------------------------------

###Test Goal 1 :
    
The ability to run unit tests, measure coverage, and report the results.

1. Running unit test:
    ```
        python tests/run_tests.py
    ```
    'run_tests.py' calls all the unit tests of this application.

2. Measure code coverage: Using python 'coverage' library,
    1. Run the code coverage for the all files.
    2. Create coverage report for cobertura jenkins plugin as well as create a html report.

3. Display the report result:
    1. Cobertura jenkins plugin will display the coverage report.
    2. post-build shell console output will show the test results.
