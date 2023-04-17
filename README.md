# Python (Flask) Web App with SQLite Database

This is a Python web app that uses the Flask framework that uses a SQLite DB to persist the data. This isn't a deployed app, but it is good use for practice of SQLAlchemy/SQL and the Flask framework. It allowed me and would allowed others to get an understating on decorators, routes and connecting to a database.

## Requirements

Installing from the [requirements.txt](./requirements.txt) handles most of the requirements, but you will also need to make sure to have a [The Movie DB](https://www.themoviedb.org) developer account to access an API key to complete the searches.

## Built With
* [Flask](https://flask.palletsprojects.com/en/2.2.x/)
* [SQLAlchemy](https://www.sqlalchemy.org)
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/)
* [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
* [Flask-Bootstrap](https://pythonhosted.org/Flask-Bootstrap/)
* [python-dotenv](https://pypi.org/project/python-dotenv/)
* [flask-wtf](https://flask-wtf.readthedocs.io/en/1.0.x/)


### Local Development

1. (Optional) [Setup a virtual environment](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments) and activate it to install requirements into the virtual environment to run instead of your computers global environment.

2. Install the project requirements.
```shell 
pip install -r requirements.txt
```

3. Create a `.env` using the `.env.sample` file as a guide. Change `THEMOVIEDB_API_KEY`, `DB_STRING`, and `SECRET_KEY` to the proper information of your instance of the SQLite database.

- `SECRET_KEY` can be set using this command
```shell  
python -c 'import secrets; print(secrets.token_hex())'
```

4. Run the migrations
```shell 
flask db upgrade
```

5. Run the local server: (or use VS Code "Run" button and select "Run server")
```shell 
flask run
```

### License
See the [LICENSE](./LICENSE) file for license rights and limitations (MIT).