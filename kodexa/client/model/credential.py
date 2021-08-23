"""
    Kodexa

    Rethink how you work with documents  # noqa: E501

    The version of the OpenAPI document: 4.0.179
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from kodexa.client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from kodexa.client.exceptions import ApiAttributeError


def lazy_import():
    from kodexa.client.model.credential_all_of import CredentialAllOf
    from kodexa.client.model.dashboard_row import DashboardRow
    from kodexa.client.model.metadata_tag import MetadataTag
    from kodexa.client.model.slug_based_metadata import SlugBasedMetadata
    globals()['CredentialAllOf'] = CredentialAllOf
    globals()['DashboardRow'] = DashboardRow
    globals()['MetadataTag'] = MetadataTag
    globals()['SlugBasedMetadata'] = SlugBasedMetadata


class Credential(ModelComposed):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('slug',): {
            'regex': {
                'pattern': r'^[a-zA-Z0-9\-_]{0,40}$',  # noqa: E501
            },
        },
        ('org_slug',): {
            'regex': {
                'pattern': r'^[a-zA-Z0-9\-_]{0,40}$',  # noqa: E501
            },
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'slug': (str,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'extension_pack_ref': (str,),  # noqa: E501
            'rows': ([DashboardRow],),  # noqa: E501
            'schema_version': (int,),  # noqa: E501
            'org_slug': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'version': (str,),  # noqa: E501
            'deployed': (datetime,),  # noqa: E501
            'public_access': (bool,),  # noqa: E501
            'ref': (str,),  # noqa: E501
            'url_of_image_for_assistant': (str,),  # noqa: E501
            'a_list_of_associated_tags': ([MetadataTag],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        val = {
        }
        if not val:
            return None
        return {'type': val}

    attribute_map = {
        'slug': 'slug',  # noqa: E501
        'type': 'type',  # noqa: E501
        'name': 'name',  # noqa: E501
        'extension_pack_ref': 'extensionPackRef',  # noqa: E501
        'rows': 'rows',  # noqa: E501
        'schema_version': 'schemaVersion',  # noqa: E501
        'org_slug': 'orgSlug',  # noqa: E501
        'description': 'description',  # noqa: E501
        'version': 'version',  # noqa: E501
        'deployed': 'deployed',  # noqa: E501
        'public_access': 'publicAccess',  # noqa: E501
        'ref': 'ref',  # noqa: E501
        'url_of_image_for_assistant': 'URL of image for assistant',  # noqa: E501
        'a_list_of_associated_tags': 'A list of associated tags',  # noqa: E501
    }

    read_only_vars = {
    }

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Credential - a model defined in OpenAPI

        Keyword Args:
            slug (str): The slug used when referencing this metadata object
            type (str): The type of metadata object
            name (str): The name of the object
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            extension_pack_ref (str): The reference to the extension pack (if the metadata object was created by an extension pack). [optional]  # noqa: E501
            rows ([DashboardRow]): [optional]  # noqa: E501
            schema_version (int): The version of the schema. [optional]  # noqa: E501
            org_slug (str): The slug of the organization that owns this metadata object. [optional]  # noqa: E501
            description (str): The description of the object. [optional]  # noqa: E501
            version (str): The version of the object. [optional]  # noqa: E501
            deployed (datetime): The date/time the object was deployed into this Kodexa instance. [optional]  # noqa: E501
            public_access (bool): Is the metadata object publicly accessible by other organizations. [optional]  # noqa: E501
            ref (str): The reference to the metadata object. [optional]  # noqa: E501
            url_of_image_for_assistant (str): [optional]  # noqa: E501
            a_list_of_associated_tags ([MetadataTag]): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)

        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
        '_composed_instances',
        '_var_name_to_model_instances',
        '_additional_properties_model_instances',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Credential - a model defined in OpenAPI

        Keyword Args:
            slug (str): The slug used when referencing this metadata object
            type (str): The type of metadata object
            name (str): The name of the object
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            extension_pack_ref (str): The reference to the extension pack (if the metadata object was created by an extension pack). [optional]  # noqa: E501
            rows ([DashboardRow]): [optional]  # noqa: E501
            schema_version (int): The version of the schema. [optional]  # noqa: E501
            org_slug (str): The slug of the organization that owns this metadata object. [optional]  # noqa: E501
            description (str): The description of the object. [optional]  # noqa: E501
            version (str): The version of the object. [optional]  # noqa: E501
            deployed (datetime): The date/time the object was deployed into this Kodexa instance. [optional]  # noqa: E501
            public_access (bool): Is the metadata object publicly accessible by other organizations. [optional]  # noqa: E501
            ref (str): The reference to the metadata object. [optional]  # noqa: E501
            url_of_image_for_assistant (str): [optional]  # noqa: E501
            a_list_of_associated_tags ([MetadataTag]): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        constant_args = {
            '_check_type': _check_type,
            '_path_to_item': _path_to_item,
            '_spec_property_naming': _spec_property_naming,
            '_configuration': _configuration,
            '_visited_composed_classes': self._visited_composed_classes,
        }
        composed_info = validate_get_composed_info(
            constant_args, kwargs, self)
        self._composed_instances = composed_info[0]
        self._var_name_to_model_instances = composed_info[1]
        self._additional_properties_model_instances = composed_info[2]
        discarded_args = composed_info[3]

        for var_name, var_value in kwargs.items():
            if var_name in discarded_args and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self._additional_properties_model_instances:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")

    @cached_property
    def _composed_schemas():
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error beause the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        lazy_import()
        return {
          'anyOf': [
          ],
          'allOf': [
              CredentialAllOf,
              SlugBasedMetadata,
          ],
          'oneOf': [
          ],
        }
