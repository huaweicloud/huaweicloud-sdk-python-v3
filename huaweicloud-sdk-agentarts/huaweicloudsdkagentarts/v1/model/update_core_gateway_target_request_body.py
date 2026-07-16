# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCoreGatewayTargetRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'target_configuration': 'CoreGatewayTargetConfiguration',
        'credential_provider_configuration': 'CoreGatewayCredentialProviderConfiguration'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'target_configuration': 'target_configuration',
        'credential_provider_configuration': 'credential_provider_configuration'
    }

    def __init__(self, name=None, description=None, target_configuration=None, credential_provider_configuration=None):
        r"""UpdateCoreGatewayTargetRequestBody

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 更新后的目标服务名称。 **约束限制：** 同一网关内目标服务名称唯一。 **取值范围：** 长度为 1-50 个字符，匹配以字母数字开头和结尾、中间可含0到48个字母数字或短横线的字符串，符合正则条件^[a-zA-Z0-9]\\([a-zA-Z0-9-]{0,48}[a-zA-Z0-9])?$。 **默认取值：** 不涉及。 
        :type name: str
        :param description: **参数解释：** 更新后的目标服务描述。 **约束限制：** 不涉及。 **取值范围：** 长度为 0-200 个字符。 **默认取值：** 不涉及。 
        :type description: str
        :param target_configuration: 
        :type target_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayTargetConfiguration`
        :param credential_provider_configuration: 
        :type credential_provider_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayCredentialProviderConfiguration`
        """
        
        

        self._name = None
        self._description = None
        self._target_configuration = None
        self._credential_provider_configuration = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if target_configuration is not None:
            self.target_configuration = target_configuration
        if credential_provider_configuration is not None:
            self.credential_provider_configuration = credential_provider_configuration

    @property
    def name(self):
        r"""Gets the name of this UpdateCoreGatewayTargetRequestBody.

        **参数解释：** 更新后的目标服务名称。 **约束限制：** 同一网关内目标服务名称唯一。 **取值范围：** 长度为 1-50 个字符，匹配以字母数字开头和结尾、中间可含0到48个字母数字或短横线的字符串，符合正则条件^[a-zA-Z0-9]\\([a-zA-Z0-9-]{0,48}[a-zA-Z0-9])?$。 **默认取值：** 不涉及。 

        :return: The name of this UpdateCoreGatewayTargetRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateCoreGatewayTargetRequestBody.

        **参数解释：** 更新后的目标服务名称。 **约束限制：** 同一网关内目标服务名称唯一。 **取值范围：** 长度为 1-50 个字符，匹配以字母数字开头和结尾、中间可含0到48个字母数字或短横线的字符串，符合正则条件^[a-zA-Z0-9]\\([a-zA-Z0-9-]{0,48}[a-zA-Z0-9])?$。 **默认取值：** 不涉及。 

        :param name: The name of this UpdateCoreGatewayTargetRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateCoreGatewayTargetRequestBody.

        **参数解释：** 更新后的目标服务描述。 **约束限制：** 不涉及。 **取值范围：** 长度为 0-200 个字符。 **默认取值：** 不涉及。 

        :return: The description of this UpdateCoreGatewayTargetRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateCoreGatewayTargetRequestBody.

        **参数解释：** 更新后的目标服务描述。 **约束限制：** 不涉及。 **取值范围：** 长度为 0-200 个字符。 **默认取值：** 不涉及。 

        :param description: The description of this UpdateCoreGatewayTargetRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def target_configuration(self):
        r"""Gets the target_configuration of this UpdateCoreGatewayTargetRequestBody.

        :return: The target_configuration of this UpdateCoreGatewayTargetRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayTargetConfiguration`
        """
        return self._target_configuration

    @target_configuration.setter
    def target_configuration(self, target_configuration):
        r"""Sets the target_configuration of this UpdateCoreGatewayTargetRequestBody.

        :param target_configuration: The target_configuration of this UpdateCoreGatewayTargetRequestBody.
        :type target_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayTargetConfiguration`
        """
        self._target_configuration = target_configuration

    @property
    def credential_provider_configuration(self):
        r"""Gets the credential_provider_configuration of this UpdateCoreGatewayTargetRequestBody.

        :return: The credential_provider_configuration of this UpdateCoreGatewayTargetRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreGatewayCredentialProviderConfiguration`
        """
        return self._credential_provider_configuration

    @credential_provider_configuration.setter
    def credential_provider_configuration(self, credential_provider_configuration):
        r"""Sets the credential_provider_configuration of this UpdateCoreGatewayTargetRequestBody.

        :param credential_provider_configuration: The credential_provider_configuration of this UpdateCoreGatewayTargetRequestBody.
        :type credential_provider_configuration: :class:`huaweicloudsdkagentarts.v1.CoreGatewayCredentialProviderConfiguration`
        """
        self._credential_provider_configuration = credential_provider_configuration

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
        if not isinstance(other, UpdateCoreGatewayTargetRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
