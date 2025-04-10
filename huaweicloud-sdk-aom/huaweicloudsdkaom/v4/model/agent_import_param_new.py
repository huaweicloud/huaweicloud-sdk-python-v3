# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgentImportParamNew:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'password': 'str',
        'agent_id': 'str',
        'inner_ip': 'str',
        'port': 'int',
        'account': 'str',
        'os_type': 'str',
        'vpc_id': 'str',
        'coc_cmdb_id': 'str'
    }

    attribute_map = {
        'password': 'password',
        'agent_id': 'agent_id',
        'inner_ip': 'inner_ip',
        'port': 'port',
        'account': 'account',
        'os_type': 'os_type',
        'vpc_id': 'vpc_id',
        'coc_cmdb_id': 'coc_cmdb_id'
    }

    def __init__(self, password=None, agent_id=None, inner_ip=None, port=None, account=None, os_type=None, vpc_id=None, coc_cmdb_id=None):
        r"""AgentImportParamNew

        The model defined in huaweicloud sdk

        :param password: 机器登录密码。
        :type password: str
        :param agent_id: agent唯一值，重复导入时需要传递。
        :type agent_id: str
        :param inner_ip: 机器IP。
        :type inner_ip: str
        :param port: 机器登录端口，默认22。
        :type port: int
        :param account: 机器ssh账号。
        :type account: str
        :param os_type: 机器操作系统类型。
        :type os_type: str
        :param vpc_id: 机器所属VPC ID。
        :type vpc_id: str
        :param coc_cmdb_id: 外来唯一标识，COC用。
        :type coc_cmdb_id: str
        """
        
        

        self._password = None
        self._agent_id = None
        self._inner_ip = None
        self._port = None
        self._account = None
        self._os_type = None
        self._vpc_id = None
        self._coc_cmdb_id = None
        self.discriminator = None

        self.password = password
        if agent_id is not None:
            self.agent_id = agent_id
        self.inner_ip = inner_ip
        self.port = port
        self.account = account
        self.os_type = os_type
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if coc_cmdb_id is not None:
            self.coc_cmdb_id = coc_cmdb_id

    @property
    def password(self):
        r"""Gets the password of this AgentImportParamNew.

        机器登录密码。

        :return: The password of this AgentImportParamNew.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this AgentImportParamNew.

        机器登录密码。

        :param password: The password of this AgentImportParamNew.
        :type password: str
        """
        self._password = password

    @property
    def agent_id(self):
        r"""Gets the agent_id of this AgentImportParamNew.

        agent唯一值，重复导入时需要传递。

        :return: The agent_id of this AgentImportParamNew.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this AgentImportParamNew.

        agent唯一值，重复导入时需要传递。

        :param agent_id: The agent_id of this AgentImportParamNew.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def inner_ip(self):
        r"""Gets the inner_ip of this AgentImportParamNew.

        机器IP。

        :return: The inner_ip of this AgentImportParamNew.
        :rtype: str
        """
        return self._inner_ip

    @inner_ip.setter
    def inner_ip(self, inner_ip):
        r"""Sets the inner_ip of this AgentImportParamNew.

        机器IP。

        :param inner_ip: The inner_ip of this AgentImportParamNew.
        :type inner_ip: str
        """
        self._inner_ip = inner_ip

    @property
    def port(self):
        r"""Gets the port of this AgentImportParamNew.

        机器登录端口，默认22。

        :return: The port of this AgentImportParamNew.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this AgentImportParamNew.

        机器登录端口，默认22。

        :param port: The port of this AgentImportParamNew.
        :type port: int
        """
        self._port = port

    @property
    def account(self):
        r"""Gets the account of this AgentImportParamNew.

        机器ssh账号。

        :return: The account of this AgentImportParamNew.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        r"""Sets the account of this AgentImportParamNew.

        机器ssh账号。

        :param account: The account of this AgentImportParamNew.
        :type account: str
        """
        self._account = account

    @property
    def os_type(self):
        r"""Gets the os_type of this AgentImportParamNew.

        机器操作系统类型。

        :return: The os_type of this AgentImportParamNew.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this AgentImportParamNew.

        机器操作系统类型。

        :param os_type: The os_type of this AgentImportParamNew.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this AgentImportParamNew.

        机器所属VPC ID。

        :return: The vpc_id of this AgentImportParamNew.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this AgentImportParamNew.

        机器所属VPC ID。

        :param vpc_id: The vpc_id of this AgentImportParamNew.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def coc_cmdb_id(self):
        r"""Gets the coc_cmdb_id of this AgentImportParamNew.

        外来唯一标识，COC用。

        :return: The coc_cmdb_id of this AgentImportParamNew.
        :rtype: str
        """
        return self._coc_cmdb_id

    @coc_cmdb_id.setter
    def coc_cmdb_id(self, coc_cmdb_id):
        r"""Sets the coc_cmdb_id of this AgentImportParamNew.

        外来唯一标识，COC用。

        :param coc_cmdb_id: The coc_cmdb_id of this AgentImportParamNew.
        :type coc_cmdb_id: str
        """
        self._coc_cmdb_id = coc_cmdb_id

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
        if not isinstance(other, AgentImportParamNew):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
