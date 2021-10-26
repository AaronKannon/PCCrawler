import os
from selenium import webdriver
from typing import Collection
from prettytable import PrettyTable
from core.deal_report import DealReport
import core.constants as const

class Search(webdriver.Chrome):
    def __init__(self, driver_path=const.PATH, teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Search, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            print('Exiting...')
            self.quit()
        else:
            print('Let open...')

    def land_first_page(self, url: str):
        self.get(url)

    def search_by_input(self, field: str):
        search_field = self.find_element_by_id("input-busca")
        search_field.send_keys(field)
        button_search = self.find_element_by_css_selector('button[class="sc-hRMWxn idbNbN"]')
        button_search.click()

    def order_by_desc(self):
        filter = self.find_element_by_css_selector('option[value="-price"]')
        filter.click()

    def change_to_list(self):
        list_button = self.find_element_by_css_selector('button[title="Visualizar em Lista"]')
        list_button.click()

    def report_results(self):
        boxes = self.find_element_by_css_selector(
            'main[class="sc-ctqQKy bSrxiI"]'
        )
        report = DealReport(boxes)
        table = PrettyTable(
            field_names=["Product Name", "Product Price", "Product Brand"]
        )
        table.add_rows(report.pull_deal_box_attributes())
        print(table)

    #class="sc-TBWPX gifNHa cardProdutoListagem"
    #class="sc-jObWnj imnAbk"
    #title="Visualizar em Lista"