from fastapi import FastAPI, HTTPException
import random
import requests


app = FastAPI()

# Dummy data for the APIs
data1 = {
    "id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "age": [25, 30, 35, 40, 45]
}

data2 = {
    "product_id": [101, 102, 103, 104, 105],
    "product_name": ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"],
    "price": [500, 300, 200, 150, 50]
}

@app.get("/api/data1")
def get_data1():
    """Fetches the first dummy dataset."""
    return {
        "status": "success",
        "data": data1
    }

@app.get("/api/data2")
def get_data2():
    """Fetches the second dummy dataset."""
    return {
        "status": "success",
        "data": data2
    }

@app.get("/api/advice")
def get_data2():
    """Fetches the second dummy dataset."""
    try:
        url = "https://api.adviceslip.com/advice"

        resp = requests.get(url=url)
        resp.raise_for_status()
        advice = resp.json()["slip"]["advice"]

        return {"advice":advice,"msg":"noice one thou"}
    except Exception as e: 
        import traceback 
        print(traceback.format_exc())
        return HTTPException(status_code=500,detail={
            "error":"internal server error"+ str(e),
        }) 
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
