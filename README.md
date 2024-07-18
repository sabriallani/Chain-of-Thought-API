# FastAPI Tutorial: Chain-of-Thought Prompting

This tutorial demonstrates how to create a FastAPI application that accepts a JSON input, performs some operations on the data, and returns the result in a Chain-of-Thought format. This example includes operations such as summing and averaging a list of numerical values.

## Step 1: Install Dependencies

Ensure you have FastAPI and Uvicorn installed. You can install them using pip:

```sh
pip install fastapi uvicorn
```

## **Step 2: Run the Application**

Save the code to a file, e.g., `main.py`, and run the application using Uvicorn:

```sh
uvicorn main:app --reload
```

## **Step 3: Example of a POST Request**

You can use `curl` to send a POST request to the `/generate-thoughts/` endpoint:

```sh
curl -X POST "http://127.0.0.1:8000/generate-thoughts/" -H "Content-Type: application/json" -d '{
    "prompt": "Analyze the following data:",
    "data": [
        {"values": [1.0, 2.0, 3.0]},
        {"values": [4.0, 5.0, 6.0]}
    ]
}'
```

### Example JSON Request Body

```json
{
    "prompt": "Analyze the following data:",
    "data": [
        {"values": [1.0, 2.0, 3.0]},
        {"values": [4.0, 5.0, 6.0]}
    ]
}
```

### Expected JSON Response

```json
{
    "result": "Analyze the following data:\nGiven the input values: [1.0, 2.0, 3.0], the sum is 6.0 and the average is 2.0.\nGiven the input values: [4.0, 5.0, 6.0], the sum is 15.0 and the average is 5.0."
}
```

## **Step 4: Testing the API using Postman**

1. **Open Postman**: If you don't have Postman installed, you can download it from [here](https://www.postman.com/downloads/).

2. **Create a New Request**:
    - Click on `New` > `Request`.
    - Name your request and save it to a collection or create a new collection.

3. **Set Up the Request**:
    - Change the request type to `POST`.
    - Enter the URL: `http://127.0.0.1:8000/generate-thoughts/`.

4. **Set the Headers**:
    - Click on the `Headers` tab.
    - Add a new key-value pair: `Content-Type: application/json`.

5. **Set the Body**:
    - Click on the `Body` tab.
    - Select `raw` and choose `JSON` from the dropdown menu.
    - Enter the following JSON in the body:
    ```json
    {
        "prompt": "Analyze the following data:",
        "data": [
            {"values": [1.0, 2.0, 3.0]},
            {"values": [4.0, 5.0, 6.0]}
        ]
    }
    ```

6. **Send the Request**:
    - Click on the `Send` button.
    - You should see a response similar to the expected JSON response above.

## **Explanation**

1. **Imports**: The necessary modules are imported for creating the FastAPI application and defining the data models.
2. **Data Models**: 
    - `DataItem`: This model holds a list of floating-point values.
    - `PromptRequest`: This model holds a prompt string and a list of `DataItem`.
3. **FastAPI Application**: The `FastAPI` application is instantiated.
4. **Function `generate_chain_of_thought`**: This function processes each `DataItem` to calculate the sum and average of its values, generating a chain of thought.
5. **Endpoint `/generate-thoughts/`**: This POST endpoint processes the request, generates the chain of thought, and returns the result.
6. **Running the Application**: The app is run on `127.0.0.1:8000` using Uvicorn.
