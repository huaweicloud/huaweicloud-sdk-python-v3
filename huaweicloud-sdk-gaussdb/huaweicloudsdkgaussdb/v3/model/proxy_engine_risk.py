# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProxyEngineRisk:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'level': 'int',
        'suggest': 'str',
        'influence': 'str',
        'guidance': 'str',
        'service_impact_duration': 'str',
        'upgrade_duration': 'str'
    }

    attribute_map = {
        'level': 'level',
        'suggest': 'suggest',
        'influence': 'influence',
        'guidance': 'guidance',
        'service_impact_duration': 'service_impact_duration',
        'upgrade_duration': 'upgrade_duration'
    }

    def __init__(self, level=None, suggest=None, influence=None, guidance=None, service_impact_duration=None, upgrade_duration=None):
        r"""ProxyEngineRisk

        The model defined in huaweicloud sdk

        :param level: **参数解释**：  风险级别。  **取值范围**： 1：一级风险。
        :type level: int
        :param suggest: **参数解释**：  建议升级原因。  **取值范围**：  不涉及。
        :type suggest: str
        :param influence: **参数解释**：  升级影响。  **取值范围**：  不涉及。
        :type influence: str
        :param guidance: **参数解释**：  升级指导。  **取值范围**：  不涉及。
        :type guidance: str
        :param service_impact_duration: **参数解释**：  预估业务影响时长。  **取值范围**：  不涉及。
        :type service_impact_duration: str
        :param upgrade_duration: **参数解释**：  预估升级时长。  **取值范围**：  不涉及。
        :type upgrade_duration: str
        """
        
        

        self._level = None
        self._suggest = None
        self._influence = None
        self._guidance = None
        self._service_impact_duration = None
        self._upgrade_duration = None
        self.discriminator = None

        if level is not None:
            self.level = level
        if suggest is not None:
            self.suggest = suggest
        if influence is not None:
            self.influence = influence
        if guidance is not None:
            self.guidance = guidance
        if service_impact_duration is not None:
            self.service_impact_duration = service_impact_duration
        if upgrade_duration is not None:
            self.upgrade_duration = upgrade_duration

    @property
    def level(self):
        r"""Gets the level of this ProxyEngineRisk.

        **参数解释**：  风险级别。  **取值范围**： 1：一级风险。

        :return: The level of this ProxyEngineRisk.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this ProxyEngineRisk.

        **参数解释**：  风险级别。  **取值范围**： 1：一级风险。

        :param level: The level of this ProxyEngineRisk.
        :type level: int
        """
        self._level = level

    @property
    def suggest(self):
        r"""Gets the suggest of this ProxyEngineRisk.

        **参数解释**：  建议升级原因。  **取值范围**：  不涉及。

        :return: The suggest of this ProxyEngineRisk.
        :rtype: str
        """
        return self._suggest

    @suggest.setter
    def suggest(self, suggest):
        r"""Sets the suggest of this ProxyEngineRisk.

        **参数解释**：  建议升级原因。  **取值范围**：  不涉及。

        :param suggest: The suggest of this ProxyEngineRisk.
        :type suggest: str
        """
        self._suggest = suggest

    @property
    def influence(self):
        r"""Gets the influence of this ProxyEngineRisk.

        **参数解释**：  升级影响。  **取值范围**：  不涉及。

        :return: The influence of this ProxyEngineRisk.
        :rtype: str
        """
        return self._influence

    @influence.setter
    def influence(self, influence):
        r"""Sets the influence of this ProxyEngineRisk.

        **参数解释**：  升级影响。  **取值范围**：  不涉及。

        :param influence: The influence of this ProxyEngineRisk.
        :type influence: str
        """
        self._influence = influence

    @property
    def guidance(self):
        r"""Gets the guidance of this ProxyEngineRisk.

        **参数解释**：  升级指导。  **取值范围**：  不涉及。

        :return: The guidance of this ProxyEngineRisk.
        :rtype: str
        """
        return self._guidance

    @guidance.setter
    def guidance(self, guidance):
        r"""Sets the guidance of this ProxyEngineRisk.

        **参数解释**：  升级指导。  **取值范围**：  不涉及。

        :param guidance: The guidance of this ProxyEngineRisk.
        :type guidance: str
        """
        self._guidance = guidance

    @property
    def service_impact_duration(self):
        r"""Gets the service_impact_duration of this ProxyEngineRisk.

        **参数解释**：  预估业务影响时长。  **取值范围**：  不涉及。

        :return: The service_impact_duration of this ProxyEngineRisk.
        :rtype: str
        """
        return self._service_impact_duration

    @service_impact_duration.setter
    def service_impact_duration(self, service_impact_duration):
        r"""Sets the service_impact_duration of this ProxyEngineRisk.

        **参数解释**：  预估业务影响时长。  **取值范围**：  不涉及。

        :param service_impact_duration: The service_impact_duration of this ProxyEngineRisk.
        :type service_impact_duration: str
        """
        self._service_impact_duration = service_impact_duration

    @property
    def upgrade_duration(self):
        r"""Gets the upgrade_duration of this ProxyEngineRisk.

        **参数解释**：  预估升级时长。  **取值范围**：  不涉及。

        :return: The upgrade_duration of this ProxyEngineRisk.
        :rtype: str
        """
        return self._upgrade_duration

    @upgrade_duration.setter
    def upgrade_duration(self, upgrade_duration):
        r"""Sets the upgrade_duration of this ProxyEngineRisk.

        **参数解释**：  预估升级时长。  **取值范围**：  不涉及。

        :param upgrade_duration: The upgrade_duration of this ProxyEngineRisk.
        :type upgrade_duration: str
        """
        self._upgrade_duration = upgrade_duration

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
        if not isinstance(other, ProxyEngineRisk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
