from main import get_temperature
import requests


class MockResponse:
    # Retorna somente o dicionário de teste
    @staticmethod
    def json():
        return {'latitude': -14.235004, 'longitude': -51.92528, 'currently': {'temperature': 62}}


def test_get_temperature_by_lat_lng(monkeypatch):

    def mockrequest(self):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mockrequest)
    result = get_temperature(None, None)

    assert result == 16
