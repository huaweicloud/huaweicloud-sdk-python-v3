# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCentralNetworkConnectionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'sort_key': 'str',
        'sort_dir': 'SortDir',
        'id': 'list[str]',
        'name': 'list[str]',
        'state': 'list[CentralNetworkConnectionStateEnum]',
        'central_network_id': 'str',
        'global_connection_bandwidth_id': 'list[str]',
        'bandwidth_type': 'BandwidthTypeEnum',
        'connection_type': 'ConnectionTypeEnum',
        'is_cross_region': 'bool'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'id': 'id',
        'name': 'name',
        'state': 'state',
        'central_network_id': 'central_network_id',
        'global_connection_bandwidth_id': 'global_connection_bandwidth_id',
        'bandwidth_type': 'bandwidth_type',
        'connection_type': 'connection_type',
        'is_cross_region': 'is_cross_region'
    }

    def __init__(self, limit=None, marker=None, sort_key=None, sort_dir=None, id=None, name=None, state=None, central_network_id=None, global_connection_bandwidth_id=None, bandwidth_type=None, connection_type=None, is_cross_region=None):
        """ListCentralNetworkConnectionsRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数。 取值范围：1~1000。
        :type limit: int
        :param marker: 翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向翻页。 翻页过程中，查询条件不能修改，包括过滤条件，排序条件，limit。
        :type marker: str
        :param sort_key: 排序字段。
        :type sort_key: str
        :param sort_dir: 指定排序是升序还是降序(asc为升序，desc为降序)。
        :type sort_dir: :class:`huaweicloudsdkcc.v3.SortDir`
        :param id: 根据id查询，可查询多个id。
        :type id: list[str]
        :param name: 根据名字查询，可查询多个名字。
        :type name: list[str]
        :param state: 根据状态查询，可查询多个状态。
        :type state: list[:class:`huaweicloudsdkcc.v3.CentralNetworkConnectionStateEnum`]
        :param central_network_id: 中心网络的ID。
        :type central_network_id: str
        :param global_connection_bandwidth_id: 根据带宽包ID过滤。
        :type global_connection_bandwidth_id: list[str]
        :param bandwidth_type: 根据带宽类型查询。带宽类型包括： - BandwidthPackage (按带宽计费，需要绑定全域互联带宽，并指定分配带宽大小) - TestBandwidth (不收费的测试带宽，仅保留最小带宽，用于测试跨地域连通性）
        :type bandwidth_type: :class:`huaweicloudsdkcc.v3.BandwidthTypeEnum`
        :param connection_type: 连接类型，支持。
        :type connection_type: :class:`huaweicloudsdkcc.v3.ConnectionTypeEnum`
        :param is_cross_region: 是否跨地域。
        :type is_cross_region: bool
        """
        
        

        self._limit = None
        self._marker = None
        self._sort_key = None
        self._sort_dir = None
        self._id = None
        self._name = None
        self._state = None
        self._central_network_id = None
        self._global_connection_bandwidth_id = None
        self._bandwidth_type = None
        self._connection_type = None
        self._is_cross_region = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if state is not None:
            self.state = state
        self.central_network_id = central_network_id
        if global_connection_bandwidth_id is not None:
            self.global_connection_bandwidth_id = global_connection_bandwidth_id
        if bandwidth_type is not None:
            self.bandwidth_type = bandwidth_type
        if connection_type is not None:
            self.connection_type = connection_type
        if is_cross_region is not None:
            self.is_cross_region = is_cross_region

    @property
    def limit(self):
        """Gets the limit of this ListCentralNetworkConnectionsRequest.

        每页返回的个数。 取值范围：1~1000。

        :return: The limit of this ListCentralNetworkConnectionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCentralNetworkConnectionsRequest.

        每页返回的个数。 取值范围：1~1000。

        :param limit: The limit of this ListCentralNetworkConnectionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListCentralNetworkConnectionsRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向翻页。 翻页过程中，查询条件不能修改，包括过滤条件，排序条件，limit。

        :return: The marker of this ListCentralNetworkConnectionsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListCentralNetworkConnectionsRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向翻页。 翻页过程中，查询条件不能修改，包括过滤条件，排序条件，limit。

        :param marker: The marker of this ListCentralNetworkConnectionsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def sort_key(self):
        """Gets the sort_key of this ListCentralNetworkConnectionsRequest.

        排序字段。

        :return: The sort_key of this ListCentralNetworkConnectionsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListCentralNetworkConnectionsRequest.

        排序字段。

        :param sort_key: The sort_key of this ListCentralNetworkConnectionsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListCentralNetworkConnectionsRequest.

        指定排序是升序还是降序(asc为升序，desc为降序)。

        :return: The sort_dir of this ListCentralNetworkConnectionsRequest.
        :rtype: :class:`huaweicloudsdkcc.v3.SortDir`
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListCentralNetworkConnectionsRequest.

        指定排序是升序还是降序(asc为升序，desc为降序)。

        :param sort_dir: The sort_dir of this ListCentralNetworkConnectionsRequest.
        :type sort_dir: :class:`huaweicloudsdkcc.v3.SortDir`
        """
        self._sort_dir = sort_dir

    @property
    def id(self):
        """Gets the id of this ListCentralNetworkConnectionsRequest.

        根据id查询，可查询多个id。

        :return: The id of this ListCentralNetworkConnectionsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListCentralNetworkConnectionsRequest.

        根据id查询，可查询多个id。

        :param id: The id of this ListCentralNetworkConnectionsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListCentralNetworkConnectionsRequest.

        根据名字查询，可查询多个名字。

        :return: The name of this ListCentralNetworkConnectionsRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListCentralNetworkConnectionsRequest.

        根据名字查询，可查询多个名字。

        :param name: The name of this ListCentralNetworkConnectionsRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def state(self):
        """Gets the state of this ListCentralNetworkConnectionsRequest.

        根据状态查询，可查询多个状态。

        :return: The state of this ListCentralNetworkConnectionsRequest.
        :rtype: list[:class:`huaweicloudsdkcc.v3.CentralNetworkConnectionStateEnum`]
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ListCentralNetworkConnectionsRequest.

        根据状态查询，可查询多个状态。

        :param state: The state of this ListCentralNetworkConnectionsRequest.
        :type state: list[:class:`huaweicloudsdkcc.v3.CentralNetworkConnectionStateEnum`]
        """
        self._state = state

    @property
    def central_network_id(self):
        """Gets the central_network_id of this ListCentralNetworkConnectionsRequest.

        中心网络的ID。

        :return: The central_network_id of this ListCentralNetworkConnectionsRequest.
        :rtype: str
        """
        return self._central_network_id

    @central_network_id.setter
    def central_network_id(self, central_network_id):
        """Sets the central_network_id of this ListCentralNetworkConnectionsRequest.

        中心网络的ID。

        :param central_network_id: The central_network_id of this ListCentralNetworkConnectionsRequest.
        :type central_network_id: str
        """
        self._central_network_id = central_network_id

    @property
    def global_connection_bandwidth_id(self):
        """Gets the global_connection_bandwidth_id of this ListCentralNetworkConnectionsRequest.

        根据带宽包ID过滤。

        :return: The global_connection_bandwidth_id of this ListCentralNetworkConnectionsRequest.
        :rtype: list[str]
        """
        return self._global_connection_bandwidth_id

    @global_connection_bandwidth_id.setter
    def global_connection_bandwidth_id(self, global_connection_bandwidth_id):
        """Sets the global_connection_bandwidth_id of this ListCentralNetworkConnectionsRequest.

        根据带宽包ID过滤。

        :param global_connection_bandwidth_id: The global_connection_bandwidth_id of this ListCentralNetworkConnectionsRequest.
        :type global_connection_bandwidth_id: list[str]
        """
        self._global_connection_bandwidth_id = global_connection_bandwidth_id

    @property
    def bandwidth_type(self):
        """Gets the bandwidth_type of this ListCentralNetworkConnectionsRequest.

        根据带宽类型查询。带宽类型包括： - BandwidthPackage (按带宽计费，需要绑定全域互联带宽，并指定分配带宽大小) - TestBandwidth (不收费的测试带宽，仅保留最小带宽，用于测试跨地域连通性）

        :return: The bandwidth_type of this ListCentralNetworkConnectionsRequest.
        :rtype: :class:`huaweicloudsdkcc.v3.BandwidthTypeEnum`
        """
        return self._bandwidth_type

    @bandwidth_type.setter
    def bandwidth_type(self, bandwidth_type):
        """Sets the bandwidth_type of this ListCentralNetworkConnectionsRequest.

        根据带宽类型查询。带宽类型包括： - BandwidthPackage (按带宽计费，需要绑定全域互联带宽，并指定分配带宽大小) - TestBandwidth (不收费的测试带宽，仅保留最小带宽，用于测试跨地域连通性）

        :param bandwidth_type: The bandwidth_type of this ListCentralNetworkConnectionsRequest.
        :type bandwidth_type: :class:`huaweicloudsdkcc.v3.BandwidthTypeEnum`
        """
        self._bandwidth_type = bandwidth_type

    @property
    def connection_type(self):
        """Gets the connection_type of this ListCentralNetworkConnectionsRequest.

        连接类型，支持。

        :return: The connection_type of this ListCentralNetworkConnectionsRequest.
        :rtype: :class:`huaweicloudsdkcc.v3.ConnectionTypeEnum`
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """Sets the connection_type of this ListCentralNetworkConnectionsRequest.

        连接类型，支持。

        :param connection_type: The connection_type of this ListCentralNetworkConnectionsRequest.
        :type connection_type: :class:`huaweicloudsdkcc.v3.ConnectionTypeEnum`
        """
        self._connection_type = connection_type

    @property
    def is_cross_region(self):
        """Gets the is_cross_region of this ListCentralNetworkConnectionsRequest.

        是否跨地域。

        :return: The is_cross_region of this ListCentralNetworkConnectionsRequest.
        :rtype: bool
        """
        return self._is_cross_region

    @is_cross_region.setter
    def is_cross_region(self, is_cross_region):
        """Sets the is_cross_region of this ListCentralNetworkConnectionsRequest.

        是否跨地域。

        :param is_cross_region: The is_cross_region of this ListCentralNetworkConnectionsRequest.
        :type is_cross_region: bool
        """
        self._is_cross_region = is_cross_region

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
        if not isinstance(other, ListCentralNetworkConnectionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
