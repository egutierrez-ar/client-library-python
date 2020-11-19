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


class Logs(object):
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
        'id': 'str',
        'log': 'str',
        'date': 'str',
        'deployment_name': 'str',
        'version': 'str',
        'pipeline_name': 'str',
        'pipeline_object_name': 'str',
        'request_id': 'str',
        'pipeline_request_id': 'str',
        'system': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'log': 'log',
        'date': 'date',
        'deployment_name': 'deployment_name',
        'version': 'version',
        'pipeline_name': 'pipeline_name',
        'pipeline_object_name': 'pipeline_object_name',
        'request_id': 'request_id',
        'pipeline_request_id': 'pipeline_request_id',
        'system': 'system'
    }

    def __init__(self, id=None, log=None, date=None, deployment_name=None, version=None, pipeline_name=None, pipeline_object_name=None, request_id=None, pipeline_request_id=None, system=None, local_vars_configuration=None):  # noqa: E501
        """Logs - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._log = None
        self._date = None
        self._deployment_name = None
        self._version = None
        self._pipeline_name = None
        self._pipeline_object_name = None
        self._request_id = None
        self._pipeline_request_id = None
        self._system = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if log is not None:
            self.log = log
        if date is not None:
            self.date = date
        if deployment_name is not None:
            self.deployment_name = deployment_name
        if version is not None:
            self.version = version
        if pipeline_name is not None:
            self.pipeline_name = pipeline_name
        if pipeline_object_name is not None:
            self.pipeline_object_name = pipeline_object_name
        if request_id is not None:
            self.request_id = request_id
        if pipeline_request_id is not None:
            self.pipeline_request_id = pipeline_request_id
        if system is not None:
            self.system = system

    @property
    def id(self):
        """Gets the id of this Logs.  # noqa: E501


        :return: The id of this Logs.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Logs.


        :param id: The id of this Logs.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) < 1):
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def log(self):
        """Gets the log of this Logs.  # noqa: E501


        :return: The log of this Logs.  # noqa: E501
        :rtype: str
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this Logs.


        :param log: The log of this Logs.  # noqa: E501
        :type: str
        """

        self._log = log

    @property
    def date(self):
        """Gets the date of this Logs.  # noqa: E501


        :return: The date of this Logs.  # noqa: E501
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Logs.


        :param date: The date of this Logs.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                date is not None and len(date) < 1):
            raise ValueError("Invalid value for `date`, length must be greater than or equal to `1`")  # noqa: E501

        self._date = date

    @property
    def deployment_name(self):
        """Gets the deployment_name of this Logs.  # noqa: E501


        :return: The deployment_name of this Logs.  # noqa: E501
        :rtype: str
        """
        return self._deployment_name

    @deployment_name.setter
    def deployment_name(self, deployment_name):
        """Sets the deployment_name of this Logs.


        :param deployment_name: The deployment_name of this Logs.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                deployment_name is not None and len(deployment_name) < 1):
            raise ValueError("Invalid value for `deployment_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._deployment_name = deployment_name

    @property
    def version(self):
        """Gets the version of this Logs.  # noqa: E501


        :return: The version of this Logs.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Logs.


        :param version: The version of this Logs.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                version is not None and len(version) < 1):
            raise ValueError("Invalid value for `version`, length must be greater than or equal to `1`")  # noqa: E501

        self._version = version

    @property
    def pipeline_name(self):
        """Gets the pipeline_name of this Logs.  # noqa: E501


        :return: The pipeline_name of this Logs.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_name

    @pipeline_name.setter
    def pipeline_name(self, pipeline_name):
        """Sets the pipeline_name of this Logs.


        :param pipeline_name: The pipeline_name of this Logs.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                pipeline_name is not None and len(pipeline_name) < 1):
            raise ValueError("Invalid value for `pipeline_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._pipeline_name = pipeline_name

    @property
    def pipeline_object_name(self):
        """Gets the pipeline_object_name of this Logs.  # noqa: E501


        :return: The pipeline_object_name of this Logs.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_object_name

    @pipeline_object_name.setter
    def pipeline_object_name(self, pipeline_object_name):
        """Sets the pipeline_object_name of this Logs.


        :param pipeline_object_name: The pipeline_object_name of this Logs.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                pipeline_object_name is not None and len(pipeline_object_name) < 1):
            raise ValueError("Invalid value for `pipeline_object_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._pipeline_object_name = pipeline_object_name

    @property
    def request_id(self):
        """Gets the request_id of this Logs.  # noqa: E501


        :return: The request_id of this Logs.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this Logs.


        :param request_id: The request_id of this Logs.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def pipeline_request_id(self):
        """Gets the pipeline_request_id of this Logs.  # noqa: E501


        :return: The pipeline_request_id of this Logs.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_request_id

    @pipeline_request_id.setter
    def pipeline_request_id(self, pipeline_request_id):
        """Sets the pipeline_request_id of this Logs.


        :param pipeline_request_id: The pipeline_request_id of this Logs.  # noqa: E501
        :type: str
        """

        self._pipeline_request_id = pipeline_request_id

    @property
    def system(self):
        """Gets the system of this Logs.  # noqa: E501


        :return: The system of this Logs.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this Logs.


        :param system: The system of this Logs.  # noqa: E501
        :type: bool
        """

        self._system = system

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
        if not isinstance(other, Logs):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Logs):
            return True

        return self.to_dict() != other.to_dict()
