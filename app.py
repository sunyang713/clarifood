from flask import Flask, render_template, request, redirect, url_for
import identifier
import locator
import re

VALID_URL_REGEX = '^https?://(?:[a-z0-9\-]+\.)+[a-z]{2,6}(?:/[^/#?]+)+\.(?:jpg|gif|png)$'
HARD = [{'website': u'http://www.vivibubbletea.com/', 'place_id': u'ChIJj7EjVSZawokRK8iYc3EFGew', 'name': u'Vivi Bubble Tea', 'address': u'49 Bayard St, New York, NY 10013, United States'}, {'website': u'http://www.coco-tea.com/', 'place_id': u'ChIJV_XwyaBZwokRy21Op4TYKCE', 'name': u'CoCo Tea', 'address': u'38 Lexington Ave, New York, NY 10010, United States'}, {'website': None, 'place_id': u'ChIJT2OTGydawokRIWblLTBVHDk', 'name': u"Sun's Organic Tea Shop", 'address': u'79 Bayard St, New York, NY 10013, United States'}, {'website': u'http://www.saintsalpusa.com/', 'place_id': u'ChIJxaxn9ptZwokRm8fifHPhju8', 'name': u"Saint's Alp Teahouse", 'address': u'39 3rd Ave, New York, NY 10003, United States'}, {'website': None, 'place_id': u'ChIJNeUW4VFawokRgS_6WC1zjWY', 'name': u"Hanco's Bubble Tea & Vietnamese Sandwich", 'address': u'147 Montague St, Brooklyn, NY 11201, United States'}]

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html', active='home', error=None)

@app.route("/about")
def about():
    return render_template('about.html', active='about')

@app.route('/find', methods=['GET', 'POST'])
def find():
    error = None
    if request.method == 'POST':
        imageUrl = request.form['image_url']
        if re.match(VALID_URL_REGEX, imageUrl):
            return identify(imageUrl)
        else:
            return render_template('index.html', error='Please enter a valid image URL.')

@app.route("/identify/<path:url>")
def identify(url):
    result = identifier.identify(url)
    # if True:
    if result:
        # return render_template('results.html', url=url, result=result['title'], locations=locator.find(query=result['alias']))
        return render_template('results.html', url=url, result=result['title'], locations=HARD)
    else:
        return redirect(url_for('unrecognized'))

@app.route("/unrecognized")
def unrecognized():
    return 'Unrecognized :('
    # return render_template('unrecognized.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    # app.run(debug=True, use_reloader=False)
    # app.run()
