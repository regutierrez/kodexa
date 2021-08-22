"""
    Kodexa

    Rethink how you work with documents  # noqa: E501

    The version of the OpenAPI document: 4.0.173
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from kodexa.client.api_client import ApiClient, Endpoint as _Endpoint
from kodexa.client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from kodexa.client.model.action import Action
from kodexa.client.model.page_action import PageAction


class ActionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_action(
            self,
            organization_slug,
            action,
            **kwargs
        ):
            """create_action  # noqa: E501

            Create a new instance of the object in the organization  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_action(organization_slug, action, async_req=True)
            >>> result = thread.get()

            Args:
                organization_slug (str):
                action (Action):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Action
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['organization_slug'] = \
                organization_slug
            kwargs['action'] = \
                action
            return self.call_with_http_info(**kwargs)

        self.create_action = _Endpoint(
            settings={
                'response_type': (Action,),
                'auth': [],
                'endpoint_path': '/api/actions/{organizationSlug}',
                'operation_id': 'create_action',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'organization_slug',
                    'action',
                ],
                'required': [
                    'organization_slug',
                    'action',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'organization_slug':
                        (str,),
                    'action':
                        (Action,),
                },
                'attribute_map': {
                    'organization_slug': 'organizationSlug',
                },
                'location_map': {
                    'organization_slug': 'path',
                    'action': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    '*/*'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__create_action
        )

        def __delete_action(
            self,
            organization_slug,
            slug,
            **kwargs
        ):
            """delete_action  # noqa: E501

            Delete the current version of the given object  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_action(organization_slug, slug, async_req=True)
            >>> result = thread.get()

            Args:
                organization_slug (str):
                slug (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                bool
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['organization_slug'] = \
                organization_slug
            kwargs['slug'] = \
                slug
            return self.call_with_http_info(**kwargs)

        self.delete_action = _Endpoint(
            settings={
                'response_type': (bool,),
                'auth': [],
                'endpoint_path': '/api/actions/{organizationSlug}/{slug}',
                'operation_id': 'delete_action',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'organization_slug',
                    'slug',
                ],
                'required': [
                    'organization_slug',
                    'slug',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'organization_slug':
                        (str,),
                    'slug':
                        (str,),
                },
                'attribute_map': {
                    'organization_slug': 'organizationSlug',
                    'slug': 'slug',
                },
                'location_map': {
                    'organization_slug': 'path',
                    'slug': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    '*/*'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__delete_action
        )

        def __delete_version_action(
            self,
            organization_slug,
            slug,
            version,
            **kwargs
        ):
            """delete_version_action  # noqa: E501

            Delete the specified version of the given object  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_version_action(organization_slug, slug, version, async_req=True)
            >>> result = thread.get()

            Args:
                organization_slug (str):
                slug (str):
                version (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                bool
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['organization_slug'] = \
                organization_slug
            kwargs['slug'] = \
                slug
            kwargs['version'] = \
                version
            return self.call_with_http_info(**kwargs)

        self.delete_version_action = _Endpoint(
            settings={
                'response_type': (bool,),
                'auth': [],
                'endpoint_path': '/api/actions/{organizationSlug}/{slug}/{version}',
                'operation_id': 'delete_version_action',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'organization_slug',
                    'slug',
                    'version',
                ],
                'required': [
                    'organization_slug',
                    'slug',
                    'version',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'organization_slug':
                        (str,),
                    'slug':
                        (str,),
                    'version':
                        (str,),
                },
                'attribute_map': {
                    'organization_slug': 'organizationSlug',
                    'slug': 'slug',
                    'version': 'version',
                },
                'location_map': {
                    'organization_slug': 'path',
                    'slug': 'path',
                    'version': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    '*/*'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__delete_version_action
        )

        def __get_action(
            self,
            organization_slug,
            slug,
            **kwargs
        ):
            """get_action  # noqa: E501

            Get the current version of the object with given slug  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_action(organization_slug, slug, async_req=True)
            >>> result = thread.get()

            Args:
                organization_slug (str):
                slug (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Action
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['organization_slug'] = \
                organization_slug
            kwargs['slug'] = \
                slug
            return self.call_with_http_info(**kwargs)

        self.get_action = _Endpoint(
            settings={
                'response_type': (Action,),
                'auth': [],
                'endpoint_path': '/api/actions/{organizationSlug}/{slug}',
                'operation_id': 'get_action',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'organization_slug',
                    'slug',
                ],
                'required': [
                    'organization_slug',
                    'slug',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'organization_slug':
                        (str,),
                    'slug':
                        (str,),
                },
                'attribute_map': {
                    'organization_slug': 'organizationSlug',
                    'slug': 'slug',
                },
                'location_map': {
                    'organization_slug': 'path',
                    'slug': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    '*/*'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_action
        )

        def __get_version_action(
            self,
            organization_slug,
            slug,
            version,
            **kwargs
        ):
            """get_version_action  # noqa: E501

            Get the specific version of the object with given slug  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_version_action(organization_slug, slug, version, async_req=True)
            >>> result = thread.get()

            Args:
                organization_slug (str):
                slug (str):
                version (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Action
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['organization_slug'] = \
                organization_slug
            kwargs['slug'] = \
                slug
            kwargs['version'] = \
                version
            return self.call_with_http_info(**kwargs)

        self.get_version_action = _Endpoint(
            settings={
                'response_type': (Action,),
                'auth': [],
                'endpoint_path': '/api/actions/{organizationSlug}/{slug}/{version}',
                'operation_id': 'get_version_action',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'organization_slug',
                    'slug',
                    'version',
                ],
                'required': [
                    'organization_slug',
                    'slug',
                    'version',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'organization_slug':
                        (str,),
                    'slug':
                        (str,),
                    'version':
                        (str,),
                },
                'attribute_map': {
                    'organization_slug': 'organizationSlug',
                    'slug': 'slug',
                    'version': 'version',
                },
                'location_map': {
                    'organization_slug': 'path',
                    'slug': 'path',
                    'version': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    '*/*'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_version_action
        )

        def __list_action(
            self,
            organization_slug,
            **kwargs
        ):
            """list_action  # noqa: E501

            Get a paginated list of the objects for an organization  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_action(organization_slug, async_req=True)
            >>> result = thread.get()

            Args:
                organization_slug (str):

            Keyword Args:
                query (str): [optional] if omitted the server will use the default value of "*"
                include_public (bool): [optional] if omitted the server will use the default value of False
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                PageAction
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['organization_slug'] = \
                organization_slug
            return self.call_with_http_info(**kwargs)

        self.list_action = _Endpoint(
            settings={
                'response_type': (PageAction,),
                'auth': [],
                'endpoint_path': '/api/actions/{organizationSlug}',
                'operation_id': 'list_action',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'organization_slug',
                    'query',
                    'include_public',
                ],
                'required': [
                    'organization_slug',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'organization_slug':
                        (str,),
                    'query':
                        (str,),
                    'include_public':
                        (bool,),
                },
                'attribute_map': {
                    'organization_slug': 'organizationSlug',
                    'query': 'query',
                    'include_public': 'includePublic',
                },
                'location_map': {
                    'organization_slug': 'path',
                    'query': 'query',
                    'include_public': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    '*/*'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_action
        )

        def __update_action(
            self,
            organization_slug,
            slug,
            action,
            **kwargs
        ):
            """update_action  # noqa: E501

            Update the current version object with given slug in the organization  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_action(organization_slug, slug, action, async_req=True)
            >>> result = thread.get()

            Args:
                organization_slug (str):
                slug (str):
                action (Action):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Action
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['organization_slug'] = \
                organization_slug
            kwargs['slug'] = \
                slug
            kwargs['action'] = \
                action
            return self.call_with_http_info(**kwargs)

        self.update_action = _Endpoint(
            settings={
                'response_type': (Action,),
                'auth': [],
                'endpoint_path': '/api/actions/{organizationSlug}/{slug}',
                'operation_id': 'update_action',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'organization_slug',
                    'slug',
                    'action',
                ],
                'required': [
                    'organization_slug',
                    'slug',
                    'action',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'organization_slug':
                        (str,),
                    'slug':
                        (str,),
                    'action':
                        (Action,),
                },
                'attribute_map': {
                    'organization_slug': 'organizationSlug',
                    'slug': 'slug',
                },
                'location_map': {
                    'organization_slug': 'path',
                    'slug': 'path',
                    'action': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    '*/*'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__update_action
        )

        def __update_version_action(
            self,
            organization_slug,
            slug,
            version,
            action,
            **kwargs
        ):
            """update_version_action  # noqa: E501

            Update the object with given slug and version in the organization  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_version_action(organization_slug, slug, version, action, async_req=True)
            >>> result = thread.get()

            Args:
                organization_slug (str):
                slug (str):
                version (str):
                action (Action):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Action
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['organization_slug'] = \
                organization_slug
            kwargs['slug'] = \
                slug
            kwargs['version'] = \
                version
            kwargs['action'] = \
                action
            return self.call_with_http_info(**kwargs)

        self.update_version_action = _Endpoint(
            settings={
                'response_type': (Action,),
                'auth': [],
                'endpoint_path': '/api/actions/{organizationSlug}/{slug}/{version}',
                'operation_id': 'update_version_action',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'organization_slug',
                    'slug',
                    'version',
                    'action',
                ],
                'required': [
                    'organization_slug',
                    'slug',
                    'version',
                    'action',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'organization_slug':
                        (str,),
                    'slug':
                        (str,),
                    'version':
                        (str,),
                    'action':
                        (Action,),
                },
                'attribute_map': {
                    'organization_slug': 'organizationSlug',
                    'slug': 'slug',
                    'version': 'version',
                },
                'location_map': {
                    'organization_slug': 'path',
                    'slug': 'path',
                    'version': 'path',
                    'action': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    '*/*'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__update_version_action
        )
