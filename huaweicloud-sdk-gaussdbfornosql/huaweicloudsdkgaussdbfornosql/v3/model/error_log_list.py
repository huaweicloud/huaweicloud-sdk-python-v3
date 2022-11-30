# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ErrorLogList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_name': 'str',
        'level': 'str',
        'time': 'str',
        'content': 'str'
    }

    attribute_map = {
        'node_name': 'node_name',
        'level': 'level',
        'time': 'time',
        'content': 'content'
    }

    def __init__(self, node_name=None, level=None, time=None, content=None):
        """ErrorLogList

        The model defined in huaweicloud sdk

        :param node_name: 节点名称。
        :type node_name: str
        :param level: 日志级别。
        :type level: str
        :param time: 发生时间，UTC时间。
        :type time: str
        :param content: 日志内容。
        :type content: str
        """
        
        

        self._node_name = None
        self._level = None
        self._time = None
        self._content = None
        self.discriminator = None

        self.node_name = node_name
        self.level = level
        self.time = time
        self.content = content

    @property
    def node_name(self):
        """Gets the node_name of this ErrorLogList.

        节点名称。

        :return: The node_name of this ErrorLogList.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """Sets the node_name of this ErrorLogList.

        节点名称。

        :param node_name: The node_name of this ErrorLogList.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def level(self):
        """Gets the level of this ErrorLogList.

        日志级别。

        :return: The level of this ErrorLogList.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this ErrorLogList.

        日志级别。

        :param level: The level of this ErrorLogList.
        :type level: str
        """
        self._level = level

    @property
    def time(self):
        """Gets the time of this ErrorLogList.

        发生时间，UTC时间。

        :return: The time of this ErrorLogList.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ErrorLogList.

        发生时间，UTC时间。

        :param time: The time of this ErrorLogList.
        :type time: str
        """
        self._time = time

    @property
    def content(self):
        """Gets the content of this ErrorLogList.

        日志内容。

        :return: The content of this ErrorLogList.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ErrorLogList.

        日志内容。

        :param content: The content of this ErrorLogList.
        :type content: str
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
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ErrorLogList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
