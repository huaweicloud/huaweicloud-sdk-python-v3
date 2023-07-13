# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DesktopUsedInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'date': 'str',
        'use_time': 'str'
    }

    attribute_map = {
        'date': 'date',
        'use_time': 'use_time'
    }

    def __init__(self, date=None, use_time=None):
        """DesktopUsedInfo

        The model defined in huaweicloud sdk

        :param date: 日期，格式：yyyy-MM-dd（UTC时间）。
        :type date: str
        :param use_time: 总共在线时间单位:小时数（h）,精确到两位小数，如：1.32。
        :type use_time: str
        """
        
        

        self._date = None
        self._use_time = None
        self.discriminator = None

        if date is not None:
            self.date = date
        if use_time is not None:
            self.use_time = use_time

    @property
    def date(self):
        """Gets the date of this DesktopUsedInfo.

        日期，格式：yyyy-MM-dd（UTC时间）。

        :return: The date of this DesktopUsedInfo.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this DesktopUsedInfo.

        日期，格式：yyyy-MM-dd（UTC时间）。

        :param date: The date of this DesktopUsedInfo.
        :type date: str
        """
        self._date = date

    @property
    def use_time(self):
        """Gets the use_time of this DesktopUsedInfo.

        总共在线时间单位:小时数（h）,精确到两位小数，如：1.32。

        :return: The use_time of this DesktopUsedInfo.
        :rtype: str
        """
        return self._use_time

    @use_time.setter
    def use_time(self, use_time):
        """Sets the use_time of this DesktopUsedInfo.

        总共在线时间单位:小时数（h）,精确到两位小数，如：1.32。

        :param use_time: The use_time of this DesktopUsedInfo.
        :type use_time: str
        """
        self._use_time = use_time

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
        if not isinstance(other, DesktopUsedInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
