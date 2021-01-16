# coding: utf-8

import pprint
import re

import six





class CreateRequestBodyCceClusterInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'cluster_name': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name'
    }

    def __init__(self, cluster_id=None, cluster_name=None):
        """CreateRequestBodyCceClusterInfo - a model defined in huaweicloud sdk"""
        
        

        self._cluster_id = None
        self._cluster_name = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name

    @property
    def cluster_id(self):
        """Gets the cluster_id of this CreateRequestBodyCceClusterInfo.

        集群ID

        :return: The cluster_id of this CreateRequestBodyCceClusterInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this CreateRequestBodyCceClusterInfo.

        集群ID

        :param cluster_id: The cluster_id of this CreateRequestBodyCceClusterInfo.
        :type: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        """Gets the cluster_name of this CreateRequestBodyCceClusterInfo.

        集群名称

        :return: The cluster_name of this CreateRequestBodyCceClusterInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this CreateRequestBodyCceClusterInfo.

        集群名称

        :param cluster_name: The cluster_name of this CreateRequestBodyCceClusterInfo.
        :type: str
        """
        self._cluster_name = cluster_name

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
        if not isinstance(other, CreateRequestBodyCceClusterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
