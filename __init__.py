from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html', active='home')

@app.route("/about")
def about():
    return render_template('about.html', active='about')

@app.route('/test/<int:number>')
def test(number):
    # show the user profile for that user
    return 'Your number: %d' % number



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
