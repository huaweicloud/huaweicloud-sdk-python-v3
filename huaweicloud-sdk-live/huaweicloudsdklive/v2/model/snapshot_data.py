# coding: utf-8

import pprint
import re

import six





class SnapshotData:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'time': 'str'
    }

    attribute_map = {
        'count': 'count',
        'time': 'time'
    }

    def __init__(self, count=None, time=None):
        """SnapshotData - a model defined in huaweicloud sdk"""
        
        

        self._count = None
        self._time = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if time is not None:
            self.time = time

    @property
    def count(self):
        """Gets the count of this SnapshotData.

        每小时内截图总数，单位为张。

        :return: The count of this SnapshotData.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this SnapshotData.

        每小时内截图总数，单位为张。

        :param count: The count of this SnapshotData.
        :type: int
        """
        self._count = count

    @property
    def time(self):
        """Gets the time of this SnapshotData.

        采样时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ 。

        :return: The time of this SnapshotData.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this SnapshotData.

        采样时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ 。

        :param time: The time of this SnapshotData.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SnapshotData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
