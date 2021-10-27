from typing import Collection
from typing_extensions import runtime
from selenium.webdriver.remote.webelement import WebElement

class DealReport:
    def __init__(self, boxes_section_element):
        self.boxes_section_element = boxes_section_element
        self.boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements_by_css_selector(
            'div[class="sc-TBWPX gifNHa cardProdutoListagem"]'
        )

    def pull_deal_box_attributes(self):
        collection = []
        for box in self.boxes:
            # Pulling the hotel name
            link = box.find_element_by_tag_name('a')
            data_name = link.find_element_by_css_selector(
                'div[class="sc-eLwHnm hGtoqp"]'
                )
            data_price = link.find_element_by_css_selector(
                'div[class="sc-bTfYFJ bBqvgl"]'
                )
            product_name = data_name.find_element_by_css_selector(
                'h2[class="sc-jObWnj imnAbk"]'
            ).get_attribute('innerHTML').strip()
            product_price = data_price.find_element_by_css_selector(
                'span[class="sc-iwjdpV ezjpDw priceCard"]'
            ).get_attribute('innerHTML').strip()
            product_brand = data_name.find_element_by_css_selector('span').get_attribute(
                'innerHTML'
            ).strip()

            collection.append(
                [product_name, product_price, product_brand]
            )
        return collection