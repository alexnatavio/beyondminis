# About:
This second mini-project is designed to display system health information, specifically CPU usage, memory usage, disk usage, active users, and active processes <br>
The script is designed to accomplish this by defining a function to fetch each measure, then a main function that calls all of these along with assigning the proper units for comprehension <br>
The information will be displayed in the CLI <br>
<br>

Included are files that will spin a Docker container running the latest image from Debian <br>
It will also install Python3, and the python package psutil - a library used to retrieve information on running processes and system utilization

# Steps:

## With a container:
**Requires Docker <br>
change working directory to 02-SystemHealthInfo <br>
`docker-compose up --build` <br>

## Without a container:
**Requires Python installed <br>
change working directory to 02-SystemHealthInfo\scripts <br>
`pip install psutil` <br>
`python SystemHealth.py` <br>

