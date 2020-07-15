# coding: utf-8

import pprint
import re

import six





class SourceInstanceBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'addrs': 'str',
        'password': 'str'
    }

    attribute_map = {
        'addrs': 'addrs',
        'password': 'password'
    }

    def __init__(self, addrs=None, password=None):
        """SourceInstanceBody - a model defined in huaweicloud sdk"""
        
        

        self._addrs = None
        self._password = None
        self.discriminator = None

        self.addrs = addrs
        if password is not None:
            self.password = password

    @property
    def addrs(self):
        """Gets the addrs of this SourceInstanceBody.

        Redis实例名称(source_instance信息中填写)。

        :return: The addrs of this SourceInstanceBody.
        :rtype: str
        """
        return self._addrs

    @addrs.setter
    def addrs(self, addrs):
        """Sets the addrs of this SourceInstanceBody.

        Redis实例名称(source_instance信息中填写)。

        :param addrs: The addrs of this SourceInstanceBody.
        :type: str
        """
        self._addrs = addrs

    @property
    def password(self):
        """Gets the password of this SourceInstanceBody.

        Redis密码，如果设置了密码，则必须填写。

        :return: The password of this SourceInstanceBody.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SourceInstanceBody.

        Redis密码，如果设置了密码，则必须填写。

        :param password: The password of this SourceInstanceBody.
        :type: str
        """
        self._password = password

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
        if not isinstance(other, SourceInstanceBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
