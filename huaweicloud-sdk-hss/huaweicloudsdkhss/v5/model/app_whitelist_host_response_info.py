# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppWhitelistHostResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_id': 'str',
        'host_id': 'str',
        'host_name': 'str',
        'public_ip': 'str',
        'private_ip': 'str',
        'os_type': 'str',
        'os_name': 'str',
        'asset_value': 'str',
        'host_status': 'str',
        'agent_status': 'str'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'host_id': 'host_id',
        'host_name': 'host_name',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'os_type': 'os_type',
        'os_name': 'os_name',
        'asset_value': 'asset_value',
        'host_status': 'host_status',
        'agent_status': 'agent_status'
    }

    def __init__(self, agent_id=None, host_id=None, host_name=None, public_ip=None, private_ip=None, os_type=None, os_name=None, asset_value=None, host_status=None, agent_status=None):
        r"""AppWhitelistHostResponseInfo

        The model defined in huaweicloud sdk

        :param agent_id: **参数解释**: 主机上安装的杀毒Agent的唯一标识ID，用于关联主机与杀毒服务 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type agent_id: str
        :param host_id: **参数解释**： 服务器（主机）的唯一标识ID **取值范围**： 字符长度1-64位 
        :type host_id: str
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 
        :type host_name: str
        :param public_ip: **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位，支持IPv4或IPv6格式（IPv4长度7-15位，IPv6长度15-39位） 
        :type public_ip: str
        :param private_ip: **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 
        :type private_ip: str
        :param os_type: **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux - Windows：Windows 
        :type os_type: str
        :param os_name: **参数解释**: 操作系统名称 **取值范围**: 字符长度0-128位 
        :type os_name: str
        :param asset_value: **参数解释**： 资产重要性。 **取值范围**： - important ：重要资产。 - common ：一般资产。 - test ：测试资产。
        :type asset_value: str
        :param host_status: **参数解释**： 主机状态 **取值范围**: - ACTIVE：正在运行 - SHUTOFF：关机 - BUILDING：创建中 - ERROR：故障 
        :type host_status: str
        :param agent_status: **参数解释**： Agent状态 **取值范围**: - installed：已安装 - not_installed：未安 - online：在线 - offline：离线 - install_failed：安装失败 - installing：安装中 - not_online：不在线的（除了在线以外的所有状态，仅作为查询条件） 
        :type agent_status: str
        """
        
        

        self._agent_id = None
        self._host_id = None
        self._host_name = None
        self._public_ip = None
        self._private_ip = None
        self._os_type = None
        self._os_name = None
        self._asset_value = None
        self._host_status = None
        self._agent_status = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if os_type is not None:
            self.os_type = os_type
        if os_name is not None:
            self.os_name = os_name
        if asset_value is not None:
            self.asset_value = asset_value
        if host_status is not None:
            self.host_status = host_status
        if agent_status is not None:
            self.agent_status = agent_status

    @property
    def agent_id(self):
        r"""Gets the agent_id of this AppWhitelistHostResponseInfo.

        **参数解释**: 主机上安装的杀毒Agent的唯一标识ID，用于关联主机与杀毒服务 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The agent_id of this AppWhitelistHostResponseInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this AppWhitelistHostResponseInfo.

        **参数解释**: 主机上安装的杀毒Agent的唯一标识ID，用于关联主机与杀毒服务 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param agent_id: The agent_id of this AppWhitelistHostResponseInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def host_id(self):
        r"""Gets the host_id of this AppWhitelistHostResponseInfo.

        **参数解释**： 服务器（主机）的唯一标识ID **取值范围**： 字符长度1-64位 

        :return: The host_id of this AppWhitelistHostResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this AppWhitelistHostResponseInfo.

        **参数解释**： 服务器（主机）的唯一标识ID **取值范围**： 字符长度1-64位 

        :param host_id: The host_id of this AppWhitelistHostResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this AppWhitelistHostResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :return: The host_name of this AppWhitelistHostResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this AppWhitelistHostResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :param host_name: The host_name of this AppWhitelistHostResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def public_ip(self):
        r"""Gets the public_ip of this AppWhitelistHostResponseInfo.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位，支持IPv4或IPv6格式（IPv4长度7-15位，IPv6长度15-39位） 

        :return: The public_ip of this AppWhitelistHostResponseInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this AppWhitelistHostResponseInfo.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位，支持IPv4或IPv6格式（IPv4长度7-15位，IPv6长度15-39位） 

        :param public_ip: The public_ip of this AppWhitelistHostResponseInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this AppWhitelistHostResponseInfo.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :return: The private_ip of this AppWhitelistHostResponseInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this AppWhitelistHostResponseInfo.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :param private_ip: The private_ip of this AppWhitelistHostResponseInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def os_type(self):
        r"""Gets the os_type of this AppWhitelistHostResponseInfo.

        **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux - Windows：Windows 

        :return: The os_type of this AppWhitelistHostResponseInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this AppWhitelistHostResponseInfo.

        **参数解释**： 操作系统类型 **取值范围**： - Linux：Linux - Windows：Windows 

        :param os_type: The os_type of this AppWhitelistHostResponseInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def os_name(self):
        r"""Gets the os_name of this AppWhitelistHostResponseInfo.

        **参数解释**: 操作系统名称 **取值范围**: 字符长度0-128位 

        :return: The os_name of this AppWhitelistHostResponseInfo.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        r"""Sets the os_name of this AppWhitelistHostResponseInfo.

        **参数解释**: 操作系统名称 **取值范围**: 字符长度0-128位 

        :param os_name: The os_name of this AppWhitelistHostResponseInfo.
        :type os_name: str
        """
        self._os_name = os_name

    @property
    def asset_value(self):
        r"""Gets the asset_value of this AppWhitelistHostResponseInfo.

        **参数解释**： 资产重要性。 **取值范围**： - important ：重要资产。 - common ：一般资产。 - test ：测试资产。

        :return: The asset_value of this AppWhitelistHostResponseInfo.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this AppWhitelistHostResponseInfo.

        **参数解释**： 资产重要性。 **取值范围**： - important ：重要资产。 - common ：一般资产。 - test ：测试资产。

        :param asset_value: The asset_value of this AppWhitelistHostResponseInfo.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def host_status(self):
        r"""Gets the host_status of this AppWhitelistHostResponseInfo.

        **参数解释**： 主机状态 **取值范围**: - ACTIVE：正在运行 - SHUTOFF：关机 - BUILDING：创建中 - ERROR：故障 

        :return: The host_status of this AppWhitelistHostResponseInfo.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        r"""Sets the host_status of this AppWhitelistHostResponseInfo.

        **参数解释**： 主机状态 **取值范围**: - ACTIVE：正在运行 - SHUTOFF：关机 - BUILDING：创建中 - ERROR：故障 

        :param host_status: The host_status of this AppWhitelistHostResponseInfo.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def agent_status(self):
        r"""Gets the agent_status of this AppWhitelistHostResponseInfo.

        **参数解释**： Agent状态 **取值范围**: - installed：已安装 - not_installed：未安 - online：在线 - offline：离线 - install_failed：安装失败 - installing：安装中 - not_online：不在线的（除了在线以外的所有状态，仅作为查询条件） 

        :return: The agent_status of this AppWhitelistHostResponseInfo.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this AppWhitelistHostResponseInfo.

        **参数解释**： Agent状态 **取值范围**: - installed：已安装 - not_installed：未安 - online：在线 - offline：离线 - install_failed：安装失败 - installing：安装中 - not_online：不在线的（除了在线以外的所有状态，仅作为查询条件） 

        :param agent_status: The agent_status of this AppWhitelistHostResponseInfo.
        :type agent_status: str
        """
        self._agent_status = agent_status

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
        if not isinstance(other, AppWhitelistHostResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
