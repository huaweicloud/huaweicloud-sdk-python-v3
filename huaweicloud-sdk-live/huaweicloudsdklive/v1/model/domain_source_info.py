# coding: utf-8

import pprint
import re

import six





class DomainSourceInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'protocol': 'str',
        'source_type': 'str',
        'sources': 'list[str]',
        'sources_priority': 'str'
    }

    attribute_map = {
        'protocol': 'protocol',
        'source_type': 'source_type',
        'sources': 'sources',
        'sources_priority': 'sources_priority'
    }

    def __init__(self, protocol=None, source_type=None, sources=None, sources_priority=None):
        """DomainSourceInfo - a model defined in huaweicloud sdk"""
        
        

        self._protocol = None
        self._source_type = None
        self._sources = None
        self._sources_priority = None
        self.discriminator = None

        if protocol is not None:
            self.protocol = protocol
        self.source_type = source_type
        if sources is not None:
            self.sources = sources
        if sources_priority is not None:
            self.sources_priority = sources_priority

    @property
    def protocol(self):
        """Gets the protocol of this DomainSourceInfo.

        回源、转推协议。

        :return: The protocol of this DomainSourceInfo.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this DomainSourceInfo.

        回源、转推协议。

        :param protocol: The protocol of this DomainSourceInfo.
        :type: str
        """
        self._protocol = protocol

    @property
    def source_type(self):
        """Gets the source_type of this DomainSourceInfo.

        源站地址类型

        :return: The source_type of this DomainSourceInfo.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this DomainSourceInfo.

        源站地址类型

        :param source_type: The source_type of this DomainSourceInfo.
        :type: str
        """
        self._source_type = source_type

    @property
    def sources(self):
        """Gets the sources of this DomainSourceInfo.

        回源、转推地址列表，格式为：{domain/IP}[:{port}]，port默认值为1935；最少1个，最多10个。

        :return: The sources of this DomainSourceInfo.
        :rtype: list[str]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this DomainSourceInfo.

        回源、转推地址列表，格式为：{domain/IP}[:{port}]，port默认值为1935；最少1个，最多10个。

        :param sources: The sources of this DomainSourceInfo.
        :type: list[str]
        """
        self._sources = sources

    @property
    def sources_priority(self):
        """Gets the sources_priority of this DomainSourceInfo.

        多个回源、转推地址的优先级。

        :return: The sources_priority of this DomainSourceInfo.
        :rtype: str
        """
        return self._sources_priority

    @sources_priority.setter
    def sources_priority(self, sources_priority):
        """Sets the sources_priority of this DomainSourceInfo.

        多个回源、转推地址的优先级。

        :param sources_priority: The sources_priority of this DomainSourceInfo.
        :type: str
        """
        self._sources_priority = sources_priority

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
        if not isinstance(other, DomainSourceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
