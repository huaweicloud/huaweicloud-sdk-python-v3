# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'level': 'int',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'level': 'level',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, level=None, offset=None, limit=None):
        r"""ListAlarmsRequest

        The model defined in huaweicloud sdk

        :param level: 告警级别 | 1 - 紧急 2 - 重要 3 - 次要 4 - 提示。
        :type level: int
        :param offset: 分页偏移量。
        :type offset: int
        :param limit: 分页大小，默认100。
        :type limit: int
        """
        
        

        self._level = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if level is not None:
            self.level = level
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def level(self):
        r"""Gets the level of this ListAlarmsRequest.

        告警级别 | 1 - 紧急 2 - 重要 3 - 次要 4 - 提示。

        :return: The level of this ListAlarmsRequest.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this ListAlarmsRequest.

        告警级别 | 1 - 紧急 2 - 重要 3 - 次要 4 - 提示。

        :param level: The level of this ListAlarmsRequest.
        :type level: int
        """
        self._level = level

    @property
    def offset(self):
        r"""Gets the offset of this ListAlarmsRequest.

        分页偏移量。

        :return: The offset of this ListAlarmsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAlarmsRequest.

        分页偏移量。

        :param offset: The offset of this ListAlarmsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAlarmsRequest.

        分页大小，默认100。

        :return: The limit of this ListAlarmsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAlarmsRequest.

        分页大小，默认100。

        :param limit: The limit of this ListAlarmsRequest.
        :type limit: int
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
        if not isinstance(other, ListAlarmsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
