from behave import *
from shared_data.shared_data import *
from behave.runner import Context

use_step_matcher("re")


@given("The user is on login page of a website")
def loading_url(context: Context):
    geturl(context)


@when(u"User type the correct <Username> in the email field and <Password> in the password field")
def enter_with_correct_credential(context:Context):
    enter_username(context,context.table[0][0]) #username from feature file with index 0
    enter_password(context,context.table[0][1]) #username from feature file with index 1

@then(u'User press "Login" button')
def login_button_press(context: Context):
    presslogin(context)


@then(u'User should see "Successfully logged in!" message')
def success_message(context: Context):
    checkloginstatus(context)


@given("User is on login page of a website")
def loading_url(context: Context):
    geturl(context)


@when(u"User type the incorrect <Username> in the email field and <Password> in the password field")
def enter_with_incorrect_credential(context:Context):
    enter_username(context,context.table[0][0]) #username from feature file with index 0
    enter_password(context,context.table[0][1]) #username from feature file with index 1


@then(u'User pressed "Login" button')
def login_button_press(context: Context):
    presslogin(context)


@then(u'User should see not see "Successfully logged in!" message')
def success_fail_message(context: Context):
    checkloginstatus(context)