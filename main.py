import os
from flask import Flask, redirect, url_for, request
from flask_mail import Mail
import logging
import threading
# CONFIG



"""
MAIL_SERVER : 127.0.0.1
MAIL_PORT : 25
MAIL_USE_TLS : False
MAIL_USE_SSL : False
MAIL_DEBUG : app.debug
MAIL_USERNAME : None
MAIL_PASSWORD : None
MAIL_DEFAULT_SENDER : None
MAIL_MAX_EMAILS : None
MAIL_SUPPRESS_SEND : app.testing
MAIL_ASCII_ATTACHMENTS : False
mail = Mail(app)
"""


app = Flask(__name__)

@app.route('/')
def redirect_to_link():
    return redirect('https://www.youtube.com/watch?v=fC7oUOUEEi4')

@app.route('/print')
def printMsg():
    app.logger.warning('testing warning log')
    app.logger.error('testing error log')
    app.logger.info("Pinged from "+request.remote_addr)
    return "Check your console"
	# app.logger.info("Pinged from "+request.remote_addr)
    # print("[WARNING] Pinged from "+request.remote_addr)

def start_website(m_host, m_port):
    port = int(os.environ.get('PORT', m_port))
    app.run(host=m_host, port=port)
x = threading.Thread(target=start_website, args=('192.168.0.43', 8080), daemon=True)

def exit():
	while True:
		cmd = input()
		if cmd == "":
			break

if __name__ == "__main__":
    x.start()
    exit()