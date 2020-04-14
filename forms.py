from wtforms.validators import DataRequired, Length, Email
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, FileField, TextAreaField

class ProfileForm(FlaskForm):
    firstname = StringField("First Name", validators = [DataRequired(),Length(min = 2, max = 20)])
    lastname = StringField("Last Name", validators = [DataRequired(),Length(min = 2, max = 20)])
    email = StringField("Email", validators = [DataRequired(),Email(message = "Email invalid")])
    location = StringField("Location", validators = [DataRequired(),Length(min = 2)])
    gender = SelectField("Gender",validators = [DataRequired()],choices = [("Male", "Male"),("Female", "Female")])
    biography = TextAreaField("Biography",validators = [Length(max = 200)])
    profilepicture = FileField("Profile Picture")
    submit = SubmitField("Add Profile")
