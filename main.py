import os
from dotenv import load_dotenv
import requests # pip install requests first!
import time

# Load environment variables from .env file
load_dotenv()

# Access environment variables
api_key = os.getenv("GROQ_API_KEY")
print(api_key)


"""
1. Upload the JSONL file to Groq
"""

def upload_file_to_groq(api_key, file_path):
    url = "https://api.groq.com/openai/v1/files"
    
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    
    # Prepare the file and form data
    files = {
        "file": ("batch_file.jsonl", open(file_path, "rb"))
    }
    
    data = {
        "purpose": "batch"
    }
    
    # Make the POST request
    response = requests.post(url, headers=headers, files=files, data=data)
    
    return response.json()

# Usage example
file_path = "batch.jsonl"  # Path to your JSONL file
# need to replace with a correct id. get an id from the above function probably thing["id"] or thing.id prolly using the first id index
file_id = "" # replace with your `id` from file upload API response object (used in the next step)

try:
    result = upload_file_to_groq(api_key, file_path)
    print(result)

    file_id = result["id"]
    print("this is the file id: " + file_id)
except Exception as e:
    print(f"Error: {e}")


"""
2. Now we make a batch object
"""

def create_batch(api_key, input_file_id):
    url = "https://api.groq.com/openai/v1/batches"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "input_file_id": input_file_id,
        "endpoint": "/v1/chat/completions",
        "completion_window": "24h"
    }
    
    response = requests.post(url, headers=headers, json=data)
    return response.json()

batch_id = ""
try:
    result = create_batch(api_key, file_id)
    print("\n step 2 result")
    print(result)
    batch_id = result["id"] # batch result id
except Exception as e:
    print(f"Error: {e}")


"""
3. Get batch status
"""

def get_batch_status(api_key, batch_id):
    url = f"https://api.groq.com/openai/v1/batches/{batch_id}"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    response = requests.get(url, headers=headers)
    return response.json()



output_file_id = ""
try:
    result = get_batch_status(api_key, batch_id)
    print("\n step4 results: ")
    print(result)

    
    count = 0

    # Corrected condition: use `result["status"]` instead of `result.status`
    while result["status"] != "completed" and count < 100:
        result = get_batch_status(api_key, batch_id)  # Update `result` inside the loop
        time.sleep(3)
        print(result["status"])
        count += 1

    print(result["status"])
    output_file_id = result.get("output_file_id")  # Use .get() to safely access keys
    print("this is outputfileid: " + output_file_id)
except Exception as e:
    print(f"Error: {e}")


"""
4. Retrieve batch results
"""

def download_file_content(api_key, output_file_id, output_file):
    url = f"https://api.groq.com/openai/v1/files/{output_file_id}/content"
    
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    
    response = requests.get(url, headers=headers)
    
    # Write the content to a file
    with open(output_file, 'wb') as f:
        f.write(response.content)
    
    return f"File downloaded successfully to {output_file}"

output_file = "batch_output.jsonl" # replace with your own file of choice to download batch job contents to
print(output_file_id)
try:
    result = download_file_content(api_key, output_file_id, output_file)
    print(result)
except Exception as e:
    print(f"Error: {e}")