# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StructLogContents:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_content': 'str',
        'line_num': 'str'
    }

    attribute_map = {
        'log_content': 'log_content',
        'line_num': 'line_num'
    }

    def __init__(self, log_content=None, line_num=None):
        r"""StructLogContents

        The model defined in huaweicloud sdk

        :param log_content: 日志原数据。
        :type log_content: str
        :param line_num: 日志单行序列号。
        :type line_num: str
        """
        
        

        self._log_content = None
        self._line_num = None
        self.discriminator = None

        if log_content is not None:
            self.log_content = log_content
        if line_num is not None:
            self.line_num = line_num

    @property
    def log_content(self):
        r"""Gets the log_content of this StructLogContents.

        日志原数据。

        :return: The log_content of this StructLogContents.
        :rtype: str
        """
        return self._log_content

    @log_content.setter
    def log_content(self, log_content):
        r"""Sets the log_content of this StructLogContents.

        日志原数据。

        :param log_content: The log_content of this StructLogContents.
        :type log_content: str
        """
        self._log_content = log_content

    @property
    def line_num(self):
        r"""Gets the line_num of this StructLogContents.

        日志单行序列号。

        :return: The line_num of this StructLogContents.
        :rtype: str
        """
        return self._line_num

    @line_num.setter
    def line_num(self, line_num):
        r"""Sets the line_num of this StructLogContents.

        日志单行序列号。

        :param line_num: The line_num of this StructLogContents.
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
        if not isinstance(other, StructLogContents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
