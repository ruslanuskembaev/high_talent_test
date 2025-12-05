def test_question_lifecycle(client):
    # create question
    resp = client.post("/questions/", json={"text": "Что нового?"})
    assert resp.status_code == 201
    q = resp.json()
    assert q["text"] == "Что нового?"

    # list questions
    resp = client.get("/questions/")
    assert resp.status_code == 200
    assert len(resp.json()) == 1

    # create answer
    resp = client.post(
        f"/questions/{q['id']}/answers/",
        json={"text": "Все работает", "user_id": "user-1"},
    )
    assert resp.status_code == 201
    answer = resp.json()
    assert answer["question_id"] == q["id"]

    # get question with answers
    resp = client.get(f"/questions/{q['id']}")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data["answers"]) == 1
    assert data["answers"][0]["id"] == answer["id"]

    # delete question cascades answers
    resp = client.delete(f"/questions/{q['id']}")
    assert resp.status_code == 204

    # answers should be gone
    resp = client.get(f"/answers/{answer['id']}")
    assert resp.status_code == 404


def test_answer_validation(client):
    # question required
    resp = client.post("/questions/999/answers/", json={"text": "x", "user_id": "u"})
    assert resp.status_code == 404

    # validation triggers
    resp = client.post("/questions/", json={"text": ""})
    assert resp.status_code == 422

    # create valid question and answer with missing user
    q_resp = client.post("/questions/", json={"text": "Test"})
    q_id = q_resp.json()["id"]
    resp = client.post(f"/questions/{q_id}/answers/", json={"text": "ok", "user_id": ""})
    assert resp.status_code == 422
