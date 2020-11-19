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


class ProjectResourceUsage(object):
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
        'deployments': 'int',
        'versions': 'int',
        'pipelines': 'int'
    }

    attribute_map = {
        'deployments': 'deployments',
        'versions': 'versions',
        'pipelines': 'pipelines'
    }

    def __init__(self, deployments=None, versions=None, pipelines=None, local_vars_configuration=None):  # noqa: E501
        """ProjectResourceUsage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._deployments = None
        self._versions = None
        self._pipelines = None
        self.discriminator = None

        if deployments is not None:
            self.deployments = deployments
        if versions is not None:
            self.versions = versions
        if pipelines is not None:
            self.pipelines = pipelines

    @property
    def deployments(self):
        """Gets the deployments of this ProjectResourceUsage.  # noqa: E501


        :return: The deployments of this ProjectResourceUsage.  # noqa: E501
        :rtype: int
        """
        return self._deployments

    @deployments.setter
    def deployments(self, deployments):
        """Sets the deployments of this ProjectResourceUsage.


        :param deployments: The deployments of this ProjectResourceUsage.  # noqa: E501
        :type: int
        """

        self._deployments = deployments

    @property
    def versions(self):
        """Gets the versions of this ProjectResourceUsage.  # noqa: E501


        :return: The versions of this ProjectResourceUsage.  # noqa: E501
        :rtype: int
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this ProjectResourceUsage.


        :param versions: The versions of this ProjectResourceUsage.  # noqa: E501
        :type: int
        """

        self._versions = versions

    @property
    def pipelines(self):
        """Gets the pipelines of this ProjectResourceUsage.  # noqa: E501


        :return: The pipelines of this ProjectResourceUsage.  # noqa: E501
        :rtype: int
        """
        return self._pipelines

    @pipelines.setter
    def pipelines(self, pipelines):
        """Sets the pipelines of this ProjectResourceUsage.


        :param pipelines: The pipelines of this ProjectResourceUsage.  # noqa: E501
        :type: int
        """

        self._pipelines = pipelines

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
        if not isinstance(other, ProjectResourceUsage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectResourceUsage):
            return True

        return self.to_dict() != other.to_dict()
