# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_entity_id': 'str',
        'event_entity_status': 'str'
    }

    attribute_map = {
        'event_entity_id': 'event_entity_id',
        'event_entity_status': 'event_entity_status'
    }

    def __init__(self, event_entity_id=None, event_entity_status=None):
        r"""EventEntity

        The model defined in huaweicloud sdk

        :param event_entity_id: **参数解释**：  事件对象ID。  **取值范围**：  实例ID或者节点ID。只能由英文字母、数字组成，后缀为in07或no07，长度为36个字符。
        :type event_entity_id: str
        :param event_entity_status: **参数解释**：  事件对象的执行状态。  **取值范围**：    - inquiring：待授权。   - scheduled：待执行。   - executing：执行中。   - completed：执行完成。   - canceled：事件关闭。   - failed：执行失败。
        :type event_entity_status: str
        """
        
        

        self._event_entity_id = None
        self._event_entity_status = None
        self.discriminator = None

        if event_entity_id is not None:
            self.event_entity_id = event_entity_id
        if event_entity_status is not None:
            self.event_entity_status = event_entity_status

    @property
    def event_entity_id(self):
        r"""Gets the event_entity_id of this EventEntity.

        **参数解释**：  事件对象ID。  **取值范围**：  实例ID或者节点ID。只能由英文字母、数字组成，后缀为in07或no07，长度为36个字符。

        :return: The event_entity_id of this EventEntity.
        :rtype: str
        """
        return self._event_entity_id

    @event_entity_id.setter
    def event_entity_id(self, event_entity_id):
        r"""Sets the event_entity_id of this EventEntity.

        **参数解释**：  事件对象ID。  **取值范围**：  实例ID或者节点ID。只能由英文字母、数字组成，后缀为in07或no07，长度为36个字符。

        :param event_entity_id: The event_entity_id of this EventEntity.
        :type event_entity_id: str
        """
        self._event_entity_id = event_entity_id

    @property
    def event_entity_status(self):
        r"""Gets the event_entity_status of this EventEntity.

        **参数解释**：  事件对象的执行状态。  **取值范围**：    - inquiring：待授权。   - scheduled：待执行。   - executing：执行中。   - completed：执行完成。   - canceled：事件关闭。   - failed：执行失败。

        :return: The event_entity_status of this EventEntity.
        :rtype: str
        """
        return self._event_entity_status

    @event_entity_status.setter
    def event_entity_status(self, event_entity_status):
        r"""Sets the event_entity_status of this EventEntity.

        **参数解释**：  事件对象的执行状态。  **取值范围**：    - inquiring：待授权。   - scheduled：待执行。   - executing：执行中。   - completed：执行完成。   - canceled：事件关闭。   - failed：执行失败。

        :param event_entity_status: The event_entity_status of this EventEntity.
        :type event_entity_status: str
        """
        self._event_entity_status = event_entity_status

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
        if not isinstance(other, EventEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
