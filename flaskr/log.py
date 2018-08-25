from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, send_file
)
from flaskr.auth import login_required
import logging
import logging.handlers
from config import DT

# create logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
handler = logging.handlers.RotatingFileHandler(filename='logging.log',
                                          maxBytes=1024*20,
                                          backupCount=1)
handler.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)-8s - %(message)s',
                              datefmt=DT)

# add formatter to handler
handler.setFormatter(formatter)

# add handler to logger
logger.addHandler(handler)


bp = Blueprint('log', __name__, url_prefix='/log')

@bp.route('/')
@login_required
def index():
    return render_template('log/log.html')

@bp.route('/showlog')
@login_required
def showlog():
    return send_file('../logging.log')

@bp.route('/getlog')
@login_required
def getlog():
    return send_file('../logging.log', attachment_filename='logging.log', as_attachment=True)