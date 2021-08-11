
class Locator(object):

    header_results_for_searched_item = "//span[contains(text(),'')]/following-sibling::span[contains(text(), '{VALUE}')]"
    button_page = "//a[text()='{VALUE}']"
    product_by_index = "//div[@data-index='{VALUE}']//h2//a"
    