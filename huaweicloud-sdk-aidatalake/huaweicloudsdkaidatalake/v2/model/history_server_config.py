# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HistoryServerConfig:

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
        'obs': 'ObsConfig',
        'flow_insight_enabled': 'bool'
    }

    attribute_map = {
        'enabled': 'enabled',
        'obs': 'obs',
        'flow_insight_enabled': 'flow_insight_enabled'
    }

    def __init__(self, enabled=None, obs=None, flow_insight_enabled=None):
        r"""HistoryServerConfig

        The model defined in huaweicloud sdk

        :param enabled: **参数解释**：存储历史服务器功能的启用/禁用状态。必须将其设置为“true”才能启用该功能。 **约束限制**：不涉及。 **取值范围**：   - true：启用。   - false：禁用。 **默认取值**：false。
        :type enabled: bool
        :param obs: 
        :type obs: :class:`huaweicloudsdkaidatalake.v2.ObsConfig`
        :param flow_insight_enabled: **参数解释**：Flow Insight是一项诊断与可观测性功能，它从Ray集群收集指标、日志及工作流执行数据，并通过History Server收集器将其传输至已配置的OBS存储。该功能仅在“enabled”参数设置为“true”时可用。 **约束限制**：不涉及。 **取值范围**：   - true：启用。   - false：禁用。 **默认取值**：false。
        :type flow_insight_enabled: bool
        """
        
        

        self._enabled = None
        self._obs = None
        self._flow_insight_enabled = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if obs is not None:
            self.obs = obs
        if flow_insight_enabled is not None:
            self.flow_insight_enabled = flow_insight_enabled

    @property
    def enabled(self):
        r"""Gets the enabled of this HistoryServerConfig.

        **参数解释**：存储历史服务器功能的启用/禁用状态。必须将其设置为“true”才能启用该功能。 **约束限制**：不涉及。 **取值范围**：   - true：启用。   - false：禁用。 **默认取值**：false。

        :return: The enabled of this HistoryServerConfig.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this HistoryServerConfig.

        **参数解释**：存储历史服务器功能的启用/禁用状态。必须将其设置为“true”才能启用该功能。 **约束限制**：不涉及。 **取值范围**：   - true：启用。   - false：禁用。 **默认取值**：false。

        :param enabled: The enabled of this HistoryServerConfig.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def obs(self):
        r"""Gets the obs of this HistoryServerConfig.

        :return: The obs of this HistoryServerConfig.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ObsConfig`
        """
        return self._obs

    @obs.setter
    def obs(self, obs):
        r"""Sets the obs of this HistoryServerConfig.

        :param obs: The obs of this HistoryServerConfig.
        :type obs: :class:`huaweicloudsdkaidatalake.v2.ObsConfig`
        """
        self._obs = obs

    @property
    def flow_insight_enabled(self):
        r"""Gets the flow_insight_enabled of this HistoryServerConfig.

        **参数解释**：Flow Insight是一项诊断与可观测性功能，它从Ray集群收集指标、日志及工作流执行数据，并通过History Server收集器将其传输至已配置的OBS存储。该功能仅在“enabled”参数设置为“true”时可用。 **约束限制**：不涉及。 **取值范围**：   - true：启用。   - false：禁用。 **默认取值**：false。

        :return: The flow_insight_enabled of this HistoryServerConfig.
        :rtype: bool
        """
        return self._flow_insight_enabled

    @flow_insight_enabled.setter
    def flow_insight_enabled(self, flow_insight_enabled):
        r"""Sets the flow_insight_enabled of this HistoryServerConfig.

        **参数解释**：Flow Insight是一项诊断与可观测性功能，它从Ray集群收集指标、日志及工作流执行数据，并通过History Server收集器将其传输至已配置的OBS存储。该功能仅在“enabled”参数设置为“true”时可用。 **约束限制**：不涉及。 **取值范围**：   - true：启用。   - false：禁用。 **默认取值**：false。

        :param flow_insight_enabled: The flow_insight_enabled of this HistoryServerConfig.
        :type flow_insight_enabled: bool
        """
        self._flow_insight_enabled = flow_insight_enabled

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
        if not isinstance(other, HistoryServerConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
