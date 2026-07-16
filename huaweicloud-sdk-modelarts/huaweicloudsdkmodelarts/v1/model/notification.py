# coding: utf-8

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
        'topic_urn': 'str',
        'events': 'list[str]'
    }

    attribute_map = {
        'topic_urn': 'topic_urn',
        'events': 'events'
    }

    def __init__(self, topic_urn=None, events=None):
        r"""Notification

        The model defined in huaweicloud sdk

        :param topic_urn: **参数解释**：消息通知服务中所选主题的URN唯一资源标识。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type topic_urn: str
        :param events: **参数解释**：触发消息通知的训练事件。 **约束限制**：枚举值： - JobStarted：作业开始 - JobCompleted：作业结束 - JobFailed：作业失败 - JobTerminated：作业终止 - JobRestarted：作业重启 - JobHanged：作业卡死 - JobPreempted：作业抢占
        :type events: list[str]
        """
        
        

        self._topic_urn = None
        self._events = None
        self.discriminator = None

        if topic_urn is not None:
            self.topic_urn = topic_urn
        if events is not None:
            self.events = events

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this Notification.

        **参数解释**：消息通知服务中所选主题的URN唯一资源标识。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The topic_urn of this Notification.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this Notification.

        **参数解释**：消息通知服务中所选主题的URN唯一资源标识。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param topic_urn: The topic_urn of this Notification.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def events(self):
        r"""Gets the events of this Notification.

        **参数解释**：触发消息通知的训练事件。 **约束限制**：枚举值： - JobStarted：作业开始 - JobCompleted：作业结束 - JobFailed：作业失败 - JobTerminated：作业终止 - JobRestarted：作业重启 - JobHanged：作业卡死 - JobPreempted：作业抢占

        :return: The events of this Notification.
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        r"""Sets the events of this Notification.

        **参数解释**：触发消息通知的训练事件。 **约束限制**：枚举值： - JobStarted：作业开始 - JobCompleted：作业结束 - JobFailed：作业失败 - JobTerminated：作业终止 - JobRestarted：作业重启 - JobHanged：作业卡死 - JobPreempted：作业抢占

        :param events: The events of this Notification.
        :type events: list[str]
        """
        self._events = events

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
        if not isinstance(other, Notification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
