from flask import Flask,render_template
from flask import request
test=Flask(__name__)

@test.route("/")
def dummy():
    return render_template("homepage.html")

@test.route("/about")
def about_func():
    return render_template("about.html")

@test.route("/login")
def blog_func():
    return render_template("login.html")

@test.route("/profile")
def login_func():
    return render_template("profile.html", b="jaipur")

@test.route("/main")
def test_args():
    return  render_template("main.html") 

@test.route("/test_form", methods=["POST", "GET"])
def test_form():
    return request.form

@test.route("/a")
def profile():
    return render_template("profile.html", b="jaipur")   




# local function...
# a=2
# b=3
# print(locals())
