# coding: utf-8

import pprint
import re

import six





class UserInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'user_num': 'int',
        'timestamp': 'str'
    }

    attribute_map = {
        'user_num': 'user_num',
        'timestamp': 'timestamp'
    }

    def __init__(self, user_num=None, timestamp=None):
        """UserInfo - a model defined in huaweicloud sdk"""
        
        

        self._user_num = None
        self._timestamp = None
        self.discriminator = None

        self.user_num = user_num
        self.timestamp = timestamp

    @property
    def user_num(self):
        """Gets the user_num of this UserInfo.

        直播流的在线人数

        :return: The user_num of this UserInfo.
        :rtype: int
        """
        return self._user_num

    @user_num.setter
    def user_num(self, user_num):
        """Sets the user_num of this UserInfo.

        直播流的在线人数

        :param user_num: The user_num of this UserInfo.
        :type: int
        """
        self._user_num = user_num

    @property
    def timestamp(self):
        """Gets the timestamp of this UserInfo.

        操作执行的时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ

        :return: The timestamp of this UserInfo.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this UserInfo.

        操作执行的时间，UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ

        :param timestamp: The timestamp of this UserInfo.
        :type: str
        """
        self._timestamp = timestamp

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
        if not isinstance(other, UserInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
