from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

class DataItem(BaseModel):
    values: List[float]

class PromptRequest(BaseModel):
    prompt: str
    data: List[DataItem]

app = FastAPI()

def generate_chain_of_thought(prompt: str, data: List[DataItem]) -> str:
    thoughts = []
    for item in data:
        values = item.values
        sum_values = sum(values)
        avg_values = sum(values) / len(values) if values else 0
        thought = (f"Given the input values: {values}, "
                   f"the sum is {sum_values} and the average is {avg_values}.")
        thoughts.append(thought)
    result = "\n".join(thoughts)
    return f"{prompt}\n{result}"

@app.post("/generate-thoughts/")
async def generate_thoughts(request: PromptRequest):
    try:
        result = generate_chain_of_thought(request.prompt, request.data)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
