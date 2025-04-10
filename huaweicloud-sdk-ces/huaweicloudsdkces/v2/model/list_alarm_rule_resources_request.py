# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmRuleResourcesRequest:

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
        r"""ListAlarmRuleResourcesRequest

        The model defined in huaweicloud sdk

        :param alarm_id: Alarm实例ID
        :type alarm_id: str
        :param offset: 分页偏移量
        :type offset: int
        :param limit: 分页大小
        :type limit: int
        """
        
        

        self._alarm_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.alarm_id = alarm_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def alarm_id(self):
        r"""Gets the alarm_id of this ListAlarmRuleResourcesRequest.

        Alarm实例ID

        :return: The alarm_id of this ListAlarmRuleResourcesRequest.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        r"""Sets the alarm_id of this ListAlarmRuleResourcesRequest.

        Alarm实例ID

        :param alarm_id: The alarm_id of this ListAlarmRuleResourcesRequest.
        :type alarm_id: str
        """
        self._alarm_id = alarm_id

    @property
    def offset(self):
        r"""Gets the offset of this ListAlarmRuleResourcesRequest.

        分页偏移量

        :return: The offset of this ListAlarmRuleResourcesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAlarmRuleResourcesRequest.

        分页偏移量

        :param offset: The offset of this ListAlarmRuleResourcesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAlarmRuleResourcesRequest.

        分页大小

        :return: The limit of this ListAlarmRuleResourcesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAlarmRuleResourcesRequest.

        分页大小

        :param limit: The limit of this ListAlarmRuleResourcesRequest.
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
        if not isinstance(other, ListAlarmRuleResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
