# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Timezones:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time_zone_desc': 'str',
        'time_zone': 'str',
        'time_zone_name': 'str',
        'time_zone_desc_us': 'str',
        'time_zone_desc_cn': 'str'
    }

    attribute_map = {
        'time_zone_desc': 'time_zone_desc',
        'time_zone': 'time_zone',
        'time_zone_name': 'time_zone_name',
        'time_zone_desc_us': 'time_zone_desc_us',
        'time_zone_desc_cn': 'time_zone_desc_cn'
    }

    def __init__(self, time_zone_desc=None, time_zone=None, time_zone_name=None, time_zone_desc_us=None, time_zone_desc_cn=None):
        r"""Timezones

        The model defined in huaweicloud sdk

        :param time_zone_desc: 时区描述。
        :type time_zone_desc: str
        :param time_zone: 时区偏移量。
        :type time_zone: str
        :param time_zone_name: 时区地名。
        :type time_zone_name: str
        :param time_zone_desc_us: 时区英文描述。
        :type time_zone_desc_us: str
        :param time_zone_desc_cn: 时区中文描述。
        :type time_zone_desc_cn: str
        """
        
        

        self._time_zone_desc = None
        self._time_zone = None
        self._time_zone_name = None
        self._time_zone_desc_us = None
        self._time_zone_desc_cn = None
        self.discriminator = None

        if time_zone_desc is not None:
            self.time_zone_desc = time_zone_desc
        if time_zone is not None:
            self.time_zone = time_zone
        if time_zone_name is not None:
            self.time_zone_name = time_zone_name
        if time_zone_desc_us is not None:
            self.time_zone_desc_us = time_zone_desc_us
        if time_zone_desc_cn is not None:
            self.time_zone_desc_cn = time_zone_desc_cn

    @property
    def time_zone_desc(self):
        r"""Gets the time_zone_desc of this Timezones.

        时区描述。

        :return: The time_zone_desc of this Timezones.
        :rtype: str
        """
        return self._time_zone_desc

    @time_zone_desc.setter
    def time_zone_desc(self, time_zone_desc):
        r"""Sets the time_zone_desc of this Timezones.

        时区描述。

        :param time_zone_desc: The time_zone_desc of this Timezones.
        :type time_zone_desc: str
        """
        self._time_zone_desc = time_zone_desc

    @property
    def time_zone(self):
        r"""Gets the time_zone of this Timezones.

        时区偏移量。

        :return: The time_zone of this Timezones.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this Timezones.

        时区偏移量。

        :param time_zone: The time_zone of this Timezones.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def time_zone_name(self):
        r"""Gets the time_zone_name of this Timezones.

        时区地名。

        :return: The time_zone_name of this Timezones.
        :rtype: str
        """
        return self._time_zone_name

    @time_zone_name.setter
    def time_zone_name(self, time_zone_name):
        r"""Sets the time_zone_name of this Timezones.

        时区地名。

        :param time_zone_name: The time_zone_name of this Timezones.
        :type time_zone_name: str
        """
        self._time_zone_name = time_zone_name

    @property
    def time_zone_desc_us(self):
        r"""Gets the time_zone_desc_us of this Timezones.

        时区英文描述。

        :return: The time_zone_desc_us of this Timezones.
        :rtype: str
        """
        return self._time_zone_desc_us

    @time_zone_desc_us.setter
    def time_zone_desc_us(self, time_zone_desc_us):
        r"""Sets the time_zone_desc_us of this Timezones.

        时区英文描述。

        :param time_zone_desc_us: The time_zone_desc_us of this Timezones.
        :type time_zone_desc_us: str
        """
        self._time_zone_desc_us = time_zone_desc_us

    @property
    def time_zone_desc_cn(self):
        r"""Gets the time_zone_desc_cn of this Timezones.

        时区中文描述。

        :return: The time_zone_desc_cn of this Timezones.
        :rtype: str
        """
        return self._time_zone_desc_cn

    @time_zone_desc_cn.setter
    def time_zone_desc_cn(self, time_zone_desc_cn):
        r"""Sets the time_zone_desc_cn of this Timezones.

        时区中文描述。

        :param time_zone_desc_cn: The time_zone_desc_cn of this Timezones.
        :type time_zone_desc_cn: str
        """
        self._time_zone_desc_cn = time_zone_desc_cn

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
        if not isinstance(other, Timezones):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
