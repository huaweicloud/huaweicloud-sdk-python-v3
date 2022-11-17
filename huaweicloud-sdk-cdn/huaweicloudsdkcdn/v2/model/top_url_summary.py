# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopUrlSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'value': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'stat_type': 'str'
    }

    attribute_map = {
        'url': 'url',
        'value': 'value',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'stat_type': 'stat_type'
    }

    def __init__(self, url=None, value=None, start_time=None, end_time=None, stat_type=None):
        """TopUrlSummary

        The model defined in huaweicloud sdk

        :param url: URL名称。
        :type url: str
        :param value: 对应查询类型的值。（流量单位：Byte）
        :type value: int
        :param start_time: 查询起始时间戳。
        :type start_time: int
        :param end_time: 查询结束时间戳
        :type end_time: int
        :param stat_type: 参数类型支持：flux(流量)，req_num(请求总数)。
        :type stat_type: str
        """
        
        

        self._url = None
        self._value = None
        self._start_time = None
        self._end_time = None
        self._stat_type = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if value is not None:
            self.value = value
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if stat_type is not None:
            self.stat_type = stat_type

    @property
    def url(self):
        """Gets the url of this TopUrlSummary.

        URL名称。

        :return: The url of this TopUrlSummary.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this TopUrlSummary.

        URL名称。

        :param url: The url of this TopUrlSummary.
        :type url: str
        """
        self._url = url

    @property
    def value(self):
        """Gets the value of this TopUrlSummary.

        对应查询类型的值。（流量单位：Byte）

        :return: The value of this TopUrlSummary.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TopUrlSummary.

        对应查询类型的值。（流量单位：Byte）

        :param value: The value of this TopUrlSummary.
        :type value: int
        """
        self._value = value

    @property
    def start_time(self):
        """Gets the start_time of this TopUrlSummary.

        查询起始时间戳。

        :return: The start_time of this TopUrlSummary.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this TopUrlSummary.

        查询起始时间戳。

        :param start_time: The start_time of this TopUrlSummary.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this TopUrlSummary.

        查询结束时间戳

        :return: The end_time of this TopUrlSummary.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this TopUrlSummary.

        查询结束时间戳

        :param end_time: The end_time of this TopUrlSummary.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def stat_type(self):
        """Gets the stat_type of this TopUrlSummary.

        参数类型支持：flux(流量)，req_num(请求总数)。

        :return: The stat_type of this TopUrlSummary.
        :rtype: str
        """
        return self._stat_type

    @stat_type.setter
    def stat_type(self, stat_type):
        """Sets the stat_type of this TopUrlSummary.

        参数类型支持：flux(流量)，req_num(请求总数)。

        :param stat_type: The stat_type of this TopUrlSummary.
        :type stat_type: str
        """
        self._stat_type = stat_type

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
        if not isinstance(other, TopUrlSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
