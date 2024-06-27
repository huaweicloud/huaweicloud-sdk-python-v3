# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChInstancesInfoRsponseInstanceOpsWindow:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'period': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'period': 'period',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, period=None, start_time=None, end_time=None):
        """ChInstancesInfoRsponseInstanceOpsWindow

        The model defined in huaweicloud sdk

        :param period: 时间窗周期。
        :type period: str
        :param start_time: 时间窗开始时间。
        :type start_time: str
        :param end_time: 时间窗结束时间。
        :type end_time: str
        """
        
        

        self._period = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if period is not None:
            self.period = period
        self.start_time = start_time
        self.end_time = end_time

    @property
    def period(self):
        """Gets the period of this ChInstancesInfoRsponseInstanceOpsWindow.

        时间窗周期。

        :return: The period of this ChInstancesInfoRsponseInstanceOpsWindow.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ChInstancesInfoRsponseInstanceOpsWindow.

        时间窗周期。

        :param period: The period of this ChInstancesInfoRsponseInstanceOpsWindow.
        :type period: str
        """
        self._period = period

    @property
    def start_time(self):
        """Gets the start_time of this ChInstancesInfoRsponseInstanceOpsWindow.

        时间窗开始时间。

        :return: The start_time of this ChInstancesInfoRsponseInstanceOpsWindow.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ChInstancesInfoRsponseInstanceOpsWindow.

        时间窗开始时间。

        :param start_time: The start_time of this ChInstancesInfoRsponseInstanceOpsWindow.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ChInstancesInfoRsponseInstanceOpsWindow.

        时间窗结束时间。

        :return: The end_time of this ChInstancesInfoRsponseInstanceOpsWindow.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ChInstancesInfoRsponseInstanceOpsWindow.

        时间窗结束时间。

        :param end_time: The end_time of this ChInstancesInfoRsponseInstanceOpsWindow.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ChInstancesInfoRsponseInstanceOpsWindow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
