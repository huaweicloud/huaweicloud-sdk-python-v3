# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Notification:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'notification_list': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'notification_list': 'notification_list'
    }

    def __init__(self, type=None, notification_list=None):
        """Notification

        The model defined in huaweicloud sdk

        :param type: 通知类型, notification代表通过SMN通知
        :type type: str
        :param notification_list: 告警状态发生变化时，被通知对象的列表。topicUrn可从SMN获取，具体操作请参考查询Topic列表。当type为notification时，notification_list列表不能为空。 说明：若alarm_action_enabled为true，对应的alarm_actions、ok_actions至少有一个不能为空。若alarm_actions、ok_actions同时存在时，notification_list值保持一致。
        :type notification_list: list[str]
        """
        
        

        self._type = None
        self._notification_list = None
        self.discriminator = None

        self.type = type
        self.notification_list = notification_list

    @property
    def type(self):
        """Gets the type of this Notification.

        通知类型, notification代表通过SMN通知

        :return: The type of this Notification.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Notification.

        通知类型, notification代表通过SMN通知

        :param type: The type of this Notification.
        :type type: str
        """
        self._type = type

    @property
    def notification_list(self):
        """Gets the notification_list of this Notification.

        告警状态发生变化时，被通知对象的列表。topicUrn可从SMN获取，具体操作请参考查询Topic列表。当type为notification时，notification_list列表不能为空。 说明：若alarm_action_enabled为true，对应的alarm_actions、ok_actions至少有一个不能为空。若alarm_actions、ok_actions同时存在时，notification_list值保持一致。

        :return: The notification_list of this Notification.
        :rtype: list[str]
        """
        return self._notification_list

    @notification_list.setter
    def notification_list(self, notification_list):
        """Sets the notification_list of this Notification.

        告警状态发生变化时，被通知对象的列表。topicUrn可从SMN获取，具体操作请参考查询Topic列表。当type为notification时，notification_list列表不能为空。 说明：若alarm_action_enabled为true，对应的alarm_actions、ok_actions至少有一个不能为空。若alarm_actions、ok_actions同时存在时，notification_list值保持一致。

        :param notification_list: The notification_list of this Notification.
        :type notification_list: list[str]
        """
        self._notification_list = notification_list

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
        if not isinstance(other, Notification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
