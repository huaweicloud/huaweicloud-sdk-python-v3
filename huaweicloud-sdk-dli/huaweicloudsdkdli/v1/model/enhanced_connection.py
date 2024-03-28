# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnhancedConnection:

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
        'available_queue_info': 'list[EnhancedConnectionResource]',
        'elastic_resource_pools': 'list[EnhancedConnectionResource]',
        'dest_vpc_id': 'str',
        'dest_network_id': 'str',
        'create_time': 'int',
        'hosts': 'list[EnhancedConnectionHost]',
        'is_privis': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'available_queue_info': 'available_queue_info',
        'elastic_resource_pools': 'elastic_resource_pools',
        'dest_vpc_id': 'dest_vpc_id',
        'dest_network_id': 'dest_network_id',
        'create_time': 'create_time',
        'hosts': 'hosts',
        'is_privis': 'isPrivis'
    }

    def __init__(self, id=None, name=None, status=None, available_queue_info=None, elastic_resource_pools=None, dest_vpc_id=None, dest_network_id=None, create_time=None, hosts=None, is_privis=None):
        """EnhancedConnection

        The model defined in huaweicloud sdk

        :param id: 连接ID，用于标识跨源连接的UUID。
        :type id: str
        :param name: 创建连接时，用户自定义的连接名称。
        :type name: str
        :param status: 连接状态，包括以下两种状态： ACTIVE：已激活 DELETED：已删除
        :type status: str
        :param available_queue_info: 各个队列创建对等连接的信息。
        :type available_queue_info: list[:class:`huaweicloudsdkdli.v1.EnhancedConnectionResource`]
        :param elastic_resource_pools: 各个弹性资源池创建对等连接的信息。
        :type elastic_resource_pools: list[:class:`huaweicloudsdkdli.v1.EnhancedConnectionResource`]
        :param dest_vpc_id: 对应服务的虚拟私有云标识。
        :type dest_vpc_id: str
        :param dest_network_id: 对应服务的子网网络标识。
        :type dest_network_id: str
        :param create_time: 创建连接的时间。为UTC的时间戳。
        :type create_time: int
        :param hosts: 用户自定义主机信息
        :type hosts: list[:class:`huaweicloudsdkdli.v1.EnhancedConnectionHost`]
        :param is_privis: 该增强跨源连接如果做过项目赋权，则该字段是\&quot;false\&quot;，否则为\&quot;true\&quot;。
        :type is_privis: bool
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._available_queue_info = None
        self._elastic_resource_pools = None
        self._dest_vpc_id = None
        self._dest_network_id = None
        self._create_time = None
        self._hosts = None
        self._is_privis = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if available_queue_info is not None:
            self.available_queue_info = available_queue_info
        if elastic_resource_pools is not None:
            self.elastic_resource_pools = elastic_resource_pools
        if dest_vpc_id is not None:
            self.dest_vpc_id = dest_vpc_id
        if dest_network_id is not None:
            self.dest_network_id = dest_network_id
        if create_time is not None:
            self.create_time = create_time
        if hosts is not None:
            self.hosts = hosts
        if is_privis is not None:
            self.is_privis = is_privis

    @property
    def id(self):
        """Gets the id of this EnhancedConnection.

        连接ID，用于标识跨源连接的UUID。

        :return: The id of this EnhancedConnection.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EnhancedConnection.

        连接ID，用于标识跨源连接的UUID。

        :param id: The id of this EnhancedConnection.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this EnhancedConnection.

        创建连接时，用户自定义的连接名称。

        :return: The name of this EnhancedConnection.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnhancedConnection.

        创建连接时，用户自定义的连接名称。

        :param name: The name of this EnhancedConnection.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this EnhancedConnection.

        连接状态，包括以下两种状态： ACTIVE：已激活 DELETED：已删除

        :return: The status of this EnhancedConnection.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EnhancedConnection.

        连接状态，包括以下两种状态： ACTIVE：已激活 DELETED：已删除

        :param status: The status of this EnhancedConnection.
        :type status: str
        """
        self._status = status

    @property
    def available_queue_info(self):
        """Gets the available_queue_info of this EnhancedConnection.

        各个队列创建对等连接的信息。

        :return: The available_queue_info of this EnhancedConnection.
        :rtype: list[:class:`huaweicloudsdkdli.v1.EnhancedConnectionResource`]
        """
        return self._available_queue_info

    @available_queue_info.setter
    def available_queue_info(self, available_queue_info):
        """Sets the available_queue_info of this EnhancedConnection.

        各个队列创建对等连接的信息。

        :param available_queue_info: The available_queue_info of this EnhancedConnection.
        :type available_queue_info: list[:class:`huaweicloudsdkdli.v1.EnhancedConnectionResource`]
        """
        self._available_queue_info = available_queue_info

    @property
    def elastic_resource_pools(self):
        """Gets the elastic_resource_pools of this EnhancedConnection.

        各个弹性资源池创建对等连接的信息。

        :return: The elastic_resource_pools of this EnhancedConnection.
        :rtype: list[:class:`huaweicloudsdkdli.v1.EnhancedConnectionResource`]
        """
        return self._elastic_resource_pools

    @elastic_resource_pools.setter
    def elastic_resource_pools(self, elastic_resource_pools):
        """Sets the elastic_resource_pools of this EnhancedConnection.

        各个弹性资源池创建对等连接的信息。

        :param elastic_resource_pools: The elastic_resource_pools of this EnhancedConnection.
        :type elastic_resource_pools: list[:class:`huaweicloudsdkdli.v1.EnhancedConnectionResource`]
        """
        self._elastic_resource_pools = elastic_resource_pools

    @property
    def dest_vpc_id(self):
        """Gets the dest_vpc_id of this EnhancedConnection.

        对应服务的虚拟私有云标识。

        :return: The dest_vpc_id of this EnhancedConnection.
        :rtype: str
        """
        return self._dest_vpc_id

    @dest_vpc_id.setter
    def dest_vpc_id(self, dest_vpc_id):
        """Sets the dest_vpc_id of this EnhancedConnection.

        对应服务的虚拟私有云标识。

        :param dest_vpc_id: The dest_vpc_id of this EnhancedConnection.
        :type dest_vpc_id: str
        """
        self._dest_vpc_id = dest_vpc_id

    @property
    def dest_network_id(self):
        """Gets the dest_network_id of this EnhancedConnection.

        对应服务的子网网络标识。

        :return: The dest_network_id of this EnhancedConnection.
        :rtype: str
        """
        return self._dest_network_id

    @dest_network_id.setter
    def dest_network_id(self, dest_network_id):
        """Sets the dest_network_id of this EnhancedConnection.

        对应服务的子网网络标识。

        :param dest_network_id: The dest_network_id of this EnhancedConnection.
        :type dest_network_id: str
        """
        self._dest_network_id = dest_network_id

    @property
    def create_time(self):
        """Gets the create_time of this EnhancedConnection.

        创建连接的时间。为UTC的时间戳。

        :return: The create_time of this EnhancedConnection.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this EnhancedConnection.

        创建连接的时间。为UTC的时间戳。

        :param create_time: The create_time of this EnhancedConnection.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def hosts(self):
        """Gets the hosts of this EnhancedConnection.

        用户自定义主机信息

        :return: The hosts of this EnhancedConnection.
        :rtype: list[:class:`huaweicloudsdkdli.v1.EnhancedConnectionHost`]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this EnhancedConnection.

        用户自定义主机信息

        :param hosts: The hosts of this EnhancedConnection.
        :type hosts: list[:class:`huaweicloudsdkdli.v1.EnhancedConnectionHost`]
        """
        self._hosts = hosts

    @property
    def is_privis(self):
        """Gets the is_privis of this EnhancedConnection.

        该增强跨源连接如果做过项目赋权，则该字段是\"false\"，否则为\"true\"。

        :return: The is_privis of this EnhancedConnection.
        :rtype: bool
        """
        return self._is_privis

    @is_privis.setter
    def is_privis(self, is_privis):
        """Sets the is_privis of this EnhancedConnection.

        该增强跨源连接如果做过项目赋权，则该字段是\"false\"，否则为\"true\"。

        :param is_privis: The is_privis of this EnhancedConnection.
        :type is_privis: bool
        """
        self._is_privis = is_privis

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
        if not isinstance(other, EnhancedConnection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
