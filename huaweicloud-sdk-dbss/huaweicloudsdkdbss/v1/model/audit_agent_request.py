# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuditAgentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_id': 'str',
        'mode': 'int',
        'agent_id': 'str',
        'agent_type': 'str',
        'agent_os': 'str',
        'agent_ip': 'str',
        'agent_nic': 'str',
        'cpu_threshold': 'int',
        'mem_threshold': 'int'
    }

    attribute_map = {
        'db_id': 'db_id',
        'mode': 'mode',
        'agent_id': 'agent_id',
        'agent_type': 'agent_type',
        'agent_os': 'agent_os',
        'agent_ip': 'agent_ip',
        'agent_nic': 'agent_nic',
        'cpu_threshold': 'cpu_threshold',
        'mem_threshold': 'mem_threshold'
    }

    def __init__(self, db_id=None, mode=None, agent_id=None, agent_type=None, agent_os=None, agent_ip=None, agent_nic=None, cpu_threshold=None, mem_threshold=None):
        r"""AuditAgentRequest

        The model defined in huaweicloud sdk

        :param db_id: 数据库ID, 可在查询数据库列表接口的ID字段获取。
        :type db_id: str
        :param mode: 模式 - 0：创建agent - 1：选择已有agent
        :type mode: int
        :param agent_id: 选择已有agent时必输
        :type agent_id: str
        :param agent_type: agent类型 - APP：应用端 - DB：数据库端
        :type agent_type: str
        :param agent_os: agent OS类型: - LINUX64_X86 - LINUX64_ARM - WINDOWS64
        :type agent_os: str
        :param agent_ip: agent IP，安装节点类型为应用端时必输。
        :type agent_ip: str
        :param agent_nic: agent审计网卡名称
        :type agent_nic: str
        :param cpu_threshold: CPU阈值
        :type cpu_threshold: int
        :param mem_threshold: 内存阈值
        :type mem_threshold: int
        """
        
        

        self._db_id = None
        self._mode = None
        self._agent_id = None
        self._agent_type = None
        self._agent_os = None
        self._agent_ip = None
        self._agent_nic = None
        self._cpu_threshold = None
        self._mem_threshold = None
        self.discriminator = None

        self.db_id = db_id
        self.mode = mode
        if agent_id is not None:
            self.agent_id = agent_id
        self.agent_type = agent_type
        self.agent_os = agent_os
        if agent_ip is not None:
            self.agent_ip = agent_ip
        if agent_nic is not None:
            self.agent_nic = agent_nic
        if cpu_threshold is not None:
            self.cpu_threshold = cpu_threshold
        if mem_threshold is not None:
            self.mem_threshold = mem_threshold

    @property
    def db_id(self):
        r"""Gets the db_id of this AuditAgentRequest.

        数据库ID, 可在查询数据库列表接口的ID字段获取。

        :return: The db_id of this AuditAgentRequest.
        :rtype: str
        """
        return self._db_id

    @db_id.setter
    def db_id(self, db_id):
        r"""Sets the db_id of this AuditAgentRequest.

        数据库ID, 可在查询数据库列表接口的ID字段获取。

        :param db_id: The db_id of this AuditAgentRequest.
        :type db_id: str
        """
        self._db_id = db_id

    @property
    def mode(self):
        r"""Gets the mode of this AuditAgentRequest.

        模式 - 0：创建agent - 1：选择已有agent

        :return: The mode of this AuditAgentRequest.
        :rtype: int
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this AuditAgentRequest.

        模式 - 0：创建agent - 1：选择已有agent

        :param mode: The mode of this AuditAgentRequest.
        :type mode: int
        """
        self._mode = mode

    @property
    def agent_id(self):
        r"""Gets the agent_id of this AuditAgentRequest.

        选择已有agent时必输

        :return: The agent_id of this AuditAgentRequest.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this AuditAgentRequest.

        选择已有agent时必输

        :param agent_id: The agent_id of this AuditAgentRequest.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def agent_type(self):
        r"""Gets the agent_type of this AuditAgentRequest.

        agent类型 - APP：应用端 - DB：数据库端

        :return: The agent_type of this AuditAgentRequest.
        :rtype: str
        """
        return self._agent_type

    @agent_type.setter
    def agent_type(self, agent_type):
        r"""Sets the agent_type of this AuditAgentRequest.

        agent类型 - APP：应用端 - DB：数据库端

        :param agent_type: The agent_type of this AuditAgentRequest.
        :type agent_type: str
        """
        self._agent_type = agent_type

    @property
    def agent_os(self):
        r"""Gets the agent_os of this AuditAgentRequest.

        agent OS类型: - LINUX64_X86 - LINUX64_ARM - WINDOWS64

        :return: The agent_os of this AuditAgentRequest.
        :rtype: str
        """
        return self._agent_os

    @agent_os.setter
    def agent_os(self, agent_os):
        r"""Sets the agent_os of this AuditAgentRequest.

        agent OS类型: - LINUX64_X86 - LINUX64_ARM - WINDOWS64

        :param agent_os: The agent_os of this AuditAgentRequest.
        :type agent_os: str
        """
        self._agent_os = agent_os

    @property
    def agent_ip(self):
        r"""Gets the agent_ip of this AuditAgentRequest.

        agent IP，安装节点类型为应用端时必输。

        :return: The agent_ip of this AuditAgentRequest.
        :rtype: str
        """
        return self._agent_ip

    @agent_ip.setter
    def agent_ip(self, agent_ip):
        r"""Sets the agent_ip of this AuditAgentRequest.

        agent IP，安装节点类型为应用端时必输。

        :param agent_ip: The agent_ip of this AuditAgentRequest.
        :type agent_ip: str
        """
        self._agent_ip = agent_ip

    @property
    def agent_nic(self):
        r"""Gets the agent_nic of this AuditAgentRequest.

        agent审计网卡名称

        :return: The agent_nic of this AuditAgentRequest.
        :rtype: str
        """
        return self._agent_nic

    @agent_nic.setter
    def agent_nic(self, agent_nic):
        r"""Sets the agent_nic of this AuditAgentRequest.

        agent审计网卡名称

        :param agent_nic: The agent_nic of this AuditAgentRequest.
        :type agent_nic: str
        """
        self._agent_nic = agent_nic

    @property
    def cpu_threshold(self):
        r"""Gets the cpu_threshold of this AuditAgentRequest.

        CPU阈值

        :return: The cpu_threshold of this AuditAgentRequest.
        :rtype: int
        """
        return self._cpu_threshold

    @cpu_threshold.setter
    def cpu_threshold(self, cpu_threshold):
        r"""Sets the cpu_threshold of this AuditAgentRequest.

        CPU阈值

        :param cpu_threshold: The cpu_threshold of this AuditAgentRequest.
        :type cpu_threshold: int
        """
        self._cpu_threshold = cpu_threshold

    @property
    def mem_threshold(self):
        r"""Gets the mem_threshold of this AuditAgentRequest.

        内存阈值

        :return: The mem_threshold of this AuditAgentRequest.
        :rtype: int
        """
        return self._mem_threshold

    @mem_threshold.setter
    def mem_threshold(self, mem_threshold):
        r"""Sets the mem_threshold of this AuditAgentRequest.

        内存阈值

        :param mem_threshold: The mem_threshold of this AuditAgentRequest.
        :type mem_threshold: int
        """
        self._mem_threshold = mem_threshold

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
        if not isinstance(other, AuditAgentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
