# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVirsubnetCidrReservationOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'virsubnet_id': 'str',
        'ip_version': 'int',
        'cidr': 'str',
        'mask': 'int',
        'name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'virsubnet_id': 'virsubnet_id',
        'ip_version': 'ip_version',
        'cidr': 'cidr',
        'mask': 'mask',
        'name': 'name',
        'description': 'description'
    }

    def __init__(self, virsubnet_id=None, ip_version=None, cidr=None, mask=None, name=None, description=None):
        r"""CreateVirsubnetCidrReservationOption

        The model defined in huaweicloud sdk

        :param virsubnet_id: **参数解释**： 子网预留网段所属的子网ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type virsubnet_id: str
        :param ip_version: **参数解释**： 子网预留网段的IP版本，支持IPv4和IPv6。 **约束限制**： 不涉及。 **取值范围**： - 4：表示IPv4。 - 6：表示IPv6。 **默认取值**： 不涉及。
        :type ip_version: int
        :param cidr: **参数解释**： 子网预留网段的IP网段。 **约束限制**： - CIDR格式，掩码长度最小值为“所属子网的网段掩码 + 2”，最大值为32（IPv4）或128（IPv6）。 - cidr和mask参数必须输入一个，两者同时输入时不能冲突。 - 子网预留网段不能包含所属子网的已使用的地址和系统预留地址（子网的第1个和最后2个地址）。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type cidr: str
        :param mask: **参数解释**： 子网预留网段的IP网段掩码长度。 **约束限制**： - 整数，预留网段的掩码长度最小值为“所属子网的网段掩码 + 2”，最大值为32（IPv4）或128（IPv6）。 - cidr和mask参数必须输入一个，两者同时输入时不能冲突。 - 子网预留网段不能包含所属子网的已使用的地址和系统预留地址（子网的第1个和最后2个地址）。 - 指定掩码长度创建预留网段，最后mask与子网掩码的差值长度的bit位由系统自动分配，例如子网cidr为192.168.21.0/24，子网掩码长度24，指定预留网段长度为27，差值长度27 - 24 &#x3D; 3，即第25,26,27这3个bit位由系统自动分配。例如：   - 第25-27的bit位分配为011，最终创建出的子网预留网段cidr是192.168.21.96/27，其中96转为二进制是0110 0000；   - 第25-27的bit位分配为110，最终创建出的子网预留网段cidr是192.168.21.192/27，其中192转为二进制是1100 0000。  **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type mask: int
        :param name: **参数解释**： 子网预留网段的名称。 **约束限制**： 1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type name: str
        :param description: **参数解释**： 子网预留网段的描述信息。 **约束限制**： 0-255个字符，不能包含“&lt;”和“&gt;”。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type description: str
        """
        
        

        self._virsubnet_id = None
        self._ip_version = None
        self._cidr = None
        self._mask = None
        self._name = None
        self._description = None
        self.discriminator = None

        self.virsubnet_id = virsubnet_id
        self.ip_version = ip_version
        if cidr is not None:
            self.cidr = cidr
        if mask is not None:
            self.mask = mask
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description

    @property
    def virsubnet_id(self):
        r"""Gets the virsubnet_id of this CreateVirsubnetCidrReservationOption.

        **参数解释**： 子网预留网段所属的子网ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The virsubnet_id of this CreateVirsubnetCidrReservationOption.
        :rtype: str
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        r"""Sets the virsubnet_id of this CreateVirsubnetCidrReservationOption.

        **参数解释**： 子网预留网段所属的子网ID。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param virsubnet_id: The virsubnet_id of this CreateVirsubnetCidrReservationOption.
        :type virsubnet_id: str
        """
        self._virsubnet_id = virsubnet_id

    @property
    def ip_version(self):
        r"""Gets the ip_version of this CreateVirsubnetCidrReservationOption.

        **参数解释**： 子网预留网段的IP版本，支持IPv4和IPv6。 **约束限制**： 不涉及。 **取值范围**： - 4：表示IPv4。 - 6：表示IPv6。 **默认取值**： 不涉及。

        :return: The ip_version of this CreateVirsubnetCidrReservationOption.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this CreateVirsubnetCidrReservationOption.

        **参数解释**： 子网预留网段的IP版本，支持IPv4和IPv6。 **约束限制**： 不涉及。 **取值范围**： - 4：表示IPv4。 - 6：表示IPv6。 **默认取值**： 不涉及。

        :param ip_version: The ip_version of this CreateVirsubnetCidrReservationOption.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def cidr(self):
        r"""Gets the cidr of this CreateVirsubnetCidrReservationOption.

        **参数解释**： 子网预留网段的IP网段。 **约束限制**： - CIDR格式，掩码长度最小值为“所属子网的网段掩码 + 2”，最大值为32（IPv4）或128（IPv6）。 - cidr和mask参数必须输入一个，两者同时输入时不能冲突。 - 子网预留网段不能包含所属子网的已使用的地址和系统预留地址（子网的第1个和最后2个地址）。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The cidr of this CreateVirsubnetCidrReservationOption.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        r"""Sets the cidr of this CreateVirsubnetCidrReservationOption.

        **参数解释**： 子网预留网段的IP网段。 **约束限制**： - CIDR格式，掩码长度最小值为“所属子网的网段掩码 + 2”，最大值为32（IPv4）或128（IPv6）。 - cidr和mask参数必须输入一个，两者同时输入时不能冲突。 - 子网预留网段不能包含所属子网的已使用的地址和系统预留地址（子网的第1个和最后2个地址）。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param cidr: The cidr of this CreateVirsubnetCidrReservationOption.
        :type cidr: str
        """
        self._cidr = cidr

    @property
    def mask(self):
        r"""Gets the mask of this CreateVirsubnetCidrReservationOption.

        **参数解释**： 子网预留网段的IP网段掩码长度。 **约束限制**： - 整数，预留网段的掩码长度最小值为“所属子网的网段掩码 + 2”，最大值为32（IPv4）或128（IPv6）。 - cidr和mask参数必须输入一个，两者同时输入时不能冲突。 - 子网预留网段不能包含所属子网的已使用的地址和系统预留地址（子网的第1个和最后2个地址）。 - 指定掩码长度创建预留网段，最后mask与子网掩码的差值长度的bit位由系统自动分配，例如子网cidr为192.168.21.0/24，子网掩码长度24，指定预留网段长度为27，差值长度27 - 24 = 3，即第25,26,27这3个bit位由系统自动分配。例如：   - 第25-27的bit位分配为011，最终创建出的子网预留网段cidr是192.168.21.96/27，其中96转为二进制是0110 0000；   - 第25-27的bit位分配为110，最终创建出的子网预留网段cidr是192.168.21.192/27，其中192转为二进制是1100 0000。  **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The mask of this CreateVirsubnetCidrReservationOption.
        :rtype: int
        """
        return self._mask

    @mask.setter
    def mask(self, mask):
        r"""Sets the mask of this CreateVirsubnetCidrReservationOption.

        **参数解释**： 子网预留网段的IP网段掩码长度。 **约束限制**： - 整数，预留网段的掩码长度最小值为“所属子网的网段掩码 + 2”，最大值为32（IPv4）或128（IPv6）。 - cidr和mask参数必须输入一个，两者同时输入时不能冲突。 - 子网预留网段不能包含所属子网的已使用的地址和系统预留地址（子网的第1个和最后2个地址）。 - 指定掩码长度创建预留网段，最后mask与子网掩码的差值长度的bit位由系统自动分配，例如子网cidr为192.168.21.0/24，子网掩码长度24，指定预留网段长度为27，差值长度27 - 24 = 3，即第25,26,27这3个bit位由系统自动分配。例如：   - 第25-27的bit位分配为011，最终创建出的子网预留网段cidr是192.168.21.96/27，其中96转为二进制是0110 0000；   - 第25-27的bit位分配为110，最终创建出的子网预留网段cidr是192.168.21.192/27，其中192转为二进制是1100 0000。  **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param mask: The mask of this CreateVirsubnetCidrReservationOption.
        :type mask: int
        """
        self._mask = mask

    @property
    def name(self):
        r"""Gets the name of this CreateVirsubnetCidrReservationOption.

        **参数解释**： 子网预留网段的名称。 **约束限制**： 1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The name of this CreateVirsubnetCidrReservationOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateVirsubnetCidrReservationOption.

        **参数解释**： 子网预留网段的名称。 **约束限制**： 1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param name: The name of this CreateVirsubnetCidrReservationOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateVirsubnetCidrReservationOption.

        **参数解释**： 子网预留网段的描述信息。 **约束限制**： 0-255个字符，不能包含“<”和“>”。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The description of this CreateVirsubnetCidrReservationOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateVirsubnetCidrReservationOption.

        **参数解释**： 子网预留网段的描述信息。 **约束限制**： 0-255个字符，不能包含“<”和“>”。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param description: The description of this CreateVirsubnetCidrReservationOption.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateVirsubnetCidrReservationOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
