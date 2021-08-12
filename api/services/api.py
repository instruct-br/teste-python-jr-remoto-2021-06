from requests import get

def get_package_name(package_name: str):
    
    api = f'https://pypi.org/pypi/{package_name}/json'
    response = get(api).json()
    return response['info']['name']

def get_current_package_version(package_name: str, package_version: str):
    api = f'https://pypi.org/pypi/{package_name}/json'
    response = get(api).json()
    return response['info']['version']
