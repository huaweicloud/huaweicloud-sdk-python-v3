# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryLtsStructLogParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'end_time': 'str',
        'sql_expression': 'str',
        'original_content': 'bool'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'sql_expression': 'sql_expression',
        'original_content': 'original_content'
    }

    def __init__(self, start_time=None, end_time=None, sql_expression=None, original_content=None):
        r"""QueryLtsStructLogParams

        The model defined in huaweicloud sdk

        :param start_time: 搜索起始时间（UTC时间，毫秒级）。
        :type start_time: str
        :param end_time: 搜索结束时间（UTC时间，毫秒级）。
        :type end_time: str
        :param sql_expression: 支持SQL语句搜索， 目前支持\&quot;GROUP BY\&quot;, \&quot;LIKE\&quot;和\&quot;WHERE\&quot;。
        :type sql_expression: str
        :param original_content: 返回内容中是否包含原始日志， 默认为false。
        :type original_content: bool
        """
        
        

        self._start_time = None
        self._end_time = None
        self._sql_expression = None
        self._original_content = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        if sql_expression is not None:
            self.sql_expression = sql_expression
        if original_content is not None:
            self.original_content = original_content

    @property
    def start_time(self):
        r"""Gets the start_time of this QueryLtsStructLogParams.

        搜索起始时间（UTC时间，毫秒级）。

        :return: The start_time of this QueryLtsStructLogParams.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this QueryLtsStructLogParams.

        搜索起始时间（UTC时间，毫秒级）。

        :param start_time: The start_time of this QueryLtsStructLogParams.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this QueryLtsStructLogParams.

        搜索结束时间（UTC时间，毫秒级）。

        :return: The end_time of this QueryLtsStructLogParams.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this QueryLtsStructLogParams.

        搜索结束时间（UTC时间，毫秒级）。

        :param end_time: The end_time of this QueryLtsStructLogParams.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def sql_expression(self):
        r"""Gets the sql_expression of this QueryLtsStructLogParams.

        支持SQL语句搜索， 目前支持\"GROUP BY\", \"LIKE\"和\"WHERE\"。

        :return: The sql_expression of this QueryLtsStructLogParams.
        :rtype: str
        """
        return self._sql_expression

    @sql_expression.setter
    def sql_expression(self, sql_expression):
        r"""Sets the sql_expression of this QueryLtsStructLogParams.

        支持SQL语句搜索， 目前支持\"GROUP BY\", \"LIKE\"和\"WHERE\"。

        :param sql_expression: The sql_expression of this QueryLtsStructLogParams.
        :type sql_expression: str
        """
        self._sql_expression = sql_expression

    @property
    def original_content(self):
        r"""Gets the original_content of this QueryLtsStructLogParams.

        返回内容中是否包含原始日志， 默认为false。

        :return: The original_content of this QueryLtsStructLogParams.
        :rtype: bool
        """
        return self._original_content

    @original_content.setter
    def original_content(self, original_content):
        r"""Sets the original_content of this QueryLtsStructLogParams.

        返回内容中是否包含原始日志， 默认为false。

        :param original_content: The original_content of this QueryLtsStructLogParams.
        :type original_content: bool
        """
        self._original_content = original_content

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
        if not isinstance(other, QueryLtsStructLogParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
