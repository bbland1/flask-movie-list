from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, DecimalField, StringField, IntegerField
from wtforms.validators import InputRequired, Optional, NumberRange

# all the input areas to add, edit or review a movie
class EditMovieForm(FlaskForm):
    update_rating = DecimalField("Update Rating (0-10)", places=2, validators=[Optional(), NumberRange(min=0, max=10)])
    review = TextAreaField("Review", validators=[Optional()])
    submit = SubmitField("Update")

class AddMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[InputRequired("A movie has to have a title.")], default="")
    submit = SubmitField("Add Movie")

class ReviewMovieForm(FlaskForm):
    rating = DecimalField("How do you rate the movie?", validators=[InputRequired(), NumberRange(min=0, max=10, message="Please make sure your rating is between 0-10")])
    review = TextAreaField("Review the movie", validators=[InputRequired()])
    submit = SubmitField("Add Movie")