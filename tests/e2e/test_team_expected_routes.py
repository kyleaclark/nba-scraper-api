import csv
import io
import json

from fastapi.testclient import TestClient


def test_get_team_expected_error_status(client: TestClient):
    resp = client.get('/api/v1/team/expected')
    assert resp.status_code == 422


def test_get_team_expected_json_resp_status(client: TestClient):
    resp = client.get(f'/api/v1/team/expected?season_year=2023')
    assert resp.status_code == 200


def test_get_team_expected_json_resp_content(client: TestClient):
    resp = client.get(f'/api/v1/team/expected?season_year=2023')

    content = json.loads(resp.content)
    season_year = content.get('season_year')
    team_expected_data = content.get('team_expected')

    assert season_year == 2023
    assert isinstance(team_expected_data, dict)
    assert len(team_expected_data) == 30


def test_get_team_expected_csv_resp_status(client: TestClient):
    resp = client.get(f'/api/v1/team/expected?season_year=2023&return_as_csv=True')
    assert resp.status_code == 200


def test_get_team_expected_csv_resp_content(client: TestClient):
    resp = client.get(f'/api/v1/team/expected?season_year=2023&return_as_csv=True')

    csv_reader = csv.DictReader(io.StringIO(resp.content.decode('utf-8')))
    team_expected_data = list(csv_reader)

    assert isinstance(team_expected_data, list)
    assert len(team_expected_data) == 30
