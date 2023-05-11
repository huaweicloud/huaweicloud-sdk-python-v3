# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TableColumnStatisticsDescription:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'last_analyzed_time': 'datetime'
    }

    attribute_map = {
        'last_analyzed_time': 'last_analyzed_time'
    }

    def __init__(self, last_analyzed_time=None):
        """TableColumnStatisticsDescription

        The model defined in huaweicloud sdk

        :param last_analyzed_time: 最后统计时间
        :type last_analyzed_time: datetime
        """
        
        

        self._last_analyzed_time = None
        self.discriminator = None

        self.last_analyzed_time = last_analyzed_time

    @property
    def last_analyzed_time(self):
        """Gets the last_analyzed_time of this TableColumnStatisticsDescription.

        最后统计时间

        :return: The last_analyzed_time of this TableColumnStatisticsDescription.
        :rtype: datetime
        """
        return self._last_analyzed_time

    @last_analyzed_time.setter
    def last_analyzed_time(self, last_analyzed_time):
        """Sets the last_analyzed_time of this TableColumnStatisticsDescription.

        最后统计时间

        :param last_analyzed_time: The last_analyzed_time of this TableColumnStatisticsDescription.
        :type last_analyzed_time: datetime
        """
        self._last_analyzed_time = last_analyzed_time

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
        if not isinstance(other, TableColumnStatisticsDescription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
