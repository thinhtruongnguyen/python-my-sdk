from aioz_api_client.exceptions import ApiException
import json
from aioz_api_client.api_client import ApiClient
from my_platform_sdk_package.services.api_key_service import ApiKeyService
from my_platform_sdk_package.services.api_key_model_service import ApiKeyModelService
from my_platform_sdk_package.services.api_key_model_verify_service import ApiKeyModelVerifyService
from my_platform_sdk_package.services.api_key_model_versioning_service import ApiKeyModelVersioningService
from my_platform_sdk_package.services.api_key_repository_service import ApiKeyRepositoryService


BASE_URL = "http://143.198.81.10:9000/api/v1/"


class ApiError(Exception):
    def __init__(self, status, body):
        self.http_status = status
        self.raw_body = body

        try:
            parsed = json.loads(body)
            self.api_status = parsed.get("status")
            self.message = parsed.get("message")
        except Exception:
            self.api_status = None
            self.message = body
            parsed = {"status": status, "message": body}

        self.status = self.api_status or self.http_status
        self.parsed_body = parsed

        super().__init__(self.message)

    def __str__(self):
        return json.dumps(self.parsed_body, ensure_ascii=False)


class HttpClient:
    def __init__(self, api_key: str, base_url: str = BASE_URL):
        self.client = ApiClient()
        if api_key:
            self.client.set_default_header("x-api-key", api_key)
        if base_url:
            self.client.configuration.host = base_url

        self.api_key_service = ApiKeyService(self)
        self.api_key_model_service = ApiKeyModelService(self.client)
        self.api_key_model_verify_service = ApiKeyModelVerifyService(self.client)
        self.api_key_model_versioning_service = ApiKeyModelVersioningService(self.client)
        self.api_key_repository_service = ApiKeyRepositoryService(self.client)

    def request(
        self,
        method: str,
        path: str,
        query_params=None,
        body=None,
        headers=None,
        timeout: float = None,
        response_model=None
    ):
        headers = headers or {}
        if body is not None:
            headers["Content-Type"] = "application/json"

        method, url, header_params, body, post_params = self.client.param_serialize(
            method=method,
            resource_path=path,
            query_params=query_params,
            header_params=headers,
            body=body,
        )

        try:
            response = self.client.call_api(
                method=method,
                url=url,
                header_params=header_params,
                body=body,
                post_params=post_params,
                _request_timeout=timeout
            )
            response.read()
            deserialized = self.client.response_deserialize(
                response_data=response,
                response_types_map={"2XX": response_model or object}
            )
            return deserialized.data

        except ApiException as e:
            status_code = e.status
            body = e.body or ""
            raise ApiError(status_code, body) from e
