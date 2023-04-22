from fastapi.testclient import TestClient


class TestRSVP:
    """All tests for rsvp.crud using the testclient"""

    def test_get_guests(self, client: TestClient, guest_fixture):
        response = client.get("/guests")
        assert response.status_code == 200

        data = response.json()
        assert data == [
            {"name": "Gina Rogari", "has_plus_one": True, "id": 1},
            {"name": "Ian Myjer", "has_plus_one": True, "id": 2},
        ]
