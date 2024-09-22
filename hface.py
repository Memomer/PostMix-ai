import requests

def query_model(prompt, api_token):

    # Define the Hugging Face API URL for the model
    api_url = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"

    # Set the headers with the API token
    headers = {
        "Authorization": f"Bearer {api_token}"
    }

    # Define the data payload with the input prompt
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": 500,  # Adjust the output length as per your need
            "temperature": 0.7,  # Adjust the creativity/randomness of the response
        }
    }

    # Make the API request
    response = requests.post(api_url, headers=headers, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse and return the generated response
        output = response.json()
        return output[0]["generated_text"]
    else:
        # Return an error message if the request failed
        return f"Error: {response.status_code}, {response.text}"

# Example usage:

