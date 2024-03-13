# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogQuery:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_offset': 'int',
        'end_offset': 'int',
        'limit': 'int',
        'sort': 'str'
    }

    attribute_map = {
        'start_offset': 'start_offset',
        'end_offset': 'end_offset',
        'limit': 'limit',
        'sort': 'sort'
    }

    def __init__(self, start_offset=None, end_offset=None, limit=None, sort=None):
        """LogQuery

        The model defined in huaweicloud sdk

        :param start_offset: 日志起始偏移
        :type start_offset: int
        :param end_offset: 日志结束偏移
        :type end_offset: int
        :param limit: 最大日志行数
        :type limit: int
        :param sort: 排序规则[\&quot;asc\&quot;,\&quot;desc\&quot;]
        :type sort: str
        """
        
        

        self._start_offset = None
        self._end_offset = None
        self._limit = None
        self._sort = None
        self.discriminator = None

        if start_offset is not None:
            self.start_offset = start_offset
        if end_offset is not None:
            self.end_offset = end_offset
        self.limit = limit
        self.sort = sort

    @property
    def start_offset(self):
        """Gets the start_offset of this LogQuery.

        日志起始偏移

        :return: The start_offset of this LogQuery.
        :rtype: int
        """
        return self._start_offset

    @start_offset.setter
    def start_offset(self, start_offset):
        """Sets the start_offset of this LogQuery.

        日志起始偏移

        :param start_offset: The start_offset of this LogQuery.
        :type start_offset: int
        """
        self._start_offset = start_offset

    @property
    def end_offset(self):
        """Gets the end_offset of this LogQuery.

        日志结束偏移

        :return: The end_offset of this LogQuery.
        :rtype: int
        """
        return self._end_offset

    @end_offset.setter
    def end_offset(self, end_offset):
        """Sets the end_offset of this LogQuery.

        日志结束偏移

        :param end_offset: The end_offset of this LogQuery.
        :type end_offset: int
        """
        self._end_offset = end_offset

    @property
    def limit(self):
        """Gets the limit of this LogQuery.

        最大日志行数

        :return: The limit of this LogQuery.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this LogQuery.

        最大日志行数

        :param limit: The limit of this LogQuery.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort(self):
        """Gets the sort of this LogQuery.

        排序规则[\"asc\",\"desc\"]

        :return: The sort of this LogQuery.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this LogQuery.

        排序规则[\"asc\",\"desc\"]

        :param sort: The sort of this LogQuery.
        :type sort: str
        """
        self._sort = sort

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
        if not isinstance(other, LogQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
