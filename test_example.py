import requests

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