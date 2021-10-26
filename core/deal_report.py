from typing import Collection
from typing_extensions import runtime
from selenium.webdriver.remote.webelement import WebElement

class DealReport:
    def __init__(self, boxes_section_element):
        self.boxes_section_element = boxes_section_element
        self.boxes = self.pull_deal_boxes()
        print(self.boxes)

    def pull_deal_boxes(self):
        print('yeay1')
        return self.boxes_section_element.find_elements_by_class_name(
            'sc-TBWPX gifNHa cardProdutoListagem'
        )

    def pull_deal_box_attributes(self):
        collection = []
        print('yeay2')
        for box in self.boxes:
            print(box)
            # Pulling the hotel name
            link = box.find_element_by_tag_name('a')
            print(link)
            data = link.find_element_by_class_name('sc-eLwHnm hGtoqp')
            print(data)
            product_name = data.find_element_by_class_name(
                'sc-jObWnj imnAbk'
            ).get_attribute('innerHTML').strip()
            product_price = data.find_element_by_class_name(
                'sc-iwjdpV ezjpDw priceCard'
            ).get_attribute('innerHTML').strip()
            product_brand = data.find_element_css_selector('span').strip()

            collection.append(
                [product_name, product_price, product_brand]
            )
            print('yeay3')
        return collection