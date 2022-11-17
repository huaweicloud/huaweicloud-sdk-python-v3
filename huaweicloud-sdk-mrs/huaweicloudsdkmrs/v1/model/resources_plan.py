# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourcesPlan:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'period_type': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'min_capacity': 'int',
        'max_capacity': 'int'
    }

    attribute_map = {
        'period_type': 'period_type',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'min_capacity': 'min_capacity',
        'max_capacity': 'max_capacity'
    }

    def __init__(self, period_type=None, start_time=None, end_time=None, min_capacity=None, max_capacity=None):
        """ResourcesPlan

        The model defined in huaweicloud sdk

        :param period_type: 资源计划的周期类型，当前只允许以下类型：  daily
        :type period_type: str
        :param start_time: 资源计划的起始时间，格式为“hour:minute”，表示时间在0:00-23:59之间。
        :type start_time: str
        :param end_time: 资源计划的结束时间，格式与“start_time”相同，不早于start_time表示的时间，且与start_time间隔不小于30min。
        :type end_time: str
        :param min_capacity: 资源计划内该节点组的最小保留节点数。  取值范围：[0～500]
        :type min_capacity: int
        :param max_capacity: 资源计划内该节点组的最大保留节点数。  取值范围：[0～500]
        :type max_capacity: int
        """
        
        

        self._period_type = None
        self._start_time = None
        self._end_time = None
        self._min_capacity = None
        self._max_capacity = None
        self.discriminator = None

        self.period_type = period_type
        self.start_time = start_time
        self.end_time = end_time
        self.min_capacity = min_capacity
        self.max_capacity = max_capacity

    @property
    def period_type(self):
        """Gets the period_type of this ResourcesPlan.

        资源计划的周期类型，当前只允许以下类型：  daily

        :return: The period_type of this ResourcesPlan.
        :rtype: str
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this ResourcesPlan.

        资源计划的周期类型，当前只允许以下类型：  daily

        :param period_type: The period_type of this ResourcesPlan.
        :type period_type: str
        """
        self._period_type = period_type

    @property
    def start_time(self):
        """Gets the start_time of this ResourcesPlan.

        资源计划的起始时间，格式为“hour:minute”，表示时间在0:00-23:59之间。

        :return: The start_time of this ResourcesPlan.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ResourcesPlan.

        资源计划的起始时间，格式为“hour:minute”，表示时间在0:00-23:59之间。

        :param start_time: The start_time of this ResourcesPlan.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ResourcesPlan.

        资源计划的结束时间，格式与“start_time”相同，不早于start_time表示的时间，且与start_time间隔不小于30min。

        :return: The end_time of this ResourcesPlan.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ResourcesPlan.

        资源计划的结束时间，格式与“start_time”相同，不早于start_time表示的时间，且与start_time间隔不小于30min。

        :param end_time: The end_time of this ResourcesPlan.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def min_capacity(self):
        """Gets the min_capacity of this ResourcesPlan.

        资源计划内该节点组的最小保留节点数。  取值范围：[0～500]

        :return: The min_capacity of this ResourcesPlan.
        :rtype: int
        """
        return self._min_capacity

    @min_capacity.setter
    def min_capacity(self, min_capacity):
        """Sets the min_capacity of this ResourcesPlan.

        资源计划内该节点组的最小保留节点数。  取值范围：[0～500]

        :param min_capacity: The min_capacity of this ResourcesPlan.
        :type min_capacity: int
        """
        self._min_capacity = min_capacity

    @property
    def max_capacity(self):
        """Gets the max_capacity of this ResourcesPlan.

        资源计划内该节点组的最大保留节点数。  取值范围：[0～500]

        :return: The max_capacity of this ResourcesPlan.
        :rtype: int
        """
        return self._max_capacity

    @max_capacity.setter
    def max_capacity(self, max_capacity):
        """Sets the max_capacity of this ResourcesPlan.

        资源计划内该节点组的最大保留节点数。  取值范围：[0～500]

        :param max_capacity: The max_capacity of this ResourcesPlan.
        :type max_capacity: int
        """
        self._max_capacity = max_capacity

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
        if not isinstance(other, ResourcesPlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
