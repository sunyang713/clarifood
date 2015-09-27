from flask import Flask, render_template
import predictor
import locator

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

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
