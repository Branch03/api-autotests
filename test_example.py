import requests
import pytest

def test_api_root():
    response = requests.get("https://api.github.com")
    assert response.status_code == 200  
    data = response.json()
    assert "current_user_url" in data

def test_api_user_octocat():
    response = requests.get("https://api.github.com/users/octocat")
    assert response.status_code == 200
    data = response.json()
    assert "login" in data 
    assert data["login"] == "octocat"

def test_api_repo_cpython():
    response = requests.get("https://api.github.com/repos/python/cpython")
    assert response.status_code == 200
    data = response.json()
    assert "full_name" in data
    assert data["full_name"] == "python/cpython"

def test_api_post():
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts",json=payload)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data

def test_api_put():
    payload =   {
    "userId": 1,
    "id": 1,
    "title": "unt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  }
    response = requests.put("https://jsonplaceholder.typicode.com/posts/1",json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data == payload

def test_api_delete():
    response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200

@pytest.mark.parametrize("username", ["octocat", "defunkt", "mojombo"])
def test_github_user(username):
    response = requests.get(f"https://api.github.com/users/{username}")
    assert response.status_code == 200
    data = response.json()
    assert data["login"] == username