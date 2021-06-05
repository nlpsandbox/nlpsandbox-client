"""
    NLP Sandbox API

    NLP Sandbox REST API  # noqa: E501

    The version of the OpenAPI document: 1.1.2
    Contact: team@nlpsandbox.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from nlpsandbox.model_utils import (  # noqa: F401
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


class License(ModelSimple):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('value',): {
            'AFL-3.0': "afl-3.0",
            'APACHE-2.0': "apache-2.0",
            'ARTISTIC-2.0': "artistic-2.0",
            'BSL-1.0': "bsl-1.0",
            'BSD-2-CLAUSE': "bsd-2-clause",
            'BSD-3-CLAUSE': "bsd-3-clause",
            'BSD-3-CLAUSE-CLEAR': "bsd-3-clause-clear",
            'CC': "cc",
            'CC0-1.0': "cc0-1.0",
            'CC-BY-4.0': "cc-by-4.0",
            'CC-BY-SA-4.0': "cc-by-sa-4.0",
            'WTFPL': "wtfpl",
            'ECL-2.0': "ecl-2.0",
            'EPL-1.0': "epl-1.0",
            'EPL-2.0': "epl-2.0",
            'EUPL-1.1': "eupl-1.1",
            'AGPL-3.0': "agpl-3.0",
            'GPL': "gpl",
            'GPL-2.0': "gpl-2.0",
            'GPL-3.0': "gpl-3.0",
            'LGPL': "lgpl",
            'LGPL-2.1': "lgpl-2.1",
            'LGPL-3.0': "lgpl-3.0",
            'ISC': "isc",
            'LPPL-1.3C': "lppl-1.3c",
            'MS-PL': "ms-pl",
            'MIT': "mit",
            'MPL-2.0': "mpl-2.0",
            'OSL-3.0': "osl-3.0",
            'POSTGRESQL': "postgresql",
            'OFL-1.1': "ofl-1.1",
            'NCSA': "ncsa",
            'UNLICENSE': "unlicense",
            'ZLIB': "zlib",
            'NONE': "none",
        },
    }

    validations = {
    }

    additional_properties_type = None

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
        return {
            'value': (str,),
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {}

    _composed_schemas = None

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):
        """License - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str): The license (license keyword used by GitHub)., must be one of ["afl-3.0", "apache-2.0", "artistic-2.0", "bsl-1.0", "bsd-2-clause", "bsd-3-clause", "bsd-3-clause-clear", "cc", "cc0-1.0", "cc-by-4.0", "cc-by-sa-4.0", "wtfpl", "ecl-2.0", "epl-1.0", "epl-2.0", "eupl-1.1", "agpl-3.0", "gpl", "gpl-2.0", "gpl-3.0", "lgpl", "lgpl-2.1", "lgpl-3.0", "isc", "lppl-1.3c", "ms-pl", "mit", "mpl-2.0", "osl-3.0", "postgresql", "ofl-1.1", "ncsa", "unlicense", "zlib", "none", ]  # noqa: E501

        Keyword Args:
            value (str): The license (license keyword used by GitHub)., must be one of ["afl-3.0", "apache-2.0", "artistic-2.0", "bsl-1.0", "bsd-2-clause", "bsd-3-clause", "bsd-3-clause-clear", "cc", "cc0-1.0", "cc-by-4.0", "cc-by-sa-4.0", "wtfpl", "ecl-2.0", "epl-1.0", "epl-2.0", "eupl-1.1", "agpl-3.0", "gpl", "gpl-2.0", "gpl-3.0", "lgpl", "lgpl-2.1", "lgpl-3.0", "isc", "lppl-1.3c", "ms-pl", "mit", "mpl-2.0", "osl-3.0", "postgresql", "ofl-1.1", "ncsa", "unlicense", "zlib", "none", ]  # noqa: E501
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
        """
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
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
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )
