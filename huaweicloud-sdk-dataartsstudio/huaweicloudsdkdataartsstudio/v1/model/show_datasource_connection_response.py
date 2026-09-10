# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDatasourceConnectionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'message': 'str',
        'id': 'str',
        'name': 'str',
        'status': 'str',
        'available_cluster_info': 'list[ConnectionClusterInfo]',
        'dest_vpc_id': 'str',
        'dest_network_id': 'str',
        'create_time': 'int',
        'hosts': 'list[ConnectionsHost]',
        'routes': 'list[ConnectionsRoute]'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'available_cluster_info': 'available_cluster_info',
        'dest_vpc_id': 'dest_vpc_id',
        'dest_network_id': 'dest_network_id',
        'create_time': 'create_time',
        'hosts': 'hosts',
        'routes': 'routes'
    }

    def __init__(self, is_success=None, message=None, id=None, name=None, status=None, available_cluster_info=None, dest_vpc_id=None, dest_network_id=None, create_time=None, hosts=None, routes=None):
        r"""ShowDatasourceConnectionResponse

        The model defined in huaweicloud sdk

        :param is_success: 执行请求是否成功。“true”表示请求执行成功。
        :type is_success: bool
        :param message: 系统提示信息，执行成功时，信息为空。
        :type message: str
        :param id: 连接ID，用于标识资源组网络连接的UUID。
        :type id: str
        :param name: 创建连接时，用户自定义的连接名称。
        :type name: str
        :param status: 连接状态，包括以下两种状态： ACTIVE：已激活 DELETED：已删除
        :type status: str
        :param available_cluster_info: 各个集群创建对等连接的信息。
        :type available_cluster_info: list[:class:`huaweicloudsdkdataartsstudio.v1.ConnectionClusterInfo`]
        :param dest_vpc_id: 对应服务的虚拟私有云标识。
        :type dest_vpc_id: str
        :param dest_network_id: 对应服务的子网网络标识。
        :type dest_network_id: str
        :param create_time: 创建连接的时间。为UTC的时间戳。
        :type create_time: int
        :param hosts: 用户自定义主机信息。
        :type hosts: list[:class:`huaweicloudsdkdataartsstudio.v1.ConnectionsHost`]
        :param routes: 用户添加的路由信息。
        :type routes: list[:class:`huaweicloudsdkdataartsstudio.v1.ConnectionsRoute`]
        """
        
        super().__init__()

        self._is_success = None
        self._message = None
        self._id = None
        self._name = None
        self._status = None
        self._available_cluster_info = None
        self._dest_vpc_id = None
        self._dest_network_id = None
        self._create_time = None
        self._hosts = None
        self._routes = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if available_cluster_info is not None:
            self.available_cluster_info = available_cluster_info
        if dest_vpc_id is not None:
            self.dest_vpc_id = dest_vpc_id
        if dest_network_id is not None:
            self.dest_network_id = dest_network_id
        if create_time is not None:
            self.create_time = create_time
        if hosts is not None:
            self.hosts = hosts
        if routes is not None:
            self.routes = routes

    @property
    def is_success(self):
        r"""Gets the is_success of this ShowDatasourceConnectionResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :return: The is_success of this ShowDatasourceConnectionResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this ShowDatasourceConnectionResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :param is_success: The is_success of this ShowDatasourceConnectionResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        r"""Gets the message of this ShowDatasourceConnectionResponse.

        系统提示信息，执行成功时，信息为空。

        :return: The message of this ShowDatasourceConnectionResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ShowDatasourceConnectionResponse.

        系统提示信息，执行成功时，信息为空。

        :param message: The message of this ShowDatasourceConnectionResponse.
        :type message: str
        """
        self._message = message

    @property
    def id(self):
        r"""Gets the id of this ShowDatasourceConnectionResponse.

        连接ID，用于标识资源组网络连接的UUID。

        :return: The id of this ShowDatasourceConnectionResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowDatasourceConnectionResponse.

        连接ID，用于标识资源组网络连接的UUID。

        :param id: The id of this ShowDatasourceConnectionResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowDatasourceConnectionResponse.

        创建连接时，用户自定义的连接名称。

        :return: The name of this ShowDatasourceConnectionResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowDatasourceConnectionResponse.

        创建连接时，用户自定义的连接名称。

        :param name: The name of this ShowDatasourceConnectionResponse.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ShowDatasourceConnectionResponse.

        连接状态，包括以下两种状态： ACTIVE：已激活 DELETED：已删除

        :return: The status of this ShowDatasourceConnectionResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowDatasourceConnectionResponse.

        连接状态，包括以下两种状态： ACTIVE：已激活 DELETED：已删除

        :param status: The status of this ShowDatasourceConnectionResponse.
        :type status: str
        """
        self._status = status

    @property
    def available_cluster_info(self):
        r"""Gets the available_cluster_info of this ShowDatasourceConnectionResponse.

        各个集群创建对等连接的信息。

        :return: The available_cluster_info of this ShowDatasourceConnectionResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ConnectionClusterInfo`]
        """
        return self._available_cluster_info

    @available_cluster_info.setter
    def available_cluster_info(self, available_cluster_info):
        r"""Sets the available_cluster_info of this ShowDatasourceConnectionResponse.

        各个集群创建对等连接的信息。

        :param available_cluster_info: The available_cluster_info of this ShowDatasourceConnectionResponse.
        :type available_cluster_info: list[:class:`huaweicloudsdkdataartsstudio.v1.ConnectionClusterInfo`]
        """
        self._available_cluster_info = available_cluster_info

    @property
    def dest_vpc_id(self):
        r"""Gets the dest_vpc_id of this ShowDatasourceConnectionResponse.

        对应服务的虚拟私有云标识。

        :return: The dest_vpc_id of this ShowDatasourceConnectionResponse.
        :rtype: str
        """
        return self._dest_vpc_id

    @dest_vpc_id.setter
    def dest_vpc_id(self, dest_vpc_id):
        r"""Sets the dest_vpc_id of this ShowDatasourceConnectionResponse.

        对应服务的虚拟私有云标识。

        :param dest_vpc_id: The dest_vpc_id of this ShowDatasourceConnectionResponse.
        :type dest_vpc_id: str
        """
        self._dest_vpc_id = dest_vpc_id

    @property
    def dest_network_id(self):
        r"""Gets the dest_network_id of this ShowDatasourceConnectionResponse.

        对应服务的子网网络标识。

        :return: The dest_network_id of this ShowDatasourceConnectionResponse.
        :rtype: str
        """
        return self._dest_network_id

    @dest_network_id.setter
    def dest_network_id(self, dest_network_id):
        r"""Sets the dest_network_id of this ShowDatasourceConnectionResponse.

        对应服务的子网网络标识。

        :param dest_network_id: The dest_network_id of this ShowDatasourceConnectionResponse.
        :type dest_network_id: str
        """
        self._dest_network_id = dest_network_id

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowDatasourceConnectionResponse.

        创建连接的时间。为UTC的时间戳。

        :return: The create_time of this ShowDatasourceConnectionResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowDatasourceConnectionResponse.

        创建连接的时间。为UTC的时间戳。

        :param create_time: The create_time of this ShowDatasourceConnectionResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def hosts(self):
        r"""Gets the hosts of this ShowDatasourceConnectionResponse.

        用户自定义主机信息。

        :return: The hosts of this ShowDatasourceConnectionResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ConnectionsHost`]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        r"""Sets the hosts of this ShowDatasourceConnectionResponse.

        用户自定义主机信息。

        :param hosts: The hosts of this ShowDatasourceConnectionResponse.
        :type hosts: list[:class:`huaweicloudsdkdataartsstudio.v1.ConnectionsHost`]
        """
        self._hosts = hosts

    @property
    def routes(self):
        r"""Gets the routes of this ShowDatasourceConnectionResponse.

        用户添加的路由信息。

        :return: The routes of this ShowDatasourceConnectionResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ConnectionsRoute`]
        """
        return self._routes

    @routes.setter
    def routes(self, routes):
        r"""Sets the routes of this ShowDatasourceConnectionResponse.

        用户添加的路由信息。

        :param routes: The routes of this ShowDatasourceConnectionResponse.
        :type routes: list[:class:`huaweicloudsdkdataartsstudio.v1.ConnectionsRoute`]
        """
        self._routes = routes

    def to_dict(self):
        import warnings
        warnings.warn("ShowDatasourceConnectionResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowDatasourceConnectionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
