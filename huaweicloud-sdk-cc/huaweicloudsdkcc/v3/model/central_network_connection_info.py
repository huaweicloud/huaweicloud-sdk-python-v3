# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CentralNetworkConnectionInfo:

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
        'plane_id': 'str',
        'global_connection_bandwidth_id': 'str',
        'bandwidth_size': 'int',
        'connection_type': 'str',
        'connection_point_pair': 'list[ConnectionPoint]',
        'state': 'str'
    }

    attribute_map = {
        'id': 'id',
        'plane_id': 'plane_id',
        'global_connection_bandwidth_id': 'global_connection_bandwidth_id',
        'bandwidth_size': 'bandwidth_size',
        'connection_type': 'connection_type',
        'connection_point_pair': 'connection_point_pair',
        'state': 'state'
    }

    def __init__(self, id=None, plane_id=None, global_connection_bandwidth_id=None, bandwidth_size=None, connection_type=None, connection_point_pair=None, state=None):
        r"""CentralNetworkConnectionInfo

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param plane_id: 中心网络平面ID。
        :type plane_id: str
        :param global_connection_bandwidth_id: 全域互联带宽ID。
        :type global_connection_bandwidth_id: str
        :param bandwidth_size: 带宽值，单位Mbps。
        :type bandwidth_size: int
        :param connection_type: 中心网络连接类型定义： - ER-ER (ER-ER Connection) - ER-GDGW (ER-GDGW Attachment Connection) - ER-ER_ROUTE_TABLE (ER-ER_ROUTE_TABLE Attachment Connection)
        :type connection_type: str
        :param connection_point_pair: 中心网络连接的两个端点定义，长度固定为2的数组。
        :type connection_point_pair: list[:class:`huaweicloudsdkcc.v3.ConnectionPoint`]
        :param state: 中心网络连接状态。 - AVAILABLE (可用) - CREATING (创建中) - UPDATING (更新中) - DELETING (删除中) - FREEZING (冻结中) - UNFREEZING (解冻中) - RECOVERING (恢复中) - FAILED (失败) - DELETED (已删除) - APPROVING (审批中) - APPROVED (已审批) - UNAPPROVED (审批未通过)
        :type state: str
        """
        
        

        self._id = None
        self._plane_id = None
        self._global_connection_bandwidth_id = None
        self._bandwidth_size = None
        self._connection_type = None
        self._connection_point_pair = None
        self._state = None
        self.discriminator = None

        self.id = id
        self.plane_id = plane_id
        if global_connection_bandwidth_id is not None:
            self.global_connection_bandwidth_id = global_connection_bandwidth_id
        if bandwidth_size is not None:
            self.bandwidth_size = bandwidth_size
        self.connection_type = connection_type
        self.connection_point_pair = connection_point_pair
        self.state = state

    @property
    def id(self):
        r"""Gets the id of this CentralNetworkConnectionInfo.

        实例ID。

        :return: The id of this CentralNetworkConnectionInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CentralNetworkConnectionInfo.

        实例ID。

        :param id: The id of this CentralNetworkConnectionInfo.
        :type id: str
        """
        self._id = id

    @property
    def plane_id(self):
        r"""Gets the plane_id of this CentralNetworkConnectionInfo.

        中心网络平面ID。

        :return: The plane_id of this CentralNetworkConnectionInfo.
        :rtype: str
        """
        return self._plane_id

    @plane_id.setter
    def plane_id(self, plane_id):
        r"""Sets the plane_id of this CentralNetworkConnectionInfo.

        中心网络平面ID。

        :param plane_id: The plane_id of this CentralNetworkConnectionInfo.
        :type plane_id: str
        """
        self._plane_id = plane_id

    @property
    def global_connection_bandwidth_id(self):
        r"""Gets the global_connection_bandwidth_id of this CentralNetworkConnectionInfo.

        全域互联带宽ID。

        :return: The global_connection_bandwidth_id of this CentralNetworkConnectionInfo.
        :rtype: str
        """
        return self._global_connection_bandwidth_id

    @global_connection_bandwidth_id.setter
    def global_connection_bandwidth_id(self, global_connection_bandwidth_id):
        r"""Sets the global_connection_bandwidth_id of this CentralNetworkConnectionInfo.

        全域互联带宽ID。

        :param global_connection_bandwidth_id: The global_connection_bandwidth_id of this CentralNetworkConnectionInfo.
        :type global_connection_bandwidth_id: str
        """
        self._global_connection_bandwidth_id = global_connection_bandwidth_id

    @property
    def bandwidth_size(self):
        r"""Gets the bandwidth_size of this CentralNetworkConnectionInfo.

        带宽值，单位Mbps。

        :return: The bandwidth_size of this CentralNetworkConnectionInfo.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        r"""Sets the bandwidth_size of this CentralNetworkConnectionInfo.

        带宽值，单位Mbps。

        :param bandwidth_size: The bandwidth_size of this CentralNetworkConnectionInfo.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

    @property
    def connection_type(self):
        r"""Gets the connection_type of this CentralNetworkConnectionInfo.

        中心网络连接类型定义： - ER-ER (ER-ER Connection) - ER-GDGW (ER-GDGW Attachment Connection) - ER-ER_ROUTE_TABLE (ER-ER_ROUTE_TABLE Attachment Connection)

        :return: The connection_type of this CentralNetworkConnectionInfo.
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        r"""Sets the connection_type of this CentralNetworkConnectionInfo.

        中心网络连接类型定义： - ER-ER (ER-ER Connection) - ER-GDGW (ER-GDGW Attachment Connection) - ER-ER_ROUTE_TABLE (ER-ER_ROUTE_TABLE Attachment Connection)

        :param connection_type: The connection_type of this CentralNetworkConnectionInfo.
        :type connection_type: str
        """
        self._connection_type = connection_type

    @property
    def connection_point_pair(self):
        r"""Gets the connection_point_pair of this CentralNetworkConnectionInfo.

        中心网络连接的两个端点定义，长度固定为2的数组。

        :return: The connection_point_pair of this CentralNetworkConnectionInfo.
        :rtype: list[:class:`huaweicloudsdkcc.v3.ConnectionPoint`]
        """
        return self._connection_point_pair

    @connection_point_pair.setter
    def connection_point_pair(self, connection_point_pair):
        r"""Sets the connection_point_pair of this CentralNetworkConnectionInfo.

        中心网络连接的两个端点定义，长度固定为2的数组。

        :param connection_point_pair: The connection_point_pair of this CentralNetworkConnectionInfo.
        :type connection_point_pair: list[:class:`huaweicloudsdkcc.v3.ConnectionPoint`]
        """
        self._connection_point_pair = connection_point_pair

    @property
    def state(self):
        r"""Gets the state of this CentralNetworkConnectionInfo.

        中心网络连接状态。 - AVAILABLE (可用) - CREATING (创建中) - UPDATING (更新中) - DELETING (删除中) - FREEZING (冻结中) - UNFREEZING (解冻中) - RECOVERING (恢复中) - FAILED (失败) - DELETED (已删除) - APPROVING (审批中) - APPROVED (已审批) - UNAPPROVED (审批未通过)

        :return: The state of this CentralNetworkConnectionInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this CentralNetworkConnectionInfo.

        中心网络连接状态。 - AVAILABLE (可用) - CREATING (创建中) - UPDATING (更新中) - DELETING (删除中) - FREEZING (冻结中) - UNFREEZING (解冻中) - RECOVERING (恢复中) - FAILED (失败) - DELETED (已删除) - APPROVING (审批中) - APPROVED (已审批) - UNAPPROVED (审批未通过)

        :param state: The state of this CentralNetworkConnectionInfo.
        :type state: str
        """
        self._state = state

    def to_dict(self):
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
        if not isinstance(other, CentralNetworkConnectionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
