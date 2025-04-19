from fastapi.testclient import TestClient
from ..api.routes import router

client = TestClient(router)

def test_list_functions():
    response = client.get("/functions/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_upload_function():
    test_function = {
        "name": "test_function",
        "language": "python",
        "timeout": 5,
        "code": "print('Hello, World!')"
    }
    response = client.post("/functions/", json=test_function)
    assert response.status_code == 200
    assert "function_id" in response.json()

def test_run_function():
    # First upload a function
    test_function = {
        "name": "test_run",
        "language": "python",
        "timeout": 5,
        "code": "print('Hello, World!')"
    }
    upload_response = client.post("/functions/", json=test_function)
    function_id = upload_response.json()["function_id"]
    
    # Then try to run it
    response = client.post(f"/functions/{function_id}/run", json={"use_gvisor": False})
    assert response.status_code == 200
    assert "result" in response.json() 