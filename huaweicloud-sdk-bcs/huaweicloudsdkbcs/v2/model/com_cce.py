# coding: utf-8

import pprint
import re

import six





class ComCCE:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cluster': 'Detail',
        'network': 'Detail',
        'security_group': 'Detail'
    }

    attribute_map = {
        'cluster': 'cluster',
        'network': 'network',
        'security_group': 'security_group'
    }

    def __init__(self, cluster=None, network=None, security_group=None):
        """ComCCE - a model defined in huaweicloud sdk"""
        
        

        self._cluster = None
        self._network = None
        self._security_group = None
        self.discriminator = None

        if cluster is not None:
            self.cluster = cluster
        if network is not None:
            self.network = network
        if security_group is not None:
            self.security_group = security_group

    @property
    def cluster(self):
        """Gets the cluster of this ComCCE.


        :return: The cluster of this ComCCE.
        :rtype: Detail
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this ComCCE.


        :param cluster: The cluster of this ComCCE.
        :type: Detail
        """
        self._cluster = cluster

    @property
    def network(self):
        """Gets the network of this ComCCE.


        :return: The network of this ComCCE.
        :rtype: Detail
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this ComCCE.


        :param network: The network of this ComCCE.
        :type: Detail
        """
        self._network = network

    @property
    def security_group(self):
        """Gets the security_group of this ComCCE.


        :return: The security_group of this ComCCE.
        :rtype: Detail
        """
        return self._security_group

    @security_group.setter
    def security_group(self, security_group):
        """Sets the security_group of this ComCCE.


        :param security_group: The security_group of this ComCCE.
        :type: Detail
        """
        self._security_group = security_group

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
        if not isinstance(other, ComCCE):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
