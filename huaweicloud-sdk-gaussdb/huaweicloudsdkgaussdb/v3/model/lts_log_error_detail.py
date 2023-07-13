# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LtsLogErrorDetail:

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
        'content': 'str',
        'line_num': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'time': 'time',
        'level': 'level',
        'content': 'content',
        'line_num': 'line_num'
    }

    def __init__(self, node_id=None, time=None, level=None, content=None, line_num=None):
        """LtsLogErrorDetail

        The model defined in huaweicloud sdk

        :param node_id: 节点ID。
        :type node_id: str
        :param time: 执行时间。
        :type time: str
        :param level: 日志级别。
        :type level: str
        :param content: 错误日志内容。
        :type content: str
        :param line_num: 日志单行序列号。
        :type line_num: str
        """
        
        

        self._node_id = None
        self._time = None
        self._level = None
        self._content = None
        self._line_num = None
        self.discriminator = None

        if node_id is not None:
            self.node_id = node_id
        if time is not None:
            self.time = time
        if level is not None:
            self.level = level
        if content is not None:
            self.content = content
        if line_num is not None:
            self.line_num = line_num

    @property
    def node_id(self):
        """Gets the node_id of this LtsLogErrorDetail.

        节点ID。

        :return: The node_id of this LtsLogErrorDetail.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this LtsLogErrorDetail.

        节点ID。

        :param node_id: The node_id of this LtsLogErrorDetail.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def time(self):
        """Gets the time of this LtsLogErrorDetail.

        执行时间。

        :return: The time of this LtsLogErrorDetail.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this LtsLogErrorDetail.

        执行时间。

        :param time: The time of this LtsLogErrorDetail.
        :type time: str
        """
        self._time = time

    @property
    def level(self):
        """Gets the level of this LtsLogErrorDetail.

        日志级别。

        :return: The level of this LtsLogErrorDetail.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this LtsLogErrorDetail.

        日志级别。

        :param level: The level of this LtsLogErrorDetail.
        :type level: str
        """
        self._level = level

    @property
    def content(self):
        """Gets the content of this LtsLogErrorDetail.

        错误日志内容。

        :return: The content of this LtsLogErrorDetail.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this LtsLogErrorDetail.

        错误日志内容。

        :param content: The content of this LtsLogErrorDetail.
        :type content: str
        """
        self._content = content

    @property
    def line_num(self):
        """Gets the line_num of this LtsLogErrorDetail.

        日志单行序列号。

        :return: The line_num of this LtsLogErrorDetail.
        :rtype: str
        """
        return self._line_num

    @line_num.setter
    def line_num(self, line_num):
        """Sets the line_num of this LtsLogErrorDetail.

        日志单行序列号。

        :param line_num: The line_num of this LtsLogErrorDetail.
        :type line_num: str
        """
        self._line_num = line_num

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
        if not isinstance(other, LtsLogErrorDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
