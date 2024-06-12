from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os
import requests
import uvicorn

app = FastAPI()

#API Key for newsapi.org
API_KEY = "5094cb4f887149b5800377bd7771b464"

BASE_URL = "https://newsapi.org/v2/"

#return server health check
@app.get("/health")
async def return_health():
    return "udlshanetst01.vuhl.root.mrc.local", 200


@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open(os.path.join("static", "index.html"), "r") as file:
        return HTMLResponse(content=file.read())

#fucntion that gets top sports headlines from NewsAPI 
#you can change the category based off specific news types you are looking for
#for example change sports to business or technology to pull different info
def get_top_headlines(country, category):
    endpoint = "top-headlines"
    params = {
        "country": country,
        "category": category,
        "apiKey": API_KEY
    }
    response = requests.get(BASE_URL + endpoint, params=params)
    if response.status_code == 200:
        articles = response.json()["articles"]
        extracted_articles = [{"author": article["author"], "title": article["title"], "url": article["url"]} for article in articles]
        return True, extracted_articles
    else:
        return False, "Failed to fetch news headlines"

@app.get("/top-sports-headlines")
async def top_headlines(country: str = "us", category: str = "sports"):
    success, result = get_top_headlines(country, category)
    if success:
        return result
    else:
        return {"error": result}

@app.get("/top-business-headlines")
async def top_headlines(country: str = "us", category: str = "business"):
    success, result = get_top_headlines(country, category)
    if success:
        return result
    else:
        return {"error": result}

@app.get("/top-entertainment-headlines")
async def top_headlines(country: str = "us", category: str = "entertainment"):
    success, result = get_top_headlines(country, category)
    if success:
        return result
    else:
        return {"error": result}

@app.get("/top-health-headlines")
async def top_headlines(country: str = "us", category: str = "health"):
    success, result = get_top_headlines(country, category)
    if success:
        return result
    else:
        return {"error": result}

@app.get("/top-general-headlines")
async def top_headlines(country: str = "us", category: str = "general"):
    success, result = get_top_headlines(country, category)
    if success:
        return result
    else:
        return {"error": result}

@app.get("/top-science-headlines")
async def top_headlines(country: str = "us", category: str = ""):
    success, result = get_top_headlines(country, category)
    if success:
        return result
    else:
        return {"error": result} 

@app.get("/top-technology-headlines")
async def top_headlines(country: str = "us", category: str = "technology"):
    success, result = get_top_headlines(country, category)
    if success:
        return result
    else:
        return {"error": result}
    
def main():
    uvicorn.run(app, host = "0.0.0.0", port=443, ssl_keyfile='./leaf.key', ssl_certfile='./leaf.crt')

#Main calling function
if __name__ == "__main__":
    main()