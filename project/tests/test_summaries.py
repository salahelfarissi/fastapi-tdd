import json

import pytest


def test_create_summary(test_app_with_db):
    response = test_app_with_db.post(
        "/summaries/",
        data=json.dumps({"url": "https://foo.bar"}),
    )

    assert response.status_code == 201
    assert response.json()["url"] == "https://foo.bar"


def test_create_summary_invalid_json(test_app):
    response = test_app.post("/summaries/", data=json.dumps({}))

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "input": {},
                "loc": ["body", "url"],
                "msg": "Field required",
                "type": "missing",
                "url": "https://errors.pydantic.dev/2.5/v/missing",
            }
        ]
    }


def test_read_summary(test_app_with_db):
    res = test_app_with_db.post(
        "/summaries/", data=json.dumps({"url": "https://foo.bar"})
    )
    summary_id = res.json()["id"]

    res = test_app_with_db.get(f"/summaries/{summary_id}")
    assert res.status_code == 200

    response_dict = res.json()
    assert response_dict["id"] == summary_id
    assert response_dict["url"] == "https://foo.bar"
    assert response_dict["summary"]
    assert response_dict["created_at"]


def test_read_summary_incorrect_id(test_app_with_db):
    res = test_app_with_db.get("/summaries/999")
    assert res.status_code == 404
    assert res.json()["detail"] == "Summary not found"
