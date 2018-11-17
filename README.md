# reportviewer
A simple raspberry pi-based report viewer for ERPNext.

The goal of this project is to create a simple script that opens a report in ERPNext, and refreshes the report periodically.

An authentication function still needs added to get this working.

## Dependencies
* Python
* pip
* Selenium
* geckodriver
* Mozilla Firefox

## Directions

1. Ensure Python is installed, along with pip
1. Install selenium `pip install selenium --user`
1. Install geckodriver
  1. download from https://github.com/mozilla/geckodriver/releases
  1. Extract download to `~/usr/local/bin`
1. Install this repo from https://github.com/cgpurbaugh/reportviewer
1. Add the following to `.bashrc`

   ```
   echo Launching ReportViewer`
   python /home/pi/reportviewer.py`
   ```

1. change `/home/pi/reportviewer.py` to the location of reportviewer.py on your system.
1. change the options in reportviewerconfig.py to match your ERPNext server.
1. reboot and test
1. if there are any problems, you can open an issue on the Github repo at https://github.com/cgpurbaugh/reportviewer
