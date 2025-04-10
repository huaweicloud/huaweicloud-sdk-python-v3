# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRangeQueryAomPromPostRequest:

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
        'start': 'str',
        'end': 'str',
        'step': 'str'
    }

    attribute_map = {
        'query': 'query',
        'start': 'start',
        'end': 'end',
        'step': 'step'
    }

    def __init__(self, query=None, start=None, end=None, step=None):
        r"""ListRangeQueryAomPromPostRequest

        The model defined in huaweicloud sdk

        :param query: PromQL表达式(参考https://prometheus.io/docs/prometheus/latest/querying/basics/)。
        :type query: str
        :param start: 起始时间戳(Unix时间戳格式，单位：秒）。
        :type start: str
        :param end: 结束时间戳(Unix时间戳格式，单位：秒）。
        :type end: str
        :param step: 查询时间步长，时间区内每step秒执行一次。
        :type step: str
        """
        
        

        self._query = None
        self._start = None
        self._end = None
        self._step = None
        self.discriminator = None

        self.query = query
        self.start = start
        self.end = end
        self.step = step

    @property
    def query(self):
        r"""Gets the query of this ListRangeQueryAomPromPostRequest.

        PromQL表达式(参考https://prometheus.io/docs/prometheus/latest/querying/basics/)。

        :return: The query of this ListRangeQueryAomPromPostRequest.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this ListRangeQueryAomPromPostRequest.

        PromQL表达式(参考https://prometheus.io/docs/prometheus/latest/querying/basics/)。

        :param query: The query of this ListRangeQueryAomPromPostRequest.
        :type query: str
        """
        self._query = query

    @property
    def start(self):
        r"""Gets the start of this ListRangeQueryAomPromPostRequest.

        起始时间戳(Unix时间戳格式，单位：秒）。

        :return: The start of this ListRangeQueryAomPromPostRequest.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this ListRangeQueryAomPromPostRequest.

        起始时间戳(Unix时间戳格式，单位：秒）。

        :param start: The start of this ListRangeQueryAomPromPostRequest.
        :type start: str
        """
        self._start = start

    @property
    def end(self):
        r"""Gets the end of this ListRangeQueryAomPromPostRequest.

        结束时间戳(Unix时间戳格式，单位：秒）。

        :return: The end of this ListRangeQueryAomPromPostRequest.
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        r"""Sets the end of this ListRangeQueryAomPromPostRequest.

        结束时间戳(Unix时间戳格式，单位：秒）。

        :param end: The end of this ListRangeQueryAomPromPostRequest.
        :type end: str
        """
        self._end = end

    @property
    def step(self):
        r"""Gets the step of this ListRangeQueryAomPromPostRequest.

        查询时间步长，时间区内每step秒执行一次。

        :return: The step of this ListRangeQueryAomPromPostRequest.
        :rtype: str
        """
        return self._step

    @step.setter
    def step(self, step):
        r"""Sets the step of this ListRangeQueryAomPromPostRequest.

        查询时间步长，时间区内每step秒执行一次。

        :param step: The step of this ListRangeQueryAomPromPostRequest.
        :type step: str
        """
        self._step = step

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
        if not isinstance(other, ListRangeQueryAomPromPostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
