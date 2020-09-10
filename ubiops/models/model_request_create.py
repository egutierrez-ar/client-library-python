# coding: utf-8

"""
    UbiOps

    Client Library to interact with the UbiOps API.  # noqa: E501

    The version of the OpenAPI document: v2.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ubiops.configuration import Configuration


class ModelRequestCreate(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'model_input_field_1': 'str',
        'model_input_field_2': 'int'
    }

    attribute_map = {
        'model_input_field_1': 'model_input_field_1',
        'model_input_field_2': 'model_input_field_2'
    }

    def __init__(self, model_input_field_1=None, model_input_field_2=None, local_vars_configuration=None):  # noqa: E501
        """ModelRequestCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._model_input_field_1 = None
        self._model_input_field_2 = None
        self.discriminator = None

        if model_input_field_1 is not None:
            self.model_input_field_1 = model_input_field_1
        if model_input_field_2 is not None:
            self.model_input_field_2 = model_input_field_2

    @property
    def model_input_field_1(self):
        """Gets the model_input_field_1 of this ModelRequestCreate.  # noqa: E501


        :return: The model_input_field_1 of this ModelRequestCreate.  # noqa: E501
        :rtype: str
        """
        return self._model_input_field_1

    @model_input_field_1.setter
    def model_input_field_1(self, model_input_field_1):
        """Sets the model_input_field_1 of this ModelRequestCreate.


        :param model_input_field_1: The model_input_field_1 of this ModelRequestCreate.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                model_input_field_1 is not None and len(model_input_field_1) < 1):
            raise ValueError("Invalid value for `model_input_field_1`, length must be greater than or equal to `1`")  # noqa: E501

        self._model_input_field_1 = model_input_field_1

    @property
    def model_input_field_2(self):
        """Gets the model_input_field_2 of this ModelRequestCreate.  # noqa: E501


        :return: The model_input_field_2 of this ModelRequestCreate.  # noqa: E501
        :rtype: int
        """
        return self._model_input_field_2

    @model_input_field_2.setter
    def model_input_field_2(self, model_input_field_2):
        """Sets the model_input_field_2 of this ModelRequestCreate.


        :param model_input_field_2: The model_input_field_2 of this ModelRequestCreate.  # noqa: E501
        :type: int
        """

        self._model_input_field_2 = model_input_field_2

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ModelRequestCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelRequestCreate):
            return True

        return self.to_dict() != other.to_dict()
