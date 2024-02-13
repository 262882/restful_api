## Development server
```
uvicorn main:app --reload  # Reload updates with code changes
```

Open interactive API documentation
```
http://127.0.0.1:8000/docs
```

## Testing requests
```
# GET
curl http://127.0.0.1:8000/

# POST
curl -X POST -H "Content-Type: application/json" -d '{
    "amount": 20,
    "description": "lottery"
}' http://localhost:8000/incomes
```

## Operations (HTTP methods)

```
POST: to create data.
GET: to read data.
PUT: to update data.
DELETE: to delete data.
```