# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoGenerateSecurityGroupHardeningConfigSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ports_to_disable': 'list[str]'
    }

    attribute_map = {
        'ports_to_disable': 'portsToDisable'
    }

    def __init__(self, ports_to_disable=None):
        r"""AutoGenerateSecurityGroupHardeningConfigSpec

        The model defined in huaweicloud sdk

        :param ports_to_disable: **参数解释：** 自动创建安全组时可选择不开放node节点相关端口，支持单端口和端口段两种形式。示例如下： &#x60;&#x60;&#x60; \&quot;portsToDisable\&quot;: [\&quot;22\&quot;, \&quot;4090-4099\&quot;] &#x60;&#x60;&#x60; **约束限制：** 若指定了节点安全组SecurityGroup，该配置项将被忽略。 只针对CCE Standard和Turbo集群的node安全组生效，不支持master安全组，不支持eni安全组。 **取值范围：** 端口号仅支持整数，范围[1-65535] **默认取值：** 不涉及 
        :type ports_to_disable: list[str]
        """
        
        

        self._ports_to_disable = None
        self.discriminator = None

        if ports_to_disable is not None:
            self.ports_to_disable = ports_to_disable

    @property
    def ports_to_disable(self):
        r"""Gets the ports_to_disable of this AutoGenerateSecurityGroupHardeningConfigSpec.

        **参数解释：** 自动创建安全组时可选择不开放node节点相关端口，支持单端口和端口段两种形式。示例如下： ``` \"portsToDisable\": [\"22\", \"4090-4099\"] ``` **约束限制：** 若指定了节点安全组SecurityGroup，该配置项将被忽略。 只针对CCE Standard和Turbo集群的node安全组生效，不支持master安全组，不支持eni安全组。 **取值范围：** 端口号仅支持整数，范围[1-65535] **默认取值：** 不涉及 

        :return: The ports_to_disable of this AutoGenerateSecurityGroupHardeningConfigSpec.
        :rtype: list[str]
        """
        return self._ports_to_disable

    @ports_to_disable.setter
    def ports_to_disable(self, ports_to_disable):
        r"""Sets the ports_to_disable of this AutoGenerateSecurityGroupHardeningConfigSpec.

        **参数解释：** 自动创建安全组时可选择不开放node节点相关端口，支持单端口和端口段两种形式。示例如下： ``` \"portsToDisable\": [\"22\", \"4090-4099\"] ``` **约束限制：** 若指定了节点安全组SecurityGroup，该配置项将被忽略。 只针对CCE Standard和Turbo集群的node安全组生效，不支持master安全组，不支持eni安全组。 **取值范围：** 端口号仅支持整数，范围[1-65535] **默认取值：** 不涉及 

        :param ports_to_disable: The ports_to_disable of this AutoGenerateSecurityGroupHardeningConfigSpec.
        :type ports_to_disable: list[str]
        """
        self._ports_to_disable = ports_to_disable

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
        if not isinstance(other, AutoGenerateSecurityGroupHardeningConfigSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
