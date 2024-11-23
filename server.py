import flask
from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_flatpages.utils import pygmented_markdown
import sqlite3
import os
from PIL import Image

from utils import database, get_all_posts

app = Flask(__name__)
cfg_file = os.environ['SITE_CFG']
app.config.from_pyfile(cfg_file)

flatpages = FlatPages(app)

@app.route('/')
def home():
    post = flatpages.get_or_404('home')
    with database.Database() as db:
        return render_template("home.html", post=post, links=db.get_header_links(), recent_posts=get_all_posts(flatpages)[:10])

@app.route("/robots.txt")
def robots():
    return flask.send_from_directory("static", "robots.txt")

@app.route('/contact/')
def contact():
    post = flatpages.get_or_404('contacts')
    with database.Database() as db:
        return render_template("contacts.html", post=post, links=db.get_header_links(), recent_posts=get_all_posts(flatpages)[:10])

@app.route('/posts/')
def all_posts():
    with database.Database() as db:
        return render_template('all_posts.html', links=db.get_header_links(), all_posts=get_all_posts(flatpages))

#Configure URL routing for each blog post by the name of Markdown file
@app.route('/post/<name>')
def post(name):
    post_dir = app.config.get("POST_DIR")
    path = '{}/{}'.format(post_dir, name)
    post = flatpages.get_or_404(path)

    with database.Database() as db:
        return render_template('blog_post.html', post=post, links=db.get_header_links())

@app.route("/resume")
def serve_resume():
    imdirpath = os.path.join(".", "static", "files")
    cv_file = 'my_cv.pdf'
    if cv_file in os.listdir(imdirpath):
        return flask.send_from_directory(imdirpath, 'my_cv.pdf')
    else:
        flask.abort(404)


@app.route("/img/<filename>")
def serve_image(filename):
    imdirpath = os.path.join(".", "static", "images")
    if filename in os.listdir(imdirpath):
        try:
            w = int(flask.request.args['w'])
            h = int(flask.request.args['h'])
        except (KeyError, ValueError):
            return flask.send_from_directory(imdirpath, filename)

        img = Image.open(os.path.join(imdirpath, filename))
        img.thumbnail((w, h), Image.LANCZOS)
        io_ = io.BytesIO()
        img.save(io_, format='JPEG')
        return flask.Response(io_.getvalue(), mimetype='image/jpeg')
    else:
        flask.abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)
