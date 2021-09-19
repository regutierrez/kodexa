# flake8: noqa

"""
    Kodexa

    Rethink how you work with documents  # noqa: E501

    The version of the OpenAPI document: ${git.build.version}
    Generated by: https://openapi-generator.tech
"""


__version__ = "1.0.0"

# import ApiClient
from kodexa.client.api_client import ApiClient

# import Configuration
from kodexa.client.configuration import Configuration

# import exceptions
from kodexa.client.exceptions import OpenApiException
from kodexa.client.exceptions import ApiAttributeError
from kodexa.client.exceptions import ApiTypeError
from kodexa.client.exceptions import ApiValueError
from kodexa.client.exceptions import ApiKeyError
from kodexa.client.exceptions import ApiException
