# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperateEventReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_instances': 'list[EventInstance]',
        'operation_type': 'str',
        'event_schedule_window': 'EventScheduleWindow'
    }

    attribute_map = {
        'event_instances': 'event_instances',
        'operation_type': 'operation_type',
        'event_schedule_window': 'event_schedule_window'
    }

    def __init__(self, event_instances=None, operation_type=None, event_schedule_window=None):
        r"""OperateEventReq

        The model defined in huaweicloud sdk

        :param event_instances: **参数解释**：  事件列表  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type event_instances: list[:class:`huaweicloudsdkrds.v3.EventInstance`]
        :param operation_type: **参数解释**：  事件操作类型：cancel|execute|reservation  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type operation_type: str
        :param event_schedule_window: 
        :type event_schedule_window: :class:`huaweicloudsdkrds.v3.EventScheduleWindow`
        """
        
        

        self._event_instances = None
        self._operation_type = None
        self._event_schedule_window = None
        self.discriminator = None

        self.event_instances = event_instances
        self.operation_type = operation_type
        if event_schedule_window is not None:
            self.event_schedule_window = event_schedule_window

    @property
    def event_instances(self):
        r"""Gets the event_instances of this OperateEventReq.

        **参数解释**：  事件列表  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The event_instances of this OperateEventReq.
        :rtype: list[:class:`huaweicloudsdkrds.v3.EventInstance`]
        """
        return self._event_instances

    @event_instances.setter
    def event_instances(self, event_instances):
        r"""Sets the event_instances of this OperateEventReq.

        **参数解释**：  事件列表  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param event_instances: The event_instances of this OperateEventReq.
        :type event_instances: list[:class:`huaweicloudsdkrds.v3.EventInstance`]
        """
        self._event_instances = event_instances

    @property
    def operation_type(self):
        r"""Gets the operation_type of this OperateEventReq.

        **参数解释**：  事件操作类型：cancel|execute|reservation  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The operation_type of this OperateEventReq.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        r"""Sets the operation_type of this OperateEventReq.

        **参数解释**：  事件操作类型：cancel|execute|reservation  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param operation_type: The operation_type of this OperateEventReq.
        :type operation_type: str
        """
        self._operation_type = operation_type

    @property
    def event_schedule_window(self):
        r"""Gets the event_schedule_window of this OperateEventReq.

        :return: The event_schedule_window of this OperateEventReq.
        :rtype: :class:`huaweicloudsdkrds.v3.EventScheduleWindow`
        """
        return self._event_schedule_window

    @event_schedule_window.setter
    def event_schedule_window(self, event_schedule_window):
        r"""Sets the event_schedule_window of this OperateEventReq.

        :param event_schedule_window: The event_schedule_window of this OperateEventReq.
        :type event_schedule_window: :class:`huaweicloudsdkrds.v3.EventScheduleWindow`
        """
        self._event_schedule_window = event_schedule_window

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
        if not isinstance(other, OperateEventReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
