from dotenv import load_dotenv

load_dotenv()   # 👈 THIS IS REQUIRED

from app import create_app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True,port=8000)
