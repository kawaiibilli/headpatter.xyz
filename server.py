from flask import Flask
from flask_flatpages import FlatPages

app = Flask(__name__)
app.config.from_object(__name__)

flatpages = FlatPages(app)

DEBUG=True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'content'
POST_DIR = 'posts'

@app.route('/')
def hello():
    return 'Hello, World!'

#Configure URL routing for each blog post by the name of Markdown file
@app.route('/post/<name>')
def post(name):
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('blog_post.html', post=post)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)
