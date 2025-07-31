# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetworkNodeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'status': 'str',
        'ip_addr': 'str',
        'ipv6_addr': 'str',
        'private_ip_addr': 'str',
        'private_ipv6_addr': 'str',
        'runtime_version': 'str',
        'os_version': 'str',
        'security_group': 'str',
        'server_id': 'str',
        'server_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'ip_addr': 'ip_addr',
        'ipv6_addr': 'ipv6_addr',
        'private_ip_addr': 'private_ip_addr',
        'private_ipv6_addr': 'private_ipv6_addr',
        'runtime_version': 'runtime_version',
        'os_version': 'os_version',
        'security_group': 'security_group',
        'server_id': 'server_id',
        'server_type': 'server_type'
    }

    def __init__(self, id=None, name=None, status=None, ip_addr=None, ipv6_addr=None, private_ip_addr=None, private_ipv6_addr=None, runtime_version=None, os_version=None, security_group=None, server_id=None, server_type=None):
        r"""NetworkNodeInfo

        The model defined in huaweicloud sdk

        :param id: 节点id
        :type id: str
        :param name: 节点
        :type name: str
        :param status: 状态
        :type status: str
        :param ip_addr: ip地址
        :type ip_addr: str
        :param ipv6_addr: ipv6地址
        :type ipv6_addr: str
        :param private_ip_addr: 私有ip地址
        :type private_ip_addr: str
        :param private_ipv6_addr: 私有ipv6地址
        :type private_ipv6_addr: str
        :param runtime_version: 运行时版本
        :type runtime_version: str
        :param os_version: os版本
        :type os_version: str
        :param security_group: 安全组
        :type security_group: str
        :param server_id: 服务器id
        :type server_id: str
        :param server_type: 服务器类型
        :type server_type: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._ip_addr = None
        self._ipv6_addr = None
        self._private_ip_addr = None
        self._private_ipv6_addr = None
        self._runtime_version = None
        self._os_version = None
        self._security_group = None
        self._server_id = None
        self._server_type = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        self.ip_addr = ip_addr
        if ipv6_addr is not None:
            self.ipv6_addr = ipv6_addr
        if private_ip_addr is not None:
            self.private_ip_addr = private_ip_addr
        if private_ipv6_addr is not None:
            self.private_ipv6_addr = private_ipv6_addr
        self.runtime_version = runtime_version
        self.os_version = os_version
        self.security_group = security_group
        if server_id is not None:
            self.server_id = server_id
        if server_type is not None:
            self.server_type = server_type

    @property
    def id(self):
        r"""Gets the id of this NetworkNodeInfo.

        节点id

        :return: The id of this NetworkNodeInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this NetworkNodeInfo.

        节点id

        :param id: The id of this NetworkNodeInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this NetworkNodeInfo.

        节点

        :return: The name of this NetworkNodeInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this NetworkNodeInfo.

        节点

        :param name: The name of this NetworkNodeInfo.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this NetworkNodeInfo.

        状态

        :return: The status of this NetworkNodeInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this NetworkNodeInfo.

        状态

        :param status: The status of this NetworkNodeInfo.
        :type status: str
        """
        self._status = status

    @property
    def ip_addr(self):
        r"""Gets the ip_addr of this NetworkNodeInfo.

        ip地址

        :return: The ip_addr of this NetworkNodeInfo.
        :rtype: str
        """
        return self._ip_addr

    @ip_addr.setter
    def ip_addr(self, ip_addr):
        r"""Sets the ip_addr of this NetworkNodeInfo.

        ip地址

        :param ip_addr: The ip_addr of this NetworkNodeInfo.
        :type ip_addr: str
        """
        self._ip_addr = ip_addr

    @property
    def ipv6_addr(self):
        r"""Gets the ipv6_addr of this NetworkNodeInfo.

        ipv6地址

        :return: The ipv6_addr of this NetworkNodeInfo.
        :rtype: str
        """
        return self._ipv6_addr

    @ipv6_addr.setter
    def ipv6_addr(self, ipv6_addr):
        r"""Sets the ipv6_addr of this NetworkNodeInfo.

        ipv6地址

        :param ipv6_addr: The ipv6_addr of this NetworkNodeInfo.
        :type ipv6_addr: str
        """
        self._ipv6_addr = ipv6_addr

    @property
    def private_ip_addr(self):
        r"""Gets the private_ip_addr of this NetworkNodeInfo.

        私有ip地址

        :return: The private_ip_addr of this NetworkNodeInfo.
        :rtype: str
        """
        return self._private_ip_addr

    @private_ip_addr.setter
    def private_ip_addr(self, private_ip_addr):
        r"""Sets the private_ip_addr of this NetworkNodeInfo.

        私有ip地址

        :param private_ip_addr: The private_ip_addr of this NetworkNodeInfo.
        :type private_ip_addr: str
        """
        self._private_ip_addr = private_ip_addr

    @property
    def private_ipv6_addr(self):
        r"""Gets the private_ipv6_addr of this NetworkNodeInfo.

        私有ipv6地址

        :return: The private_ipv6_addr of this NetworkNodeInfo.
        :rtype: str
        """
        return self._private_ipv6_addr

    @private_ipv6_addr.setter
    def private_ipv6_addr(self, private_ipv6_addr):
        r"""Sets the private_ipv6_addr of this NetworkNodeInfo.

        私有ipv6地址

        :param private_ipv6_addr: The private_ipv6_addr of this NetworkNodeInfo.
        :type private_ipv6_addr: str
        """
        self._private_ipv6_addr = private_ipv6_addr

    @property
    def runtime_version(self):
        r"""Gets the runtime_version of this NetworkNodeInfo.

        运行时版本

        :return: The runtime_version of this NetworkNodeInfo.
        :rtype: str
        """
        return self._runtime_version

    @runtime_version.setter
    def runtime_version(self, runtime_version):
        r"""Sets the runtime_version of this NetworkNodeInfo.

        运行时版本

        :param runtime_version: The runtime_version of this NetworkNodeInfo.
        :type runtime_version: str
        """
        self._runtime_version = runtime_version

    @property
    def os_version(self):
        r"""Gets the os_version of this NetworkNodeInfo.

        os版本

        :return: The os_version of this NetworkNodeInfo.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        r"""Sets the os_version of this NetworkNodeInfo.

        os版本

        :param os_version: The os_version of this NetworkNodeInfo.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def security_group(self):
        r"""Gets the security_group of this NetworkNodeInfo.

        安全组

        :return: The security_group of this NetworkNodeInfo.
        :rtype: str
        """
        return self._security_group

    @security_group.setter
    def security_group(self, security_group):
        r"""Sets the security_group of this NetworkNodeInfo.

        安全组

        :param security_group: The security_group of this NetworkNodeInfo.
        :type security_group: str
        """
        self._security_group = security_group

    @property
    def server_id(self):
        r"""Gets the server_id of this NetworkNodeInfo.

        服务器id

        :return: The server_id of this NetworkNodeInfo.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this NetworkNodeInfo.

        服务器id

        :param server_id: The server_id of this NetworkNodeInfo.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def server_type(self):
        r"""Gets the server_type of this NetworkNodeInfo.

        服务器类型

        :return: The server_type of this NetworkNodeInfo.
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        r"""Sets the server_type of this NetworkNodeInfo.

        服务器类型

        :param server_type: The server_type of this NetworkNodeInfo.
        :type server_type: str
        """
        self._server_type = server_type

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
        if not isinstance(other, NetworkNodeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
