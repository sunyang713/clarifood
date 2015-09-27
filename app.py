from flask import Flask, render_template, request
import predictor

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html', active='home')

@app.route("/about")
def about():
    return render_template('about.html', active='about')


@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
		return predict(request.form['image_url'])

@app.route("/predict/<path:url>")
def predict(url):
    return str(predictor.predict(url))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
