If running the app by "python run.py" command line, an error like the follow appears:

    'SELECT * FROM user WHERE id = ?', (user_id,)
    sqlite3.OperationalError: no such table: user

probably the database is not initialized. To initialize it:

export FLASK_APP=repodeploy
export FLASK_ENV=deployment
flask init-db
export FLASK_APP=
export FLASK_ENV=