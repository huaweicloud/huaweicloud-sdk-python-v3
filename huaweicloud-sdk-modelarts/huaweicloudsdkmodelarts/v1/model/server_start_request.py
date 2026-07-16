# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerStartRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'arch': 'str',
        'charging_mode': 'str',
        'server_type': 'str'
    }

    attribute_map = {
        'arch': 'arch',
        'charging_mode': 'charging_mode',
        'server_type': 'server_type'
    }

    def __init__(self, arch=None, charging_mode=None, server_type=None):
        r"""ServerStartRequest

        The model defined in huaweicloud sdk

        :param arch: **参数解释**：服务器架构信息。 **约束限制**：不涉及 **取值范围**： - -ARM - X86 **默认取值**：不涉及
        :type arch: str
        :param charging_mode: **参数解释**：服务器规格计费模式。 **约束限制**：不涉及。 **取值范围**： - [COMMON：同时支持包周期和按需](tag:hws,hws_hk) - POST_PAID：按需 - [PRE_PAID：包周期](tag:hws,hws_hk) **默认取值**：不涉及
        :type charging_mode: str
        :param server_type: **参数解释**：服务器类型。 **约束限制**：不涉及。 **取值范围**： - BMS：裸金属服务 - ECS：弹性云服务 - HPS：超节点服务 **默认取值**：不涉及
        :type server_type: str
        """
        
        

        self._arch = None
        self._charging_mode = None
        self._server_type = None
        self.discriminator = None

        if arch is not None:
            self.arch = arch
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if server_type is not None:
            self.server_type = server_type

    @property
    def arch(self):
        r"""Gets the arch of this ServerStartRequest.

        **参数解释**：服务器架构信息。 **约束限制**：不涉及 **取值范围**： - -ARM - X86 **默认取值**：不涉及

        :return: The arch of this ServerStartRequest.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this ServerStartRequest.

        **参数解释**：服务器架构信息。 **约束限制**：不涉及 **取值范围**： - -ARM - X86 **默认取值**：不涉及

        :param arch: The arch of this ServerStartRequest.
        :type arch: str
        """
        self._arch = arch

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this ServerStartRequest.

        **参数解释**：服务器规格计费模式。 **约束限制**：不涉及。 **取值范围**： - [COMMON：同时支持包周期和按需](tag:hws,hws_hk) - POST_PAID：按需 - [PRE_PAID：包周期](tag:hws,hws_hk) **默认取值**：不涉及

        :return: The charging_mode of this ServerStartRequest.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this ServerStartRequest.

        **参数解释**：服务器规格计费模式。 **约束限制**：不涉及。 **取值范围**： - [COMMON：同时支持包周期和按需](tag:hws,hws_hk) - POST_PAID：按需 - [PRE_PAID：包周期](tag:hws,hws_hk) **默认取值**：不涉及

        :param charging_mode: The charging_mode of this ServerStartRequest.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def server_type(self):
        r"""Gets the server_type of this ServerStartRequest.

        **参数解释**：服务器类型。 **约束限制**：不涉及。 **取值范围**： - BMS：裸金属服务 - ECS：弹性云服务 - HPS：超节点服务 **默认取值**：不涉及

        :return: The server_type of this ServerStartRequest.
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        r"""Sets the server_type of this ServerStartRequest.

        **参数解释**：服务器类型。 **约束限制**：不涉及。 **取值范围**： - BMS：裸金属服务 - ECS：弹性云服务 - HPS：超节点服务 **默认取值**：不涉及

        :param server_type: The server_type of this ServerStartRequest.
        :type server_type: str
        """
        self._server_type = server_type

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
        if not isinstance(other, ServerStartRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
