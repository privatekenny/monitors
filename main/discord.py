from discord_webhook import DiscordWebhook, DiscordEmbed
import os, sys

PARENT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)))

# ROOT PATH
sys.path.append(PARENT_DIR)
from etc.config import *


def discord_event(product_items, status, channel_webhook, base_url):
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
    webhook = DiscordWebhook(url=channel_webhook, rate_limit_retry=True, timeout=10)
    embed = DiscordEmbed(title=name, url=link, color='03b2f8')

    # Set author info
    embed.set_author(name='usedgear.arcteryx.com', url=base_url,
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
        cPrint(value=e, color="red")
        log.warn(e)
