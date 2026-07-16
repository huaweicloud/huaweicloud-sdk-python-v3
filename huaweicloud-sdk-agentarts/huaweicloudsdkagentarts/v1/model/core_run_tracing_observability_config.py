# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreRunTracingObservabilityConfig:

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
        'service_group': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'service_group': 'service_group'
    }

    def __init__(self, enabled=None, service_group=None):
        r"""CoreRunTracingObservabilityConfig

        The model defined in huaweicloud sdk

        :param enabled: **参数解释**: 是否开启调用链采集，默认为false。 - 未开启，托管运行时过程产生的调用链数据无法上报至应用性能管理服务(APM)。 - 开启后，托管运行时过程产生的调用链数据会上报应用性能管理服务(APM)。 **约束限制**: 不涉及。 **取值范围**: - true - false **默认值**: false 
        :type enabled: bool
        :param service_group: **参数解释**: 调用链服务应用名。 **约束限制**: 不涉及。 **取值范围**: 长度为 1 - 64 个字符。 **默认取值**: 不涉及。 
        :type service_group: str
        """
        
        

        self._enabled = None
        self._service_group = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if service_group is not None:
            self.service_group = service_group

    @property
    def enabled(self):
        r"""Gets the enabled of this CoreRunTracingObservabilityConfig.

        **参数解释**: 是否开启调用链采集，默认为false。 - 未开启，托管运行时过程产生的调用链数据无法上报至应用性能管理服务(APM)。 - 开启后，托管运行时过程产生的调用链数据会上报应用性能管理服务(APM)。 **约束限制**: 不涉及。 **取值范围**: - true - false **默认值**: false 

        :return: The enabled of this CoreRunTracingObservabilityConfig.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this CoreRunTracingObservabilityConfig.

        **参数解释**: 是否开启调用链采集，默认为false。 - 未开启，托管运行时过程产生的调用链数据无法上报至应用性能管理服务(APM)。 - 开启后，托管运行时过程产生的调用链数据会上报应用性能管理服务(APM)。 **约束限制**: 不涉及。 **取值范围**: - true - false **默认值**: false 

        :param enabled: The enabled of this CoreRunTracingObservabilityConfig.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def service_group(self):
        r"""Gets the service_group of this CoreRunTracingObservabilityConfig.

        **参数解释**: 调用链服务应用名。 **约束限制**: 不涉及。 **取值范围**: 长度为 1 - 64 个字符。 **默认取值**: 不涉及。 

        :return: The service_group of this CoreRunTracingObservabilityConfig.
        :rtype: str
        """
        return self._service_group

    @service_group.setter
    def service_group(self, service_group):
        r"""Sets the service_group of this CoreRunTracingObservabilityConfig.

        **参数解释**: 调用链服务应用名。 **约束限制**: 不涉及。 **取值范围**: 长度为 1 - 64 个字符。 **默认取值**: 不涉及。 

        :param service_group: The service_group of this CoreRunTracingObservabilityConfig.
        :type service_group: str
        """
        self._service_group = service_group

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
        if not isinstance(other, CoreRunTracingObservabilityConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
