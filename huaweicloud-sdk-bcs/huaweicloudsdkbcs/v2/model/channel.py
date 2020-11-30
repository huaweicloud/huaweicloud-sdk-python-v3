# coding: utf-8

import pprint
import re

import six





class Channel:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'create_time': 'str',
        'peers': 'dict(str, list[str])'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'create_time': 'create_time',
        'peers': 'peers'
    }

    def __init__(self, name=None, description=None, create_time=None, peers=None):
        """Channel - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._description = None
        self._create_time = None
        self._peers = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if peers is not None:
            self.peers = peers

    @property
    def name(self):
        """Gets the name of this Channel.

        通道名

        :return: The name of this Channel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Channel.

        通道名

        :param name: The name of this Channel.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this Channel.

        通道细节描述

        :return: The description of this Channel.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Channel.

        通道细节描述

        :param description: The description of this Channel.
        :type: str
        """
        self._description = description

    @property
    def create_time(self):
        """Gets the create_time of this Channel.

        通道创建时间

        :return: The create_time of this Channel.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Channel.

        通道创建时间

        :param create_time: The create_time of this Channel.
        :type: str
        """
        self._create_time = create_time

    @property
    def peers(self):
        """Gets the peers of this Channel.

        key:组织名，value:节点名称列表

        :return: The peers of this Channel.
        :rtype: dict(str, list[str])
        """
        return self._peers

    @peers.setter
    def peers(self, peers):
        """Sets the peers of this Channel.

        key:组织名，value:节点名称列表

        :param peers: The peers of this Channel.
        :type: dict(str, list[str])
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
        if not isinstance(other, Channel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
