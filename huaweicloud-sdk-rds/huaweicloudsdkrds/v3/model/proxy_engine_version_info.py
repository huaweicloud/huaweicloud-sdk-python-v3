# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProxyEngineVersionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'current_engine_version': 'str',
        'target_engine_version': 'str',
        'upgrade_flag': 'bool',
        'proxy_id': 'str',
        'risks': 'list[EngineRiskDesc]'
    }

    attribute_map = {
        'current_engine_version': 'current_engine_version',
        'target_engine_version': 'target_engine_version',
        'upgrade_flag': 'upgrade_flag',
        'proxy_id': 'proxy_id',
        'risks': 'risks'
    }

    def __init__(self, current_engine_version=None, target_engine_version=None, upgrade_flag=None, proxy_id=None, risks=None):
        r"""ProxyEngineVersionInfo

        The model defined in huaweicloud sdk

        :param current_engine_version: **参数解释**：  当前引擎版本。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type current_engine_version: str
        :param target_engine_version: **参数解释**：  目标引擎版本。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type target_engine_version: str
        :param upgrade_flag: **参数解释**：  是否可升级标志。true表示可以升级，false表示不可升级。  **约束限制**：  不涉及。  **取值范围**：  - true - false  **默认取值**：  不涉及。
        :type upgrade_flag: bool
        :param proxy_id: **参数解释**：  代理节点ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type proxy_id: str
        :param risks: **参数解释**：  升级风险列表。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type risks: list[:class:`huaweicloudsdkrds.v3.EngineRiskDesc`]
        """
        
        

        self._current_engine_version = None
        self._target_engine_version = None
        self._upgrade_flag = None
        self._proxy_id = None
        self._risks = None
        self.discriminator = None

        if current_engine_version is not None:
            self.current_engine_version = current_engine_version
        if target_engine_version is not None:
            self.target_engine_version = target_engine_version
        if upgrade_flag is not None:
            self.upgrade_flag = upgrade_flag
        if proxy_id is not None:
            self.proxy_id = proxy_id
        if risks is not None:
            self.risks = risks

    @property
    def current_engine_version(self):
        r"""Gets the current_engine_version of this ProxyEngineVersionInfo.

        **参数解释**：  当前引擎版本。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The current_engine_version of this ProxyEngineVersionInfo.
        :rtype: str
        """
        return self._current_engine_version

    @current_engine_version.setter
    def current_engine_version(self, current_engine_version):
        r"""Sets the current_engine_version of this ProxyEngineVersionInfo.

        **参数解释**：  当前引擎版本。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param current_engine_version: The current_engine_version of this ProxyEngineVersionInfo.
        :type current_engine_version: str
        """
        self._current_engine_version = current_engine_version

    @property
    def target_engine_version(self):
        r"""Gets the target_engine_version of this ProxyEngineVersionInfo.

        **参数解释**：  目标引擎版本。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The target_engine_version of this ProxyEngineVersionInfo.
        :rtype: str
        """
        return self._target_engine_version

    @target_engine_version.setter
    def target_engine_version(self, target_engine_version):
        r"""Sets the target_engine_version of this ProxyEngineVersionInfo.

        **参数解释**：  目标引擎版本。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param target_engine_version: The target_engine_version of this ProxyEngineVersionInfo.
        :type target_engine_version: str
        """
        self._target_engine_version = target_engine_version

    @property
    def upgrade_flag(self):
        r"""Gets the upgrade_flag of this ProxyEngineVersionInfo.

        **参数解释**：  是否可升级标志。true表示可以升级，false表示不可升级。  **约束限制**：  不涉及。  **取值范围**：  - true - false  **默认取值**：  不涉及。

        :return: The upgrade_flag of this ProxyEngineVersionInfo.
        :rtype: bool
        """
        return self._upgrade_flag

    @upgrade_flag.setter
    def upgrade_flag(self, upgrade_flag):
        r"""Sets the upgrade_flag of this ProxyEngineVersionInfo.

        **参数解释**：  是否可升级标志。true表示可以升级，false表示不可升级。  **约束限制**：  不涉及。  **取值范围**：  - true - false  **默认取值**：  不涉及。

        :param upgrade_flag: The upgrade_flag of this ProxyEngineVersionInfo.
        :type upgrade_flag: bool
        """
        self._upgrade_flag = upgrade_flag

    @property
    def proxy_id(self):
        r"""Gets the proxy_id of this ProxyEngineVersionInfo.

        **参数解释**：  代理节点ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The proxy_id of this ProxyEngineVersionInfo.
        :rtype: str
        """
        return self._proxy_id

    @proxy_id.setter
    def proxy_id(self, proxy_id):
        r"""Sets the proxy_id of this ProxyEngineVersionInfo.

        **参数解释**：  代理节点ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param proxy_id: The proxy_id of this ProxyEngineVersionInfo.
        :type proxy_id: str
        """
        self._proxy_id = proxy_id

    @property
    def risks(self):
        r"""Gets the risks of this ProxyEngineVersionInfo.

        **参数解释**：  升级风险列表。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The risks of this ProxyEngineVersionInfo.
        :rtype: list[:class:`huaweicloudsdkrds.v3.EngineRiskDesc`]
        """
        return self._risks

    @risks.setter
    def risks(self, risks):
        r"""Sets the risks of this ProxyEngineVersionInfo.

        **参数解释**：  升级风险列表。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param risks: The risks of this ProxyEngineVersionInfo.
        :type risks: list[:class:`huaweicloudsdkrds.v3.EngineRiskDesc`]
        """
        self._risks = risks

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
        if not isinstance(other, ProxyEngineVersionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
