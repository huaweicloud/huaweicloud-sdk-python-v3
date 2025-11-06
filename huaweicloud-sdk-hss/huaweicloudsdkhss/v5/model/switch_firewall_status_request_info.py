# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchFirewallStatusRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'firewall_status': 'str',
        'host_id_list': 'list[str]'
    }

    attribute_map = {
        'firewall_status': 'firewall_status',
        'host_id_list': 'host_id_list'
    }

    def __init__(self, firewall_status=None, host_id_list=None):
        r"""SwitchFirewallStatusRequestInfo

        The model defined in huaweicloud sdk

        :param firewall_status: **参数解释**： 防火墙开启状态 **约束限制**： 不涉及 **取值范围**：   - Opened：开启windows防火墙   - Closed：关闭windows防火墙 **默认取值**： 不涉及 
        :type firewall_status: str
        :param host_id_list: **参数解释**： 主机ID列表 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type host_id_list: list[str]
        """
        
        

        self._firewall_status = None
        self._host_id_list = None
        self.discriminator = None

        self.firewall_status = firewall_status
        self.host_id_list = host_id_list

    @property
    def firewall_status(self):
        r"""Gets the firewall_status of this SwitchFirewallStatusRequestInfo.

        **参数解释**： 防火墙开启状态 **约束限制**： 不涉及 **取值范围**：   - Opened：开启windows防火墙   - Closed：关闭windows防火墙 **默认取值**： 不涉及 

        :return: The firewall_status of this SwitchFirewallStatusRequestInfo.
        :rtype: str
        """
        return self._firewall_status

    @firewall_status.setter
    def firewall_status(self, firewall_status):
        r"""Sets the firewall_status of this SwitchFirewallStatusRequestInfo.

        **参数解释**： 防火墙开启状态 **约束限制**： 不涉及 **取值范围**：   - Opened：开启windows防火墙   - Closed：关闭windows防火墙 **默认取值**： 不涉及 

        :param firewall_status: The firewall_status of this SwitchFirewallStatusRequestInfo.
        :type firewall_status: str
        """
        self._firewall_status = firewall_status

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this SwitchFirewallStatusRequestInfo.

        **参数解释**： 主机ID列表 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The host_id_list of this SwitchFirewallStatusRequestInfo.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this SwitchFirewallStatusRequestInfo.

        **参数解释**： 主机ID列表 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param host_id_list: The host_id_list of this SwitchFirewallStatusRequestInfo.
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
        if not isinstance(other, SwitchFirewallStatusRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
