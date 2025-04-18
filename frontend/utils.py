import requests

BASE_URL = "http://localhost:8000"

def upload_function(name, language, timeout, code):
    payload = {
        "name": name,
        "language": language,
        "timeout": timeout,
        "code": code
    }
    res = requests.post(f"{BASE_URL}/functions/", json=payload)
    return res.json()

def get_functions():
    res = requests.get(f"{BASE_URL}/functions/")
    return res.json()

def run_function(function_id, use_gvisor=False):
    data = {"use_gvisor": use_gvisor}
    res = requests.post(f"{BASE_URL}/functions/{function_id}/run", json=data)
    print(f"Raw response: {res.text}")
    print(f"Response status code: {res.status_code}")
    return res.json()

def delete_function(function_id):
    res = requests.delete(f"{BASE_URL}/functions/{function_id}")
    return res.json()

def get_logs(function_id):
    res = requests.get(f"{BASE_URL}/functions/{function_id}/logs")
    return res.json()

def get_metrics(function_id):
    res = requests.get(f"{BASE_URL}/functions/{function_id}/metrics")
    return res.json()

def get_code(function_id):
    res = requests.get(f"{BASE_URL}/functions/{function_id}/code")
    return res.json()

def update_code(function_id, new_code):
    print(f"Updating Function {function_id} with code: {new_code[:100]}")
    res = requests.put(f"{BASE_URL}/functions/{function_id}", json={"code": new_code})
    return res.json()
