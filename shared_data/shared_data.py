import time
from behave.runner import Context

data = "url_data_set.txt"


def geturl(context: Context):
    file = open(data, "r+") #Open the file in read mode
    url = file.readline() #reading one line from the file
    file.close() #file is close
    context.driver.get(url) #Intial selenium web driver to open the url


def checkloginstatus(context: Context):
    try:
        assert ("Error message") not in context.driver.page_source
    except AssertionError:
        print("Login failed")
    else:
        print("Login success")
#exception, try and catch

#fine elements by xpath

def enter_username(context: Context, username):
    elem1 = context.driver.find_element_by_xpath("//div[1]/input[1]")
    elem1.send_keys(username) #enter the username in selected field


def enter_password(context: Context, password):
    elem2 = context.driver.find_element_by_xpath("//div[2]/input[1]")
    elem2.send_keys(password) #enter the password in selected field


def presslogin(context: Context):
    context.driver.find_element_by_xpath("//button[contains(text(),'Login')]").click()
    #login button is pressed

def wait_and_quit(context: Context):
    time.sleep(10) #wait for 5 second
    context.driver.close() #close the driver(browser)