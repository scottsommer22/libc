import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Retrieve and adjust the DATABASE_URL
raw_db_url = os.getenv('DATABASE_URL')
if raw_db_url and raw_db_url.startswith("postgres://"):
    raw_db_url = raw_db_url.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = raw_db_url

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the Roto table
class Roto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    r = db.Column(db.Integer, nullable=False)
    hr = db.Column(db.Integer, nullable=False)
    rbi = db.Column(db.Integer, nullable=False)
    sb = db.Column(db.Integer, nullable=False)
    bb = db.Column(db.Integer, nullable=False)
    avg = db.Column(db.Float, nullable=False)
    ops = db.Column(db.Float, nullable=False)
    w = db.Column(db.Integer, nullable=False)
    k = db.Column(db.Integer, nullable=False)
    era = db.Column(db.Float, nullable=False)
    whip = db.Column(db.Float, nullable=False)
    qs = db.Column(db.Integer, nullable=False)
    sv_h = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    bat = db.Column(db.Integer, nullable=False)
    pitch = db.Column(db.Integer, nullable=False)
    rank = db.Column(db.Integer, nullable=False)
    b_rank = db.Column(db.Integer, nullable=False)
    p_rank = db.Column(db.Integer, nullable=False)

@app.route('/')
def home():
    return "LIBC App connected to Heroku Postgres!"

@app.route('/roto')
def roto_view():
    data = Roto.query.all()
    return render_template('roto.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)