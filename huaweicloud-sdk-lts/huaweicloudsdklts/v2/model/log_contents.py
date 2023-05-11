# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogContents:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content': 'str',
        'line_num': 'str',
        'labels': 'dict(str, str)'
    }

    attribute_map = {
        'content': 'content',
        'line_num': 'line_num',
        'labels': 'labels'
    }

    def __init__(self, content=None, line_num=None, labels=None):
        """LogContents

        The model defined in huaweicloud sdk

        :param content: 日志原数据。
        :type content: str
        :param line_num: 日志单行序列号。
        :type line_num: str
        :param labels: 该条日志包含的 labels。
        :type labels: dict(str, str)
        """
        
        

        self._content = None
        self._line_num = None
        self._labels = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if line_num is not None:
            self.line_num = line_num
        if labels is not None:
            self.labels = labels

    @property
    def content(self):
        """Gets the content of this LogContents.

        日志原数据。

        :return: The content of this LogContents.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this LogContents.

        日志原数据。

        :param content: The content of this LogContents.
        :type content: str
        """
        self._content = content

    @property
    def line_num(self):
        """Gets the line_num of this LogContents.

        日志单行序列号。

        :return: The line_num of this LogContents.
        :rtype: str
        """
        return self._line_num

    @line_num.setter
    def line_num(self, line_num):
        """Sets the line_num of this LogContents.

        日志单行序列号。

        :param line_num: The line_num of this LogContents.
        :type line_num: str
        """
        self._line_num = line_num

    @property
    def labels(self):
        """Gets the labels of this LogContents.

        该条日志包含的 labels。

        :return: The labels of this LogContents.
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this LogContents.

        该条日志包含的 labels。

        :param labels: The labels of this LogContents.
        :type labels: dict(str, str)
        """
        self._labels = labels

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
        if not isinstance(other, LogContents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
