# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SpeedLimitInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'begin': 'str',
        'end': 'str',
        'speed': 'str'
    }

    attribute_map = {
        'begin': 'begin',
        'end': 'end',
        'speed': 'speed'
    }

    def __init__(self, begin=None, end=None, speed=None):
        """SpeedLimitInfo

        The model defined in huaweicloud sdk

        :param begin: 开始限速时间，此时间为UTC时间，开始时间为整时，若有分钟，则会忽略，格式为hh:mm，小时数为两位，例如：01:00。
        :type begin: str
        :param end: 结束时间，此时间为UTC时间，输入必须为59分结尾，格式为hh:mm，例如：15:59。
        :type end: str
        :param speed: 限速值，取值范围为1~9999，单位为MB/s。
        :type speed: str
        """
        
        

        self._begin = None
        self._end = None
        self._speed = None
        self.discriminator = None

        self.begin = begin
        self.end = end
        self.speed = speed

    @property
    def begin(self):
        """Gets the begin of this SpeedLimitInfo.

        开始限速时间，此时间为UTC时间，开始时间为整时，若有分钟，则会忽略，格式为hh:mm，小时数为两位，例如：01:00。

        :return: The begin of this SpeedLimitInfo.
        :rtype: str
        """
        return self._begin

    @begin.setter
    def begin(self, begin):
        """Sets the begin of this SpeedLimitInfo.

        开始限速时间，此时间为UTC时间，开始时间为整时，若有分钟，则会忽略，格式为hh:mm，小时数为两位，例如：01:00。

        :param begin: The begin of this SpeedLimitInfo.
        :type begin: str
        """
        self._begin = begin

    @property
    def end(self):
        """Gets the end of this SpeedLimitInfo.

        结束时间，此时间为UTC时间，输入必须为59分结尾，格式为hh:mm，例如：15:59。

        :return: The end of this SpeedLimitInfo.
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this SpeedLimitInfo.

        结束时间，此时间为UTC时间，输入必须为59分结尾，格式为hh:mm，例如：15:59。

        :param end: The end of this SpeedLimitInfo.
        :type end: str
        """
        self._end = end

    @property
    def speed(self):
        """Gets the speed of this SpeedLimitInfo.

        限速值，取值范围为1~9999，单位为MB/s。

        :return: The speed of this SpeedLimitInfo.
        :rtype: str
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this SpeedLimitInfo.

        限速值，取值范围为1~9999，单位为MB/s。

        :param speed: The speed of this SpeedLimitInfo.
        :type speed: str
        """
        self._speed = speed

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
        if not isinstance(other, SpeedLimitInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
