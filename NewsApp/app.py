from flask import Flask, render_template
import requests 

app = Flask(__name__)

@app.route("/")
def index():
    url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=1eaee59ec1264a3e84ae59c7ac87bbe3"
    r = requests.get(url).json()  # Corrected: added parentheses to call json()

    cases = {
        'articles': r['articles']
    }

    return render_template("index.html", case=cases)  # Corrected: changed 'case' to 'cases'

if __name__ == "__main__":
    app.run(debug=True)
