from fastapi import FastAPI

app = FastAPI()

# Path/endpoint/route refers to the last part of the URL starting from the first /
# Path operations are evaluated in order

@app.get("/")
async def root():
    return {"message": "Hello World"}  # Can return dict, list, str, int, etc.

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": f"This is item: {item_id}"}
