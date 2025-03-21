# batch-processing

https://github.com/user-attachments/assets/2dceeee6-fb68-4979-a409-9b5d6afde245

### Set up:

Create a .jsonl file with your batch processing calls. Each line would be a new Groq batch processing call.

Example input .jsonl file with one request:
```
{"custom_id": "request-2", "method": "POST", "url": "/v1/chat/completions", "body": {"model": "llama-3.1-8b-instant", "messages": [{"role": "system", "content": "You are a helpful translation assistant. Translate the following into spanish."}, {"role": "user", "content": "Hello, how are you today?"}]}}
```

### Create a virtual environment
python3 -m venv venv

### Activate it
source venv/bin/activate

### Install the packages
pip3 install groq requests python-dotenv


## How to run it
python3 main.py

### Example output in terminal:
```
This is the file_id from Step 2: file_01jpthgx92e3ts09bma0bfchmt
This is the Batch object id from Step 3: batch_01jpthgxffe8ms4zqdkf1aejjp

Step 4 results: 
Your batch status is: validating
Your batch status is: in_progress
Your batch status is: completed
This is your output_file_id from Step 4: file_01jpthh1e3e739wba761nfgvj2

File downloaded successfully to batch_output.jsonl
```

Example output .jsonl file
```
{"id":"batch_req_out_01jpra5p4ve4v8k14zkqn6agjm","custom_id":"request-2","response":{"status_code":200,"request_id":"req_01jpra5n2qef6s66k65v8sy51h","body":{"id":"chatcmpl-f822c700-75aa-4fa3-8f2c-3f65cca8a1d3","object":"chat.completion","created":1742425217,"model":"llama-3.1-8b-instant","choices":[{"index":0,"message":{"role":"assistant","content":"\"Hola, ¿cómo estás hoy\" or more commonly in informal settings: \"Hola, ¿qué onda hoy\". \n\nIf you want it to be a more formal conversation, you could use: \"Buenos días, ¿cómo está hoy?\""},"logprobs":null,"finish_reason":"stop"}],"usage":{"queue_time":1.0087154420000002,"prompt_tokens":55,"prompt_time":0.009901563,"completion_tokens":55,"completion_time":0.073333333,"total_tokens":110,"total_time":0.083234896},"system_fingerprint":"fp_076aab041c","x_groq":{"id":"req_01jpra5n2qef6s66k65v8sy51h"}}},"error":null}
```

View more detailed documentation on batch processing [here.](https://console.groq.com/docs/batch)
