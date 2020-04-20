To run the tests from the command line just use the command "python civic_info_tests.py" (without the quotes).
Make sure that your command prompt is at the location where civic_info_tests.py is located.
Remember to add your issued API Key to the indicated location in civic_info.yaml

To run in Jenkins:
If you want to logging to be sent to Jenkins instead of the specified file,
 change the logging code in lines 5-10 of civic_info_tests.py
As setup run pip install -r requirements.txt from the directory where civic_info_tests.py exists.
Make sure it's the same Python virtual environment that you will be running from Jenkins.
Specify job as "Execute in Window Batch Command" and run
#!/bin/sh
python <absolute path for civic_info_tests>\civic_info_tests.py