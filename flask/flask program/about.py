from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return '<h1>Vinmathi</h1> <p>Learn more be smart </p>'


@app.route('/about')
def about():
    return '<h3>Vinmathi Infotech dvk</h3>'


if __name__ =='__main__':
    app.run(debug = True)
    


