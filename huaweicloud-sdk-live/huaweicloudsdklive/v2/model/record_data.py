# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecordData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'concurrent_count': 'int',
        'time': 'str'
    }

    attribute_map = {
        'concurrent_count': 'concurrent_count',
        'time': 'time'
    }

    def __init__(self, concurrent_count=None, time=None):
        """RecordData

        The model defined in huaweicloud sdk

        :param concurrent_count: 最大并发路数。
        :type concurrent_count: int
        :param time: 采样时间，每小时内最大并发路数时间点。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ 。
        :type time: str
        """
        
        

        self._concurrent_count = None
        self._time = None
        self.discriminator = None

        if concurrent_count is not None:
            self.concurrent_count = concurrent_count
        if time is not None:
            self.time = time

    @property
    def concurrent_count(self):
        """Gets the concurrent_count of this RecordData.

        最大并发路数。

        :return: The concurrent_count of this RecordData.
        :rtype: int
        """
        return self._concurrent_count

    @concurrent_count.setter
    def concurrent_count(self, concurrent_count):
        """Sets the concurrent_count of this RecordData.

        最大并发路数。

        :param concurrent_count: The concurrent_count of this RecordData.
        :type concurrent_count: int
        """
        self._concurrent_count = concurrent_count

    @property
    def time(self):
        """Gets the time of this RecordData.

        采样时间，每小时内最大并发路数时间点。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ 。

        :return: The time of this RecordData.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this RecordData.

        采样时间，每小时内最大并发路数时间点。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ 。

        :param time: The time of this RecordData.
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
        if not isinstance(other, RecordData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
