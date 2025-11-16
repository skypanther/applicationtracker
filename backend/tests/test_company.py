from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from ..database import get_db
from ..server import app
from ..schemas.company import CompanySchema

client = TestClient(app)

def test_get_company(test_client):
    response = test_client.get("/company")
    assert response.status_code == 200
    response_json = response.json()
    assert response_json == []

def test_create_company(test_client, company_payload):
    response = test_client.post("/company", json=company_payload)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["company_id"] == 1
    assert response_json["name"] == "Fake Company"
    assert response_json["website"] == "www.example.com"

def test_update_company(test_client, company_payload, company_update_payload):
    response = test_client.post("/company", json=company_payload)
    assert response.status_code == 200

    response = test_client.put("/company/1", json=company_update_payload)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["company_id"] == 1
    assert response_json["name"] == "Bogus Company"
    assert response_json["website"] == "www.bogus.com"

def test_delete_company(test_client, company_payload):
    response = test_client.post("/company", json=company_payload)
    assert response.status_code == 200

    response = test_client.delete("/company/1")
    assert response.status_code == 200
    response_json = response.json()
    # the delete endpoint returns the company that was deleted
    assert response_json["company_id"] == 1
    assert response_json["name"] == "Fake Company"
    assert response_json["website"] == "www.example.com"
