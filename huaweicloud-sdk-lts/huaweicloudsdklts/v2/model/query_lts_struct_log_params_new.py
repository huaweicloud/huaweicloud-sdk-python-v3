# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryLtsStructLogParamsNew:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'query': 'str',
        'format': 'str',
        'time_range': 'TimeRange',
        'whether_to_rows': 'bool'
    }

    attribute_map = {
        'query': 'query',
        'format': 'format',
        'time_range': 'time_range',
        'whether_to_rows': 'whether_to_rows'
    }

    def __init__(self, query=None, format=None, time_range=None, whether_to_rows=None):
        """QueryLtsStructLogParamsNew

        The model defined in huaweicloud sdk

        :param query: sql语句字符串。
        :type query: str
        :param format: 查询结果格式。当前仅支持：\&quot;k-v\&quot;。
        :type format: str
        :param time_range: 
        :type time_range: :class:`huaweicloudsdklts.v2.TimeRange`
        :param whether_to_rows: 返回数据格式，是否为行数据，默认为false。
        :type whether_to_rows: bool
        """
        
        

        self._query = None
        self._format = None
        self._time_range = None
        self._whether_to_rows = None
        self.discriminator = None

        self.query = query
        self.format = format
        self.time_range = time_range
        if whether_to_rows is not None:
            self.whether_to_rows = whether_to_rows

    @property
    def query(self):
        """Gets the query of this QueryLtsStructLogParamsNew.

        sql语句字符串。

        :return: The query of this QueryLtsStructLogParamsNew.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this QueryLtsStructLogParamsNew.

        sql语句字符串。

        :param query: The query of this QueryLtsStructLogParamsNew.
        :type query: str
        """
        self._query = query

    @property
    def format(self):
        """Gets the format of this QueryLtsStructLogParamsNew.

        查询结果格式。当前仅支持：\"k-v\"。

        :return: The format of this QueryLtsStructLogParamsNew.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this QueryLtsStructLogParamsNew.

        查询结果格式。当前仅支持：\"k-v\"。

        :param format: The format of this QueryLtsStructLogParamsNew.
        :type format: str
        """
        self._format = format

    @property
    def time_range(self):
        """Gets the time_range of this QueryLtsStructLogParamsNew.

        :return: The time_range of this QueryLtsStructLogParamsNew.
        :rtype: :class:`huaweicloudsdklts.v2.TimeRange`
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """Sets the time_range of this QueryLtsStructLogParamsNew.

        :param time_range: The time_range of this QueryLtsStructLogParamsNew.
        :type time_range: :class:`huaweicloudsdklts.v2.TimeRange`
        """
        self._time_range = time_range

    @property
    def whether_to_rows(self):
        """Gets the whether_to_rows of this QueryLtsStructLogParamsNew.

        返回数据格式，是否为行数据，默认为false。

        :return: The whether_to_rows of this QueryLtsStructLogParamsNew.
        :rtype: bool
        """
        return self._whether_to_rows

    @whether_to_rows.setter
    def whether_to_rows(self, whether_to_rows):
        """Sets the whether_to_rows of this QueryLtsStructLogParamsNew.

        返回数据格式，是否为行数据，默认为false。

        :param whether_to_rows: The whether_to_rows of this QueryLtsStructLogParamsNew.
        :type whether_to_rows: bool
        """
        self._whether_to_rows = whether_to_rows

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
        if not isinstance(other, QueryLtsStructLogParamsNew):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
