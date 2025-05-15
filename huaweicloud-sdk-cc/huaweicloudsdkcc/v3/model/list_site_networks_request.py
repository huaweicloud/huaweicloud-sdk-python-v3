# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSiteNetworksRequest:

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
        'state': 'list[SiteNetworkStateEnum]',
        'enterprise_project_id': 'list[str]',
        'global_dc_gateway_id': 'list[str]',
        'global_connection_bandwidth_id': 'list[str]',
        'connection_id': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'id': 'id',
        'name': 'name',
        'state': 'state',
        'enterprise_project_id': 'enterprise_project_id',
        'global_dc_gateway_id': 'global_dc_gateway_id',
        'global_connection_bandwidth_id': 'global_connection_bandwidth_id',
        'connection_id': 'connection_id'
    }

    def __init__(self, limit=None, marker=None, sort_key=None, sort_dir=None, id=None, name=None, state=None, enterprise_project_id=None, global_dc_gateway_id=None, global_connection_bandwidth_id=None, connection_id=None):
        r"""ListSiteNetworksRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数。 取值范围：1~1000。
        :type limit: int
        :param marker: 翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。
        :type marker: str
        :param sort_key: 排序字段。
        :type sort_key: str
        :param sort_dir: 指定排序是升序还是降序（asc为升序，desc为降序）。
        :type sort_dir: :class:`huaweicloudsdkcc.v3.SortDir`
        :param id: 根据ID查询，可查询多个ID。
        :type id: list[str]
        :param name: 根据名字查询，可查询多个名字。
        :type name: list[str]
        :param state: 根据状态查询，可查询多个状态。
        :type state: list[:class:`huaweicloudsdkcc.v3.SiteNetworkStateEnum`]
        :param enterprise_project_id: 根据企业项目ID过滤列表。
        :type enterprise_project_id: list[str]
        :param global_dc_gateway_id: 根据GDW实例ID过滤列表。
        :type global_dc_gateway_id: list[str]
        :param global_connection_bandwidth_id: 根据带宽包ID过滤。
        :type global_connection_bandwidth_id: list[str]
        :param connection_id: 分支连接的ID。
        :type connection_id: list[str]
        """
        
        

        self._limit = None
        self._marker = None
        self._sort_key = None
        self._sort_dir = None
        self._id = None
        self._name = None
        self._state = None
        self._enterprise_project_id = None
        self._global_dc_gateway_id = None
        self._global_connection_bandwidth_id = None
        self._connection_id = None
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
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if global_dc_gateway_id is not None:
            self.global_dc_gateway_id = global_dc_gateway_id
        if global_connection_bandwidth_id is not None:
            self.global_connection_bandwidth_id = global_connection_bandwidth_id
        if connection_id is not None:
            self.connection_id = connection_id

    @property
    def limit(self):
        r"""Gets the limit of this ListSiteNetworksRequest.

        每页返回的个数。 取值范围：1~1000。

        :return: The limit of this ListSiteNetworksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSiteNetworksRequest.

        每页返回的个数。 取值范围：1~1000。

        :param limit: The limit of this ListSiteNetworksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListSiteNetworksRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。

        :return: The marker of this ListSiteNetworksRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListSiteNetworksRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。

        :param marker: The marker of this ListSiteNetworksRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListSiteNetworksRequest.

        排序字段。

        :return: The sort_key of this ListSiteNetworksRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListSiteNetworksRequest.

        排序字段。

        :param sort_key: The sort_key of this ListSiteNetworksRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListSiteNetworksRequest.

        指定排序是升序还是降序（asc为升序，desc为降序）。

        :return: The sort_dir of this ListSiteNetworksRequest.
        :rtype: :class:`huaweicloudsdkcc.v3.SortDir`
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListSiteNetworksRequest.

        指定排序是升序还是降序（asc为升序，desc为降序）。

        :param sort_dir: The sort_dir of this ListSiteNetworksRequest.
        :type sort_dir: :class:`huaweicloudsdkcc.v3.SortDir`
        """
        self._sort_dir = sort_dir

    @property
    def id(self):
        r"""Gets the id of this ListSiteNetworksRequest.

        根据ID查询，可查询多个ID。

        :return: The id of this ListSiteNetworksRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListSiteNetworksRequest.

        根据ID查询，可查询多个ID。

        :param id: The id of this ListSiteNetworksRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListSiteNetworksRequest.

        根据名字查询，可查询多个名字。

        :return: The name of this ListSiteNetworksRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListSiteNetworksRequest.

        根据名字查询，可查询多个名字。

        :param name: The name of this ListSiteNetworksRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def state(self):
        r"""Gets the state of this ListSiteNetworksRequest.

        根据状态查询，可查询多个状态。

        :return: The state of this ListSiteNetworksRequest.
        :rtype: list[:class:`huaweicloudsdkcc.v3.SiteNetworkStateEnum`]
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListSiteNetworksRequest.

        根据状态查询，可查询多个状态。

        :param state: The state of this ListSiteNetworksRequest.
        :type state: list[:class:`huaweicloudsdkcc.v3.SiteNetworkStateEnum`]
        """
        self._state = state

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListSiteNetworksRequest.

        根据企业项目ID过滤列表。

        :return: The enterprise_project_id of this ListSiteNetworksRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListSiteNetworksRequest.

        根据企业项目ID过滤列表。

        :param enterprise_project_id: The enterprise_project_id of this ListSiteNetworksRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def global_dc_gateway_id(self):
        r"""Gets the global_dc_gateway_id of this ListSiteNetworksRequest.

        根据GDW实例ID过滤列表。

        :return: The global_dc_gateway_id of this ListSiteNetworksRequest.
        :rtype: list[str]
        """
        return self._global_dc_gateway_id

    @global_dc_gateway_id.setter
    def global_dc_gateway_id(self, global_dc_gateway_id):
        r"""Sets the global_dc_gateway_id of this ListSiteNetworksRequest.

        根据GDW实例ID过滤列表。

        :param global_dc_gateway_id: The global_dc_gateway_id of this ListSiteNetworksRequest.
        :type global_dc_gateway_id: list[str]
        """
        self._global_dc_gateway_id = global_dc_gateway_id

    @property
    def global_connection_bandwidth_id(self):
        r"""Gets the global_connection_bandwidth_id of this ListSiteNetworksRequest.

        根据带宽包ID过滤。

        :return: The global_connection_bandwidth_id of this ListSiteNetworksRequest.
        :rtype: list[str]
        """
        return self._global_connection_bandwidth_id

    @global_connection_bandwidth_id.setter
    def global_connection_bandwidth_id(self, global_connection_bandwidth_id):
        r"""Sets the global_connection_bandwidth_id of this ListSiteNetworksRequest.

        根据带宽包ID过滤。

        :param global_connection_bandwidth_id: The global_connection_bandwidth_id of this ListSiteNetworksRequest.
        :type global_connection_bandwidth_id: list[str]
        """
        self._global_connection_bandwidth_id = global_connection_bandwidth_id

    @property
    def connection_id(self):
        r"""Gets the connection_id of this ListSiteNetworksRequest.

        分支连接的ID。

        :return: The connection_id of this ListSiteNetworksRequest.
        :rtype: list[str]
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this ListSiteNetworksRequest.

        分支连接的ID。

        :param connection_id: The connection_id of this ListSiteNetworksRequest.
        :type connection_id: list[str]
        """
        self._connection_id = connection_id

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
        if not isinstance(other, ListSiteNetworksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
