import pytest
import requests
from weather_app import get_weather_data, get_wind_speed_data, get_pressure_data

# Mock API response for testing
mock_response = {
    "list": [
        {
            "dt_txt": "2019-03-29 12:00:00",
            "main": {
                "temp": 285.888,
                "pressure": 1010.12
            },
            "wind": {
                "speed": 4.01
            },
            "weather": [
                {
                    "description": "clear sky"
                }
            ]
        }
    ]
}

class MockResponse:
    def __init__(self, status_code, json_data):
        self.status_code = status_code
        self.json_data = json_data

    def json(self):
        return self.json_data

@pytest.fixture
def mock_requests_get(monkeypatch):
    # Mock the requests.get() function to return the mock response
    def mock_get(*args, **kwargs):
        return MockResponse(200, mock_response)
    monkeypatch.setattr(requests, 'get', mock_get)

def test_get_weather_data(mock_requests_get, monkeypatch, capsys):
    # Input date and validate output
    monkeypatch.setattr('builtins.input', lambda _: '2019-03-29 12:00:00')
    get_weather_data()
    captured = capsys.readouterr()
    assert "Temperature at 2019-03-29 12:00:00: 285.888 Kelvin" in captured.out

def test_get_wind_speed_data(mock_requests_get, monkeypatch, capsys):
    # Input date and validate output
    monkeypatch.setattr('builtins.input', lambda _: '2019-03-29 12:00:00')
    get_wind_speed_data()
    captured = capsys.readouterr()
    assert "Wind Speed at 2019-03-29 12:00:00: 4.01 m/s" in captured.out

def test_get_pressure_data(mock_requests_get, monkeypatch, capsys):
    # Input date and validate output
    monkeypatch.setattr('builtins.input', lambda _: '2019-03-29 12:00:00')
    get_pressure_data()
    captured = capsys.readouterr()
    assert "Pressure at 2019-03-29 12:00:00: 1010.12 hPa" in captured.out

