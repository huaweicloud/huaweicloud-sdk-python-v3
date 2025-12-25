# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Event:

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
        'event_name': 'str'
    }

    attribute_map = {
        'event_id': 'event_id',
        'event_name': 'event_name'
    }

    def __init__(self, event_id=None, event_name=None):
        r"""Event

        The model defined in huaweicloud sdk

        :param event_id: **参数解释**： 事件ID。 **取值范围**： 不涉及。 
        :type event_id: str
        :param event_name: **参数解释**： 事件名称。 **取值范围**： 不涉及。 
        :type event_name: str
        """
        
        

        self._event_id = None
        self._event_name = None
        self.discriminator = None

        self.event_id = event_id
        self.event_name = event_name

    @property
    def event_id(self):
        r"""Gets the event_id of this Event.

        **参数解释**： 事件ID。 **取值范围**： 不涉及。 

        :return: The event_id of this Event.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        r"""Sets the event_id of this Event.

        **参数解释**： 事件ID。 **取值范围**： 不涉及。 

        :param event_id: The event_id of this Event.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def event_name(self):
        r"""Gets the event_name of this Event.

        **参数解释**： 事件名称。 **取值范围**： 不涉及。 

        :return: The event_name of this Event.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        r"""Sets the event_name of this Event.

        **参数解释**： 事件名称。 **取值范围**： 不涉及。 

        :param event_name: The event_name of this Event.
        :type event_name: str
        """
        self._event_name = event_name

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
        if not isinstance(other, Event):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
