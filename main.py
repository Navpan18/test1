from fastapi import FastAPI, HTTPException
import requests
import subprocess

def run_python_verbose():
    try:
        # Run the 'python -v' command in a subprocess
        subprocess.run(['python', '-v'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running 'python -v': {e}")

# Call the function

app = FastAPI()
run_python_verbose()

@app.get("/")
async def root():
    return {"message": "Hello World"}
