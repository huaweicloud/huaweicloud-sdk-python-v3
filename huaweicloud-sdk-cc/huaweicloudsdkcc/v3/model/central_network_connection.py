# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CentralNetworkConnection:

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
        'description': 'str',
        'domain_id': 'str',
        'enterprise_project_id': 'str',
        'central_network_id': 'str',
        'central_network_plane_id': 'str',
        'global_connection_bandwidth_id': 'str',
        'bandwidth_type': 'BandwidthTypeEnum',
        'bandwidth_size': 'int',
        'state': 'CentralNetworkConnectionStateEnum',
        'is_frozen': 'bool',
        'connection_type': 'ConnectionTypeEnum',
        'connection_point_pair': 'list[ConnectionPoint]',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'domain_id': 'domain_id',
        'enterprise_project_id': 'enterprise_project_id',
        'central_network_id': 'central_network_id',
        'central_network_plane_id': 'central_network_plane_id',
        'global_connection_bandwidth_id': 'global_connection_bandwidth_id',
        'bandwidth_type': 'bandwidth_type',
        'bandwidth_size': 'bandwidth_size',
        'state': 'state',
        'is_frozen': 'is_frozen',
        'connection_type': 'connection_type',
        'connection_point_pair': 'connection_point_pair',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, description=None, domain_id=None, enterprise_project_id=None, central_network_id=None, central_network_plane_id=None, global_connection_bandwidth_id=None, bandwidth_type=None, bandwidth_size=None, state=None, is_frozen=None, connection_type=None, connection_point_pair=None, created_at=None, updated_at=None):
        r"""CentralNetworkConnection

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param name: 实例名称。
        :type name: str
        :param description: 实例描述。不支持 &lt;&gt;。
        :type description: str
        :param domain_id: 实例所属账号ID。
        :type domain_id: str
        :param enterprise_project_id: 实例所属企业项目ID。
        :type enterprise_project_id: str
        :param central_network_id: 中心网络ID。
        :type central_network_id: str
        :param central_network_plane_id: 中心网络平面ID。
        :type central_network_plane_id: str
        :param global_connection_bandwidth_id: 全域互联带宽ID。
        :type global_connection_bandwidth_id: str
        :param bandwidth_type: 
        :type bandwidth_type: :class:`huaweicloudsdkcc.v3.BandwidthTypeEnum`
        :param bandwidth_size: 带宽值，单位Mbps。
        :type bandwidth_size: int
        :param state: 
        :type state: :class:`huaweicloudsdkcc.v3.CentralNetworkConnectionStateEnum`
        :param is_frozen: 是否冻结。
        :type is_frozen: bool
        :param connection_type: 
        :type connection_type: :class:`huaweicloudsdkcc.v3.ConnectionTypeEnum`
        :param connection_point_pair: 中心网络连接的两个端点定义，长度固定为2的数组。
        :type connection_point_pair: list[:class:`huaweicloudsdkcc.v3.ConnectionPoint`]
        :param created_at: 实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type created_at: datetime
        :param updated_at: 实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._domain_id = None
        self._enterprise_project_id = None
        self._central_network_id = None
        self._central_network_plane_id = None
        self._global_connection_bandwidth_id = None
        self._bandwidth_type = None
        self._bandwidth_size = None
        self._state = None
        self._is_frozen = None
        self._connection_type = None
        self._connection_point_pair = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.domain_id = domain_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.central_network_id = central_network_id
        self.central_network_plane_id = central_network_plane_id
        if global_connection_bandwidth_id is not None:
            self.global_connection_bandwidth_id = global_connection_bandwidth_id
        self.bandwidth_type = bandwidth_type
        if bandwidth_size is not None:
            self.bandwidth_size = bandwidth_size
        self.state = state
        self.is_frozen = is_frozen
        self.connection_type = connection_type
        self.connection_point_pair = connection_point_pair
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this CentralNetworkConnection.

        实例ID。

        :return: The id of this CentralNetworkConnection.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CentralNetworkConnection.

        实例ID。

        :param id: The id of this CentralNetworkConnection.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CentralNetworkConnection.

        实例名称。

        :return: The name of this CentralNetworkConnection.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CentralNetworkConnection.

        实例名称。

        :param name: The name of this CentralNetworkConnection.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CentralNetworkConnection.

        实例描述。不支持 <>。

        :return: The description of this CentralNetworkConnection.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CentralNetworkConnection.

        实例描述。不支持 <>。

        :param description: The description of this CentralNetworkConnection.
        :type description: str
        """
        self._description = description

    @property
    def domain_id(self):
        r"""Gets the domain_id of this CentralNetworkConnection.

        实例所属账号ID。

        :return: The domain_id of this CentralNetworkConnection.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this CentralNetworkConnection.

        实例所属账号ID。

        :param domain_id: The domain_id of this CentralNetworkConnection.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CentralNetworkConnection.

        实例所属企业项目ID。

        :return: The enterprise_project_id of this CentralNetworkConnection.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CentralNetworkConnection.

        实例所属企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this CentralNetworkConnection.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def central_network_id(self):
        r"""Gets the central_network_id of this CentralNetworkConnection.

        中心网络ID。

        :return: The central_network_id of this CentralNetworkConnection.
        :rtype: str
        """
        return self._central_network_id

    @central_network_id.setter
    def central_network_id(self, central_network_id):
        r"""Sets the central_network_id of this CentralNetworkConnection.

        中心网络ID。

        :param central_network_id: The central_network_id of this CentralNetworkConnection.
        :type central_network_id: str
        """
        self._central_network_id = central_network_id

    @property
    def central_network_plane_id(self):
        r"""Gets the central_network_plane_id of this CentralNetworkConnection.

        中心网络平面ID。

        :return: The central_network_plane_id of this CentralNetworkConnection.
        :rtype: str
        """
        return self._central_network_plane_id

    @central_network_plane_id.setter
    def central_network_plane_id(self, central_network_plane_id):
        r"""Sets the central_network_plane_id of this CentralNetworkConnection.

        中心网络平面ID。

        :param central_network_plane_id: The central_network_plane_id of this CentralNetworkConnection.
        :type central_network_plane_id: str
        """
        self._central_network_plane_id = central_network_plane_id

    @property
    def global_connection_bandwidth_id(self):
        r"""Gets the global_connection_bandwidth_id of this CentralNetworkConnection.

        全域互联带宽ID。

        :return: The global_connection_bandwidth_id of this CentralNetworkConnection.
        :rtype: str
        """
        return self._global_connection_bandwidth_id

    @global_connection_bandwidth_id.setter
    def global_connection_bandwidth_id(self, global_connection_bandwidth_id):
        r"""Sets the global_connection_bandwidth_id of this CentralNetworkConnection.

        全域互联带宽ID。

        :param global_connection_bandwidth_id: The global_connection_bandwidth_id of this CentralNetworkConnection.
        :type global_connection_bandwidth_id: str
        """
        self._global_connection_bandwidth_id = global_connection_bandwidth_id

    @property
    def bandwidth_type(self):
        r"""Gets the bandwidth_type of this CentralNetworkConnection.

        :return: The bandwidth_type of this CentralNetworkConnection.
        :rtype: :class:`huaweicloudsdkcc.v3.BandwidthTypeEnum`
        """
        return self._bandwidth_type

    @bandwidth_type.setter
    def bandwidth_type(self, bandwidth_type):
        r"""Sets the bandwidth_type of this CentralNetworkConnection.

        :param bandwidth_type: The bandwidth_type of this CentralNetworkConnection.
        :type bandwidth_type: :class:`huaweicloudsdkcc.v3.BandwidthTypeEnum`
        """
        self._bandwidth_type = bandwidth_type

    @property
    def bandwidth_size(self):
        r"""Gets the bandwidth_size of this CentralNetworkConnection.

        带宽值，单位Mbps。

        :return: The bandwidth_size of this CentralNetworkConnection.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        r"""Sets the bandwidth_size of this CentralNetworkConnection.

        带宽值，单位Mbps。

        :param bandwidth_size: The bandwidth_size of this CentralNetworkConnection.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

    @property
    def state(self):
        r"""Gets the state of this CentralNetworkConnection.

        :return: The state of this CentralNetworkConnection.
        :rtype: :class:`huaweicloudsdkcc.v3.CentralNetworkConnectionStateEnum`
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this CentralNetworkConnection.

        :param state: The state of this CentralNetworkConnection.
        :type state: :class:`huaweicloudsdkcc.v3.CentralNetworkConnectionStateEnum`
        """
        self._state = state

    @property
    def is_frozen(self):
        r"""Gets the is_frozen of this CentralNetworkConnection.

        是否冻结。

        :return: The is_frozen of this CentralNetworkConnection.
        :rtype: bool
        """
        return self._is_frozen

    @is_frozen.setter
    def is_frozen(self, is_frozen):
        r"""Sets the is_frozen of this CentralNetworkConnection.

        是否冻结。

        :param is_frozen: The is_frozen of this CentralNetworkConnection.
        :type is_frozen: bool
        """
        self._is_frozen = is_frozen

    @property
    def connection_type(self):
        r"""Gets the connection_type of this CentralNetworkConnection.

        :return: The connection_type of this CentralNetworkConnection.
        :rtype: :class:`huaweicloudsdkcc.v3.ConnectionTypeEnum`
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        r"""Sets the connection_type of this CentralNetworkConnection.

        :param connection_type: The connection_type of this CentralNetworkConnection.
        :type connection_type: :class:`huaweicloudsdkcc.v3.ConnectionTypeEnum`
        """
        self._connection_type = connection_type

    @property
    def connection_point_pair(self):
        r"""Gets the connection_point_pair of this CentralNetworkConnection.

        中心网络连接的两个端点定义，长度固定为2的数组。

        :return: The connection_point_pair of this CentralNetworkConnection.
        :rtype: list[:class:`huaweicloudsdkcc.v3.ConnectionPoint`]
        """
        return self._connection_point_pair

    @connection_point_pair.setter
    def connection_point_pair(self, connection_point_pair):
        r"""Sets the connection_point_pair of this CentralNetworkConnection.

        中心网络连接的两个端点定义，长度固定为2的数组。

        :param connection_point_pair: The connection_point_pair of this CentralNetworkConnection.
        :type connection_point_pair: list[:class:`huaweicloudsdkcc.v3.ConnectionPoint`]
        """
        self._connection_point_pair = connection_point_pair

    @property
    def created_at(self):
        r"""Gets the created_at of this CentralNetworkConnection.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The created_at of this CentralNetworkConnection.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CentralNetworkConnection.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param created_at: The created_at of this CentralNetworkConnection.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CentralNetworkConnection.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The updated_at of this CentralNetworkConnection.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CentralNetworkConnection.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param updated_at: The updated_at of this CentralNetworkConnection.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, CentralNetworkConnection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
