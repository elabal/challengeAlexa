
class Locator(object):

    header_results_for_searched_item = "//span[contains(text(),'results for')]/following-sibling::span[contains(text(), '{VALUE}')]]"
    button_page = "//a[text()='{VALUE}']"
