from selenium import webdriver

def before_all(context):
    context.driver = webdriver.Chrome(executable_path="C:\\Users\\rmishra\\Downloads\\logintest_dlg-master\\browser\\chromedriver.exe")
def after_all(context):
    context.driver.quit()
