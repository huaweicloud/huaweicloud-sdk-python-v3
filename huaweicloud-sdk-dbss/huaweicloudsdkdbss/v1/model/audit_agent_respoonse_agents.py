# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuditAgentRespoonseAgents:

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
        'agent_type': 'str',
        'agent_os': 'str',
        'agent_ip': 'str',
        'mem_threshold': 'int',
        'cpu_threshold': 'int',
        'status': 'int',
        'agent_nic': 'str',
        'db_name': 'str',
        'datacap_status': 'int',
        'agent_url': 'str',
        'universal': 'bool',
        'sha256': 'str'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'agent_type': 'agent_type',
        'agent_os': 'agent_os',
        'agent_ip': 'agent_ip',
        'mem_threshold': 'mem_threshold',
        'cpu_threshold': 'cpu_threshold',
        'status': 'status',
        'agent_nic': 'agent_nic',
        'db_name': 'db_name',
        'datacap_status': 'datacap_status',
        'agent_url': 'agent_url',
        'universal': 'universal',
        'sha256': 'sha256'
    }

    def __init__(self, agent_id=None, agent_type=None, agent_os=None, agent_ip=None, mem_threshold=None, cpu_threshold=None, status=None, agent_nic=None, db_name=None, datacap_status=None, agent_url=None, universal=None, sha256=None):
        r"""AuditAgentRespoonseAgents

        The model defined in huaweicloud sdk

        :param agent_id: agent ID
        :type agent_id: str
        :param agent_type: agent 类型
        :type agent_type: str
        :param agent_os: agent OS
        :type agent_os: str
        :param agent_ip: agent安装节点IP
        :type agent_ip: str
        :param mem_threshold: 内存阈值
        :type mem_threshold: int
        :param cpu_threshold: cpu阈值
        :type cpu_threshold: int
        :param status: agent状态
        :type status: int
        :param agent_nic: agent网卡
        :type agent_nic: str
        :param db_name: 数据库名称
        :type db_name: str
        :param datacap_status: 数据流量抓取状态
        :type datacap_status: int
        :param agent_url: agent安装地址
        :type agent_url: str
        :param universal: 是否CCE场景
        :type universal: bool
        :param sha256: sha256值
        :type sha256: str
        """
        
        

        self._agent_id = None
        self._agent_type = None
        self._agent_os = None
        self._agent_ip = None
        self._mem_threshold = None
        self._cpu_threshold = None
        self._status = None
        self._agent_nic = None
        self._db_name = None
        self._datacap_status = None
        self._agent_url = None
        self._universal = None
        self._sha256 = None
        self.discriminator = None

        self.agent_id = agent_id
        self.agent_type = agent_type
        self.agent_os = agent_os
        self.agent_ip = agent_ip
        if mem_threshold is not None:
            self.mem_threshold = mem_threshold
        if cpu_threshold is not None:
            self.cpu_threshold = cpu_threshold
        if status is not None:
            self.status = status
        if agent_nic is not None:
            self.agent_nic = agent_nic
        if db_name is not None:
            self.db_name = db_name
        if datacap_status is not None:
            self.datacap_status = datacap_status
        if agent_url is not None:
            self.agent_url = agent_url
        if universal is not None:
            self.universal = universal
        if sha256 is not None:
            self.sha256 = sha256

    @property
    def agent_id(self):
        r"""Gets the agent_id of this AuditAgentRespoonseAgents.

        agent ID

        :return: The agent_id of this AuditAgentRespoonseAgents.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this AuditAgentRespoonseAgents.

        agent ID

        :param agent_id: The agent_id of this AuditAgentRespoonseAgents.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def agent_type(self):
        r"""Gets the agent_type of this AuditAgentRespoonseAgents.

        agent 类型

        :return: The agent_type of this AuditAgentRespoonseAgents.
        :rtype: str
        """
        return self._agent_type

    @agent_type.setter
    def agent_type(self, agent_type):
        r"""Sets the agent_type of this AuditAgentRespoonseAgents.

        agent 类型

        :param agent_type: The agent_type of this AuditAgentRespoonseAgents.
        :type agent_type: str
        """
        self._agent_type = agent_type

    @property
    def agent_os(self):
        r"""Gets the agent_os of this AuditAgentRespoonseAgents.

        agent OS

        :return: The agent_os of this AuditAgentRespoonseAgents.
        :rtype: str
        """
        return self._agent_os

    @agent_os.setter
    def agent_os(self, agent_os):
        r"""Sets the agent_os of this AuditAgentRespoonseAgents.

        agent OS

        :param agent_os: The agent_os of this AuditAgentRespoonseAgents.
        :type agent_os: str
        """
        self._agent_os = agent_os

    @property
    def agent_ip(self):
        r"""Gets the agent_ip of this AuditAgentRespoonseAgents.

        agent安装节点IP

        :return: The agent_ip of this AuditAgentRespoonseAgents.
        :rtype: str
        """
        return self._agent_ip

    @agent_ip.setter
    def agent_ip(self, agent_ip):
        r"""Sets the agent_ip of this AuditAgentRespoonseAgents.

        agent安装节点IP

        :param agent_ip: The agent_ip of this AuditAgentRespoonseAgents.
        :type agent_ip: str
        """
        self._agent_ip = agent_ip

    @property
    def mem_threshold(self):
        r"""Gets the mem_threshold of this AuditAgentRespoonseAgents.

        内存阈值

        :return: The mem_threshold of this AuditAgentRespoonseAgents.
        :rtype: int
        """
        return self._mem_threshold

    @mem_threshold.setter
    def mem_threshold(self, mem_threshold):
        r"""Sets the mem_threshold of this AuditAgentRespoonseAgents.

        内存阈值

        :param mem_threshold: The mem_threshold of this AuditAgentRespoonseAgents.
        :type mem_threshold: int
        """
        self._mem_threshold = mem_threshold

    @property
    def cpu_threshold(self):
        r"""Gets the cpu_threshold of this AuditAgentRespoonseAgents.

        cpu阈值

        :return: The cpu_threshold of this AuditAgentRespoonseAgents.
        :rtype: int
        """
        return self._cpu_threshold

    @cpu_threshold.setter
    def cpu_threshold(self, cpu_threshold):
        r"""Sets the cpu_threshold of this AuditAgentRespoonseAgents.

        cpu阈值

        :param cpu_threshold: The cpu_threshold of this AuditAgentRespoonseAgents.
        :type cpu_threshold: int
        """
        self._cpu_threshold = cpu_threshold

    @property
    def status(self):
        r"""Gets the status of this AuditAgentRespoonseAgents.

        agent状态

        :return: The status of this AuditAgentRespoonseAgents.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AuditAgentRespoonseAgents.

        agent状态

        :param status: The status of this AuditAgentRespoonseAgents.
        :type status: int
        """
        self._status = status

    @property
    def agent_nic(self):
        r"""Gets the agent_nic of this AuditAgentRespoonseAgents.

        agent网卡

        :return: The agent_nic of this AuditAgentRespoonseAgents.
        :rtype: str
        """
        return self._agent_nic

    @agent_nic.setter
    def agent_nic(self, agent_nic):
        r"""Sets the agent_nic of this AuditAgentRespoonseAgents.

        agent网卡

        :param agent_nic: The agent_nic of this AuditAgentRespoonseAgents.
        :type agent_nic: str
        """
        self._agent_nic = agent_nic

    @property
    def db_name(self):
        r"""Gets the db_name of this AuditAgentRespoonseAgents.

        数据库名称

        :return: The db_name of this AuditAgentRespoonseAgents.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this AuditAgentRespoonseAgents.

        数据库名称

        :param db_name: The db_name of this AuditAgentRespoonseAgents.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def datacap_status(self):
        r"""Gets the datacap_status of this AuditAgentRespoonseAgents.

        数据流量抓取状态

        :return: The datacap_status of this AuditAgentRespoonseAgents.
        :rtype: int
        """
        return self._datacap_status

    @datacap_status.setter
    def datacap_status(self, datacap_status):
        r"""Sets the datacap_status of this AuditAgentRespoonseAgents.

        数据流量抓取状态

        :param datacap_status: The datacap_status of this AuditAgentRespoonseAgents.
        :type datacap_status: int
        """
        self._datacap_status = datacap_status

    @property
    def agent_url(self):
        r"""Gets the agent_url of this AuditAgentRespoonseAgents.

        agent安装地址

        :return: The agent_url of this AuditAgentRespoonseAgents.
        :rtype: str
        """
        return self._agent_url

    @agent_url.setter
    def agent_url(self, agent_url):
        r"""Sets the agent_url of this AuditAgentRespoonseAgents.

        agent安装地址

        :param agent_url: The agent_url of this AuditAgentRespoonseAgents.
        :type agent_url: str
        """
        self._agent_url = agent_url

    @property
    def universal(self):
        r"""Gets the universal of this AuditAgentRespoonseAgents.

        是否CCE场景

        :return: The universal of this AuditAgentRespoonseAgents.
        :rtype: bool
        """
        return self._universal

    @universal.setter
    def universal(self, universal):
        r"""Sets the universal of this AuditAgentRespoonseAgents.

        是否CCE场景

        :param universal: The universal of this AuditAgentRespoonseAgents.
        :type universal: bool
        """
        self._universal = universal

    @property
    def sha256(self):
        r"""Gets the sha256 of this AuditAgentRespoonseAgents.

        sha256值

        :return: The sha256 of this AuditAgentRespoonseAgents.
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        r"""Sets the sha256 of this AuditAgentRespoonseAgents.

        sha256值

        :param sha256: The sha256 of this AuditAgentRespoonseAgents.
        :type sha256: str
        """
        self._sha256 = sha256

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
        if not isinstance(other, AuditAgentRespoonseAgents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
