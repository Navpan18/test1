from fastapi import FastAPI, HTTPException
import subprocess
import requests
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
    url = 'https://ytdlbot2.onrender.com/'
    timeout_seconds = 5
    
    try:
        # Make a GET request with a timeout
        response = requests.get(url, timeout=timeout_seconds)
        response.raise_for_status()  # Raise an exception for bad responses (4xx and 5xx status codes)
        
        # Process the response here
        print("Request successful:", response.text)
        return {"message": "okk"}
    
    except requests.exceptions.Timeout:
        print(f"Request to {url} timed out after {timeout_seconds} seconds.")
        return {"message": "timed out"}
    
    except requests.exceptions.RequestException as e:
        print(f"Request to {url} failed: {e}")
        return {"message": "kuch aur"}
@app.get("/okk2")
async def okk2():
    url = 'https://ytdlbot2.onrender.com/okk'
    timeout_seconds = 5
    
    try:
        # Make a GET request with a timeout
        response = requests.get(url, timeout=timeout_seconds)
        response.raise_for_status()  # Raise an exception for bad responses (4xx and 5xx status codes)
        
        # Process the response here
        print("Request successful:", response.text)
        return {"message": "okk"}
    
    except requests.exceptions.Timeout:
        print(f"Request to {url} timed out after {timeout_seconds} seconds.")
        return {"message": "timed out"}
    
    except requests.exceptions.RequestException as e:
        print(f"Request to {url} failed: {e}")
        return {"message": "kuch aur"}
    
