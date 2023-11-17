# About:
This second mini-project is designed to display system health information, specifically CPU usage, memory usage, disk usage, active users, and active processes.
This is accomplished with a Python script utilizing the `psutil` library
The information will be displayed in the CLI <br>
<br>

##Steps:

## Running the script:
*Requires Python installed <br>
*Requires Pip (Python package installer) <br>

Clone the repository <br>
change working directory to 02-SystemHealthInfo\scripts <br>
`pip3 install psutil` <br>
`python3 SystemHealth.py` <br>

If Python and Pip are not installed <br>
`sudo apt update` to get latest package list <br>
`sudo apt install python 3` to install Python3
`sudo apt install python3-pip` to install Pip


## Testing in Container
To ensure this would work on a Debian-based platform it was tested using a Docker container with a Debian-based image <br>
Following the steps below will create the container, install all necessary requirements, execute the script to show system health information, and then exit the container. <br>

*Requires Docker <br>
change working directory to 02-SystemHealthInfo <br>
`docker-compose up --build` <br>
