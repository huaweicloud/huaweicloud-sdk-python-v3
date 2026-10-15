# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlinkSavepointStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'state': 'FlinkSavepointState',
        'state_message': 'str'
    }

    attribute_map = {
        'state': 'state',
        'state_message': 'state_message'
    }

    def __init__(self, state=None, state_message=None):
        r"""FlinkSavepointStatus

        The model defined in huaweicloud sdk

        :param state: 
        :type state: :class:`huaweicloudsdkaidatalake.v2.FlinkSavepointState`
        :param state_message: **参数解释**：状态消息详情。 **取值范围**：0~512个字符。 
        :type state_message: str
        """
        
        

        self._state = None
        self._state_message = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if state_message is not None:
            self.state_message = state_message

    @property
    def state(self):
        r"""Gets the state of this FlinkSavepointStatus.

        :return: The state of this FlinkSavepointStatus.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.FlinkSavepointState`
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this FlinkSavepointStatus.

        :param state: The state of this FlinkSavepointStatus.
        :type state: :class:`huaweicloudsdkaidatalake.v2.FlinkSavepointState`
        """
        self._state = state

    @property
    def state_message(self):
        r"""Gets the state_message of this FlinkSavepointStatus.

        **参数解释**：状态消息详情。 **取值范围**：0~512个字符。 

        :return: The state_message of this FlinkSavepointStatus.
        :rtype: str
        """
        return self._state_message

    @state_message.setter
    def state_message(self, state_message):
        r"""Sets the state_message of this FlinkSavepointStatus.

        **参数解释**：状态消息详情。 **取值范围**：0~512个字符。 

        :param state_message: The state_message of this FlinkSavepointStatus.
        :type state_message: str
        """
        self._state_message = state_message

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
        if not isinstance(other, FlinkSavepointStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
