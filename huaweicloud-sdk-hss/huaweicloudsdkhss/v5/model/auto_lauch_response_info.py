# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoLauchResponseInfo:

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
        'host_ip': 'str',
        'name': 'str',
        'type': 'int',
        'path': 'str',
        'hash': 'str',
        'run_user': 'str',
        'recent_scan_time': 'int'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'host_id': 'host_id',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'name': 'name',
        'type': 'type',
        'path': 'path',
        'hash': 'hash',
        'run_user': 'run_user',
        'recent_scan_time': 'recent_scan_time'
    }

    def __init__(self, agent_id=None, host_id=None, host_name=None, host_ip=None, name=None, type=None, path=None, hash=None, run_user=None, recent_scan_time=None):
        """AutoLauchResponseInfo

        The model defined in huaweicloud sdk

        :param agent_id: agent_id
        :type agent_id: str
        :param host_id: 主机id
        :type host_id: str
        :param host_name: 服务器名称
        :type host_name: str
        :param host_ip: 服务器ip
        :type host_ip: str
        :param name: 自启动项名称
        :type name: str
        :param type: 自启动项类型
        :type type: int
        :param path: 路径
        :type path: str
        :param hash: 文件hash
        :type hash: str
        :param run_user: 运行用户
        :type run_user: str
        :param recent_scan_time: 最近扫描时间
        :type recent_scan_time: int
        """
        
        

        self._agent_id = None
        self._host_id = None
        self._host_name = None
        self._host_ip = None
        self._name = None
        self._type = None
        self._path = None
        self._hash = None
        self._run_user = None
        self._recent_scan_time = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if path is not None:
            self.path = path
        if hash is not None:
            self.hash = hash
        if run_user is not None:
            self.run_user = run_user
        if recent_scan_time is not None:
            self.recent_scan_time = recent_scan_time

    @property
    def agent_id(self):
        """Gets the agent_id of this AutoLauchResponseInfo.

        agent_id

        :return: The agent_id of this AutoLauchResponseInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this AutoLauchResponseInfo.

        agent_id

        :param agent_id: The agent_id of this AutoLauchResponseInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def host_id(self):
        """Gets the host_id of this AutoLauchResponseInfo.

        主机id

        :return: The host_id of this AutoLauchResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this AutoLauchResponseInfo.

        主机id

        :param host_id: The host_id of this AutoLauchResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        """Gets the host_name of this AutoLauchResponseInfo.

        服务器名称

        :return: The host_name of this AutoLauchResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this AutoLauchResponseInfo.

        服务器名称

        :param host_name: The host_name of this AutoLauchResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        """Gets the host_ip of this AutoLauchResponseInfo.

        服务器ip

        :return: The host_ip of this AutoLauchResponseInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this AutoLauchResponseInfo.

        服务器ip

        :param host_ip: The host_ip of this AutoLauchResponseInfo.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def name(self):
        """Gets the name of this AutoLauchResponseInfo.

        自启动项名称

        :return: The name of this AutoLauchResponseInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AutoLauchResponseInfo.

        自启动项名称

        :param name: The name of this AutoLauchResponseInfo.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this AutoLauchResponseInfo.

        自启动项类型

        :return: The type of this AutoLauchResponseInfo.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AutoLauchResponseInfo.

        自启动项类型

        :param type: The type of this AutoLauchResponseInfo.
        :type type: int
        """
        self._type = type

    @property
    def path(self):
        """Gets the path of this AutoLauchResponseInfo.

        路径

        :return: The path of this AutoLauchResponseInfo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this AutoLauchResponseInfo.

        路径

        :param path: The path of this AutoLauchResponseInfo.
        :type path: str
        """
        self._path = path

    @property
    def hash(self):
        """Gets the hash of this AutoLauchResponseInfo.

        文件hash

        :return: The hash of this AutoLauchResponseInfo.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this AutoLauchResponseInfo.

        文件hash

        :param hash: The hash of this AutoLauchResponseInfo.
        :type hash: str
        """
        self._hash = hash

    @property
    def run_user(self):
        """Gets the run_user of this AutoLauchResponseInfo.

        运行用户

        :return: The run_user of this AutoLauchResponseInfo.
        :rtype: str
        """
        return self._run_user

    @run_user.setter
    def run_user(self, run_user):
        """Sets the run_user of this AutoLauchResponseInfo.

        运行用户

        :param run_user: The run_user of this AutoLauchResponseInfo.
        :type run_user: str
        """
        self._run_user = run_user

    @property
    def recent_scan_time(self):
        """Gets the recent_scan_time of this AutoLauchResponseInfo.

        最近扫描时间

        :return: The recent_scan_time of this AutoLauchResponseInfo.
        :rtype: int
        """
        return self._recent_scan_time

    @recent_scan_time.setter
    def recent_scan_time(self, recent_scan_time):
        """Sets the recent_scan_time of this AutoLauchResponseInfo.

        最近扫描时间

        :param recent_scan_time: The recent_scan_time of this AutoLauchResponseInfo.
        :type recent_scan_time: int
        """
        self._recent_scan_time = recent_scan_time

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
        if not isinstance(other, AutoLauchResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
