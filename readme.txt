To run the tests from the command line just use the command "python civic_info_tests.py" (without the quotes).
Make sure that your command prompt is at the location where civic_info_tests.py is located
To run in Jenkins
As setup run pip install -r requirements.txt from the directory where civic_info_tests.py exists.
Make sure it's the same Python virtual environment that you will be running from Jenkins.
Specify job as "Execute in Window Batch Command" and run
#!/bin/sh
python <absolute path of civic_info_tests>\civic_info_tests.py