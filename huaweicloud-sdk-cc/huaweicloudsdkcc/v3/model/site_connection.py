# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SiteConnection:

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
        'site_network_id': 'str',
        'state': 'SiteConnectionStateEnum',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'edge_pair': 'list[DirectedEdge]',
        'cross_region_type': 'CrossRegionTypeEnum',
        'global_connection_bandwidth_id': 'str',
        'bandwidth_size': 'int',
        'is_frozen': 'bool',
        'frozen_effect': 'FrozenEffectEnum',
        'is_bind_bandwidth': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'site_network_id': 'site_network_id',
        'state': 'state',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'edge_pair': 'edge_pair',
        'cross_region_type': 'cross_region_type',
        'global_connection_bandwidth_id': 'global_connection_bandwidth_id',
        'bandwidth_size': 'bandwidth_size',
        'is_frozen': 'is_frozen',
        'frozen_effect': 'frozen_effect',
        'is_bind_bandwidth': 'is_bind_bandwidth'
    }

    def __init__(self, id=None, site_network_id=None, state=None, created_at=None, updated_at=None, edge_pair=None, cross_region_type=None, global_connection_bandwidth_id=None, bandwidth_size=None, is_frozen=None, frozen_effect=None, is_bind_bandwidth=None):
        r"""SiteConnection

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param site_network_id: 分支网络ID。
        :type site_network_id: str
        :param state: 
        :type state: :class:`huaweicloudsdkcc.v3.SiteConnectionStateEnum`
        :param created_at: 实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type created_at: datetime
        :param updated_at: 实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。
        :type updated_at: datetime
        :param edge_pair: 分支网络连接的两个端点定义，长度固定为2的数组。
        :type edge_pair: list[:class:`huaweicloudsdkcc.v3.DirectedEdge`]
        :param cross_region_type: 
        :type cross_region_type: :class:`huaweicloudsdkcc.v3.CrossRegionTypeEnum`
        :param global_connection_bandwidth_id: 全域互联带宽ID。
        :type global_connection_bandwidth_id: str
        :param bandwidth_size: 带宽值，单位Mbps。
        :type bandwidth_size: int
        :param is_frozen: 是否冻结。
        :type is_frozen: bool
        :param frozen_effect: 
        :type frozen_effect: :class:`huaweicloudsdkcc.v3.FrozenEffectEnum`
        :param is_bind_bandwidth: 是否绑定带宽包。
        :type is_bind_bandwidth: bool
        """
        
        

        self._id = None
        self._site_network_id = None
        self._state = None
        self._created_at = None
        self._updated_at = None
        self._edge_pair = None
        self._cross_region_type = None
        self._global_connection_bandwidth_id = None
        self._bandwidth_size = None
        self._is_frozen = None
        self._frozen_effect = None
        self._is_bind_bandwidth = None
        self.discriminator = None

        self.id = id
        self.site_network_id = site_network_id
        self.state = state
        self.created_at = created_at
        self.updated_at = updated_at
        self.edge_pair = edge_pair
        self.cross_region_type = cross_region_type
        if global_connection_bandwidth_id is not None:
            self.global_connection_bandwidth_id = global_connection_bandwidth_id
        if bandwidth_size is not None:
            self.bandwidth_size = bandwidth_size
        self.is_frozen = is_frozen
        if frozen_effect is not None:
            self.frozen_effect = frozen_effect
        if is_bind_bandwidth is not None:
            self.is_bind_bandwidth = is_bind_bandwidth

    @property
    def id(self):
        r"""Gets the id of this SiteConnection.

        实例ID。

        :return: The id of this SiteConnection.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SiteConnection.

        实例ID。

        :param id: The id of this SiteConnection.
        :type id: str
        """
        self._id = id

    @property
    def site_network_id(self):
        r"""Gets the site_network_id of this SiteConnection.

        分支网络ID。

        :return: The site_network_id of this SiteConnection.
        :rtype: str
        """
        return self._site_network_id

    @site_network_id.setter
    def site_network_id(self, site_network_id):
        r"""Sets the site_network_id of this SiteConnection.

        分支网络ID。

        :param site_network_id: The site_network_id of this SiteConnection.
        :type site_network_id: str
        """
        self._site_network_id = site_network_id

    @property
    def state(self):
        r"""Gets the state of this SiteConnection.

        :return: The state of this SiteConnection.
        :rtype: :class:`huaweicloudsdkcc.v3.SiteConnectionStateEnum`
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this SiteConnection.

        :param state: The state of this SiteConnection.
        :type state: :class:`huaweicloudsdkcc.v3.SiteConnectionStateEnum`
        """
        self._state = state

    @property
    def created_at(self):
        r"""Gets the created_at of this SiteConnection.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The created_at of this SiteConnection.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this SiteConnection.

        实例创建时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param created_at: The created_at of this SiteConnection.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this SiteConnection.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :return: The updated_at of this SiteConnection.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this SiteConnection.

        实例更新时间。UTC时间格式，yyyy-MM-ddTHH:mm:ss。

        :param updated_at: The updated_at of this SiteConnection.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def edge_pair(self):
        r"""Gets the edge_pair of this SiteConnection.

        分支网络连接的两个端点定义，长度固定为2的数组。

        :return: The edge_pair of this SiteConnection.
        :rtype: list[:class:`huaweicloudsdkcc.v3.DirectedEdge`]
        """
        return self._edge_pair

    @edge_pair.setter
    def edge_pair(self, edge_pair):
        r"""Sets the edge_pair of this SiteConnection.

        分支网络连接的两个端点定义，长度固定为2的数组。

        :param edge_pair: The edge_pair of this SiteConnection.
        :type edge_pair: list[:class:`huaweicloudsdkcc.v3.DirectedEdge`]
        """
        self._edge_pair = edge_pair

    @property
    def cross_region_type(self):
        r"""Gets the cross_region_type of this SiteConnection.

        :return: The cross_region_type of this SiteConnection.
        :rtype: :class:`huaweicloudsdkcc.v3.CrossRegionTypeEnum`
        """
        return self._cross_region_type

    @cross_region_type.setter
    def cross_region_type(self, cross_region_type):
        r"""Sets the cross_region_type of this SiteConnection.

        :param cross_region_type: The cross_region_type of this SiteConnection.
        :type cross_region_type: :class:`huaweicloudsdkcc.v3.CrossRegionTypeEnum`
        """
        self._cross_region_type = cross_region_type

    @property
    def global_connection_bandwidth_id(self):
        r"""Gets the global_connection_bandwidth_id of this SiteConnection.

        全域互联带宽ID。

        :return: The global_connection_bandwidth_id of this SiteConnection.
        :rtype: str
        """
        return self._global_connection_bandwidth_id

    @global_connection_bandwidth_id.setter
    def global_connection_bandwidth_id(self, global_connection_bandwidth_id):
        r"""Sets the global_connection_bandwidth_id of this SiteConnection.

        全域互联带宽ID。

        :param global_connection_bandwidth_id: The global_connection_bandwidth_id of this SiteConnection.
        :type global_connection_bandwidth_id: str
        """
        self._global_connection_bandwidth_id = global_connection_bandwidth_id

    @property
    def bandwidth_size(self):
        r"""Gets the bandwidth_size of this SiteConnection.

        带宽值，单位Mbps。

        :return: The bandwidth_size of this SiteConnection.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        r"""Sets the bandwidth_size of this SiteConnection.

        带宽值，单位Mbps。

        :param bandwidth_size: The bandwidth_size of this SiteConnection.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

    @property
    def is_frozen(self):
        r"""Gets the is_frozen of this SiteConnection.

        是否冻结。

        :return: The is_frozen of this SiteConnection.
        :rtype: bool
        """
        return self._is_frozen

    @is_frozen.setter
    def is_frozen(self, is_frozen):
        r"""Sets the is_frozen of this SiteConnection.

        是否冻结。

        :param is_frozen: The is_frozen of this SiteConnection.
        :type is_frozen: bool
        """
        self._is_frozen = is_frozen

    @property
    def frozen_effect(self):
        r"""Gets the frozen_effect of this SiteConnection.

        :return: The frozen_effect of this SiteConnection.
        :rtype: :class:`huaweicloudsdkcc.v3.FrozenEffectEnum`
        """
        return self._frozen_effect

    @frozen_effect.setter
    def frozen_effect(self, frozen_effect):
        r"""Sets the frozen_effect of this SiteConnection.

        :param frozen_effect: The frozen_effect of this SiteConnection.
        :type frozen_effect: :class:`huaweicloudsdkcc.v3.FrozenEffectEnum`
        """
        self._frozen_effect = frozen_effect

    @property
    def is_bind_bandwidth(self):
        r"""Gets the is_bind_bandwidth of this SiteConnection.

        是否绑定带宽包。

        :return: The is_bind_bandwidth of this SiteConnection.
        :rtype: bool
        """
        return self._is_bind_bandwidth

    @is_bind_bandwidth.setter
    def is_bind_bandwidth(self, is_bind_bandwidth):
        r"""Sets the is_bind_bandwidth of this SiteConnection.

        是否绑定带宽包。

        :param is_bind_bandwidth: The is_bind_bandwidth of this SiteConnection.
        :type is_bind_bandwidth: bool
        """
        self._is_bind_bandwidth = is_bind_bandwidth

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
        if not isinstance(other, SiteConnection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
