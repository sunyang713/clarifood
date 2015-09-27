from flask import Flask, render_template, request
import predictor
import locator
import re


app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html', active='home')

@app.route("/about")
def about():
    return render_template('about.html', active='about')


@app.route('/find', methods=['GET', 'POST'])
def find():
    if request.method == 'POST':
        imageUrl = request.form['image_url']
        isValidUrl = re.match('^https?://(?:[a-z0-9\-]+\.)+[a-z]{2,6}(?:/[^/#?]+)+\.(?:jpg|gif|png)$', imageUrl)
        if isValidUrl:
            return locations(request.form['image_url'])
        else:
            return render_template('index.html', active='home', error=True)

@app.route("/predict/<path:url>")
def predict(url):
    return str(predictor.predict(url))

@app.route("/locations/<path:url>")
def locations(url):
    if (predictor.predict(url)):
       return str(locator.find(query="bubbletea"))
    else:
        return "Not bubble tea"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    # app.run(debug=True) # for testing
