import uvicorn

from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    uvicorn.run("app.poke_app:app", host="0.0.0.0", port=8088, reload=True)
