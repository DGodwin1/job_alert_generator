from flask import Flask, render_template, request

from .jobAlertGenerator import(
    VBT_get_brand,
    VBT_get_title,
    VBT_get_location,
    make_soup,
    generate_job_alert_anchor,
    make_soup,
    create_snazzy_HTML_block
)

app = Flask(__name__)

@app.route('/')
def homepage():
    # here we will ask the user to enter the links they want to parse.
    return render_template('main.html')

@app.route('/links', methods=['POST', 'GET'])
def links():
    if request.method == 'POST':
        result = request.form
        links = result.get("urls").split()

        # Get the information out of each link
        # and make some nice html.
        anchors = []
        for link in links:
            if not link.startswith("https://www.voguebusiness.com/talent/jobs"):
                return render_template('error.html', links=", ".join(links), link=link)
            soup = make_soup(link)
            title = VBT_get_title(soup)
            brand = VBT_get_brand(soup)
            location = VBT_get_location(soup)
            anchors.append(generate_job_alert_anchor(title, brand, location, link))

    return render_template('newsletterLinks.html', anchors = create_snazzy_HTML_block(anchors))
