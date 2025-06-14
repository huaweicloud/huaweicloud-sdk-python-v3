# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PortResponseInfo:

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
        'laddr': 'str',
        'status': 'str',
        'port': 'int',
        'type': 'str',
        'pid': 'int',
        'path': 'str',
        'agent_id': 'str',
        'container_id': 'str'
    }

    attribute_map = {
        'host_id': 'host_id',
        'laddr': 'laddr',
        'status': 'status',
        'port': 'port',
        'type': 'type',
        'pid': 'pid',
        'path': 'path',
        'agent_id': 'agent_id',
        'container_id': 'container_id'
    }

    def __init__(self, host_id=None, laddr=None, status=None, port=None, type=None, pid=None, path=None, agent_id=None, container_id=None):
        r"""PortResponseInfo

        The model defined in huaweicloud sdk

        :param host_id: 主机id
        :type host_id: str
        :param laddr: 监听ip
        :type laddr: str
        :param status: port status, normal, danger or unknow   - \&quot;normal\&quot; : 正常   - \&quot;danger\&quot; : 危险   - \&quot;unknown\&quot; : 未知
        :type status: str
        :param port: 端口号
        :type port: int
        :param type: 端口类型：目前包括TCP，UDP两种
        :type type: str
        :param pid: 进程ID
        :type pid: int
        :param path: 进程可执行文件路径
        :type path: str
        :param agent_id: agent id
        :type agent_id: str
        :param container_id: 容器id
        :type container_id: str
        """
        
        

        self._host_id = None
        self._laddr = None
        self._status = None
        self._port = None
        self._type = None
        self._pid = None
        self._path = None
        self._agent_id = None
        self._container_id = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if laddr is not None:
            self.laddr = laddr
        if status is not None:
            self.status = status
        if port is not None:
            self.port = port
        if type is not None:
            self.type = type
        if pid is not None:
            self.pid = pid
        if path is not None:
            self.path = path
        if agent_id is not None:
            self.agent_id = agent_id
        if container_id is not None:
            self.container_id = container_id

    @property
    def host_id(self):
        r"""Gets the host_id of this PortResponseInfo.

        主机id

        :return: The host_id of this PortResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this PortResponseInfo.

        主机id

        :param host_id: The host_id of this PortResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def laddr(self):
        r"""Gets the laddr of this PortResponseInfo.

        监听ip

        :return: The laddr of this PortResponseInfo.
        :rtype: str
        """
        return self._laddr

    @laddr.setter
    def laddr(self, laddr):
        r"""Sets the laddr of this PortResponseInfo.

        监听ip

        :param laddr: The laddr of this PortResponseInfo.
        :type laddr: str
        """
        self._laddr = laddr

    @property
    def status(self):
        r"""Gets the status of this PortResponseInfo.

        port status, normal, danger or unknow   - \"normal\" : 正常   - \"danger\" : 危险   - \"unknown\" : 未知

        :return: The status of this PortResponseInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this PortResponseInfo.

        port status, normal, danger or unknow   - \"normal\" : 正常   - \"danger\" : 危险   - \"unknown\" : 未知

        :param status: The status of this PortResponseInfo.
        :type status: str
        """
        self._status = status

    @property
    def port(self):
        r"""Gets the port of this PortResponseInfo.

        端口号

        :return: The port of this PortResponseInfo.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this PortResponseInfo.

        端口号

        :param port: The port of this PortResponseInfo.
        :type port: int
        """
        self._port = port

    @property
    def type(self):
        r"""Gets the type of this PortResponseInfo.

        端口类型：目前包括TCP，UDP两种

        :return: The type of this PortResponseInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PortResponseInfo.

        端口类型：目前包括TCP，UDP两种

        :param type: The type of this PortResponseInfo.
        :type type: str
        """
        self._type = type

    @property
    def pid(self):
        r"""Gets the pid of this PortResponseInfo.

        进程ID

        :return: The pid of this PortResponseInfo.
        :rtype: int
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        r"""Sets the pid of this PortResponseInfo.

        进程ID

        :param pid: The pid of this PortResponseInfo.
        :type pid: int
        """
        self._pid = pid

    @property
    def path(self):
        r"""Gets the path of this PortResponseInfo.

        进程可执行文件路径

        :return: The path of this PortResponseInfo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this PortResponseInfo.

        进程可执行文件路径

        :param path: The path of this PortResponseInfo.
        :type path: str
        """
        self._path = path

    @property
    def agent_id(self):
        r"""Gets the agent_id of this PortResponseInfo.

        agent id

        :return: The agent_id of this PortResponseInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this PortResponseInfo.

        agent id

        :param agent_id: The agent_id of this PortResponseInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def container_id(self):
        r"""Gets the container_id of this PortResponseInfo.

        容器id

        :return: The container_id of this PortResponseInfo.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this PortResponseInfo.

        容器id

        :param container_id: The container_id of this PortResponseInfo.
        :type container_id: str
        """
        self._container_id = container_id

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
        if not isinstance(other, PortResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
