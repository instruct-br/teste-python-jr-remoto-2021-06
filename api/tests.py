from django.test import TestCase
from .services.api import get_package_name, get_current_package_version

def test_connection_api_pypi_is_working_to_get_current_package_name():
    assert get_package_name("sampleproject") == "sampleproject"

def test_connection_api_pypi_is_working_to_get_current_package_version():
    assert get_current_package_version("sampleproject") == "2.0.0"

def test_connection_api_pypi_is_working_to_get_package_releases():
    assert get_current_package_releases("sampleproject") == ["1.0", "1.2.0", "1.3.0", "1.3.1", "2.0.0"]
