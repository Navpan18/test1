from fastapi import FastAPI, HTTPException
import subprocess

def run_python_verbose():
    try:
        # Run the 'python -v' command in a subprocess
        print("okk")
        subprocess.run(['python', 'ytdlbot/ytdl_bot.py'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running 'python -v': {e}")

# Call the function

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.get("/okk")
async def okk():
    run_python_verbose()
    
