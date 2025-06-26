# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlarmSubUpdateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'enable': 'int',
        'alarm_level': 'str',
        'notification_target': 'str',
        'notification_target_name': 'str',
        'notification_target_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'enable': 'enable',
        'alarm_level': 'alarm_level',
        'notification_target': 'notification_target',
        'notification_target_name': 'notification_target_name',
        'notification_target_type': 'notification_target_type'
    }

    def __init__(self, name=None, enable=None, alarm_level=None, notification_target=None, notification_target_name=None, notification_target_type=None):
        r"""AlarmSubUpdateRequest

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 告警订阅名称。 **取值范围**： 不涉及。
        :type name: str
        :param enable: **参数解释**： 是否开启订阅。 **取值范围**： 不涉及。
        :type enable: int
        :param alarm_level: **参数解释**： 告警级别。 **取值范围**： 不涉及。
        :type alarm_level: str
        :param notification_target: **参数解释**： 消息主题地址。 **取值范围**： 不涉及。
        :type notification_target: str
        :param notification_target_name: **参数解释**： 消息主题名称。 **取值范围**： 不涉及。
        :type notification_target_name: str
        :param notification_target_type: **参数解释**： 消息主题类型，支持SMN。 **取值范围**： 不涉及。
        :type notification_target_type: str
        """
        
        

        self._name = None
        self._enable = None
        self._alarm_level = None
        self._notification_target = None
        self._notification_target_name = None
        self._notification_target_type = None
        self.discriminator = None

        self.name = name
        if enable is not None:
            self.enable = enable
        if alarm_level is not None:
            self.alarm_level = alarm_level
        self.notification_target = notification_target
        self.notification_target_name = notification_target_name
        self.notification_target_type = notification_target_type

    @property
    def name(self):
        r"""Gets the name of this AlarmSubUpdateRequest.

        **参数解释**： 告警订阅名称。 **取值范围**： 不涉及。

        :return: The name of this AlarmSubUpdateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AlarmSubUpdateRequest.

        **参数解释**： 告警订阅名称。 **取值范围**： 不涉及。

        :param name: The name of this AlarmSubUpdateRequest.
        :type name: str
        """
        self._name = name

    @property
    def enable(self):
        r"""Gets the enable of this AlarmSubUpdateRequest.

        **参数解释**： 是否开启订阅。 **取值范围**： 不涉及。

        :return: The enable of this AlarmSubUpdateRequest.
        :rtype: int
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this AlarmSubUpdateRequest.

        **参数解释**： 是否开启订阅。 **取值范围**： 不涉及。

        :param enable: The enable of this AlarmSubUpdateRequest.
        :type enable: int
        """
        self._enable = enable

    @property
    def alarm_level(self):
        r"""Gets the alarm_level of this AlarmSubUpdateRequest.

        **参数解释**： 告警级别。 **取值范围**： 不涉及。

        :return: The alarm_level of this AlarmSubUpdateRequest.
        :rtype: str
        """
        return self._alarm_level

    @alarm_level.setter
    def alarm_level(self, alarm_level):
        r"""Sets the alarm_level of this AlarmSubUpdateRequest.

        **参数解释**： 告警级别。 **取值范围**： 不涉及。

        :param alarm_level: The alarm_level of this AlarmSubUpdateRequest.
        :type alarm_level: str
        """
        self._alarm_level = alarm_level

    @property
    def notification_target(self):
        r"""Gets the notification_target of this AlarmSubUpdateRequest.

        **参数解释**： 消息主题地址。 **取值范围**： 不涉及。

        :return: The notification_target of this AlarmSubUpdateRequest.
        :rtype: str
        """
        return self._notification_target

    @notification_target.setter
    def notification_target(self, notification_target):
        r"""Sets the notification_target of this AlarmSubUpdateRequest.

        **参数解释**： 消息主题地址。 **取值范围**： 不涉及。

        :param notification_target: The notification_target of this AlarmSubUpdateRequest.
        :type notification_target: str
        """
        self._notification_target = notification_target

    @property
    def notification_target_name(self):
        r"""Gets the notification_target_name of this AlarmSubUpdateRequest.

        **参数解释**： 消息主题名称。 **取值范围**： 不涉及。

        :return: The notification_target_name of this AlarmSubUpdateRequest.
        :rtype: str
        """
        return self._notification_target_name

    @notification_target_name.setter
    def notification_target_name(self, notification_target_name):
        r"""Sets the notification_target_name of this AlarmSubUpdateRequest.

        **参数解释**： 消息主题名称。 **取值范围**： 不涉及。

        :param notification_target_name: The notification_target_name of this AlarmSubUpdateRequest.
        :type notification_target_name: str
        """
        self._notification_target_name = notification_target_name

    @property
    def notification_target_type(self):
        r"""Gets the notification_target_type of this AlarmSubUpdateRequest.

        **参数解释**： 消息主题类型，支持SMN。 **取值范围**： 不涉及。

        :return: The notification_target_type of this AlarmSubUpdateRequest.
        :rtype: str
        """
        return self._notification_target_type

    @notification_target_type.setter
    def notification_target_type(self, notification_target_type):
        r"""Sets the notification_target_type of this AlarmSubUpdateRequest.

        **参数解释**： 消息主题类型，支持SMN。 **取值范围**： 不涉及。

        :param notification_target_type: The notification_target_type of this AlarmSubUpdateRequest.
        :type notification_target_type: str
        """
        self._notification_target_type = notification_target_type

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
        if not isinstance(other, AlarmSubUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
