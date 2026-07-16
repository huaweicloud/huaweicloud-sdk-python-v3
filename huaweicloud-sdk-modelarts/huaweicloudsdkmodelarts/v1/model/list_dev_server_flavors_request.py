# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDevServerFlavorsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_type': 'str',
        'arch': 'str',
        'charging_mode': 'str'
    }

    attribute_map = {
        'server_type': 'server_type',
        'arch': 'arch',
        'charging_mode': 'charging_mode'
    }

    def __init__(self, server_type=None, arch=None, charging_mode=None):
        r"""ListDevServerFlavorsRequest

        The model defined in huaweicloud sdk

        :param server_type: **参数解释**：服务类型。 **约束限制**：不涉及。 **取值范围**： - BMS：资源类型为裸金属服务器 - ECS：资源类型为弹性云服务器 - HPS：资源类型为超节点服务器  **默认取值**：不涉及。
        :type server_type: str
        :param arch: **参数解释**：规格的CPU架构。 **约束限制**：不涉及。 **取值范围**： - X86：CPU架构为X86 - ARM：CPU架构为ARM **默认取值**：不涉及。
        :type arch: str
        :param charging_mode: **参数解释**：计费模式。 **约束限制**：不涉及。 **取值范围**： - PRE_PAID：计费模式为包年/包月 - POST_PAID：计费模式为按需计费 **默认取值**：不涉及。
        :type charging_mode: str
        """
        
        

        self._server_type = None
        self._arch = None
        self._charging_mode = None
        self.discriminator = None

        if server_type is not None:
            self.server_type = server_type
        if arch is not None:
            self.arch = arch
        if charging_mode is not None:
            self.charging_mode = charging_mode

    @property
    def server_type(self):
        r"""Gets the server_type of this ListDevServerFlavorsRequest.

        **参数解释**：服务类型。 **约束限制**：不涉及。 **取值范围**： - BMS：资源类型为裸金属服务器 - ECS：资源类型为弹性云服务器 - HPS：资源类型为超节点服务器  **默认取值**：不涉及。

        :return: The server_type of this ListDevServerFlavorsRequest.
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        r"""Sets the server_type of this ListDevServerFlavorsRequest.

        **参数解释**：服务类型。 **约束限制**：不涉及。 **取值范围**： - BMS：资源类型为裸金属服务器 - ECS：资源类型为弹性云服务器 - HPS：资源类型为超节点服务器  **默认取值**：不涉及。

        :param server_type: The server_type of this ListDevServerFlavorsRequest.
        :type server_type: str
        """
        self._server_type = server_type

    @property
    def arch(self):
        r"""Gets the arch of this ListDevServerFlavorsRequest.

        **参数解释**：规格的CPU架构。 **约束限制**：不涉及。 **取值范围**： - X86：CPU架构为X86 - ARM：CPU架构为ARM **默认取值**：不涉及。

        :return: The arch of this ListDevServerFlavorsRequest.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this ListDevServerFlavorsRequest.

        **参数解释**：规格的CPU架构。 **约束限制**：不涉及。 **取值范围**： - X86：CPU架构为X86 - ARM：CPU架构为ARM **默认取值**：不涉及。

        :param arch: The arch of this ListDevServerFlavorsRequest.
        :type arch: str
        """
        self._arch = arch

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this ListDevServerFlavorsRequest.

        **参数解释**：计费模式。 **约束限制**：不涉及。 **取值范围**： - PRE_PAID：计费模式为包年/包月 - POST_PAID：计费模式为按需计费 **默认取值**：不涉及。

        :return: The charging_mode of this ListDevServerFlavorsRequest.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this ListDevServerFlavorsRequest.

        **参数解释**：计费模式。 **约束限制**：不涉及。 **取值范围**： - PRE_PAID：计费模式为包年/包月 - POST_PAID：计费模式为按需计费 **默认取值**：不涉及。

        :param charging_mode: The charging_mode of this ListDevServerFlavorsRequest.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

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
        if not isinstance(other, ListDevServerFlavorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
