from flask import Flask, render_template
import predictor

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run()

@app.route("/predict/<path:url>")
def predict(url):
    return str(predictor.predict(url))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    # app.run(debug=True) # for testing
