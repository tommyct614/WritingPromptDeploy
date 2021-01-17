from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import csv
import random

app = Flask(__name__, static_url_path="/static")
Bootstrap(app)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///writing-prompts.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Prompts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prompt = db.Column(db.Text, unique=True, nullable=False)
    author = db.Column(db.Text, nullable=False)
    link = db.Column(db.Text, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Prompt {self.id}>'

# db.create_all()

# with open("Writing_prompt.csv", encoding="utf-8") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",")
#     for row in csv_reader:
#         new_prompt = Prompts(prompt=row[0], author=row[1], link=row[2])
#         db.session.add(new_prompt)
#         db.session.commit()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/prompt", methods=["GET","POST"])
def prompt():
    index = random.randint(0,200)
    entry = Prompts.query.get(index)
    reply_quote = entry.prompt
    reply_author = entry.author
    reply_link = entry.link
    return render_template("prompt.html", quote=reply_quote, author=reply_author, link=reply_link)

if __name__ == "__main__":
    app.run(debug=True)
