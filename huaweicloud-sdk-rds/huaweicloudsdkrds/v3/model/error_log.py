# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ErrorLog:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'time': 'str',
        'level': 'str',
        'content': 'str'
    }

    attribute_map = {
        'time': 'time',
        'level': 'level',
        'content': 'content'
    }

    def __init__(self, time=None, level=None, content=None):
        """ErrorLog - a model defined in huaweicloud sdk"""
        
        

        self._time = None
        self._level = None
        self._content = None
        self.discriminator = None

        self.time = time
        self.level = level
        self.content = content

    @property
    def time(self):
        """Gets the time of this ErrorLog.

        日期时间UTC时间。

        :return: The time of this ErrorLog.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ErrorLog.

        日期时间UTC时间。

        :param time: The time of this ErrorLog.
        :type: str
        """
        self._time = time

    @property
    def level(self):
        """Gets the level of this ErrorLog.

        日志级别。

        :return: The level of this ErrorLog.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this ErrorLog.

        日志级别。

        :param level: The level of this ErrorLog.
        :type: str
        """
        self._level = level

    @property
    def content(self):
        """Gets the content of this ErrorLog.

        错误日志内容。

        :return: The content of this ErrorLog.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ErrorLog.

        错误日志内容。

        :param content: The content of this ErrorLog.
        :type: str
        """
        self._content = content

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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ErrorLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
