from bs4 import BeautifulSoup
import json
import requests
from requests.exceptions import Timeout
from discord_webhook import DiscordWebhook, DiscordEmbed
from threading import Thread, current_thread
import time
import sys
import os

PARENT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)))

# ROOT PATH /monitor/
sys.path.append(PARENT_DIR)
from etc.config import *
from etc import config
from models.Product import Product
from models.Status import Status

art()
config.load()
DELAY = config.get['Config']['Delay']
WEBHOOK = config.get['Config']['Webhook']
KEYWORD = config.get['Config']['Keywords']
BASE_URL = config.get['Config']['Url']
SEARCH = '/shop/search?q='
used_arc_headers = {

    "authority": "www.usedgear.arcteryx.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "ccept-language": "en-US,en;q=0.9",
    "sec-ch-ua-platform": "macOS",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/98.0.4758.102 Safari/537.36 "
}


def build_url(search_key: str):
    """
    Builds Website Query Param
    :return:
    """
    url = BASE_URL + SEARCH + search_key
    return url


def update_json(current_stock):
    """
    Store Products In Json File
    :param current_stock:
    :return:
    """

    try:
        with open('instock.json', 'w') as f:
            json.dump(current_stock, f, indent=2)
            f.close()
    except Exception as e:
        log.error(e)


def multiple_sizes(item):

    # Check if there are multiple sizes for the item
    size = item.find("span", {"class": "sizes"}).select("ol > li")
    if len(size) > 1:
        return True


def get_info(url: str, headers: dict):
    """
    Scrapes webpage and returns dom elements
    :return: Dom elements
    """

    global r
    try:
        s = requests.Session()
        r = s.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        empty_page = soup.find("div", {"class": "Search isEmpty"})

        # Checking if results are blank
        if empty_page:
            cPrint(f"NO RESULTS", current_thread().name, "red")
            log.info("NO RESULTS")
            return 1
        else:
            list_of_products = soup.find("div", {"class": "List"})
            return list_of_products

    # Catch exception and change proxy/user agent
    except requests.ConnectionError as e:
        print(f"Error Connecting To: {build_url()}: {e}")

    finally:
        r.close()


def create_product(html_item_list, search_key: str, start: bool):
    final_items = {}
    items = []
    try:
        for item in html_item_list.findAll("li", {"class": "TileItem"}):

            # Only retrieve items that match the keyword
            if search_key.upper() in item.text.upper():

                # Declare variables
                name = item.find("span", {"class": "title"}).text
                size = item.find("span", {"class": "sizes"}).text
                price = item.find("div", {"class": "price"}).find("span").text
                image = item.find('img')['src']
                size_list = item.find("span", {"class": "sizes"}).select("ol > li")

                # Retrieve link and split the parameter
                link = BASE_URL + item.find('a').get('href')
                link_new = link.split('&aqi=', 1)[0]

                if not multiple_sizes(item):

                    # Create a product dictionary for each item
                    new_product = Product(name, size, price, link_new, image)

                    # Add product dictionary to list
                    items.append(new_product.get_product())

                else:

                    # Create a product dictionary for each size
                    for sizes in size_list:
                        new_product = Product(name, sizes.text, price, link_new, image)
                        items.append(new_product.get_product())

        # Creates key(keyword): pair(list of products) in final_items dictionary
        final_items.setdefault(search_key, items)

        if not start:
            cPrint(f"{len(items)} Results For {search_key}", current_thread().name, "yellow")
            log_request.info(f"Retrieved {len(items)}: {items}")

        return final_items

    except Exception as e:
        log.error(f"[Method: create_product()] - issue with product list: {e}")


def stock_comparitor(current_stock, products: list, start: bool, search_key: str):
    """
    Compares items scraped from website with database
    :param search_key:
    :param start: determine whether to push to discord
    :param current_stock: List of items stored in a dict for tracking
    :param products: List of items stored in dict scraped from website
    """
    global instock

    # First startup will initialize data
    if start:
        current_stock[search_key] = products[search_key]

        cPrint(f"Database Built For {search_key.upper()}", current_thread().name, "yellow")
        log.info(f"Database Built For {search_key.upper()}")

        # Update json file
        update_json(current_stock)
        return current_stock

    for product in products[search_key]:
        if product not in current_stock[search_key]:
            try:

                # Append new products to instock list
                current_stock[search_key].append(product)

                cPrint(
                    f"[NEW] {product['name']} [{product['size']}] - [{product['price']}] - {product['link']}",
                    current_thread().name, "green")
                log.info(
                    f"[NEW] [{product['name']}] - {product['size']} - {product['price']} - {product['link']}")

                # Send discord notification
                discord_event(product, Status.NEW)

                # Update json file
                update_json(current_stock)

            except Exception as e:
                cPrint(e, current_thread().name, "red")
                log.error(e)

        # Check if instock item has been removed from the website
        elif check_out_of_stock(current_stock, products, search_key):
            pass

    instock = current_stock
    return instock


def check_out_of_stock(current_stock, list_items, search_key):
    for stock in current_stock[search_key]:

        # Check if instock items are no longer in the new list of items from the website
        if stock not in list_items[search_key]:

            # Remove the item from instock list
            current_stock[search_key].remove(stock)

            # Update json
            update_json(current_stock)

            cPrint(f"[SOLD] {stock['name']} [{stock['size']}] - {stock['link']}", current_thread().name, "red")
            log.info(f"[SOLD]: {stock['name']} - {stock['size']} - {stock['link']}")

            # Send discord notification
            discord_event(stock, Status.SOLD)

            return True


def discord_event(product_items, status):
    """
    https://github.com/lovvskillz/python-discord-webhook
    Sends a Discord notification to the specified webhook URL
    """

    name = product_items['name']
    link = product_items['link']
    image = product_items['image']
    size = product_items['size']
    price = product_items['price']

    # Determine if there are multiple sizes
    if isinstance(size, list):
        new_size = ' - '.join(map(str, size))
    else:
        new_size = size

    # Webhook constructor
    webhook = DiscordWebhook(url=WEBHOOK, rate_limit_retry=True, timeout=10)
    embed = DiscordEmbed(title=name, url=link, color='03b2f8')

    # Set author info
    embed.set_author(name='usedgear.arcteryx.com', url=BASE_URL,
                     icon_url='https://www.usedgear.arcteryx.com/assets/images/logo.png')

    # Set thumbnail image
    embed.set_thumbnail(url='https://www.usedgear.arcteryx.com/assets/images/logo.png')

    # Set item image
    embed.set_image(url=image)

    # Set item info
    embed.add_embed_field(name='Price', value=price)
    embed.add_embed_field(name='Sizes', value=f'{new_size}')
    embed.add_embed_field(name='Status', value=status)

    # Set footer info
    embed.set_timestamp()

    # Add embedded data
    webhook.add_embed(embed)

    try:
        # Send webhook
        response = webhook.execute()
        if response.status_code == 200:
            log.info(f"DISCORD SENT: {name} - {new_size} - {link}")

    except Exception as e:
        cPrint(e, current_thread().name, "red")
        log.warn(e)


def monitor(search_key: str, start: bool):
    global instock

    while True:
        try:
            # Setup dictionary for instock
            instock.setdefault(search_key, [])

            # Returns all new products
            retrieve_products = get_info(build_url(search_key.upper()), used_arc_headers)

            if retrieve_products != 1 and retrieve_products != None:
                new_products = create_product(retrieve_products, search_key.upper(), start)

                # Compares new stock with old stock and notify discord
                stock_comparitor(instock, new_products, start, search_key.upper())

                # Now we want to ping for any new or sold items
                start = False

            if retrieve_products is None:
                cPrint(f"Issue Getting Items From {BASE_URL}. Site May Not Be Supported", current_thread().name, "red")
                log.error(f"Issue Getting Items From {BASE_URL}. Site May Not Be Supported")
                quit()

            # Now we want to ping for any new or sold items
            start = False

            # Interval for polling
            time.sleep(DELAY)

        except Exception as e:
            cPrint(e, current_thread().name, "red")
            log.error(e)


if __name__ == '__main__':
    instock = {}
    threads = []
    thread_num = 0
    first_start = True

    # Create a thread for each keyword
    for keyword in KEYWORD:
        thread_num += 1
        t = Thread(name=f"thread{thread_num}", target=monitor, args=(keyword, first_start))
        threads.append(t)
        t.start()
