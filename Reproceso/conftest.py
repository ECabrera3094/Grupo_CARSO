import pytest
def pytest_addoption(parser):
    parser.addoption("--date", action="store", default="2024-12-12", help="Fecha para el TestCase")
    parser.addoption("--countries", action="store", default="US,MX", help="Lista de países separados por comas")


@pytest.fixture
def test_params(request):
    date = request.config.getoption("--date")
    countries = request.config.getoption("--countries")
    return date, countries