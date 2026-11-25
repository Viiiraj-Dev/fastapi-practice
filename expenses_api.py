from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class ExpenseIn(BaseModel):
    amount: float = Field(gt=0) # must be greater than 0
    category: str # required
    note: str = "" # optional, defaults to empty


expenses = []  # temporary storage, lives in memory

@app.post("/expenses", status_code=201)
def add_expense(expense: ExpenseIn):
    item = {"id": len(expenses)+1, **expense.model_dump()}
    expenses.append(item)
    return item

@app.get("/expenses")
def list_expenses():
    return expenses

@app.get("/expenses/{expense_id}")
def get_expense(expense_id: int):
    for item in expenses:
        if item["id"] == expense_id:
            return item
    raise HTTPException(status_code=404, detail="Expense Not Found")


@app.get("/expenses/total")
def get_total():
    sum(expenses["amount"])