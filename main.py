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

@app.get("/pages/{slug}")
def pages(slug: str):
    page = PAGES.get(slug)
    if not page:
        raise HTTPException (status_code = 404, detail = "Not found")
    return page