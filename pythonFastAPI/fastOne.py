import fastapi as FastAPI

app = FastAPI() # create API object

@app.get("/")
def home():
    return {"Data" : "Test"}
