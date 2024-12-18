from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from typing import List

# Initialize FastAPI app
app = FastAPI()

# Database connection
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# Initialize database
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()

# Call database initialization
init_db()

# Pydantic model for item
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

class ItemResponse(Item):
    id: int

# CRUD Routes
@app.post("/items/", response_model=ItemResponse)
def create_item(item: Item):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO items (name, description, price) VALUES (?, ?, ?)",
        (item.name, item.description, item.price),
    )
    conn.commit()
    item_id = cursor.lastrowid
    conn.close()
    return ItemResponse(id=item_id, **item.dict())

@app.get("/items/", response_model=List[ItemResponse])
def get_items():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    rows = cursor.fetchall()
    conn.close()
    return [ItemResponse(**dict(row)) for row in rows]

@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE id = ?", (item_id,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Item not found")
    return ItemResponse(**dict(row))

@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: Item):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE items SET name = ?, description = ?, price = ? WHERE id = ?",
        (item.name, item.description, item.price, item_id),
    )
    conn.commit()
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Item not found")
    conn.close()
    return ItemResponse(id=item_id, **item.dict())

@app.delete("/items/{item_id}", response_model=dict)
def delete_item(item_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
    conn.commit()
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Item not found")
    conn.close()
    return {"detail": "Item deleted successfully"}