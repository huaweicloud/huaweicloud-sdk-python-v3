# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmLevelInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_level': 'int',
        'alarm_number': 'int'
    }

    attribute_map = {
        'alarm_level': 'alarm_level',
        'alarm_number': 'alarm_number'
    }

    def __init__(self, alarm_level=None, alarm_number=None):
        r"""AlarmLevelInfo

        The model defined in huaweicloud sdk

        :param alarm_level: 告警级别
        :type alarm_level: int
        :param alarm_number: 告警数量
        :type alarm_number: int
        """
        
        

        self._alarm_level = None
        self._alarm_number = None
        self.discriminator = None

        if alarm_level is not None:
            self.alarm_level = alarm_level
        if alarm_number is not None:
            self.alarm_number = alarm_number

    @property
    def alarm_level(self):
        r"""Gets the alarm_level of this AlarmLevelInfo.

        告警级别

        :return: The alarm_level of this AlarmLevelInfo.
        :rtype: int
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        r"""Sets the alarm_level of this AlarmLevelInfo.

        告警级别

        :param alarm_level: The alarm_level of this AlarmLevelInfo.
        :type alarm_level: int
        """
        self._alarm_level = alarm_level

    @property
    def alarm_number(self):
        r"""Gets the alarm_number of this AlarmLevelInfo.

        告警数量

        :return: The alarm_number of this AlarmLevelInfo.
        :rtype: int
        """
        return self._alarm_number

    @alarm_number.setter
    def alarm_number(self, alarm_number):
        r"""Sets the alarm_number of this AlarmLevelInfo.

        告警数量

        :param alarm_number: The alarm_number of this AlarmLevelInfo.
        :type alarm_number: int
        """
        self._alarm_number = alarm_number

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
        if not isinstance(other, AlarmLevelInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
