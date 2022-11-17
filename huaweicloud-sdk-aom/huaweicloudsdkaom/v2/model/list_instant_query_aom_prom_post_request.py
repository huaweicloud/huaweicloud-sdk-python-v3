# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstantQueryAomPromPostRequest:

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
        'time': 'str'
    }

    attribute_map = {
        'query': 'query',
        'time': 'time'
    }

    def __init__(self, query=None, time=None):
        """ListInstantQueryAomPromPostRequest

        The model defined in huaweicloud sdk

        :param query: PromQL表达式(参考https://prometheus.io/docs/prometheus/latest/querying/basics/)。
        :type query: str
        :param time: 指定用于计算 PromQL 的时间戳，(Unix时间戳格式，单位：秒）。
        :type time: str
        """
        
        

        self._query = None
        self._time = None
        self.discriminator = None

        self.query = query
        if time is not None:
            self.time = time

    @property
    def query(self):
        """Gets the query of this ListInstantQueryAomPromPostRequest.

        PromQL表达式(参考https://prometheus.io/docs/prometheus/latest/querying/basics/)。

        :return: The query of this ListInstantQueryAomPromPostRequest.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this ListInstantQueryAomPromPostRequest.

        PromQL表达式(参考https://prometheus.io/docs/prometheus/latest/querying/basics/)。

        :param query: The query of this ListInstantQueryAomPromPostRequest.
        :type query: str
        """
        self._query = query

    @property
    def time(self):
        """Gets the time of this ListInstantQueryAomPromPostRequest.

        指定用于计算 PromQL 的时间戳，(Unix时间戳格式，单位：秒）。

        :return: The time of this ListInstantQueryAomPromPostRequest.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ListInstantQueryAomPromPostRequest.

        指定用于计算 PromQL 的时间戳，(Unix时间戳格式，单位：秒）。

        :param time: The time of this ListInstantQueryAomPromPostRequest.
        :type time: str
        """
        self._time = time

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
        if not isinstance(other, ListInstantQueryAomPromPostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
