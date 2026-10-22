# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateHistoryServerConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'obs': 'ObsConfig'
    }

    attribute_map = {
        'enabled': 'enabled',
        'obs': 'obs'
    }

    def __init__(self, enabled=None, obs=None):
        r"""CreateHistoryServerConfig

        The model defined in huaweicloud sdk

        :param enabled: **参数解释**：存储历史服务器功能的启用/禁用状态。必须将其设置为“true”才能启用该功能。 **约束限制**：不涉及。 **取值范围**：   - true：启用。   - false：禁用。 **默认取值**：false。
        :type enabled: bool
        :param obs: 
        :type obs: :class:`huaweicloudsdkaidatalake.v2.ObsConfig`
        """
        
        

        self._enabled = None
        self._obs = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if obs is not None:
            self.obs = obs

    @property
    def enabled(self):
        r"""Gets the enabled of this CreateHistoryServerConfig.

        **参数解释**：存储历史服务器功能的启用/禁用状态。必须将其设置为“true”才能启用该功能。 **约束限制**：不涉及。 **取值范围**：   - true：启用。   - false：禁用。 **默认取值**：false。

        :return: The enabled of this CreateHistoryServerConfig.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this CreateHistoryServerConfig.

        **参数解释**：存储历史服务器功能的启用/禁用状态。必须将其设置为“true”才能启用该功能。 **约束限制**：不涉及。 **取值范围**：   - true：启用。   - false：禁用。 **默认取值**：false。

        :param enabled: The enabled of this CreateHistoryServerConfig.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def obs(self):
        r"""Gets the obs of this CreateHistoryServerConfig.

        :return: The obs of this CreateHistoryServerConfig.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ObsConfig`
        """
        return self._obs

    @obs.setter
    def obs(self, obs):
        r"""Sets the obs of this CreateHistoryServerConfig.

        :param obs: The obs of this CreateHistoryServerConfig.
        :type obs: :class:`huaweicloudsdkaidatalake.v2.ObsConfig`
        """
        self._obs = obs

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
        if not isinstance(other, CreateHistoryServerConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
