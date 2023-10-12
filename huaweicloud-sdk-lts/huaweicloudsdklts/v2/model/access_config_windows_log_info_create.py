# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessConfigWindowsLogInfoCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'categorys': 'list[str]',
        'time_offset': 'AccessConfigTimeOffset',
        'event_level': 'list[str]'
    }

    attribute_map = {
        'categorys': 'categorys',
        'time_offset': 'time_offset',
        'event_level': 'event_level'
    }

    def __init__(self, categorys=None, time_offset=None, event_level=None):
        """AccessConfigWindowsLogInfoCreate

        The model defined in huaweicloud sdk

        :param categorys: 采集Windows事件日志类型。Application：应用系统，System：系统，Security：安全，Setup：启动
        :type categorys: list[str]
        :param time_offset: 
        :type time_offset: :class:`huaweicloudsdklts.v2.AccessConfigTimeOffset`
        :param event_level: 事件等级。information：info，warning：告警，error：错误，critical：关键，verbose：冗长
        :type event_level: list[str]
        """
        
        

        self._categorys = None
        self._time_offset = None
        self._event_level = None
        self.discriminator = None

        self.categorys = categorys
        self.time_offset = time_offset
        self.event_level = event_level

    @property
    def categorys(self):
        """Gets the categorys of this AccessConfigWindowsLogInfoCreate.

        采集Windows事件日志类型。Application：应用系统，System：系统，Security：安全，Setup：启动

        :return: The categorys of this AccessConfigWindowsLogInfoCreate.
        :rtype: list[str]
        """
        return self._categorys

    @categorys.setter
    def categorys(self, categorys):
        """Sets the categorys of this AccessConfigWindowsLogInfoCreate.

        采集Windows事件日志类型。Application：应用系统，System：系统，Security：安全，Setup：启动

        :param categorys: The categorys of this AccessConfigWindowsLogInfoCreate.
        :type categorys: list[str]
        """
        self._categorys = categorys

    @property
    def time_offset(self):
        """Gets the time_offset of this AccessConfigWindowsLogInfoCreate.

        :return: The time_offset of this AccessConfigWindowsLogInfoCreate.
        :rtype: :class:`huaweicloudsdklts.v2.AccessConfigTimeOffset`
        """
        return self._time_offset

    @time_offset.setter
    def time_offset(self, time_offset):
        """Sets the time_offset of this AccessConfigWindowsLogInfoCreate.

        :param time_offset: The time_offset of this AccessConfigWindowsLogInfoCreate.
        :type time_offset: :class:`huaweicloudsdklts.v2.AccessConfigTimeOffset`
        """
        self._time_offset = time_offset

    @property
    def event_level(self):
        """Gets the event_level of this AccessConfigWindowsLogInfoCreate.

        事件等级。information：info，warning：告警，error：错误，critical：关键，verbose：冗长

        :return: The event_level of this AccessConfigWindowsLogInfoCreate.
        :rtype: list[str]
        """
        return self._event_level

    @event_level.setter
    def event_level(self, event_level):
        """Sets the event_level of this AccessConfigWindowsLogInfoCreate.

        事件等级。information：info，warning：告警，error：错误，critical：关键，verbose：冗长

        :param event_level: The event_level of this AccessConfigWindowsLogInfoCreate.
        :type event_level: list[str]
        """
        self._event_level = event_level

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
        if not isinstance(other, AccessConfigWindowsLogInfoCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
