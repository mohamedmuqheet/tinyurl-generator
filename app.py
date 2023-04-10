from flask import Flask, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy
import string
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'mysecretkey'

db = SQLAlchemy(app)

class Urls(db.Model):
    id_ = db.Column("id_", db.Integer, primary_key=True)
    long = db.Column("long", db.String())
    short = db.Column("short", db.String(10))

    def __init__(self, long, short):
        self.long = long
        self.short = short

def shorten_url():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters = random.choices(letters, k=3)
        rand_letters = "".join(rand_letters)
        short_url = Urls.query.filter_by(short=rand_letters).first()
        if not short_url:
            return rand_letters

def validate_url(url):
    # This is a simple function to validate a URL
    if url.startswith('http://') or url.startswith('https://'):
        return True
    else:
        return False

def create_short_url(long_url):
    found_url = Urls.query.filter_by(long=long_url).first()

    if found_url:
        return found_url.short
    else:
        short_url = shorten_url()
        new_url = Urls(long_url, short_url)
        db.session.add(new_url)
        db.session.commit()
        return short_url

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.is_json:
            long_url = request.json.get('long_url')
            if not long_url:
                return jsonify({'error': 'bad request'}), 400
        else:
            long_url = request.form.get('long_url')
            if not long_url:
                return jsonify({'error': 'bad request'}), 400

        if not validate_url(long_url):
            return jsonify({'error': 'invalid URL'}), 400

        short_url = create_short_url(long_url)
        short_url_display = request.host_url + short_url
        return jsonify({'short_url': short_url_display}), 201

    return '''
        <form method="post">
            <label>Long URL:</label>
            <input type="text" name="long_url">
            <input type="submit" value="Shorten">
        </form>
    '''

@app.route('/<short_url>', methods=['GET'])
def retrieve_url(short_url):
    long_url = Urls.query.filter_by(short=short_url).first()
    if long_url:
        return redirect(long_url.long)
    else:
        return jsonify({'error': 'not found'}), 404

@app.route('/urls', methods=['GET'])
def list_urls():
    urls = Urls.query.all()
    response = []
    for url in urls:
        response.append({'short_url': request.host_url + url.short, 'long_url': url.long})
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)

