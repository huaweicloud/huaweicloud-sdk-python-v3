# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmHandleHistoriesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'alarm_id': 'alarm_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, alarm_id=None, offset=None, limit=None):
        """ListAlarmHandleHistoriesRequest

        The model defined in huaweicloud sdk

        :param alarm_id: 告警id
        :type alarm_id: str
        :param offset: 偏移量
        :type offset: int
        :param limit: 每页限制数量
        :type limit: int
        """
        
        

        self._alarm_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.alarm_id = alarm_id
        self.offset = offset
        self.limit = limit

    @property
    def alarm_id(self):
        """Gets the alarm_id of this ListAlarmHandleHistoriesRequest.

        告警id

        :return: The alarm_id of this ListAlarmHandleHistoriesRequest.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        """Sets the alarm_id of this ListAlarmHandleHistoriesRequest.

        告警id

        :param alarm_id: The alarm_id of this ListAlarmHandleHistoriesRequest.
        :type alarm_id: str
        """
        self._alarm_id = alarm_id

    @property
    def offset(self):
        """Gets the offset of this ListAlarmHandleHistoriesRequest.

        偏移量

        :return: The offset of this ListAlarmHandleHistoriesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAlarmHandleHistoriesRequest.

        偏移量

        :param offset: The offset of this ListAlarmHandleHistoriesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListAlarmHandleHistoriesRequest.

        每页限制数量

        :return: The limit of this ListAlarmHandleHistoriesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAlarmHandleHistoriesRequest.

        每页限制数量

        :param limit: The limit of this ListAlarmHandleHistoriesRequest.
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
        if not isinstance(other, ListAlarmHandleHistoriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
