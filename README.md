# Python (Flask) Web App with SQLite Database

![License](https://img.shields.io/github/license/bbland1/flask-sqlite-movie-list?style=plastic)
![Top Language](https://img.shields.io/github/languages/top/bbland1/flask-sqlite-movie-list?style=plastic)
![Contributors](https://img.shields.io/github/contributors-anon/bbland1/flask-sqlite-movie-list?style=plastic)

A Python web app that uses the Flask framework and SQLite database for data persistence to store a users top 10 movies based on the entered rating out of 10. Utilized SQLAlchemy/SQL and Flask to practice decorators, routes, and database connectivity. Although not deployed, the project served as a valuable practice exercise for understanding web development concepts and building robust backend functionality. Strengthened skills in web development frameworks, database connectivity, and data persistence using Flask and SQLAlchemy.

#### Edit a moive's rating or review
https://user-images.githubusercontent.com/104288486/232853071-743c8410-80ae-4e53-ad81-bfe850db7fad.mov




#### Delete a movie from database
https://user-images.githubusercontent.com/104288486/232853656-d32b47ad-f72c-49ba-af00-998081f2ae99.mov




#### Add movie to database
https://user-images.githubusercontent.com/104288486/232859149-4f54e0aa-d034-4394-bdaf-30881de1c10d.mov


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
