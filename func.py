from requests import get, utils
from bs4 import BeautifulSoup
from csv import DictWriter


def create_csv(data):
    info = ["name", "url", "price", "dis_price", "discounted"]
    with open('product_prices.csv', 'w', encoding='utf-8') as csvfile:
        writer_csv = DictWriter(csvfile, fieldnames=info)
        writer_csv.writeheader()
        writer_csv.writerows(data)


def prepare_beau4_soup(website):
    soup = BeautifulSoup(website, 'html.parser')
    prod_selector = soup.select('div.ty-grid-list__item.ty-quick-view-button__wrapper.grid_dato')
    products = []
    for prod in prod_selector:
        product_name = str(prod.select('a.product-title')[0].text)
        product_url = str(prod.select('a.product-title')[0]['href'])
        try:
            original_price = str(prod.select('span.ty-price-num')[0].text)
        except IndexError:
            original_price = False
        try:
            discounted_price = str(prod.select('span.ty-list-price.ty-nowrap')[0].text)
        except IndexError:
            discounted_price = 0

        if discounted_price == 0:
            discounted = False
        else:
            discounted = True
        if original_price:
            products.append({"name": product_name, "url": product_url, "price": original_price,
                            "dis_price": discounted_price, "discounted": discounted})
    return products


def get_response(url):
    headers = utils.default_headers()
    headers.update(
        {
            'User-Agent': 'My User Agent 1.0',
        }
    )
    response = get(f"{url}?sl=ge&items_per_page=999", headers=headers)
    create_csv(prepare_beau4_soup(response.text))
