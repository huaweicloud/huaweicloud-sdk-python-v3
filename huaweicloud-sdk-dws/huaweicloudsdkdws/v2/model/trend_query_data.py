# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrendQueryData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'str',
        'timestamp': 'int'
    }

    attribute_map = {
        'result': 'result',
        'timestamp': 'timestamp'
    }

    def __init__(self, result=None, timestamp=None):
        """TrendQueryData

        The model defined in huaweicloud sdk

        :param result: 查询结果。
        :type result: str
        :param timestamp: 时间戳。
        :type timestamp: int
        """
        
        

        self._result = None
        self._timestamp = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def result(self):
        """Gets the result of this TrendQueryData.

        查询结果。

        :return: The result of this TrendQueryData.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this TrendQueryData.

        查询结果。

        :param result: The result of this TrendQueryData.
        :type result: str
        """
        self._result = result

    @property
    def timestamp(self):
        """Gets the timestamp of this TrendQueryData.

        时间戳。

        :return: The timestamp of this TrendQueryData.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this TrendQueryData.

        时间戳。

        :param timestamp: The timestamp of this TrendQueryData.
        :type timestamp: int
        """
        self._timestamp = timestamp

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
        if not isinstance(other, TrendQueryData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
