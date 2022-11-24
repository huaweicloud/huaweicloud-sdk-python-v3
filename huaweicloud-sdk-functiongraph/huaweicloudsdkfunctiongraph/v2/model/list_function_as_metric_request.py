# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFunctionAsMetricRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'limit': 'str'
    }

    attribute_map = {
        'type': 'type',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'limit': 'limit'
    }

    def __init__(self, type=None, start_time=None, end_time=None, limit=None):
        """ListFunctionAsMetricRequest

        The model defined in huaweicloud sdk

        :param type: 指标类型，默认值为failcount。
        :type type: str
        :param start_time: 起始时间。
        :type start_time: str
        :param end_time: 结束时间。
        :type end_time: str
        :param limit: 指标类型，默认值为failcount。
        :type limit: str
        """
        
        

        self._type = None
        self._start_time = None
        self._end_time = None
        self._limit = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if limit is not None:
            self.limit = limit

    @property
    def type(self):
        """Gets the type of this ListFunctionAsMetricRequest.

        指标类型，默认值为failcount。

        :return: The type of this ListFunctionAsMetricRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListFunctionAsMetricRequest.

        指标类型，默认值为failcount。

        :param type: The type of this ListFunctionAsMetricRequest.
        :type type: str
        """
        self._type = type

    @property
    def start_time(self):
        """Gets the start_time of this ListFunctionAsMetricRequest.

        起始时间。

        :return: The start_time of this ListFunctionAsMetricRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListFunctionAsMetricRequest.

        起始时间。

        :param start_time: The start_time of this ListFunctionAsMetricRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListFunctionAsMetricRequest.

        结束时间。

        :return: The end_time of this ListFunctionAsMetricRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListFunctionAsMetricRequest.

        结束时间。

        :param end_time: The end_time of this ListFunctionAsMetricRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def limit(self):
        """Gets the limit of this ListFunctionAsMetricRequest.

        指标类型，默认值为failcount。

        :return: The limit of this ListFunctionAsMetricRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListFunctionAsMetricRequest.

        指标类型，默认值为failcount。

        :param limit: The limit of this ListFunctionAsMetricRequest.
        :type limit: str
        """
        self._limit = limit

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
        if not isinstance(other, ListFunctionAsMetricRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
