from behave import given, when, then
from hamcrest import assert_that, equal_to
from features.pages.inventory_page import InventoryPage
from features.pages.login_page import LoginPage

products = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket",
            "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]
wrong_images = ['https://www.saucedemo.com/static/media/sl-404.168b1cce.jpg',
                'https://www.saucedemo.com/static/media/sl-404.168b1cce.jpg',
                'https://www.saucedemo.com/static/media/sl-404.168b1cce.jpg',
                'https://www.saucedemo.com/static/media/sl-404.168b1cce.jpg',
                'https://www.saucedemo.com/static/media/sl-404.168b1cce.jpg',
                'https://www.saucedemo.com/static/media/sl-404.168b1cce.jpg']


@given("I am on the login page")
def step_impl(context):
    page = LoginPage(context)
    page.load()


@when("I enter valid credentials")
def step_impl(context):
    page = LoginPage(context)
    page.enter_user("standard_user")
    page.enter_password("secret_sauce")
    page.click_login()


@when("I enter invalid credentials")
def step_impl(context):
    page = LoginPage(context)
    page.enter_user("user")
    page.enter_password("wrong_password")
    page.click_login()


@when("I enter locked out user credentials")
def step_impl(context):
    page = LoginPage(context)
    page.enter_user("locked_out_user")
    page.enter_password("secret_sauce")
    page.click_login()


@when("I enter problem user credentials")
def step_impl(context):
    page = LoginPage(context)
    page.enter_user("problem_user")
    page.enter_password("secret_sauce")
    page.click_login()


@when("I enter existing user and wrong password")
def step_impl(context):
    page = LoginPage(context)
    page.enter_user("standard_user")
    page.enter_password("wrong_password")
    page.click_login()


@when("I enter existing user and empty password")
def step_impl(context):
    page = LoginPage(context)
    page.enter_user("standard_user")
    page.enter_password("")
    page.click_login()


@when("I enter empty user and existing password")
def step_impl(context):
    page = LoginPage(context)
    page.enter_user("")
    page.enter_password("secret_sauce")
    page.click_login()


@when("I enter empty user and empty password")
def step_impl(context):
    page = LoginPage(context)
    page.enter_user("")
    page.enter_password("")
    page.click_login()


@when("I try to access the inventory page without logging in")
def step_impl(context):
    page = InventoryPage(context)
    page.load()


@then("I should be logged in to the inventory page")
def step_impl(context):
    page = InventoryPage(context)
    assert_that(page.is_on_page(), equal_to(True))


@then("I should see the inventory products in the page")
def step_impl(context):
    page = InventoryPage(context)
    assert_that(page.get_product_names(), equal_to(products))


@then("I should see the invalid credentials error message")
def step_impl(context):
    page = LoginPage(context)
    assert_that(page.get_error_message(),
                equal_to("Epic sadface: Username and password do not match any user in this service"))


@then("I should see the locked out user error message")
def step_impl(context):
    page = LoginPage(context)
    assert_that(page.get_error_message(), equal_to("Epic sadface: Sorry, this user has been locked out."))


@then("I should see the inventory page with all the item images loaded with the same image")
def step_impl(context):
    page = InventoryPage(context)
    assert_that(page.get_product_images_source(), equal_to(wrong_images))


@then("I should see the empty user error message")
def step_impl(context):
    page = LoginPage(context)
    assert_that(page.get_error_message(), equal_to("Epic sadface: Username is required"))


@then("I should see the empty password error message")
def step_impl(context):
    page = LoginPage(context)
    assert_that(page.get_error_message(), equal_to("Epic sadface: Password is required"))


@then("I should see the empty user error message only")
def step_impl(context):
    page = LoginPage(context)
    assert_that(page.get_error_message(), equal_to("Epic sadface: Username is required"))


@then("I should see the login page")
def step_impl(context):
    page = LoginPage(context)
    assert_that(page.is_on_page(), equal_to(True))


@then("I should see the required login error message")
def step_impl(context):
    page = LoginPage(context)
    assert_that(page.get_error_message(),
                equal_to("Epic sadface: You can only access '/inventory.html' when you are logged in."))
