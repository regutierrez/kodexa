"""
    Kodexa

    Rethink how you work with documents  # noqa: E501

    The version of the OpenAPI document: ${git.build.version}
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
from kodexa.client.model.execution import Execution
from kodexa.client.model.page_execution import PageExecution
from kodexa.client.model.page_session import PageSession
from kodexa.client.model.query_context import QueryContext
from kodexa.client.model.session import Session
from kodexa.client.model.session_event import SessionEvent
from kodexa.client.model.session_store import SessionStore


class SessionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_execution(
            self,
            id,
            execution_id,
            **kwargs
        ):
            """get_execution  # noqa: E501

            Get the specified execution in the session  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_execution(id, execution_id, async_req=True)
            >>> result = thread.get()

            Args:
                id (str):
                execution_id (str):

            Keyword Args:
                x_access_token (str): [optional]
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
                Execution
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
            kwargs['id'] = \
                id
            kwargs['execution_id'] = \
                execution_id
            return self.call_with_http_info(**kwargs)

        self.get_execution = _Endpoint(
            settings={
                'response_type': (Execution,),
                'auth': [],
                'endpoint_path': '/api/sessions/{id}/executions/{executionId}',
                'operation_id': 'get_execution',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'execution_id',
                    'x_access_token',
                ],
                'required': [
                    'id',
                    'execution_id',
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
                    'id':
                        (str,),
                    'execution_id':
                        (str,),
                    'x_access_token':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'execution_id': 'executionId',
                    'x_access_token': 'x-access-token',
                },
                'location_map': {
                    'id': 'path',
                    'execution_id': 'path',
                    'x_access_token': 'header',
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
            callable=__get_execution
        )

        def __get_execution_store(
            self,
            session_id,
            store_id,
            execution_id,
            **kwargs
        ):
            """get_execution_store  # noqa: E501

            Get the data and structure of a session store  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_execution_store(session_id, store_id, execution_id, async_req=True)
            >>> result = thread.get()

            Args:
                session_id (str):
                store_id (str):
                execution_id (str):

            Keyword Args:
                x_access_token (str): [optional]
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
                SessionStore
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
            kwargs['session_id'] = \
                session_id
            kwargs['store_id'] = \
                store_id
            kwargs['execution_id'] = \
                execution_id
            return self.call_with_http_info(**kwargs)

        self.get_execution_store = _Endpoint(
            settings={
                'response_type': (SessionStore,),
                'auth': [],
                'endpoint_path': '/api/sessions/{sessionId}/executions/{executionId}/stores/{storeId}',
                'operation_id': 'get_execution_store',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'session_id',
                    'store_id',
                    'execution_id',
                    'x_access_token',
                ],
                'required': [
                    'session_id',
                    'store_id',
                    'execution_id',
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
                    'session_id':
                        (str,),
                    'store_id':
                        (str,),
                    'execution_id':
                        (str,),
                    'x_access_token':
                        (str,),
                },
                'attribute_map': {
                    'session_id': 'sessionId',
                    'store_id': 'storeId',
                    'execution_id': 'executionId',
                    'x_access_token': 'x-access-token',
                },
                'location_map': {
                    'session_id': 'path',
                    'store_id': 'path',
                    'execution_id': 'path',
                    'x_access_token': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_execution_store
        )

        def __get_session(
            self,
            x_access_token,
            session_id,
            **kwargs
        ):
            """get_session  # noqa: E501

            Get the specific session  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_session(x_access_token, session_id, async_req=True)
            >>> result = thread.get()

            Args:
                x_access_token (str):
                session_id (str):

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
                Session
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
            kwargs['x_access_token'] = \
                x_access_token
            kwargs['session_id'] = \
                session_id
            return self.call_with_http_info(**kwargs)

        self.get_session = _Endpoint(
            settings={
                'response_type': (Session,),
                'auth': [],
                'endpoint_path': '/api/sessions/{sessionId}',
                'operation_id': 'get_session',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_access_token',
                    'session_id',
                ],
                'required': [
                    'x_access_token',
                    'session_id',
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
                    'x_access_token':
                        (str,),
                    'session_id':
                        (str,),
                },
                'attribute_map': {
                    'x_access_token': 'x-access-token',
                    'session_id': 'sessionId',
                },
                'location_map': {
                    'x_access_token': 'header',
                    'session_id': 'path',
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
            callable=__get_session
        )

        def __list_executions(
            self,
            id,
            query_context,
            **kwargs
        ):
            """list_executions  # noqa: E501

            Gets paginated list of executions in the session  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_executions(id, query_context, async_req=True)
            >>> result = thread.get()

            Args:
                id (str):
                query_context (QueryContext):

            Keyword Args:
                x_access_token (str): [optional]
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
                PageExecution
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
            kwargs['id'] = \
                id
            kwargs['query_context'] = \
                query_context
            return self.call_with_http_info(**kwargs)

        self.list_executions = _Endpoint(
            settings={
                'response_type': (PageExecution,),
                'auth': [],
                'endpoint_path': '/api/sessions/{id}/executions',
                'operation_id': 'list_executions',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'query_context',
                    'x_access_token',
                ],
                'required': [
                    'id',
                    'query_context',
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
                    'id':
                        (str,),
                    'query_context':
                        (QueryContext,),
                    'x_access_token':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'query_context': 'queryContext',
                    'x_access_token': 'x-access-token',
                },
                'location_map': {
                    'id': 'path',
                    'query_context': 'query',
                    'x_access_token': 'header',
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
            callable=__list_executions
        )

        def __list_sessions(
            self,
            query_context,
            **kwargs
        ):
            """list_sessions  # noqa: E501

            Get a list of the sessions by access token  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_sessions(query_context, async_req=True)
            >>> result = thread.get()

            Args:
                query_context (QueryContext):

            Keyword Args:
                x_access_token (str): [optional]
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
                PageSession
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
            kwargs['query_context'] = \
                query_context
            return self.call_with_http_info(**kwargs)

        self.list_sessions = _Endpoint(
            settings={
                'response_type': (PageSession,),
                'auth': [],
                'endpoint_path': '/api/sessions',
                'operation_id': 'list_sessions',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'query_context',
                    'x_access_token',
                ],
                'required': [
                    'query_context',
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
                    'query_context':
                        (QueryContext,),
                    'x_access_token':
                        (str,),
                },
                'attribute_map': {
                    'query_context': 'queryContext',
                    'x_access_token': 'x-access-token',
                },
                'location_map': {
                    'query_context': 'query',
                    'x_access_token': 'header',
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
            callable=__list_sessions
        )

        def __process_event(
            self,
            x_access_token,
            session_id,
            session_event,
            **kwargs
        ):
            """process_event  # noqa: E501

            Pass, and process, a new event in the session  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.process_event(x_access_token, session_id, session_event, async_req=True)
            >>> result = thread.get()

            Args:
                x_access_token (str):
                session_id (str):
                session_event (SessionEvent):

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
                Execution
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
            kwargs['x_access_token'] = \
                x_access_token
            kwargs['session_id'] = \
                session_id
            kwargs['session_event'] = \
                session_event
            return self.call_with_http_info(**kwargs)

        self.process_event = _Endpoint(
            settings={
                'response_type': (Execution,),
                'auth': [],
                'endpoint_path': '/api/sessions/{sessionId}/events',
                'operation_id': 'process_event',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_access_token',
                    'session_id',
                    'session_event',
                ],
                'required': [
                    'x_access_token',
                    'session_id',
                    'session_event',
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
                    'x_access_token':
                        (str,),
                    'session_id':
                        (str,),
                    'session_event':
                        (SessionEvent,),
                },
                'attribute_map': {
                    'x_access_token': 'x-access-token',
                    'session_id': 'sessionId',
                },
                'location_map': {
                    'x_access_token': 'header',
                    'session_id': 'path',
                    'session_event': 'body',
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
            callable=__process_event
        )

        def __update_execution_store(
            self,
            session_id,
            store_id,
            execution_id,
            session_store,
            **kwargs
        ):
            """update_execution_store  # noqa: E501

            Update a execution-based store content  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_execution_store(session_id, store_id, execution_id, session_store, async_req=True)
            >>> result = thread.get()

            Args:
                session_id (str):
                store_id (str):
                execution_id (str):
                session_store (SessionStore):

            Keyword Args:
                x_access_token (str): [optional]
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
                SessionStore
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
            kwargs['session_id'] = \
                session_id
            kwargs['store_id'] = \
                store_id
            kwargs['execution_id'] = \
                execution_id
            kwargs['session_store'] = \
                session_store
            return self.call_with_http_info(**kwargs)

        self.update_execution_store = _Endpoint(
            settings={
                'response_type': (SessionStore,),
                'auth': [],
                'endpoint_path': '/api/sessions/{sessionId}/executions/{executionId}/stores/{storeId}',
                'operation_id': 'update_execution_store',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'session_id',
                    'store_id',
                    'execution_id',
                    'session_store',
                    'x_access_token',
                ],
                'required': [
                    'session_id',
                    'store_id',
                    'execution_id',
                    'session_store',
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
                    'session_id':
                        (str,),
                    'store_id':
                        (str,),
                    'execution_id':
                        (str,),
                    'session_store':
                        (SessionStore,),
                    'x_access_token':
                        (str,),
                },
                'attribute_map': {
                    'session_id': 'sessionId',
                    'store_id': 'storeId',
                    'execution_id': 'executionId',
                    'x_access_token': 'x-access-token',
                },
                'location_map': {
                    'session_id': 'path',
                    'store_id': 'path',
                    'execution_id': 'path',
                    'session_store': 'body',
                    'x_access_token': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__update_execution_store
        )
