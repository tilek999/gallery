from flask import Flask, render_template, request


app=Flask(__name__)

@app.route("/")
def gallery():
    gal = open("gallery.txt", "r", encoding="utf-8")
    gal.list = [row for row in gal]
    gal.close
    return render_template("gallery.html")

@app.route("/add-picture", methods=["POST"])
def add_picture():
    picture = request.form.get("picture")
    gal = open('gallery.txt', 'a+', encoding="utf-8")
    gal.write(picture)
    gal.close()
    return render_template("p.html")

@app.route("/ad")
def add():
    return render_template("ad.html")    