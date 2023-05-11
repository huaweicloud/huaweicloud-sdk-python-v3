# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserResponseInfo:

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
        'user_name': 'str',
        'login_permission': 'bool',
        'root_permission': 'bool',
        'user_group_name': 'str',
        'user_home_dir': 'str',
        'shell': 'str',
        'expire_time': 'int',
        'recent_scan_time': 'int'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'host_id': 'host_id',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'user_name': 'user_name',
        'login_permission': 'login_permission',
        'root_permission': 'root_permission',
        'user_group_name': 'user_group_name',
        'user_home_dir': 'user_home_dir',
        'shell': 'shell',
        'expire_time': 'expire_time',
        'recent_scan_time': 'recent_scan_time'
    }

    def __init__(self, agent_id=None, host_id=None, host_name=None, host_ip=None, user_name=None, login_permission=None, root_permission=None, user_group_name=None, user_home_dir=None, shell=None, expire_time=None, recent_scan_time=None):
        """UserResponseInfo

        The model defined in huaweicloud sdk

        :param agent_id: agent_id
        :type agent_id: str
        :param host_id: 服务器ID
        :type host_id: str
        :param host_name: 服务器名称
        :type host_name: str
        :param host_ip: 服务器ip
        :type host_ip: str
        :param user_name: 用户名
        :type user_name: str
        :param login_permission: 是否有登陆权限
        :type login_permission: bool
        :param root_permission: 是否有root权限
        :type root_permission: bool
        :param user_group_name: 用户组
        :type user_group_name: str
        :param user_home_dir: 用户目录
        :type user_home_dir: str
        :param shell: 用户启动shell
        :type shell: str
        :param expire_time: 到期时间，采用时间戳，默认毫秒，
        :type expire_time: int
        :param recent_scan_time: 最近扫描时间
        :type recent_scan_time: int
        """
        
        

        self._agent_id = None
        self._host_id = None
        self._host_name = None
        self._host_ip = None
        self._user_name = None
        self._login_permission = None
        self._root_permission = None
        self._user_group_name = None
        self._user_home_dir = None
        self._shell = None
        self._expire_time = None
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
        if user_name is not None:
            self.user_name = user_name
        if login_permission is not None:
            self.login_permission = login_permission
        if root_permission is not None:
            self.root_permission = root_permission
        if user_group_name is not None:
            self.user_group_name = user_group_name
        if user_home_dir is not None:
            self.user_home_dir = user_home_dir
        if shell is not None:
            self.shell = shell
        if expire_time is not None:
            self.expire_time = expire_time
        if recent_scan_time is not None:
            self.recent_scan_time = recent_scan_time

    @property
    def agent_id(self):
        """Gets the agent_id of this UserResponseInfo.

        agent_id

        :return: The agent_id of this UserResponseInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this UserResponseInfo.

        agent_id

        :param agent_id: The agent_id of this UserResponseInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def host_id(self):
        """Gets the host_id of this UserResponseInfo.

        服务器ID

        :return: The host_id of this UserResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this UserResponseInfo.

        服务器ID

        :param host_id: The host_id of this UserResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        """Gets the host_name of this UserResponseInfo.

        服务器名称

        :return: The host_name of this UserResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this UserResponseInfo.

        服务器名称

        :param host_name: The host_name of this UserResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        """Gets the host_ip of this UserResponseInfo.

        服务器ip

        :return: The host_ip of this UserResponseInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this UserResponseInfo.

        服务器ip

        :param host_ip: The host_ip of this UserResponseInfo.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def user_name(self):
        """Gets the user_name of this UserResponseInfo.

        用户名

        :return: The user_name of this UserResponseInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this UserResponseInfo.

        用户名

        :param user_name: The user_name of this UserResponseInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def login_permission(self):
        """Gets the login_permission of this UserResponseInfo.

        是否有登陆权限

        :return: The login_permission of this UserResponseInfo.
        :rtype: bool
        """
        return self._login_permission

    @login_permission.setter
    def login_permission(self, login_permission):
        """Sets the login_permission of this UserResponseInfo.

        是否有登陆权限

        :param login_permission: The login_permission of this UserResponseInfo.
        :type login_permission: bool
        """
        self._login_permission = login_permission

    @property
    def root_permission(self):
        """Gets the root_permission of this UserResponseInfo.

        是否有root权限

        :return: The root_permission of this UserResponseInfo.
        :rtype: bool
        """
        return self._root_permission

    @root_permission.setter
    def root_permission(self, root_permission):
        """Sets the root_permission of this UserResponseInfo.

        是否有root权限

        :param root_permission: The root_permission of this UserResponseInfo.
        :type root_permission: bool
        """
        self._root_permission = root_permission

    @property
    def user_group_name(self):
        """Gets the user_group_name of this UserResponseInfo.

        用户组

        :return: The user_group_name of this UserResponseInfo.
        :rtype: str
        """
        return self._user_group_name

    @user_group_name.setter
    def user_group_name(self, user_group_name):
        """Sets the user_group_name of this UserResponseInfo.

        用户组

        :param user_group_name: The user_group_name of this UserResponseInfo.
        :type user_group_name: str
        """
        self._user_group_name = user_group_name

    @property
    def user_home_dir(self):
        """Gets the user_home_dir of this UserResponseInfo.

        用户目录

        :return: The user_home_dir of this UserResponseInfo.
        :rtype: str
        """
        return self._user_home_dir

    @user_home_dir.setter
    def user_home_dir(self, user_home_dir):
        """Sets the user_home_dir of this UserResponseInfo.

        用户目录

        :param user_home_dir: The user_home_dir of this UserResponseInfo.
        :type user_home_dir: str
        """
        self._user_home_dir = user_home_dir

    @property
    def shell(self):
        """Gets the shell of this UserResponseInfo.

        用户启动shell

        :return: The shell of this UserResponseInfo.
        :rtype: str
        """
        return self._shell

    @shell.setter
    def shell(self, shell):
        """Sets the shell of this UserResponseInfo.

        用户启动shell

        :param shell: The shell of this UserResponseInfo.
        :type shell: str
        """
        self._shell = shell

    @property
    def expire_time(self):
        """Gets the expire_time of this UserResponseInfo.

        到期时间，采用时间戳，默认毫秒，

        :return: The expire_time of this UserResponseInfo.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this UserResponseInfo.

        到期时间，采用时间戳，默认毫秒，

        :param expire_time: The expire_time of this UserResponseInfo.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def recent_scan_time(self):
        """Gets the recent_scan_time of this UserResponseInfo.

        最近扫描时间

        :return: The recent_scan_time of this UserResponseInfo.
        :rtype: int
        """
        return self._recent_scan_time

    @recent_scan_time.setter
    def recent_scan_time(self, recent_scan_time):
        """Sets the recent_scan_time of this UserResponseInfo.

        最近扫描时间

        :param recent_scan_time: The recent_scan_time of this UserResponseInfo.
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
        if not isinstance(other, UserResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
