from dagster import load_assets_from_package_module, repository
from helper_pkg import hello_helper
from dagsterproj import assets

hello_helper()

@repository
def dagsterproj():
    return [load_assets_from_package_module(assets)]
