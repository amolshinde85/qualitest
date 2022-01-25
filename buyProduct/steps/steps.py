from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import environment
from time import sleep

driver = None
url = environment.products_page


def test_before():
    print("Before starting tests, initiating the browser session.")
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(10)


def test_finally():
    print("After tests ran, ending the browser session.")
    print("inside")
    driver.quit()


@given('I add four different products to my wish list')
def step_implement_add_four_products(context):
    print("I add four different products to my wish list")
    test_before()
    accept_cookies = driver.find_element(By.XPATH, "//a[@class='cc-btn cc-accept-all cc-btn-no-href']")
    accept_cookies.click()
    sleep(1)
    select_item = driver.find_elements(By.XPATH, "//a[@class='add_to_wishlist single_add_to_wishlist']")
    for element in range(0, 4):
        sleep(3)
        select_item[element].click()
    sleep(2)


@when('I view my wishlist table')
def step_implement_view_wishlist(context):
    print("I view my wishlist table")
    driver.find_element(By.XPATH, "//div[@class='header-wishlist']").click()
    sleep(2)


@then('I find total four selected items in my wish list')
def step_implement_total_four_selected(context):
    print("I find total four selected items in my wish list")
    products_in_wish_list = driver.find_elements(By.XPATH,
                                                 "//tbody[@class ='wishlist-items-wrapper']//td[@ class ='product-name']")
    sleep(2)
    desired_product_list = ['Bikini', 'Black pants', 'Black trousers', 'Evening trousers']
    for product in range(len(products_in_wish_list)):
        assert products_in_wish_list[product].text in desired_product_list


@when('I search for the lowest price item to my cart')
def step_implement_search_lowest_price_item(context):
    print("I search for the lowest price item to my cart")
    items_in_wish_list = driver.find_elements(By.XPATH,
                                              "//table[@class='shop_table cart wishlist_table wishlist_view traditional responsive   ']//tr//span[@class='woocommerce-Price-amount amount']/bdi")

    for item in range(len(items_in_wish_list) - 1):
        if item == 0:
            item_price = float(items_in_wish_list[item].text.strip('£'))
        next_item_price = float(items_in_wish_list[item + 1].text.strip('£'))
        if next_item_price < item_price:
            item_price = next_item_price

    driver.find_element(By.XPATH,
                        "//td//*[contains(text(), '" + str(
                            item_price) + "')]//following::td[@class='product-add-to-cart']").click()
    sleep(2)
    driver.find_element(By.XPATH, "//div[@class='header-cart-inner']//i[@class='la la-shopping-bag']").click()
    sleep(2)


@then('I am able to verify the item in the cart')
def step_implement_verify_item_low_price(context):
    print("I am able to verify the item in the cart")
    actual_product_in_cart = driver.find_element(By.XPATH, "//td[@class ='product-name']//a")
    product_added_in_cart = 'Bikini'
    assert actual_product_in_cart.text == product_added_in_cart
    test_finally()