import os
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required

bp = Blueprint('deploy', __name__, url_prefix='/deploy')

@bp.route('/', methods=('GET', 'POST'))
@login_required
def index():
    if request.method == 'POST':
        bbrepo = request.form['bitbucket-repository']
        ghrepo = request.form['github-repository']
        branch = request.form['bitbucket-branch']
        error = None

        if not bbrepo:
            error = 'Bitbucket repository is required.'
        if not ghrepo:
            error = 'GitHub repository is required.'
        if not branch:
            branch = 'master'

        if error is not None:
            flash(error)
        else:
            # TODO: verificare path di deploy.sh
            # TODO: vedere come far passare variabili python come parametri UNIX
            # TODO: cambiare pulsante DONE
            # TODO: vedere come leggere log di deploy.sh in html
            os.system('./deploy.sh bbrepo ghrepo branch')
            return redirect(url_for('blog.index'))

    return render_template('deploy/index.html')
