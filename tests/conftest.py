import pytest
from config import API_KEY, BASE_URL
from my_platform_sdk_package.http_client import HttpClient
from my_platform_sdk_package.services.api_key_service import ApiKeyService
from my_platform_sdk_package.services.api_key_model_service import ApiKeyModelService
from my_platform_sdk_package.services.api_key_model_verify_service import ApiKeyModelVerifyService
from my_platform_sdk_package.services.api_key_model_versioning_service import ApiKeyModelVersioningService
from my_platform_sdk_package.services.api_key_repository_service import ApiKeyRepositoryService


@pytest.fixture(scope="session")
def api():
    return HttpClient(api_key=API_KEY, base_url=BASE_URL)

@pytest.fixture(scope="session")
def api_key_repository_service(api):
    return ApiKeyRepositoryService(api)

@pytest.fixture(scope="session")
def api_key_model_versioning_service(api):
    return ApiKeyModelVersioningService(api)

@pytest.fixture(scope="session")
def api_key_model_service(api):
    return ApiKeyModelService(api)

@pytest.fixture(scope="session")
def api_key_service(api):
    return ApiKeyService(api)

@pytest.fixture(scope="session")
def api_key_model_verify_service(api):
    return ApiKeyModelVerifyService(api)

