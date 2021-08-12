from requests import get
import ipdb

def get_package_name(package_name: str):
    api = f'https://pypi.org/pypi/{package_name}/json'
    response = get(api).json()
    return response['info']['name']

def get_current_package_version(package_name: str):
    api = f'https://pypi.org/pypi/{package_name}/json'
    response = get(api).json()
    return response['info']['version']

def get_current_package_releases(package_name: str):
    api = f'https://pypi.org/pypi/{package_name}/json'
    response = get(api).json()
    return list(response['releases'].keys())
