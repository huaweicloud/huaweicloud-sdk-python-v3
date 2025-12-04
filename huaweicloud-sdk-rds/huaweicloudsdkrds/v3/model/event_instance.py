# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_id': 'str',
        'instance_id': 'str'
    }

    attribute_map = {
        'event_id': 'event_id',
        'instance_id': 'instance_id'
    }

    def __init__(self, event_id=None, instance_id=None):
        r"""EventInstance

        The model defined in huaweicloud sdk

        :param event_id: **参数解释**：  事件id  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type event_id: str
        :param instance_id: **参数解释**：  实例id  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type instance_id: str
        """
        
        

        self._event_id = None
        self._instance_id = None
        self.discriminator = None

        self.event_id = event_id
        self.instance_id = instance_id

    @property
    def event_id(self):
        r"""Gets the event_id of this EventInstance.

        **参数解释**：  事件id  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The event_id of this EventInstance.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        r"""Sets the event_id of this EventInstance.

        **参数解释**：  事件id  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param event_id: The event_id of this EventInstance.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this EventInstance.

        **参数解释**：  实例id  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The instance_id of this EventInstance.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this EventInstance.

        **参数解释**：  实例id  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param instance_id: The instance_id of this EventInstance.
        :type instance_id: str
        """
        self._instance_id = instance_id

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
        if not isinstance(other, EventInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
