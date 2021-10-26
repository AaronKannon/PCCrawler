from core.search import Search
import time


def set_field() -> str:
    field = input("Input your search: ")
    return field

def crawl_one_site(url: str):
        with Search() as crawler:
            crawler.land_first_page(url)
            field = set_field()
            crawler.search_by_input(field)
            crawler.order_by_desc()
            crawler.change_to_list()
            crawler.refresh()
            crawler.report_results()
            time.sleep(10)