# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityCheckPolicyGroupHostInfo:

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
        'agent_version': 'str',
        'version': 'str',
        'group_name': 'str'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'host_id': 'host_id',
        'host_name': 'host_name',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'agent_version': 'agent_version',
        'version': 'version',
        'group_name': 'group_name'
    }

    def __init__(self, agent_id=None, host_id=None, host_name=None, public_ip=None, private_ip=None, agent_version=None, version=None, group_name=None):
        r"""SecurityCheckPolicyGroupHostInfo

        The model defined in huaweicloud sdk

        :param agent_id: **参数解释**: agent id **取值范围**: 字符长度1-64位，支持字母、数字、连字符、下划线，不能以特殊字符开头或结尾 
        :type agent_id: str
        :param host_id: **参数解释**: 主机ID **取值范围**: 字符长度1-128 
        :type host_id: str
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 
        :type host_name: str
        :param public_ip: **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-128位 
        :type public_ip: str
        :param private_ip: **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 
        :type private_ip: str
        :param agent_version: **参数解释**： agent版本 **取值范围**: 字符长度1-64位 
        :type agent_version: str
        :param version: **参数解释**： 防护版本 **取值范围**: 字符长度1-256位 
        :type version: str
        :param group_name: **参数解释**： 服务器组名称 **取值范围**: 字符长度1-256位 
        :type group_name: str
        """
        
        

        self._agent_id = None
        self._host_id = None
        self._host_name = None
        self._public_ip = None
        self._private_ip = None
        self._agent_version = None
        self._version = None
        self._group_name = None
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
        if agent_version is not None:
            self.agent_version = agent_version
        if version is not None:
            self.version = version
        if group_name is not None:
            self.group_name = group_name

    @property
    def agent_id(self):
        r"""Gets the agent_id of this SecurityCheckPolicyGroupHostInfo.

        **参数解释**: agent id **取值范围**: 字符长度1-64位，支持字母、数字、连字符、下划线，不能以特殊字符开头或结尾 

        :return: The agent_id of this SecurityCheckPolicyGroupHostInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this SecurityCheckPolicyGroupHostInfo.

        **参数解释**: agent id **取值范围**: 字符长度1-64位，支持字母、数字、连字符、下划线，不能以特殊字符开头或结尾 

        :param agent_id: The agent_id of this SecurityCheckPolicyGroupHostInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def host_id(self):
        r"""Gets the host_id of this SecurityCheckPolicyGroupHostInfo.

        **参数解释**: 主机ID **取值范围**: 字符长度1-128 

        :return: The host_id of this SecurityCheckPolicyGroupHostInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this SecurityCheckPolicyGroupHostInfo.

        **参数解释**: 主机ID **取值范围**: 字符长度1-128 

        :param host_id: The host_id of this SecurityCheckPolicyGroupHostInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this SecurityCheckPolicyGroupHostInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :return: The host_name of this SecurityCheckPolicyGroupHostInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this SecurityCheckPolicyGroupHostInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :param host_name: The host_name of this SecurityCheckPolicyGroupHostInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def public_ip(self):
        r"""Gets the public_ip of this SecurityCheckPolicyGroupHostInfo.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-128位 

        :return: The public_ip of this SecurityCheckPolicyGroupHostInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this SecurityCheckPolicyGroupHostInfo.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-128位 

        :param public_ip: The public_ip of this SecurityCheckPolicyGroupHostInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this SecurityCheckPolicyGroupHostInfo.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :return: The private_ip of this SecurityCheckPolicyGroupHostInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this SecurityCheckPolicyGroupHostInfo.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :param private_ip: The private_ip of this SecurityCheckPolicyGroupHostInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def agent_version(self):
        r"""Gets the agent_version of this SecurityCheckPolicyGroupHostInfo.

        **参数解释**： agent版本 **取值范围**: 字符长度1-64位 

        :return: The agent_version of this SecurityCheckPolicyGroupHostInfo.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        r"""Sets the agent_version of this SecurityCheckPolicyGroupHostInfo.

        **参数解释**： agent版本 **取值范围**: 字符长度1-64位 

        :param agent_version: The agent_version of this SecurityCheckPolicyGroupHostInfo.
        :type agent_version: str
        """
        self._agent_version = agent_version

    @property
    def version(self):
        r"""Gets the version of this SecurityCheckPolicyGroupHostInfo.

        **参数解释**： 防护版本 **取值范围**: 字符长度1-256位 

        :return: The version of this SecurityCheckPolicyGroupHostInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this SecurityCheckPolicyGroupHostInfo.

        **参数解释**： 防护版本 **取值范围**: 字符长度1-256位 

        :param version: The version of this SecurityCheckPolicyGroupHostInfo.
        :type version: str
        """
        self._version = version

    @property
    def group_name(self):
        r"""Gets the group_name of this SecurityCheckPolicyGroupHostInfo.

        **参数解释**： 服务器组名称 **取值范围**: 字符长度1-256位 

        :return: The group_name of this SecurityCheckPolicyGroupHostInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this SecurityCheckPolicyGroupHostInfo.

        **参数解释**： 服务器组名称 **取值范围**: 字符长度1-256位 

        :param group_name: The group_name of this SecurityCheckPolicyGroupHostInfo.
        :type group_name: str
        """
        self._group_name = group_name

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
        if not isinstance(other, SecurityCheckPolicyGroupHostInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
