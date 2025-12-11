# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AvailableHostListDataList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'host_name': 'str',
        'private_ip': 'str',
        'agent_id': 'str',
        'conflict_port': 'list[int]',
        'os_type': 'str',
        'group_name': 'str',
        'group_id': 'str'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_name': 'host_name',
        'private_ip': 'private_ip',
        'agent_id': 'agent_id',
        'conflict_port': 'conflict_port',
        'os_type': 'os_type',
        'group_name': 'group_name',
        'group_id': 'group_id'
    }

    def __init__(self, host_id=None, host_name=None, private_ip=None, agent_id=None, conflict_port=None, os_type=None, group_name=None, group_id=None):
        r"""AvailableHostListDataList

        The model defined in huaweicloud sdk

        :param host_id: **参数解释**： 服务器（主机）的唯一标识ID **取值范围**： 字符长度1-64位 
        :type host_id: str
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 
        :type host_name: str
        :param private_ip: **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 
        :type private_ip: str
        :param agent_id: **参数解释**: 主机上安装的杀毒Agent的唯一标识ID，用于关联主机与杀毒服务 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type agent_id: str
        :param conflict_port: 冲突的端口
        :type conflict_port: list[int]
        :param os_type: 操作系统类型，包含如下2种。 - Linux ：Linux。 - Windows ：Windows.
        :type os_type: str
        :param group_name: 分组名称
        :type group_name: str
        :param group_id: 分组id
        :type group_id: str
        """
        
        

        self._host_id = None
        self._host_name = None
        self._private_ip = None
        self._agent_id = None
        self._conflict_port = None
        self._os_type = None
        self._group_name = None
        self._group_id = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if private_ip is not None:
            self.private_ip = private_ip
        if agent_id is not None:
            self.agent_id = agent_id
        if conflict_port is not None:
            self.conflict_port = conflict_port
        if os_type is not None:
            self.os_type = os_type
        if group_name is not None:
            self.group_name = group_name
        if group_id is not None:
            self.group_id = group_id

    @property
    def host_id(self):
        r"""Gets the host_id of this AvailableHostListDataList.

        **参数解释**： 服务器（主机）的唯一标识ID **取值范围**： 字符长度1-64位 

        :return: The host_id of this AvailableHostListDataList.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this AvailableHostListDataList.

        **参数解释**： 服务器（主机）的唯一标识ID **取值范围**： 字符长度1-64位 

        :param host_id: The host_id of this AvailableHostListDataList.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this AvailableHostListDataList.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :return: The host_name of this AvailableHostListDataList.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this AvailableHostListDataList.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :param host_name: The host_name of this AvailableHostListDataList.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def private_ip(self):
        r"""Gets the private_ip of this AvailableHostListDataList.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :return: The private_ip of this AvailableHostListDataList.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this AvailableHostListDataList.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :param private_ip: The private_ip of this AvailableHostListDataList.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def agent_id(self):
        r"""Gets the agent_id of this AvailableHostListDataList.

        **参数解释**: 主机上安装的杀毒Agent的唯一标识ID，用于关联主机与杀毒服务 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The agent_id of this AvailableHostListDataList.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this AvailableHostListDataList.

        **参数解释**: 主机上安装的杀毒Agent的唯一标识ID，用于关联主机与杀毒服务 **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param agent_id: The agent_id of this AvailableHostListDataList.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def conflict_port(self):
        r"""Gets the conflict_port of this AvailableHostListDataList.

        冲突的端口

        :return: The conflict_port of this AvailableHostListDataList.
        :rtype: list[int]
        """
        return self._conflict_port

    @conflict_port.setter
    def conflict_port(self, conflict_port):
        r"""Sets the conflict_port of this AvailableHostListDataList.

        冲突的端口

        :param conflict_port: The conflict_port of this AvailableHostListDataList.
        :type conflict_port: list[int]
        """
        self._conflict_port = conflict_port

    @property
    def os_type(self):
        r"""Gets the os_type of this AvailableHostListDataList.

        操作系统类型，包含如下2种。 - Linux ：Linux。 - Windows ：Windows.

        :return: The os_type of this AvailableHostListDataList.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this AvailableHostListDataList.

        操作系统类型，包含如下2种。 - Linux ：Linux。 - Windows ：Windows.

        :param os_type: The os_type of this AvailableHostListDataList.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def group_name(self):
        r"""Gets the group_name of this AvailableHostListDataList.

        分组名称

        :return: The group_name of this AvailableHostListDataList.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this AvailableHostListDataList.

        分组名称

        :param group_name: The group_name of this AvailableHostListDataList.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def group_id(self):
        r"""Gets the group_id of this AvailableHostListDataList.

        分组id

        :return: The group_id of this AvailableHostListDataList.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this AvailableHostListDataList.

        分组id

        :param group_id: The group_id of this AvailableHostListDataList.
        :type group_id: str
        """
        self._group_id = group_id

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
        if not isinstance(other, AvailableHostListDataList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
