from django.test import TestCase
from .services.api import get_package_name, get_current_package_version

def test_connection_api_pypi_is_working_to_get_current_package_name():
    assert get_package_name("sampleproject") == "sampleproject"

def test_connection_api_pypi_is_working_to_get_current_package_version():
    assert get_current_package_version("sampleproject", "2.0.0") == "2.0.0"


