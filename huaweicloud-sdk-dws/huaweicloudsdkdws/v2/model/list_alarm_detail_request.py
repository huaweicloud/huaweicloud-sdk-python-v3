# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time_zone': 'str',
        'offset': 'str',
        'limit': 'str'
    }

    attribute_map = {
        'time_zone': 'time_zone',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, time_zone=None, offset=None, limit=None):
        r"""ListAlarmDetailRequest

        The model defined in huaweicloud sdk

        :param time_zone: 时区
        :type time_zone: str
        :param offset: 当前页
        :type offset: str
        :param limit: 总页数
        :type limit: str
        """
        
        

        self._time_zone = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.time_zone = time_zone
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def time_zone(self):
        r"""Gets the time_zone of this ListAlarmDetailRequest.

        时区

        :return: The time_zone of this ListAlarmDetailRequest.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        r"""Sets the time_zone of this ListAlarmDetailRequest.

        时区

        :param time_zone: The time_zone of this ListAlarmDetailRequest.
        :type time_zone: str
        """
        self._time_zone = time_zone

    @property
    def offset(self):
        r"""Gets the offset of this ListAlarmDetailRequest.

        当前页

        :return: The offset of this ListAlarmDetailRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAlarmDetailRequest.

        当前页

        :param offset: The offset of this ListAlarmDetailRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAlarmDetailRequest.

        总页数

        :return: The limit of this ListAlarmDetailRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAlarmDetailRequest.

        总页数

        :param limit: The limit of this ListAlarmDetailRequest.
        :type limit: str
        """
        self._limit = limit

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
        if not isinstance(other, ListAlarmDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
