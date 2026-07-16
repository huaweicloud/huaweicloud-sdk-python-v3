# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreToolsMetricsObservabilityConfig:

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
        'instance_id': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'instance_id': 'instance_id'
    }

    def __init__(self, enabled=None, instance_id=None):
        r"""CoreToolsMetricsObservabilityConfig

        The model defined in huaweicloud sdk

        :param enabled: **参数解释：** 是否开启自定义指标采集。 **约束限制：** 不涉及。 **取值范围：** - true 开启。 - false 关闭。 **默认取值：** false。
        :type enabled: bool
        :param instance_id: **参数解释：** 自定义指标实例ID。 **约束限制：** 不涉及。 **取值范围：** 长度不能超过64个字符。 **默认取值：** 不涉及。
        :type instance_id: str
        """
        
        

        self._enabled = None
        self._instance_id = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if instance_id is not None:
            self.instance_id = instance_id

    @property
    def enabled(self):
        r"""Gets the enabled of this CoreToolsMetricsObservabilityConfig.

        **参数解释：** 是否开启自定义指标采集。 **约束限制：** 不涉及。 **取值范围：** - true 开启。 - false 关闭。 **默认取值：** false。

        :return: The enabled of this CoreToolsMetricsObservabilityConfig.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this CoreToolsMetricsObservabilityConfig.

        **参数解释：** 是否开启自定义指标采集。 **约束限制：** 不涉及。 **取值范围：** - true 开启。 - false 关闭。 **默认取值：** false。

        :param enabled: The enabled of this CoreToolsMetricsObservabilityConfig.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def instance_id(self):
        r"""Gets the instance_id of this CoreToolsMetricsObservabilityConfig.

        **参数解释：** 自定义指标实例ID。 **约束限制：** 不涉及。 **取值范围：** 长度不能超过64个字符。 **默认取值：** 不涉及。

        :return: The instance_id of this CoreToolsMetricsObservabilityConfig.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this CoreToolsMetricsObservabilityConfig.

        **参数解释：** 自定义指标实例ID。 **约束限制：** 不涉及。 **取值范围：** 长度不能超过64个字符。 **默认取值：** 不涉及。

        :param instance_id: The instance_id of this CoreToolsMetricsObservabilityConfig.
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
        if not isinstance(other, CoreToolsMetricsObservabilityConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
