# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppliedHostListDataList:

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
        'applied_port': 'list[int]'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_name': 'host_name',
        'private_ip': 'private_ip',
        'agent_id': 'agent_id',
        'conflict_port': 'conflict_port',
        'applied_port': 'applied_port'
    }

    def __init__(self, host_id=None, host_name=None, private_ip=None, agent_id=None, conflict_port=None, applied_port=None):
        r"""AppliedHostListDataList

        The model defined in huaweicloud sdk

        :param host_id: **参数解释**： 主机ID **取值范围**： 字符长度1-64位 
        :type host_id: str
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 
        :type host_name: str
        :param private_ip: **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 
        :type private_ip: str
        :param agent_id: **参数解释**: Agent ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type agent_id: str
        :param conflict_port: 冲突的端口
        :type conflict_port: list[int]
        :param applied_port: 应用端口
        :type applied_port: list[int]
        """
        
        

        self._host_id = None
        self._host_name = None
        self._private_ip = None
        self._agent_id = None
        self._conflict_port = None
        self._applied_port = None
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
        if applied_port is not None:
            self.applied_port = applied_port

    @property
    def host_id(self):
        r"""Gets the host_id of this AppliedHostListDataList.

        **参数解释**： 主机ID **取值范围**： 字符长度1-64位 

        :return: The host_id of this AppliedHostListDataList.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this AppliedHostListDataList.

        **参数解释**： 主机ID **取值范围**： 字符长度1-64位 

        :param host_id: The host_id of this AppliedHostListDataList.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this AppliedHostListDataList.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :return: The host_name of this AppliedHostListDataList.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this AppliedHostListDataList.

        **参数解释**: 服务器名称 **取值范围**: 字符长度1-256位 

        :param host_name: The host_name of this AppliedHostListDataList.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def private_ip(self):
        r"""Gets the private_ip of this AppliedHostListDataList.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :return: The private_ip of this AppliedHostListDataList.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this AppliedHostListDataList.

        **参数解释**： 服务器私有IP **取值范围**： 字符长度1-128位 

        :param private_ip: The private_ip of this AppliedHostListDataList.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def agent_id(self):
        r"""Gets the agent_id of this AppliedHostListDataList.

        **参数解释**: Agent ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The agent_id of this AppliedHostListDataList.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this AppliedHostListDataList.

        **参数解释**: Agent ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param agent_id: The agent_id of this AppliedHostListDataList.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def conflict_port(self):
        r"""Gets the conflict_port of this AppliedHostListDataList.

        冲突的端口

        :return: The conflict_port of this AppliedHostListDataList.
        :rtype: list[int]
        """
        return self._conflict_port

    @conflict_port.setter
    def conflict_port(self, conflict_port):
        r"""Sets the conflict_port of this AppliedHostListDataList.

        冲突的端口

        :param conflict_port: The conflict_port of this AppliedHostListDataList.
        :type conflict_port: list[int]
        """
        self._conflict_port = conflict_port

    @property
    def applied_port(self):
        r"""Gets the applied_port of this AppliedHostListDataList.

        应用端口

        :return: The applied_port of this AppliedHostListDataList.
        :rtype: list[int]
        """
        return self._applied_port

    @applied_port.setter
    def applied_port(self, applied_port):
        r"""Sets the applied_port of this AppliedHostListDataList.

        应用端口

        :param applied_port: The applied_port of this AppliedHostListDataList.
        :type applied_port: list[int]
        """
        self._applied_port = applied_port

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
        if not isinstance(other, AppliedHostListDataList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
