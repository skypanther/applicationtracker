from fastapi.testclient import TestClient
from ..server import app

client = TestClient(app)

def test_get_job_app(test_client):
    response = test_client.get("/job_app")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json == []

def test_create_job_app(test_client, job_app_payload, company_payload):
    # need a company
    response = test_client.post("/company", json=company_payload)
    assert response.status_code == 200

    response = test_client.post("/job_app", json=job_app_payload)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["job_app_id"] == 1
    assert response_json["job_title"] == "Developer"
    assert response_json["source"] == "LinkedIn"

def test_job_app_update(test_client, job_app_payload, job_app_update_payload):
    # need a job app
    response = test_client.post("/job_app", json=job_app_payload)
    assert response.status_code == 200

    response = test_client.put('/job_app/1', json=job_app_update_payload)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["job_title"] == "Software Engineer"

def test_job_app_delete(test_client, job_app_payload):
    # need a job app
    response = test_client.post("/job_app", json=job_app_payload)
    assert response.status_code == 200

    response = test_client.delete("/job_app/1")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["job_title"] == "Developer"