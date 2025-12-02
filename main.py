from flask import Flask, render_template
import feedparser

app = Flask(__name__)

@app.route('/')
def index():
    feed = feedparser.parse('https://static.cricinfo.com/rss/livescores.xml')
    return render_template('index.html', entries=feed.entries)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
