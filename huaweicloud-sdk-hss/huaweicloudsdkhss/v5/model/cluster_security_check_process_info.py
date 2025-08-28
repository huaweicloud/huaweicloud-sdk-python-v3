# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterSecurityCheckProcessInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'container_id': 'str',
        'container_name': 'str',
        'host_name': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'start_time': 'int',
        'pid': 'int',
        'permission': 'str',
        'user_name': 'str',
        'launch_params': 'str',
        'hash': 'str'
    }

    attribute_map = {
        'container_id': 'container_id',
        'container_name': 'container_name',
        'host_name': 'host_name',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'start_time': 'start_time',
        'pid': 'pid',
        'permission': 'permission',
        'user_name': 'user_name',
        'launch_params': 'launch_params',
        'hash': 'hash'
    }

    def __init__(self, container_id=None, container_name=None, host_name=None, private_ip=None, public_ip=None, start_time=None, pid=None, permission=None, user_name=None, launch_params=None, hash=None):
        r"""ClusterSecurityCheckProcessInfo

        The model defined in huaweicloud sdk

        :param container_id: **参数解释**： 容器ID **取值范围**： 不涉及 
        :type container_id: str
        :param container_name: **参数解释**： 容器名称 **取值范围**： 不涉及 
        :type container_name: str
        :param host_name: **参数解释**： 节点名称 **取值范围**： 不涉及 
        :type host_name: str
        :param private_ip: **参数解释**： 私有IP地址 **取值范围**： 不涉及 
        :type private_ip: str
        :param public_ip: **参数解释**： 公有IP地址 **取值范围**： 不涉及 
        :type public_ip: str
        :param start_time: **参数解释**： 启动时间 **取值范围**： 不涉及 
        :type start_time: int
        :param pid: **参数解释**： 进程PID **取值范围**： 不涉及 
        :type pid: int
        :param permission: **参数解释**： 文件权限 **取值范围**： 不涉及 
        :type permission: str
        :param user_name: **参数解释**： 运行用户 **取值范围**： 不涉及 
        :type user_name: str
        :param launch_params: **参数解释**： 启动参数 **取值范围**： 不涉及 
        :type launch_params: str
        :param hash: **参数解释**： 文件hash **取值范围**： 不涉及 
        :type hash: str
        """
        
        

        self._container_id = None
        self._container_name = None
        self._host_name = None
        self._private_ip = None
        self._public_ip = None
        self._start_time = None
        self._pid = None
        self._permission = None
        self._user_name = None
        self._launch_params = None
        self._hash = None
        self.discriminator = None

        if container_id is not None:
            self.container_id = container_id
        if container_name is not None:
            self.container_name = container_name
        if host_name is not None:
            self.host_name = host_name
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
        if start_time is not None:
            self.start_time = start_time
        if pid is not None:
            self.pid = pid
        if permission is not None:
            self.permission = permission
        if user_name is not None:
            self.user_name = user_name
        if launch_params is not None:
            self.launch_params = launch_params
        if hash is not None:
            self.hash = hash

    @property
    def container_id(self):
        r"""Gets the container_id of this ClusterSecurityCheckProcessInfo.

        **参数解释**： 容器ID **取值范围**： 不涉及 

        :return: The container_id of this ClusterSecurityCheckProcessInfo.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this ClusterSecurityCheckProcessInfo.

        **参数解释**： 容器ID **取值范围**： 不涉及 

        :param container_id: The container_id of this ClusterSecurityCheckProcessInfo.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def container_name(self):
        r"""Gets the container_name of this ClusterSecurityCheckProcessInfo.

        **参数解释**： 容器名称 **取值范围**： 不涉及 

        :return: The container_name of this ClusterSecurityCheckProcessInfo.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this ClusterSecurityCheckProcessInfo.

        **参数解释**： 容器名称 **取值范围**： 不涉及 

        :param container_name: The container_name of this ClusterSecurityCheckProcessInfo.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def host_name(self):
        r"""Gets the host_name of this ClusterSecurityCheckProcessInfo.

        **参数解释**： 节点名称 **取值范围**： 不涉及 

        :return: The host_name of this ClusterSecurityCheckProcessInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ClusterSecurityCheckProcessInfo.

        **参数解释**： 节点名称 **取值范围**： 不涉及 

        :param host_name: The host_name of this ClusterSecurityCheckProcessInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ClusterSecurityCheckProcessInfo.

        **参数解释**： 私有IP地址 **取值范围**： 不涉及 

        :return: The private_ip of this ClusterSecurityCheckProcessInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ClusterSecurityCheckProcessInfo.

        **参数解释**： 私有IP地址 **取值范围**： 不涉及 

        :param private_ip: The private_ip of this ClusterSecurityCheckProcessInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ClusterSecurityCheckProcessInfo.

        **参数解释**： 公有IP地址 **取值范围**： 不涉及 

        :return: The public_ip of this ClusterSecurityCheckProcessInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ClusterSecurityCheckProcessInfo.

        **参数解释**： 公有IP地址 **取值范围**： 不涉及 

        :param public_ip: The public_ip of this ClusterSecurityCheckProcessInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def start_time(self):
        r"""Gets the start_time of this ClusterSecurityCheckProcessInfo.

        **参数解释**： 启动时间 **取值范围**： 不涉及 

        :return: The start_time of this ClusterSecurityCheckProcessInfo.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ClusterSecurityCheckProcessInfo.

        **参数解释**： 启动时间 **取值范围**： 不涉及 

        :param start_time: The start_time of this ClusterSecurityCheckProcessInfo.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def pid(self):
        r"""Gets the pid of this ClusterSecurityCheckProcessInfo.

        **参数解释**： 进程PID **取值范围**： 不涉及 

        :return: The pid of this ClusterSecurityCheckProcessInfo.
        :rtype: int
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        r"""Sets the pid of this ClusterSecurityCheckProcessInfo.

        **参数解释**： 进程PID **取值范围**： 不涉及 

        :param pid: The pid of this ClusterSecurityCheckProcessInfo.
        :type pid: int
        """
        self._pid = pid

    @property
    def permission(self):
        r"""Gets the permission of this ClusterSecurityCheckProcessInfo.

        **参数解释**： 文件权限 **取值范围**： 不涉及 

        :return: The permission of this ClusterSecurityCheckProcessInfo.
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        r"""Sets the permission of this ClusterSecurityCheckProcessInfo.

        **参数解释**： 文件权限 **取值范围**： 不涉及 

        :param permission: The permission of this ClusterSecurityCheckProcessInfo.
        :type permission: str
        """
        self._permission = permission

    @property
    def user_name(self):
        r"""Gets the user_name of this ClusterSecurityCheckProcessInfo.

        **参数解释**： 运行用户 **取值范围**： 不涉及 

        :return: The user_name of this ClusterSecurityCheckProcessInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ClusterSecurityCheckProcessInfo.

        **参数解释**： 运行用户 **取值范围**： 不涉及 

        :param user_name: The user_name of this ClusterSecurityCheckProcessInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def launch_params(self):
        r"""Gets the launch_params of this ClusterSecurityCheckProcessInfo.

        **参数解释**： 启动参数 **取值范围**： 不涉及 

        :return: The launch_params of this ClusterSecurityCheckProcessInfo.
        :rtype: str
        """
        return self._launch_params

    @launch_params.setter
    def launch_params(self, launch_params):
        r"""Sets the launch_params of this ClusterSecurityCheckProcessInfo.

        **参数解释**： 启动参数 **取值范围**： 不涉及 

        :param launch_params: The launch_params of this ClusterSecurityCheckProcessInfo.
        :type launch_params: str
        """
        self._launch_params = launch_params

    @property
    def hash(self):
        r"""Gets the hash of this ClusterSecurityCheckProcessInfo.

        **参数解释**： 文件hash **取值范围**： 不涉及 

        :return: The hash of this ClusterSecurityCheckProcessInfo.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        r"""Sets the hash of this ClusterSecurityCheckProcessInfo.

        **参数解释**： 文件hash **取值范围**： 不涉及 

        :param hash: The hash of this ClusterSecurityCheckProcessInfo.
        :type hash: str
        """
        self._hash = hash

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
        if not isinstance(other, ClusterSecurityCheckProcessInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
