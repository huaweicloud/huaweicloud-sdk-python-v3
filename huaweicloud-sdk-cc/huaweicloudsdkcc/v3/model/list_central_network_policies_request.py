# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCentralNetworkPoliciesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'central_network_id': 'str',
        'limit': 'int',
        'marker': 'str',
        'sort_key': 'str',
        'sort_dir': 'SortDir',
        'id': 'list[str]',
        'state': 'list[CentralNetworkPolicyStateEnum]',
        'version': 'list[Version]',
        'is_applied': 'bool'
    }

    attribute_map = {
        'central_network_id': 'central_network_id',
        'limit': 'limit',
        'marker': 'marker',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'id': 'id',
        'state': 'state',
        'version': 'version',
        'is_applied': 'is_applied'
    }

    def __init__(self, central_network_id=None, limit=None, marker=None, sort_key=None, sort_dir=None, id=None, state=None, version=None, is_applied=None):
        r"""ListCentralNetworkPoliciesRequest

        The model defined in huaweicloud sdk

        :param central_network_id: 中心网络的ID。
        :type central_network_id: str
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
        :param state: 根据状态查询，可查询多个状态。
        :type state: list[:class:`huaweicloudsdkcc.v3.CentralNetworkPolicyStateEnum`]
        :param version: 根据版本查询，可查询多个名字。
        :type version: list[:class:`huaweicloudsdkcc.v3.Version`]
        :param is_applied: 是否被应用。
        :type is_applied: bool
        """
        
        

        self._central_network_id = None
        self._limit = None
        self._marker = None
        self._sort_key = None
        self._sort_dir = None
        self._id = None
        self._state = None
        self._version = None
        self._is_applied = None
        self.discriminator = None

        self.central_network_id = central_network_id
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
        if state is not None:
            self.state = state
        if version is not None:
            self.version = version
        if is_applied is not None:
            self.is_applied = is_applied

    @property
    def central_network_id(self):
        r"""Gets the central_network_id of this ListCentralNetworkPoliciesRequest.

        中心网络的ID。

        :return: The central_network_id of this ListCentralNetworkPoliciesRequest.
        :rtype: str
        """
        return self._central_network_id

    @central_network_id.setter
    def central_network_id(self, central_network_id):
        r"""Sets the central_network_id of this ListCentralNetworkPoliciesRequest.

        中心网络的ID。

        :param central_network_id: The central_network_id of this ListCentralNetworkPoliciesRequest.
        :type central_network_id: str
        """
        self._central_network_id = central_network_id

    @property
    def limit(self):
        r"""Gets the limit of this ListCentralNetworkPoliciesRequest.

        每页返回的个数。 取值范围：1~1000。

        :return: The limit of this ListCentralNetworkPoliciesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCentralNetworkPoliciesRequest.

        每页返回的个数。 取值范围：1~1000。

        :param limit: The limit of this ListCentralNetworkPoliciesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListCentralNetworkPoliciesRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。

        :return: The marker of this ListCentralNetworkPoliciesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListCentralNetworkPoliciesRequest.

        翻页信息，从上次API调用返回的翻页数据中获取，可填写前一页marker或者后一页marker，填入前一页previous_marker就向前翻页，后一页next_marker就向后翻页。 翻页过程中，查询条件不能修改，包括过滤条件、排序条件、limit。

        :param marker: The marker of this ListCentralNetworkPoliciesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListCentralNetworkPoliciesRequest.

        排序字段。

        :return: The sort_key of this ListCentralNetworkPoliciesRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListCentralNetworkPoliciesRequest.

        排序字段。

        :param sort_key: The sort_key of this ListCentralNetworkPoliciesRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListCentralNetworkPoliciesRequest.

        指定排序是升序还是降序（asc为升序，desc为降序）。

        :return: The sort_dir of this ListCentralNetworkPoliciesRequest.
        :rtype: :class:`huaweicloudsdkcc.v3.SortDir`
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListCentralNetworkPoliciesRequest.

        指定排序是升序还是降序（asc为升序，desc为降序）。

        :param sort_dir: The sort_dir of this ListCentralNetworkPoliciesRequest.
        :type sort_dir: :class:`huaweicloudsdkcc.v3.SortDir`
        """
        self._sort_dir = sort_dir

    @property
    def id(self):
        r"""Gets the id of this ListCentralNetworkPoliciesRequest.

        根据ID查询，可查询多个ID。

        :return: The id of this ListCentralNetworkPoliciesRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListCentralNetworkPoliciesRequest.

        根据ID查询，可查询多个ID。

        :param id: The id of this ListCentralNetworkPoliciesRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def state(self):
        r"""Gets the state of this ListCentralNetworkPoliciesRequest.

        根据状态查询，可查询多个状态。

        :return: The state of this ListCentralNetworkPoliciesRequest.
        :rtype: list[:class:`huaweicloudsdkcc.v3.CentralNetworkPolicyStateEnum`]
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListCentralNetworkPoliciesRequest.

        根据状态查询，可查询多个状态。

        :param state: The state of this ListCentralNetworkPoliciesRequest.
        :type state: list[:class:`huaweicloudsdkcc.v3.CentralNetworkPolicyStateEnum`]
        """
        self._state = state

    @property
    def version(self):
        r"""Gets the version of this ListCentralNetworkPoliciesRequest.

        根据版本查询，可查询多个名字。

        :return: The version of this ListCentralNetworkPoliciesRequest.
        :rtype: list[:class:`huaweicloudsdkcc.v3.Version`]
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ListCentralNetworkPoliciesRequest.

        根据版本查询，可查询多个名字。

        :param version: The version of this ListCentralNetworkPoliciesRequest.
        :type version: list[:class:`huaweicloudsdkcc.v3.Version`]
        """
        self._version = version

    @property
    def is_applied(self):
        r"""Gets the is_applied of this ListCentralNetworkPoliciesRequest.

        是否被应用。

        :return: The is_applied of this ListCentralNetworkPoliciesRequest.
        :rtype: bool
        """
        return self._is_applied

    @is_applied.setter
    def is_applied(self, is_applied):
        r"""Sets the is_applied of this ListCentralNetworkPoliciesRequest.

        是否被应用。

        :param is_applied: The is_applied of this ListCentralNetworkPoliciesRequest.
        :type is_applied: bool
        """
        self._is_applied = is_applied

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
        if not isinstance(other, ListCentralNetworkPoliciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
