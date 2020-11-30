# coding: utf-8

import pprint
import re

import six





class Org:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'msp_id': 'str',
        'domain': 'str',
        'peers': 'dict(str, Node)'
    }

    attribute_map = {
        'msp_id': 'msp_id',
        'domain': 'domain',
        'peers': 'peers'
    }

    def __init__(self, msp_id=None, domain=None, peers=None):
        """Org - a model defined in huaweicloud sdk"""
        
        

        self._msp_id = None
        self._domain = None
        self._peers = None
        self.discriminator = None

        if msp_id is not None:
            self.msp_id = msp_id
        if domain is not None:
            self.domain = domain
        if peers is not None:
            self.peers = peers

    @property
    def msp_id(self):
        """Gets the msp_id of this Org.

        组织MSP标识

        :return: The msp_id of this Org.
        :rtype: str
        """
        return self._msp_id

    @msp_id.setter
    def msp_id(self, msp_id):
        """Sets the msp_id of this Org.

        组织MSP标识

        :param msp_id: The msp_id of this Org.
        :type: str
        """
        self._msp_id = msp_id

    @property
    def domain(self):
        """Gets the domain of this Org.

        组织域名

        :return: The domain of this Org.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this Org.

        组织域名

        :param domain: The domain of this Org.
        :type: str
        """
        self._domain = domain

    @property
    def peers(self):
        """Gets the peers of this Org.

        key:节点名称，value：节点详细信息

        :return: The peers of this Org.
        :rtype: dict(str, Node)
        """
        return self._peers

    @peers.setter
    def peers(self, peers):
        """Sets the peers of this Org.

        key:节点名称，value：节点详细信息

        :param peers: The peers of this Org.
        :type: dict(str, Node)
        """
        self._peers = peers

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
        if not isinstance(other, Org):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
