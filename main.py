from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/health", status_code = 200)
def health():
    return{"status": "OK"}

PAGES = {
    "home": {"title":"home page"},
    "store": {"title": "store"},
    "about": {"title":"abobut us"}
}

@app.get("/pages")
def pages():
    result = []
    for slug in PAGES:
        result.append
        ({"slug": slug,
         "title": PAGES[slug]["title"]})
    return result

@app.get("/pages/{slug}")
def pages_slug(slug: str):
    page = PAGES.get(slug)
    if not page:
        raise HTTPException (status_code = 404, detail = "Not found")
    return page

@app.get("/pages/{slug}/title")
def pages_slug_title(slug: str):
    page_title = PAGES.get(slug)
    if not page_title:
        raise HTTPException (status_code = 404, detail = "Not found")
    title = page_title.get("title")
    return {"title": title}
@app.get("/pages/{slug}/exists")
def pages_slug_exist(slug: str):
    exists: bool = slug in PAGES
    return {"exists": exists}