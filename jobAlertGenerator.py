from bs4 import BeautifulSoup
import requests

# All of this is based on very specific CSS selectors and HTML that, for now, are only good for VBT.
# That said, there's no reason we couldn't expand the selectors to take in a particular route and to parse other sites.
def VBT_get_title(s):
    return s.select("body > main > div.container.job-description > div > div.col > div > div.job-description-header.search-item-body > h1")[0].get_text()

def VBT_get_brand(s):
    return s.select("body > main > div.container.job-description > div > div.col > div > div.job-description-header.search-item-body > div.search-item-meta.gold-line.line-equal-height.text-uppercase > span > a")[0].get_text()

def VBT_get_location(s):
    # you slice [1::] to skip the brand name in the same div.
    # todo: FIX this janky thing to look at the title element and pull deets for location out of there. 
    print(" ".join(s.select("body > main > div.container.job-description > div > div.col > div > div.job-description-header.search-item-body > div.search-item-meta.gold-line.line-equal-height.text-uppercase")[0].get_text().split()[2::]))
    return " ".join(s.select("body > main > div.container.job-description > div > div.col > div > div.job-description-header.search-item-body > div.search-item-meta.gold-line.line-equal-height.text-uppercase")[0].get_text().split()[1::])

def generate_job_alert_anchor(title, brand, location, url):
    # based on what the user passes to the function, we generate some nice HTML
    # the html is specifically for job alerts for VBT.
    return "<a href=\"{}\" style=\"color: black;text-decoration: none;\"><strong>{}, </strong>{}<br />{}</a><br />".format(url, title, brand, location)

def create_snazzy_HTML_block(anchors):
    # From a list of strings, generate a block of nice HTML.
    html = []
    for job in anchors:
        html.append(job)

    # Make sure there's a new line between each HTML anchor.
    return "<br/> \n".join(html)

def make_soup(link):
    return BeautifulSoup(requests.get(link).text, 'html.parser')
