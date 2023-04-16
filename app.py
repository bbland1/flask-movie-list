import os
import requests
from dotenv import load_dotenv

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from forms import EditMovieForm, AddMovieForm, ReviewMovieForm
from models import Movies, db

# load .env file & variables
load_dotenv()
MOVIEDB_API = os.environ["THEMOVIEDB_API_KEY"]
MOVIEDB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIEDB_DETAILS_URL = "https://api.themoviedb.org/3/movie"
MOVIEDB_IMG_URL = "https://image.tmdb.org/t/p/w500/"

# make the flask app
app = Flask(__name__)
csrf = CSRFProtect(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DB_STRING"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]

# initialize the db with the app and add flask-bootstrap to the app
db.init_app(app)
Bootstrap(app)

# set to allow possible changes to the schema to be run with code
migrate = Migrate(app, db)

# use to create the db 
with app.app_context():
    db.create_all()


# set up the various routes
#! the only thing at this moment that could be good to change is where the rank of the movies is set
#! the rank is set at the home route right now and while sorting the movies there seems to be good users may like to change a rank
#! right now there is no where to change the rank unless the rating is changed to be higher or lower than what is already in the db

@app.route("/")
def home():
    # pull the movie data from the db
    movie_list = db.session.execute(db.select(Movies).order_by(Movies.rating.desc())).scalars().all()
    # using the ordered list set the ranks for each movie in the list & commit
    for i in range(len(movie_list)):
        movie_list[i].ranking = i + 1
    db.session.commit()
    # pass to the template
    return render_template("index.html", movies=movie_list)

@app.route("/add", methods=["GET", "POST"])
def add():
    # initiate the add form
    add_form = AddMovieForm()
    # checks for the post method?
    # when form actually submitted
    if add_form.validate_on_submit():
        # taking the name of the movie from the form
        movie = add_form.title.data
        search_params = {
            "api_key": MOVIEDB_API,
            "query": movie
        }
        # API call to "https://www.themoviedb.org"
        movie_search_response = requests.get(MOVIEDB_SEARCH_URL, params=search_params)
        # JSON the results
        movie_data = movie_search_response.json()["results"]
        # post method pass to template 
        return render_template("select.html", movies=movie_data)
    # initial passing of template to show for get method
    return render_template("add.html", form=add_form)

@app.route("/details", methods=["GET", "POST"])
def details():
    # initiate the review form
    review_form = ReviewMovieForm()
    # get the movie id from the search query address to pass for the API call
    movie_id = request.args.get("movie_id")
    search_params = {
        "api_key": MOVIEDB_API,
        "language": "en-US"
    }
    # API call to "https://www.themoviedb.org"
    movie_search_response = requests.get(f"{MOVIEDB_DETAILS_URL}/{movie_id}", params=search_params)
    # JSON the results
    movie_details = movie_search_response.json()
    if review_form.validate_on_submit():
        # adding the found movie to the database with the model 
        movie = Movies(
            title=movie_details["title"],
            # this will take the release date and split to only show the year from the call results that are in "2023-04-15"
            year=movie_details["release_date"][0:4],
            description=movie_details["overview"],
            rating=review_form.rating.data,
            review=review_form.review.data,
            img_url=f"{MOVIEDB_IMG_URL}{movie_details['poster_path']}")
        # add the movie
        db.session.add(movie)
        # commit to the database so it saves
        db.session.commit()
        # redirect it back to the home page from the post method
        return redirect(url_for("home"))
    # get method template pull and passing information
    return render_template("review.html", form=review_form, movie=movie_details)


@app.route("/update", methods=["GET", "POST"])
def update():
    # initiate the edit form
    update_form = EditMovieForm()
    # get the movie id from the search query address to pass for the API call
    movie_id = request.args.get("movie_id")
    if update_form.validate_on_submit():
        # post method working
        # getting the specific movie clicked on from the db to update information
        movie_to_update = db.session.execute(db.select(Movies).filter_by(id=movie_id)).scalar_one()
        # update rating if the rating information was passed
        if update_form.update_rating.data:
            movie_to_update.rating = update_form.update_rating.data
        # update the review if the the review information was passed
        if update_form.review.data:
            movie_to_update.review = update_form.review.data
        # commit the changes
        db.session.commit()
        # redirect it to the home page
        return redirect(url_for("home"))
    # getting the specific movie from the click and query to pass to the edit template
    movie = db.session.execute(db.select(Movies).filter_by(id=movie_id)).scalar_one()
    return render_template("edit.html", form=update_form, movie=movie)

@app.route("/delete")
def delete():
    # getting the specific movie from the click and query to delete
    movie_id = request.args.get("movie_id")
    # find that specific movie in the db
    movie_to_delete = db.session.execute(db.select(Movies).filter_by(id=movie_id)).scalar_one()
    # delete that movie 
    db.session.delete(movie_to_delete)
    # save the delete
    db.session.commit()
    # redirect tot he home page
    return redirect(url_for("home"))

# when the app's name is main run the app
if __name__ == "__main__":
    app.run()
