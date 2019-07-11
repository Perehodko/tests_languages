link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_in_basket_is_present(browser, present=False):
    browser.get(link)

    try:
        find_btn = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
        present = True
    except NoSuchElementException:
        present = False
    print("Basket is present: ", present)
