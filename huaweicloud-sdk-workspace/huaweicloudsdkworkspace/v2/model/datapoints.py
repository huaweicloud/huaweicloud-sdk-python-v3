# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Datapoints:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'average': 'float',
        'timestamp': 'int'
    }

    attribute_map = {
        'average': 'average',
        'timestamp': 'timestamp'
    }

    def __init__(self, average=None, timestamp=None):
        r"""Datapoints

        The model defined in huaweicloud sdk

        :param average: 平均数值。
        :type average: float
        :param timestamp: 时间戳。
        :type timestamp: int
        """
        
        

        self._average = None
        self._timestamp = None
        self.discriminator = None

        if average is not None:
            self.average = average
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def average(self):
        r"""Gets the average of this Datapoints.

        平均数值。

        :return: The average of this Datapoints.
        :rtype: float
        """
        return self._average

    @average.setter
    def average(self, average):
        r"""Sets the average of this Datapoints.

        平均数值。

        :param average: The average of this Datapoints.
        :type average: float
        """
        self._average = average

    @property
    def timestamp(self):
        r"""Gets the timestamp of this Datapoints.

        时间戳。

        :return: The timestamp of this Datapoints.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this Datapoints.

        时间戳。

        :param timestamp: The timestamp of this Datapoints.
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
        if not isinstance(other, Datapoints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
