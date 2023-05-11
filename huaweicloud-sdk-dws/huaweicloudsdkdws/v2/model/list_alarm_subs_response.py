# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmSubsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'alarm_subscriptions': 'list[AlarmSubscriptionResponse]'
    }

    attribute_map = {
        'count': 'count',
        'alarm_subscriptions': 'alarm_subscriptions'
    }

    def __init__(self, count=None, alarm_subscriptions=None):
        """ListAlarmSubsResponse

        The model defined in huaweicloud sdk

        :param count: 告警订阅总数
        :type count: int
        :param alarm_subscriptions: 告警订阅列表
        :type alarm_subscriptions: list[:class:`huaweicloudsdkdws.v2.AlarmSubscriptionResponse`]
        """
        
        super(ListAlarmSubsResponse, self).__init__()

        self._count = None
        self._alarm_subscriptions = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if alarm_subscriptions is not None:
            self.alarm_subscriptions = alarm_subscriptions

    @property
    def count(self):
        """Gets the count of this ListAlarmSubsResponse.

        告警订阅总数

        :return: The count of this ListAlarmSubsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListAlarmSubsResponse.

        告警订阅总数

        :param count: The count of this ListAlarmSubsResponse.
        :type count: int
        """
        self._count = count

    @property
    def alarm_subscriptions(self):
        """Gets the alarm_subscriptions of this ListAlarmSubsResponse.

        告警订阅列表

        :return: The alarm_subscriptions of this ListAlarmSubsResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.AlarmSubscriptionResponse`]
        """
        return self._alarm_subscriptions

    @alarm_subscriptions.setter
    def alarm_subscriptions(self, alarm_subscriptions):
        """Sets the alarm_subscriptions of this ListAlarmSubsResponse.

        告警订阅列表

        :param alarm_subscriptions: The alarm_subscriptions of this ListAlarmSubsResponse.
        :type alarm_subscriptions: list[:class:`huaweicloudsdkdws.v2.AlarmSubscriptionResponse`]
        """
        self._alarm_subscriptions = alarm_subscriptions

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
        if not isinstance(other, ListAlarmSubsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
