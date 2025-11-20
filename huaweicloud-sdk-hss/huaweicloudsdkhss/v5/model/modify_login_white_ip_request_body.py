# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyLoginWhiteIpRequestBody:

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
        'white_ip': 'str',
        'host_id_list': 'list[str]'
    }

    attribute_map = {
        'enabled': 'enabled',
        'white_ip': 'white_ip',
        'host_id_list': 'host_id_list'
    }

    def __init__(self, enabled=None, white_ip=None, host_id_list=None):
        r"""ModifyLoginWhiteIpRequestBody

        The model defined in huaweicloud sdk

        :param enabled: **参数解释**： 白名单启用状态 **约束限制**： 不涉及 **取值范围**： - true：已启用 - false：已禁用  **默认取值**： false 
        :type enabled: bool
        :param white_ip: **参数解释**： 白名单IP或IP网段，IP网段由IP地址和掩码组成，以“/”连接，单一账号最多可添加10个SSH登录IP白名单。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type white_ip: str
        :param host_id_list: **参数解释**： 服务器列表，不可为NULL，删除白名单IP或IP网段时，需要将服务器ID列表置为空列表[]。 **约束限制**： 不可为NULL **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type host_id_list: list[str]
        """
        
        

        self._enabled = None
        self._white_ip = None
        self._host_id_list = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        self.white_ip = white_ip
        self.host_id_list = host_id_list

    @property
    def enabled(self):
        r"""Gets the enabled of this ModifyLoginWhiteIpRequestBody.

        **参数解释**： 白名单启用状态 **约束限制**： 不涉及 **取值范围**： - true：已启用 - false：已禁用  **默认取值**： false 

        :return: The enabled of this ModifyLoginWhiteIpRequestBody.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ModifyLoginWhiteIpRequestBody.

        **参数解释**： 白名单启用状态 **约束限制**： 不涉及 **取值范围**： - true：已启用 - false：已禁用  **默认取值**： false 

        :param enabled: The enabled of this ModifyLoginWhiteIpRequestBody.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def white_ip(self):
        r"""Gets the white_ip of this ModifyLoginWhiteIpRequestBody.

        **参数解释**： 白名单IP或IP网段，IP网段由IP地址和掩码组成，以“/”连接，单一账号最多可添加10个SSH登录IP白名单。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The white_ip of this ModifyLoginWhiteIpRequestBody.
        :rtype: str
        """
        return self._white_ip

    @white_ip.setter
    def white_ip(self, white_ip):
        r"""Sets the white_ip of this ModifyLoginWhiteIpRequestBody.

        **参数解释**： 白名单IP或IP网段，IP网段由IP地址和掩码组成，以“/”连接，单一账号最多可添加10个SSH登录IP白名单。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param white_ip: The white_ip of this ModifyLoginWhiteIpRequestBody.
        :type white_ip: str
        """
        self._white_ip = white_ip

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this ModifyLoginWhiteIpRequestBody.

        **参数解释**： 服务器列表，不可为NULL，删除白名单IP或IP网段时，需要将服务器ID列表置为空列表[]。 **约束限制**： 不可为NULL **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The host_id_list of this ModifyLoginWhiteIpRequestBody.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this ModifyLoginWhiteIpRequestBody.

        **参数解释**： 服务器列表，不可为NULL，删除白名单IP或IP网段时，需要将服务器ID列表置为空列表[]。 **约束限制**： 不可为NULL **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param host_id_list: The host_id_list of this ModifyLoginWhiteIpRequestBody.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

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
        if not isinstance(other, ModifyLoginWhiteIpRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
