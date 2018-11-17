import time
from selenium import webdriver

def main():
    #Define server.  Make sure to include the / at the end of the URL.  
    #example: http://localhost:8000/"
    server = "http://localhost:8000/"

    #Define your report name (Same as set in ERPNext)
    report = "Test Report"
    #The following defines the address.  This can be hard coded if necessary, if so the server and report variables can be ignored.
    url = server + "desk#query-report/" + report
    # open URL in browser
    driver = webdriver.Firefox()
    driver.get(url)

    #timer
    #the following sets the refresh interval in seconds
    refresh_interval = 30
    while 1==1:
        time.sleep(refresh_interval)
        driver.refresh()

main()
