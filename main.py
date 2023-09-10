from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField, validators, BooleanField
from wtforms.validators import DataRequired, length, Email
from flask_bootstrap import Bootstrap4
from flask import Flask


app = Flask(__name__)
app.secret_key = ""
bootstrap = Bootstrap4(app)

class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), length(min=8)])
    accept_rules = BooleanField('I accept the site rules', [validators.InputRequired()])
    submit = SubmitField(label="Log In")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if request.method == 'POST' and login_form.validate_on_submit():
        if login_form.email == "admin@email.com" and login_form.password == "12345678":
            return render_template('denied.html')
        else:
            return render_template('success.html')
    return render_template('login.html', form=login_form)



if __name__ == '__main__':
    app.run(debug=True)
