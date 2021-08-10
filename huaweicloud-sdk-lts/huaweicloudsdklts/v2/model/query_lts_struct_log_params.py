# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryLTSStructLogParams:


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
        """QueryLTSStructLogParams - a model defined in huaweicloud sdk"""
        
        

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
        """Gets the start_time of this QueryLTSStructLogParams.

        搜索起始时间（UTC时间，毫秒级）。

        :return: The start_time of this QueryLTSStructLogParams.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this QueryLTSStructLogParams.

        搜索起始时间（UTC时间，毫秒级）。

        :param start_time: The start_time of this QueryLTSStructLogParams.
        :type: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this QueryLTSStructLogParams.

        搜索结束时间（UTC时间，毫秒级）。

        :return: The end_time of this QueryLTSStructLogParams.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this QueryLTSStructLogParams.

        搜索结束时间（UTC时间，毫秒级）。

        :param end_time: The end_time of this QueryLTSStructLogParams.
        :type: str
        """
        self._end_time = end_time

    @property
    def sql_expression(self):
        """Gets the sql_expression of this QueryLTSStructLogParams.

        支持SQL语句搜索， 目前支持\"GROUP BY\", \"LIKE\"和\"WHERE\"。

        :return: The sql_expression of this QueryLTSStructLogParams.
        :rtype: str
        """
        return self._sql_expression

    @sql_expression.setter
    def sql_expression(self, sql_expression):
        """Sets the sql_expression of this QueryLTSStructLogParams.

        支持SQL语句搜索， 目前支持\"GROUP BY\", \"LIKE\"和\"WHERE\"。

        :param sql_expression: The sql_expression of this QueryLTSStructLogParams.
        :type: str
        """
        self._sql_expression = sql_expression

    @property
    def original_content(self):
        """Gets the original_content of this QueryLTSStructLogParams.

        返回内容中是否包含原始日志， 默认为false。

        :return: The original_content of this QueryLTSStructLogParams.
        :rtype: bool
        """
        return self._original_content

    @original_content.setter
    def original_content(self, original_content):
        """Sets the original_content of this QueryLTSStructLogParams.

        返回内容中是否包含原始日志， 默认为false。

        :param original_content: The original_content of this QueryLTSStructLogParams.
        :type: bool
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
        if not isinstance(other, QueryLTSStructLogParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
