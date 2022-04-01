import os
from datetime import datetime
from termcolor import colored
import logging.handlers as handlers
import colorama
import yaml
import logging
from termcolor import cprint
from etc.handlers import GZipRotator
from pyfiglet import figlet_format

colorama.init()

get = None

PARENT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)))

CONFIG_PATH_FORMAT = os.path.join(PARENT_DIR, r'etc/config%s.yml')
LOG_PATH = os.path.join(PARENT_DIR, r'logs/info.log')
LOG_PATH2 = os.path.join(PARENT_DIR, r'logs/requests.log')
log = logging.getLogger('1')
log_request = logging.getLogger('2')


def load():
    global get

    # Get The Active Profile
    active_profile = read(load_config(''))['env']

    # YAML Contents
    get = read(load_config(active_profile))

    # Set Logging
    log = logging.getLogger('1')
    log.setLevel(logging.DEBUG)
    handler = logging.handlers.TimedRotatingFileHandler(LOG_PATH, when='midnight', backupCount=30)
    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: [%(threadName)s] -> %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    handler.setFormatter(formatter)
    handler.rotator = GZipRotator()
    log.addHandler(handler)

    # Set Logging For Requests
    log_request = logging.getLogger('2')
    log_request.setLevel(logging.INFO)
    handler = logging.handlers.TimedRotatingFileHandler(LOG_PATH2, when='midnight', backupCount=30)
    formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: [%(threadName)s] -> %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    handler.setFormatter(formatter)
    handler.rotator = GZipRotator()
    log_request.addHandler(handler)

    # Log Active Profile
    log.info(f"Loaded Profile -> {active_profile}")
    log.info(f"Loaded Config  -> {get['config']}")
    cPrint(f"Loaded Profile -> {active_profile}", thread=None, color='cyan')
    cPrint(f"Loaded Config  -> {get['config']}", thread=None, color='cyan')

    # Change requests level
    logging.getLogger("urllib3").setLevel(logging.WARNING)


def read(path):
    try:
        with open(r'' + path) as file:
            return yaml.safe_load(file)
    except Exception as e:
        log.error(e)


def load_config(active_profile):
    if active_profile == '':
        return CONFIG_PATH_FORMAT % ''
    else:
        return CONFIG_PATH_FORMAT % ('-' + active_profile)


def date_time():
    """
    :return: Current date (MM/DD/YYYY) and 24hr time (HH/MM/SS) PST
    """
    return datetime.now().strftime('%m/%d/%Y %I:%M:%S %p')


# colored printing
def cPrint(value, thread=None, color=None):
    if thread:
        string = f"{date_time()} :: [{thread}] -> {value}"
        text = colored(string, color)
        print(text)
    else:
        string = f"{date_time()} :: {value}"
        text = colored(string, color)
        print(text)


def art():
    cprint(figlet_format('MONITOR', font='lean'), 'yellow', attrs=['bold'])
