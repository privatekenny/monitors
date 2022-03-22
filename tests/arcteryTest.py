from main.arcftery import *
from bs4 import BeautifulSoup

BASE_URL = 'https://www.usedgear.arcteryx.com'
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
config.load()
DELAY = get['Config']['Delay']
WEBHOOK = config.get['Config']['Webhook']

def test_stock_comparitor():
    discord_start = False
    keyword = 'BETA AR'

    # Global instock db
    instock = {
        "BETA AR": [
            {
                "name": "Beta AR Pant Men's",
                "size": "S",
                "price": "$251.00 - $279.00",
                "link": "https://www.usedgear.arcteryx.com/p/arcteryx-beta-ar-pant-mens-mens/12702?color=Black",
                "image": "https://res.cloudinary.com/yerdle/image/upload/w_550,h_550,c_fit/v1559840301/production/partners/4/inventoryItem/278554/yz83dkhd9arvokggdyhy.jpg"
            },
            {
                "name": "Beta AR Pant Men's",
                "size": "XXL",
                "price": "$251.00 - $279.00",
                "link": "https://www.usedgear.arcteryx.com/p/arcteryx-beta-ar-pant-mens-mens/12702?color=Black",
                "image": "https://res.cloudinary.com/yerdle/image/upload/w_550,h_550,c_fit/v1559840301/production/partners/4/inventoryItem/278554/yz83dkhd9arvokggdyhy.jpg"
            }
        ]}

    # Add product
    new_instock = {
        "BETA AR": [
            {
                "name": "Beta AR Pant Men's",
                "size": "S",
                "price": "$251.00 - $279.00",
                "link": "https://www.usedgear.arcteryx.com/p/arcteryx-beta-ar-pant-mens-mens/12702?color=Black",
                "image": "https://res.cloudinary.com/yerdle/image/upload/w_550,h_550,c_fit/v1559840301/production/partners/4/inventoryItem/278554/yz83dkhd9arvokggdyhy.jpg"
            },
            {
                "name": "Beta AR Pant Men's",
                "size": "XXL",
                "price": "$251.00 - $279.00",
                "link": "https://www.usedgear.arcteryx.com/p/arcteryx-beta-ar-pant-mens-mens/12702?color=Black",
                "image": "https://res.cloudinary.com/yerdle/image/upload/w_550,h_550,c_fit/v1559840301/production/partners/4/inventoryItem/278554/yz83dkhd9arvokggdyhy.jpg"
            },
            {
                "name": "Beta AR THIS IS NEW Men's",
                "size": "L",
                "price": "$251.00",
                "link": "https://www.usedgear.arcteryx.com/p/arcteryx-beta-ar-pant-mens-mens/12702?color=NEW",
                "image": "https://res.cloudinary.com/yerdle/image/upload/w_550,h_550,c_fit/v1559840301/production/partners/4/inventoryItem/278554/sdsd.jpg"
            }
        ]
    }
    add_product = {
        "BETA AR": [
            {
                "name": "Beta AR THIS IS NEW Men's",
                "size": "L",
                "price": "$251.00",
                "link": "https://www.usedgear.arcteryx.com/p/arcteryx-beta-ar-pant-mens-mens/12702?color=NEW",
                "image": "https://res.cloudinary.com/yerdle/image/upload/w_550,h_550,c_fit/v1559840301/production/partners/4/inventoryItem/278554/sdsd.jpg"
            }
        ]
    }

    # Remove product
    new_instock_remove = {
        "BETA AR": [
            {
                "name": "Beta AR Pant Men's",
                "size": "XXL",
                "price": "$251.00 - $279.00",
                "link": "https://www.usedgear.arcteryx.com/p/arcteryx-beta-ar-pant-mens-mens/12702?color=Black",
                "image": "https://res.cloudinary.com/yerdle/image/upload/w_550,h_550,c_fit/v1559840301/production/partners/4/inventoryItem/278554/yz83dkhd9arvokggdyhy.jpg"
            },
            {
                "name": "Beta AR THIS IS NEW Men's",
                "size": "L",
                "price": "$251.00",
                "link": "https://www.usedgear.arcteryx.com/p/arcteryx-beta-ar-pant-mens-mens/12702?color=NEW",
                "image": "https://res.cloudinary.com/yerdle/image/upload/w_550,h_550,c_fit/v1559840301/production/partners/4/inventoryItem/278554/sdsd.jpg"
            }
        ]
    }
    remove_product = {
        "BETA AR": [
            {
                "name": "Beta AR THIS IS NEW Men's",
                "size": "L",
                "price": "$251.00",
                "link": "https://www.usedgear.arcteryx.com/p/arcteryx-beta-ar-pant-mens-mens/12702?color=NEW",
                "image": "https://res.cloudinary.com/yerdle/image/upload/w_550,h_550,c_fit/v1559840301/production/partners/4/inventoryItem/278554/sdsd.jpg"
            },
            {
                "name": "Beta AR Pant Men's",
                "size": "XXL",
                "price": "$251.00 - $279.00",
                "link": "https://www.usedgear.arcteryx.com/p/arcteryx-beta-ar-pant-mens-mens/12702?color=Black",
                "image": "https://res.cloudinary.com/yerdle/image/upload/w_550,h_550,c_fit/v1559840301/production/partners/4/inventoryItem/278554/yz83dkhd9arvokggdyhy.jpg"
            }
        ]
    }

    assert stock_comparitor(instock, add_product, discord_start, keyword)[keyword] == new_instock[keyword]

    assert stock_comparitor(instock, remove_product, discord_start, keyword)[keyword] == new_instock_remove[keyword]


def test_check_out_of_stock():
    keyword = 'BETA AR'
    instock = {
        "BETA AR": [
            {
                "name": "Beta AR Pant Men's",
                "size": "L",
                "price": "$251.00 - $279.00",
                "link": "https://www.usedgear.arcteryx.com/p/arcteryx-beta-ar-pant-mens-mens/12702?color=Black",
                "image": "https://res.cloudinary.com/yerdle/image/upload/w_550,h_550,c_fit/v1559840301/production/partners/4/inventoryItem/278554/yz83dkhd9arvokggdyhy.jpg"
            },
            {
                "name": "Beta AR THIS SHOULD BE HERE Men's",
                "size": [
                    "S"
                ],
                "price": "$251.00",
                "link": "https://www.usedgear.arcteryx.com/p/arcteryx-beta-ar-pant-mens-mens/12702?color=Black",
                "image": "https://res.cloudinary.com/yerdle/image/upload/w_550,h_550,c_fit/v1559840301/production/partners/4/inventoryItem/278554/yz83dkhd9arvokggdyhy.jpg"
            }
        ]
    }
    add_product = {
        "BETA AR": [
            {
                "name": "Beta AR Jacket Women",
                "size": "M",
                "price": "$252.00",
                "link": "https://www.usedgear.arcteryx.com/p/arcteryx-beta-ar-pant-mens-mens/12702?color=NEW",
                "image": "https://res.cloudinary.com/yerdle/image/upload/w_550,h_550,c_fit/v1559840301/production/partners/4/inventoryItem/278554/sdsd.jpg"
            },
            {
                "name": "Beta AR TEST SWAG",
                "size": [
                    "S"
                ],
                "price": "$253.00",
                "link": "https://www.usedgear.arcteryx.com/p/arcteryx-beta-pant-mens-mens/12702?color=NEW",
                "image": "https://res.cloudinary.com/yerdle/image/upload/50,h_550,c_fit/v1559840301/production/partners/4/inventoryItem/278554/sdsd.jpg"
            }
        ]
    }

    check_out_of_stock(instock, add_product, keyword)

    assert check_out_of_stock(instock, add_product, keyword) == True


def test_create_product():
    keywords = "BETA AR"
    build_url(keywords.upper()), used_arc_headers, keywords.upper()
    request = BeautifulSoup("""
    <div class="List">
    <ol>
        <li aria-expanded="true" aria-label="shop item Beta AR Pant Men's" class="TileItem" tabindex="-1"><a
                href="/p/arcteryx-beta-ar-pant-mens-mens/12702?color=Black&amp;aqi=9cf5f8032d181f46973e3d4eac30ef55"
                tabindex="0">
            <div class="img-wrap"><img alt=""
                                       src="https://res.cloudinary.com/yerdle/image/upload/w_550,h_550,c_fit/v1559840301/production/partners/4/inventoryItem/278554/yz83dkhd9arvokggdyhy.jpg"/>
            </div>
            <footer><span class="sizes"><ol><li>S</li><li>XL</li><li>XXL</li></ol></span><h4><span class="title"
                                                                                      title="Beta AR Pant Men's">Beta AR Pant Men's</span>
            </h4>
                <div class="price">
                    <div><span aria-label="price $279.00">$279.00</span><span>used</span></div>
                    <del aria-label="compare to original price $399.00" class="originally" role="note">
                        <span>$399.00</span><span></span></del>
                </div>
                <div class="rating" data-bv-product-id="12702" data-bv-show="inline_rating"></div>
            </footer>
        </a></li>
        <li aria-expanded="true" aria-label="shop item Beta AR Pant Men's" class="TileItem" tabindex="-1"><a
                href="/p/arcteryx-beta-ar-pant-mens-mens/12702?color=Black&amp;aqi=9cf5f8032d181f46973e3d4eac30ef55"
                tabindex="0">
            <div class="img-wrap"><img alt=""
                                       src="https://res.cloudinary.com/yerdle/image/upload/w_550,h_550,c_fit/v1559840301/production/partners/4/inventoryItem/278554/yz83dkhd9arvokggdyhy.jpg"/>
            </div>
            <footer><span class="sizes"><ol><li>M</li></ol></span><h4><span class="title"
                                                                                                   title="Beta AR Jacket Men's">Beta AR Jacket Men's</span>
            </h4>
                <div class="price">
                    <div><span aria-label="price $279.00">$279.00</span><span>used</span></div>
                    <del aria-label="compare to original price $399.00" class="originally" role="note">
                        <span>$399.00</span><span></span></del>
                </div>
                <div class="rating" data-bv-product-id="12702" data-bv-show="inline_rating"></div>
            </footer>
        </a></li>
    </ol>
</div>
    """, "lxml")

    expected_response = {
        "BETA AR": [
            {
                "name": "Beta AR Pant Men's",
                "size": "S",
                "price": "$279.00",
                "link": "https://www.usedgear.arcteryx.com/p/arcteryx-beta-ar-pant-mens-mens/12702?color=Black",
                "image": "https://res.cloudinary.com/yerdle/image/upload/w_550,h_550,c_fit/v1559840301/production/partners/4/inventoryItem/278554/yz83dkhd9arvokggdyhy.jpg"
            },
            {
                "name": "Beta AR Pant Men's",
                "size": "XL",
                "price": "$279.00",
                "link": "https://www.usedgear.arcteryx.com/p/arcteryx-beta-ar-pant-mens-mens/12702?color=Black",
                "image": "https://res.cloudinary.com/yerdle/image/upload/w_550,h_550,c_fit/v1559840301/production/partners/4/inventoryItem/278554/yz83dkhd9arvokggdyhy.jpg"
            },
            {
                "name": "Beta AR Pant Men's",
                "size": "XXL",
                "price": "$279.00",
                "link": "https://www.usedgear.arcteryx.com/p/arcteryx-beta-ar-pant-mens-mens/12702?color=Black",
                "image": "https://res.cloudinary.com/yerdle/image/upload/w_550,h_550,c_fit/v1559840301/production/partners/4/inventoryItem/278554/yz83dkhd9arvokggdyhy.jpg"
            },
            {
                "name": "Beta AR Jacket Men's",
                "size": "M",
                "price": "$279.00",
                "link": "https://www.usedgear.arcteryx.com/p/arcteryx-beta-ar-pant-mens-mens/12702?color=Black",
                "image": "https://res.cloudinary.com/yerdle/image/upload/w_550,h_550,c_fit/v1559840301/production/partners/4/inventoryItem/278554/yz83dkhd9arvokggdyhy.jpg"
            }
        ]
    }

    assert create_product(request, keywords) == expected_response
