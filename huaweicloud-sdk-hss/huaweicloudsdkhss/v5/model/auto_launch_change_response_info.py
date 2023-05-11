# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoLaunchChangeResponseInfo:

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
        'variation_type': 'str',
        'type': 'int',
        'host_id': 'str',
        'host_name': 'str',
        'host_ip': 'str',
        'path': 'str',
        'hash': 'str',
        'run_user': 'str',
        'name': 'str',
        'recent_scan_time': 'int'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'variation_type': 'variation_type',
        'type': 'type',
        'host_id': 'host_id',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'path': 'path',
        'hash': 'hash',
        'run_user': 'run_user',
        'name': 'name',
        'recent_scan_time': 'recent_scan_time'
    }

    def __init__(self, agent_id=None, variation_type=None, type=None, host_id=None, host_name=None, host_ip=None, path=None, hash=None, run_user=None, name=None, recent_scan_time=None):
        """AutoLaunchChangeResponseInfo

        The model defined in huaweicloud sdk

        :param agent_id: agent_id
        :type agent_id: str
        :param variation_type: the type of change   - add ：新建   - delete ：删除   - modify ：修改
        :type variation_type: str
        :param type: 自启动项类型
        :type type: int
        :param host_id: host_id
        :type host_id: str
        :param host_name: 弹性服务器名称
        :type host_name: str
        :param host_ip: 主机IP
        :type host_ip: str
        :param path: 路径
        :type path: str
        :param hash: 文件hash
        :type hash: str
        :param run_user: 运行用户
        :type run_user: str
        :param name: 自启动项名称
        :type name: str
        :param recent_scan_time: 最近更新时间
        :type recent_scan_time: int
        """
        
        

        self._agent_id = None
        self._variation_type = None
        self._type = None
        self._host_id = None
        self._host_name = None
        self._host_ip = None
        self._path = None
        self._hash = None
        self._run_user = None
        self._name = None
        self._recent_scan_time = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if variation_type is not None:
            self.variation_type = variation_type
        if type is not None:
            self.type = type
        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        if path is not None:
            self.path = path
        if hash is not None:
            self.hash = hash
        if run_user is not None:
            self.run_user = run_user
        if name is not None:
            self.name = name
        if recent_scan_time is not None:
            self.recent_scan_time = recent_scan_time

    @property
    def agent_id(self):
        """Gets the agent_id of this AutoLaunchChangeResponseInfo.

        agent_id

        :return: The agent_id of this AutoLaunchChangeResponseInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this AutoLaunchChangeResponseInfo.

        agent_id

        :param agent_id: The agent_id of this AutoLaunchChangeResponseInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def variation_type(self):
        """Gets the variation_type of this AutoLaunchChangeResponseInfo.

        the type of change   - add ：新建   - delete ：删除   - modify ：修改

        :return: The variation_type of this AutoLaunchChangeResponseInfo.
        :rtype: str
        """
        return self._variation_type

    @variation_type.setter
    def variation_type(self, variation_type):
        """Sets the variation_type of this AutoLaunchChangeResponseInfo.

        the type of change   - add ：新建   - delete ：删除   - modify ：修改

        :param variation_type: The variation_type of this AutoLaunchChangeResponseInfo.
        :type variation_type: str
        """
        self._variation_type = variation_type

    @property
    def type(self):
        """Gets the type of this AutoLaunchChangeResponseInfo.

        自启动项类型

        :return: The type of this AutoLaunchChangeResponseInfo.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AutoLaunchChangeResponseInfo.

        自启动项类型

        :param type: The type of this AutoLaunchChangeResponseInfo.
        :type type: int
        """
        self._type = type

    @property
    def host_id(self):
        """Gets the host_id of this AutoLaunchChangeResponseInfo.

        host_id

        :return: The host_id of this AutoLaunchChangeResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this AutoLaunchChangeResponseInfo.

        host_id

        :param host_id: The host_id of this AutoLaunchChangeResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        """Gets the host_name of this AutoLaunchChangeResponseInfo.

        弹性服务器名称

        :return: The host_name of this AutoLaunchChangeResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this AutoLaunchChangeResponseInfo.

        弹性服务器名称

        :param host_name: The host_name of this AutoLaunchChangeResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        """Gets the host_ip of this AutoLaunchChangeResponseInfo.

        主机IP

        :return: The host_ip of this AutoLaunchChangeResponseInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this AutoLaunchChangeResponseInfo.

        主机IP

        :param host_ip: The host_ip of this AutoLaunchChangeResponseInfo.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def path(self):
        """Gets the path of this AutoLaunchChangeResponseInfo.

        路径

        :return: The path of this AutoLaunchChangeResponseInfo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this AutoLaunchChangeResponseInfo.

        路径

        :param path: The path of this AutoLaunchChangeResponseInfo.
        :type path: str
        """
        self._path = path

    @property
    def hash(self):
        """Gets the hash of this AutoLaunchChangeResponseInfo.

        文件hash

        :return: The hash of this AutoLaunchChangeResponseInfo.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this AutoLaunchChangeResponseInfo.

        文件hash

        :param hash: The hash of this AutoLaunchChangeResponseInfo.
        :type hash: str
        """
        self._hash = hash

    @property
    def run_user(self):
        """Gets the run_user of this AutoLaunchChangeResponseInfo.

        运行用户

        :return: The run_user of this AutoLaunchChangeResponseInfo.
        :rtype: str
        """
        return self._run_user

    @run_user.setter
    def run_user(self, run_user):
        """Sets the run_user of this AutoLaunchChangeResponseInfo.

        运行用户

        :param run_user: The run_user of this AutoLaunchChangeResponseInfo.
        :type run_user: str
        """
        self._run_user = run_user

    @property
    def name(self):
        """Gets the name of this AutoLaunchChangeResponseInfo.

        自启动项名称

        :return: The name of this AutoLaunchChangeResponseInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AutoLaunchChangeResponseInfo.

        自启动项名称

        :param name: The name of this AutoLaunchChangeResponseInfo.
        :type name: str
        """
        self._name = name

    @property
    def recent_scan_time(self):
        """Gets the recent_scan_time of this AutoLaunchChangeResponseInfo.

        最近更新时间

        :return: The recent_scan_time of this AutoLaunchChangeResponseInfo.
        :rtype: int
        """
        return self._recent_scan_time

    @recent_scan_time.setter
    def recent_scan_time(self, recent_scan_time):
        """Sets the recent_scan_time of this AutoLaunchChangeResponseInfo.

        最近更新时间

        :param recent_scan_time: The recent_scan_time of this AutoLaunchChangeResponseInfo.
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
        if not isinstance(other, AutoLaunchChangeResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
