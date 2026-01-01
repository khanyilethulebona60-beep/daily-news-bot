import requests
from datetime import datetime

NEWS_API_KEY = "PUT_API_KEY_HERE"
URL = "https://newsapi.org/v2/top-headlines"

PARAMS = {
    "category": "business",
    "language": "en",
    "pageSize": 5,
    "apiKey": NEWS_API_KEY
}

def get_news():
    response = requests.get(URL, params=PARAMS)
    data = response.json()
    articles = data.get("articles", [])

    today = datetime.utcnow().strftime("%Y-%m-%d")
    output = f"Daily Market News – {today}\n\n"

    for a in articles:
        title = a.get("title")
        source = a.get("source", {}).get("name")
        link = a.get("url")
        output += f"- {title} ({source})\n  {link}\n\n"

    return output

if __name__ == "__main__":
    print(get_news())
