from fastapi import FastAPI
#from app.api.routes import auth,articles 

app = FastAPI()

@app.get("/")
def health_check():
    return {"status":"ok"}


