#####

About:
This second mini-project is designed to display system health information, specifically CPU usage, memory usage, disk usage, active users, and active processes
The script is designed to accomplish this by defining a function to fetch each measure, then a main function that calls all of these along with assigning the proper units for comprehension
The information will be displayed in the CLI

#####

Using a Docker container:
included are the files that will spin a Docker container running the latest image from Debian
It will also install Python3, and the python package psutil - a library used to retrieve information on running processes and system utilization

Steps:
**Requires Docker
change working directory to 02-SystemHealthInfo
`docker-compose up --build`

#####

Without a container:
**Requires Python is installed
change working directory to 02-SystemHealthInfo\scripts
`pip install psutil`
`python SystemHealth.py`


#####
