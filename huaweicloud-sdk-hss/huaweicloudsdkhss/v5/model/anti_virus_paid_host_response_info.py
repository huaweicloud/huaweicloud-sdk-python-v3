# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AntiVirusPaidHostResponseInfo:

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
        'group_id': 'str',
        'public_ip': 'str',
        'private_ip': 'str',
        'agent_id': 'str',
        'os_type': 'str'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_name': 'host_name',
        'group_id': 'group_id',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'agent_id': 'agent_id',
        'os_type': 'os_type'
    }

    def __init__(self, host_id=None, host_name=None, group_id=None, public_ip=None, private_ip=None, agent_id=None, os_type=None):
        r"""AntiVirusPaidHostResponseInfo

        The model defined in huaweicloud sdk

        :param host_id: **参数解释**： 主机ID **取值范围**： 字符长度1-64位 
        :type host_id: str
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 
        :type host_name: str
        :param group_id: **参数解释**: 服务器组ID **取值范围**: 字符长度0-64位 
        :type group_id: str
        :param public_ip: **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 
        :type public_ip: str
        :param private_ip: **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 
        :type private_ip: str
        :param agent_id: **参数解释**: Agent ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type agent_id: str
        :param os_type: 操作系统类型，包含如下2种。   - Linux ：Linux   - Windows ：Windows
        :type os_type: str
        """
        
        

        self._host_id = None
        self._host_name = None
        self._group_id = None
        self._public_ip = None
        self._private_ip = None
        self._agent_id = None
        self._os_type = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if group_id is not None:
            self.group_id = group_id
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if agent_id is not None:
            self.agent_id = agent_id
        if os_type is not None:
            self.os_type = os_type

    @property
    def host_id(self):
        r"""Gets the host_id of this AntiVirusPaidHostResponseInfo.

        **参数解释**： 主机ID **取值范围**： 字符长度1-64位 

        :return: The host_id of this AntiVirusPaidHostResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this AntiVirusPaidHostResponseInfo.

        **参数解释**： 主机ID **取值范围**： 字符长度1-64位 

        :param host_id: The host_id of this AntiVirusPaidHostResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this AntiVirusPaidHostResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :return: The host_name of this AntiVirusPaidHostResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this AntiVirusPaidHostResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :param host_name: The host_name of this AntiVirusPaidHostResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def group_id(self):
        r"""Gets the group_id of this AntiVirusPaidHostResponseInfo.

        **参数解释**: 服务器组ID **取值范围**: 字符长度0-64位 

        :return: The group_id of this AntiVirusPaidHostResponseInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this AntiVirusPaidHostResponseInfo.

        **参数解释**: 服务器组ID **取值范围**: 字符长度0-64位 

        :param group_id: The group_id of this AntiVirusPaidHostResponseInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def public_ip(self):
        r"""Gets the public_ip of this AntiVirusPaidHostResponseInfo.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 

        :return: The public_ip of this AntiVirusPaidHostResponseInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this AntiVirusPaidHostResponseInfo.

        **参数解释**： 弹性公网IP地址 **取值范围**： 字符长度1-256位 

        :param public_ip: The public_ip of this AntiVirusPaidHostResponseInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this AntiVirusPaidHostResponseInfo.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :return: The private_ip of this AntiVirusPaidHostResponseInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this AntiVirusPaidHostResponseInfo.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :param private_ip: The private_ip of this AntiVirusPaidHostResponseInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def agent_id(self):
        r"""Gets the agent_id of this AntiVirusPaidHostResponseInfo.

        **参数解释**: Agent ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The agent_id of this AntiVirusPaidHostResponseInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this AntiVirusPaidHostResponseInfo.

        **参数解释**: Agent ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param agent_id: The agent_id of this AntiVirusPaidHostResponseInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def os_type(self):
        r"""Gets the os_type of this AntiVirusPaidHostResponseInfo.

        操作系统类型，包含如下2种。   - Linux ：Linux   - Windows ：Windows

        :return: The os_type of this AntiVirusPaidHostResponseInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this AntiVirusPaidHostResponseInfo.

        操作系统类型，包含如下2种。   - Linux ：Linux   - Windows ：Windows

        :param os_type: The os_type of this AntiVirusPaidHostResponseInfo.
        :type os_type: str
        """
        self._os_type = os_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AntiVirusPaidHostResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
