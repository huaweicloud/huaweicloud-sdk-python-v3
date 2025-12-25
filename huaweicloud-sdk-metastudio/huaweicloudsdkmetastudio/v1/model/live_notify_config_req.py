# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LiveNotifyConfigReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'notify_events': 'list[str]'
    }

    attribute_map = {
        'action': 'action',
        'notify_events': 'notify_events'
    }

    def __init__(self, action=None, notify_events=None):
        r"""LiveNotifyConfigReq

        The model defined in huaweicloud sdk

        :param action: 确认操作。 * add: 增加。 * del: 删除。 * replace：替换。
        :type action: str
        :param notify_events: **参数解释**： 启用通知事件列表。 **约束限制**： 不涉及 **默认取值**： 无。
        :type notify_events: list[str]
        """
        
        

        self._action = None
        self._notify_events = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if notify_events is not None:
            self.notify_events = notify_events

    @property
    def action(self):
        r"""Gets the action of this LiveNotifyConfigReq.

        确认操作。 * add: 增加。 * del: 删除。 * replace：替换。

        :return: The action of this LiveNotifyConfigReq.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this LiveNotifyConfigReq.

        确认操作。 * add: 增加。 * del: 删除。 * replace：替换。

        :param action: The action of this LiveNotifyConfigReq.
        :type action: str
        """
        self._action = action

    @property
    def notify_events(self):
        r"""Gets the notify_events of this LiveNotifyConfigReq.

        **参数解释**： 启用通知事件列表。 **约束限制**： 不涉及 **默认取值**： 无。

        :return: The notify_events of this LiveNotifyConfigReq.
        :rtype: list[str]
        """
        return self._notify_events

    @notify_events.setter
    def notify_events(self, notify_events):
        r"""Sets the notify_events of this LiveNotifyConfigReq.

        **参数解释**： 启用通知事件列表。 **约束限制**： 不涉及 **默认取值**： 无。

        :param notify_events: The notify_events of this LiveNotifyConfigReq.
        :type notify_events: list[str]
        """
        self._notify_events = notify_events

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LiveNotifyConfigReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
