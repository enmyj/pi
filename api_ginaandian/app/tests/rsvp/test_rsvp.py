from fastapi.testclient import TestClient


class TestRSVP:
    """All tests for rsvp.crud using the testclient"""

    def test_get_rsvp_empty(self, client: TestClient):
        response = client.get("/rsvp")
        assert response.status_code == 200

        data = response.json()
        assert data == []

    def test_get_rsvp_not_empty(self, client: TestClient, rsvp_fixture):
        response = client.get("/rsvp")
        assert response.status_code == 200

        data = response.json()
        assert len(data) > 1

    def test_post_rsvp(self, client: TestClient):
        response = client.post(
            "/rsvp",
            json={
                "name": "Gina Rogari",
                "plus_one_name": "Ian Myjer",
                "rsvp": True,
                "shuttle": True,
            },
        )
        assert response.status_code == 200

    def test_delete_rsvp(self, client: TestClient, rsvp_fixture):
        response = client.delete("/rsvp/1")
        assert response.status_code == 200

        response = client.delete("/rsvp/1")
        assert response.status_code != 200

    def test_patch_rsvp(self, client: TestClient, rsvp_fixture):
        response = client.patch("/rsvp/1", json={"name": "foobar", "shuttle": False})
        assert response.status_code == 200

        response = client.get("/rsvp/1")
        assert response.status_code == 200
        data = response.json()
        assert data["shuttle"] is False
