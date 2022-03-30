import json
import os
import sys
from flask import Flask, render_template, redirect

PARENT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)))

# ROOT PATH
sys.path.append(PARENT_DIR)
from main.arcteryx import *

app = Flask(__name__)


@app.route('/')
def dashboard():
    newItems = []
    stores = []
    startTime = get_status('startTime')
    try:
        with open('./main/instock.json', 'r') as f:
            data = json.load(f)
            for key, value in data.items():
                for items in value:
                    newItems.append(items)
        url = config.get['config']['url']
        stores.append(url)
        print(stores)
    except ValueError:
        print("No Items")
        pass
    return render_template('home.html', newItems=newItems, stores=stores, status=get_status('monitor'), startTime=startTime)


@app.route('/logs')
def logs():
    f = open('./logs/info.log', 'r')
    t = f.readlines()
    logs = ""
    for lines in t:
        logs += ''.join(f"{lines}")

    return render_template('logs.html', logs=logs)


@app.route('/settings')
def settings():
    return render_template('settings.html')


@app.route('/stop')
def stop():
    change_status('monitor', 'Stopped')
    return redirect('/')


@app.route('/start')
def start():
    change_status('monitor', 'Active')
    change_status('startTime', date_time())
    cPrint("STARTING MONITOR", thread=None, color="green")
    main()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
