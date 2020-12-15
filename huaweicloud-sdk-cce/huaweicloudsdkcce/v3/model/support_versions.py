# coding: utf-8

import pprint
import re

import six





class SupportVersions:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cluster_type': 'str',
        'cluster_version': 'list[str]'
    }

    attribute_map = {
        'cluster_type': 'clusterType',
        'cluster_version': 'clusterVersion'
    }

    def __init__(self, cluster_type=None, cluster_version=None):
        """SupportVersions - a model defined in huaweicloud sdk"""
        
        

        self._cluster_type = None
        self._cluster_version = None
        self.discriminator = None

        self.cluster_type = cluster_type
        self.cluster_version = cluster_version

    @property
    def cluster_type(self):
        """Gets the cluster_type of this SupportVersions.

        支持的集群类型

        :return: The cluster_type of this SupportVersions.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        """Sets the cluster_type of this SupportVersions.

        支持的集群类型

        :param cluster_type: The cluster_type of this SupportVersions.
        :type: str
        """
        self._cluster_type = cluster_type

    @property
    def cluster_version(self):
        """Gets the cluster_version of this SupportVersions.

        支持的集群版本（正则表达式）

        :return: The cluster_version of this SupportVersions.
        :rtype: list[str]
        """
        return self._cluster_version

    @cluster_version.setter
    def cluster_version(self, cluster_version):
        """Sets the cluster_version of this SupportVersions.

        支持的集群版本（正则表达式）

        :param cluster_version: The cluster_version of this SupportVersions.
        :type: list[str]
        """
        self._cluster_version = cluster_version

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
                if attr in self.sensitive_list:
                    result[attr] = "****"
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
        if not isinstance(other, SupportVersions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
