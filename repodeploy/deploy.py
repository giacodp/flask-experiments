import subprocess
from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from repodeploy.auth import login_required

bp = Blueprint('deploy', __name__)

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
            # TODO: see how to implement LDAP authentication, e.g. https://github.com/admiralobvious/flask-simpleldap, https://code.tutsplus.com/tutorials/flask-authentication-with-ldap--cms-23101
            subprocess.call(['bash', 'repodeploy/deploy.sh', bbrepo, ghrepo, branch])
            return redirect(url_for('log.index'))

    return render_template('deploy/index.html')
