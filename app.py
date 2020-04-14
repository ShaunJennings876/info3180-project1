from flask import Flask, render_template, redirect, url_for, flash
from forms import ProfileForm
from flask_sqlalchemy import SQLAlchemy
import datetime
import os



app = Flask(__name__)
app.config['SECRET_KEY'] = '0cd928499ef25040589c8ac79fb3def3'
app.config['SQLALCHEMY_DATABASE_URI'] ="postgresql:// yecsapnzlttgcb:8860d3512549e3ebba04aa68ede74496e30041ff458ea1d4 6d7c4ed7f5402af0@ec2-54-221-244-196.compute-1.amazonaws.com:543 2/d9d6gbbcjoc71g"

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(20), nullable = False)
    lastname = db.Column(db.String(20), nullable = False)
    gender = db.Column(db.String(6), default = "not specified")
    email = db.Column(db.String(120), unique = True, nullable = False)
    location = db.Column(db.String(30))
    biography = db.Column(db.String(200))
    profile_picture = db.Column(db.String(20),default = 'default.jpg')
    created_on = db.Column(db.DateTime, nullable = False, default = datetime.datetime.utcnow)

    def __repr__(self):
        return f"User({self.firstname},{self.lastname},{self.email})"


@app.route("/")
@app.route("/profile", methods = ['GET','POST'])
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.firstname.data}.','success')
        user = User(firstname = form.firstname.data, lastname = form.lastname.data, gender = form.gender.data,
                    email = form.email.data, location = form.location.data, biography = form.biography.data,
                    profile_picture = form.profilepicture.data.filename)
        file = form.profilepicture.data
        file.save(os.path.join(app.root_path, 'static', file.filename))
        #file.save(file.filename)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('profiles'))
    return render_template("profile.html", title = 'Add Profile', form = form)

@app.route("/profiles")
def profiles():
    users = db.session.query(User).all()
    return render_template("profiles.html", title = "Profiles", users = users)

@app.route("/profile/<userid>")
def individual_profile(userid):
    user = db.session.query(User).filter_by(id = int(userid)).all()[0]
    return render_template("individual_profile.html", user = user)

if __name__ == "__main__":
    app.run(debug = True)
