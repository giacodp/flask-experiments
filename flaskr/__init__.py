import os

from flask import Flask#, send_file


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)

    from . import prova
    @app.route('/prova')
    def prova_1():
        return prova.prov()

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    from . import deploy
    app.register_blueprint(deploy.bp)

    #import logging
    #logging.basicConfig(filename='logging.log', level=logging.INFO)
    #@app.route('/log-temp')
    #def show_log():
    #    with open("logging.log", "r") as logfile:
    #        return send_file('../logging.log', attachment_filename='logging.log', as_attachment=False)
    #    return render_template('log.html')

    from . import log
    app.register_blueprint(log.bp)

    return app