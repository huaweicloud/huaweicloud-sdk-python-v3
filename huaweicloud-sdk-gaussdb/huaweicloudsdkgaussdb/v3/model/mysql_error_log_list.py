# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlErrorLogList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'time': 'str',
        'level': 'str',
        'content': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'time': 'time',
        'level': 'level',
        'content': 'content'
    }

    def __init__(self, node_id=None, time=None, level=None, content=None):
        """MysqlErrorLogList

        The model defined in huaweicloud sdk

        :param node_id: 节点ID。
        :type node_id: str
        :param time: 日期时间UTC时间。
        :type time: str
        :param level: 日志级别。
        :type level: str
        :param content: 错误日志内容。
        :type content: str
        """
        
        

        self._node_id = None
        self._time = None
        self._level = None
        self._content = None
        self.discriminator = None

        if node_id is not None:
            self.node_id = node_id
        if time is not None:
            self.time = time
        if level is not None:
            self.level = level
        if content is not None:
            self.content = content

    @property
    def node_id(self):
        """Gets the node_id of this MysqlErrorLogList.

        节点ID。

        :return: The node_id of this MysqlErrorLogList.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this MysqlErrorLogList.

        节点ID。

        :param node_id: The node_id of this MysqlErrorLogList.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def time(self):
        """Gets the time of this MysqlErrorLogList.

        日期时间UTC时间。

        :return: The time of this MysqlErrorLogList.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this MysqlErrorLogList.

        日期时间UTC时间。

        :param time: The time of this MysqlErrorLogList.
        :type time: str
        """
        self._time = time

    @property
    def level(self):
        """Gets the level of this MysqlErrorLogList.

        日志级别。

        :return: The level of this MysqlErrorLogList.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this MysqlErrorLogList.

        日志级别。

        :param level: The level of this MysqlErrorLogList.
        :type level: str
        """
        self._level = level

    @property
    def content(self):
        """Gets the content of this MysqlErrorLogList.

        错误日志内容。

        :return: The content of this MysqlErrorLogList.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this MysqlErrorLogList.

        错误日志内容。

        :param content: The content of this MysqlErrorLogList.
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
        if not isinstance(other, MysqlErrorLogList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
