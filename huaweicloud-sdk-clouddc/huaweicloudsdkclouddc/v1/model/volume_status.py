# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VolumeStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'state': 'str',
        'health': 'str'
    }

    attribute_map = {
        'state': 'state',
        'health': 'health'
    }

    def __init__(self, state=None, health=None):
        r"""VolumeStatus

        The model defined in huaweicloud sdk

        :param state: **参数解释**： 逻辑卷状态 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type state: str
        :param health: 硬件健康状态： OK：健康 Warning：警告 Critical：严重 Unknown：未知
        :type health: str
        """
        
        

        self._state = None
        self._health = None
        self.discriminator = None

        if state is not None:
            self.state = state
        if health is not None:
            self.health = health

    @property
    def state(self):
        r"""Gets the state of this VolumeStatus.

        **参数解释**： 逻辑卷状态 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The state of this VolumeStatus.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this VolumeStatus.

        **参数解释**： 逻辑卷状态 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param state: The state of this VolumeStatus.
        :type state: str
        """
        self._state = state

    @property
    def health(self):
        r"""Gets the health of this VolumeStatus.

        硬件健康状态： OK：健康 Warning：警告 Critical：严重 Unknown：未知

        :return: The health of this VolumeStatus.
        :rtype: str
        """
        return self._health

    @health.setter
    def health(self, health):
        r"""Sets the health of this VolumeStatus.

        硬件健康状态： OK：健康 Warning：警告 Critical：严重 Unknown：未知

        :param health: The health of this VolumeStatus.
        :type health: str
        """
        self._health = health

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
        if not isinstance(other, VolumeStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
