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


class PipelineRequestModelRequest(object):
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
        'request_id': 'str',
        'pipeline_object': 'str',
        'success': 'bool',
        'request_data': 'object',
        'result': 'object',
        'error_message': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'pipeline_object': 'pipeline_object',
        'success': 'success',
        'request_data': 'request_data',
        'result': 'result',
        'error_message': 'error_message'
    }

    def __init__(self, request_id=None, pipeline_object=None, success=None, request_data=None, result=None, error_message=None, local_vars_configuration=None):  # noqa: E501
        """PipelineRequestModelRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._request_id = None
        self._pipeline_object = None
        self._success = None
        self._request_data = None
        self._result = None
        self._error_message = None
        self.discriminator = None

        self.request_id = request_id
        self.pipeline_object = pipeline_object
        self.success = success
        self.request_data = request_data
        self.result = result
        self.error_message = error_message

    @property
    def request_id(self):
        """Gets the request_id of this PipelineRequestModelRequest.  # noqa: E501


        :return: The request_id of this PipelineRequestModelRequest.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this PipelineRequestModelRequest.


        :param request_id: The request_id of this PipelineRequestModelRequest.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def pipeline_object(self):
        """Gets the pipeline_object of this PipelineRequestModelRequest.  # noqa: E501


        :return: The pipeline_object of this PipelineRequestModelRequest.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_object

    @pipeline_object.setter
    def pipeline_object(self, pipeline_object):
        """Sets the pipeline_object of this PipelineRequestModelRequest.


        :param pipeline_object: The pipeline_object of this PipelineRequestModelRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and pipeline_object is None:  # noqa: E501
            raise ValueError("Invalid value for `pipeline_object`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                pipeline_object is not None and len(pipeline_object) < 1):
            raise ValueError("Invalid value for `pipeline_object`, length must be greater than or equal to `1`")  # noqa: E501

        self._pipeline_object = pipeline_object

    @property
    def success(self):
        """Gets the success of this PipelineRequestModelRequest.  # noqa: E501


        :return: The success of this PipelineRequestModelRequest.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this PipelineRequestModelRequest.


        :param success: The success of this PipelineRequestModelRequest.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and success is None:  # noqa: E501
            raise ValueError("Invalid value for `success`, must not be `None`")  # noqa: E501

        self._success = success

    @property
    def request_data(self):
        """Gets the request_data of this PipelineRequestModelRequest.  # noqa: E501


        :return: The request_data of this PipelineRequestModelRequest.  # noqa: E501
        :rtype: object
        """
        return self._request_data

    @request_data.setter
    def request_data(self, request_data):
        """Sets the request_data of this PipelineRequestModelRequest.


        :param request_data: The request_data of this PipelineRequestModelRequest.  # noqa: E501
        :type: object
        """

        self._request_data = request_data

    @property
    def result(self):
        """Gets the result of this PipelineRequestModelRequest.  # noqa: E501


        :return: The result of this PipelineRequestModelRequest.  # noqa: E501
        :rtype: object
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this PipelineRequestModelRequest.


        :param result: The result of this PipelineRequestModelRequest.  # noqa: E501
        :type: object
        """

        self._result = result

    @property
    def error_message(self):
        """Gets the error_message of this PipelineRequestModelRequest.  # noqa: E501


        :return: The error_message of this PipelineRequestModelRequest.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this PipelineRequestModelRequest.


        :param error_message: The error_message of this PipelineRequestModelRequest.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

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
        if not isinstance(other, PipelineRequestModelRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PipelineRequestModelRequest):
            return True

        return self.to_dict() != other.to_dict()
