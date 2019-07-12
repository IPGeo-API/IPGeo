#### How to use IPGeo
Before running on your local computer, make sure you have python 3.6+ with the latest version of pandas installed and your key and request.txt in the same folder as the python file.
Request.txt should be formated in one IP address per line.
To Install Pandas, run ```pip install pandas```.
Before running for the first time, make a folder named "results". This will have all the .json and .csv files stored in it after running.
To query IP, run ```python request.py``` in your command prompt environment with the pandas installed.
A file named result.csv and result.json are saved which have the relevant information regarding your IP Search.

Errors are more than likely caused by a non existant IP in the data base.