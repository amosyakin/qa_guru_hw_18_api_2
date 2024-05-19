from selene import browser, have


def should_cart_have_product_name(product_name):
    browser.element('.shopping-cart-page').should(have.text(product_name))
