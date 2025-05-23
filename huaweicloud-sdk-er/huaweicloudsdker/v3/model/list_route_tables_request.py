# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRouteTablesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'er_id': 'str',
        'limit': 'int',
        'marker': 'str',
        'state': 'list[str]',
        'is_default_propagation_table': 'bool',
        'is_default_association_table': 'bool',
        'sort_key': 'list[str]',
        'sort_dir': 'list[str]'
    }

    attribute_map = {
        'er_id': 'er_id',
        'limit': 'limit',
        'marker': 'marker',
        'state': 'state',
        'is_default_propagation_table': 'is_default_propagation_table',
        'is_default_association_table': 'is_default_association_table',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, er_id=None, limit=None, marker=None, state=None, is_default_propagation_table=None, is_default_association_table=None, sort_key=None, sort_dir=None):
        r"""ListRouteTablesRequest

        The model defined in huaweicloud sdk

        :param er_id: 企业路由器实例ID
        :type er_id: str
        :param limit: 每页返回的个数。 取值范围：0~2000。
        :type limit: int
        :param marker: 上一页最后一条记录的企业路由器实例的id，为空时为查询第一页。 使用说明：必须与limit一起使用。
        :type marker: str
        :param state: 状态
        :type state: list[str]
        :param is_default_propagation_table: 是否为默认传播路由表
        :type is_default_propagation_table: bool
        :param is_default_association_table: 是否为默认关联路由表
        :type is_default_association_table: bool
        :param sort_key: 按关键字排序，默认按照id排序，可选值:id|name|state
        :type sort_key: list[str]
        :param sort_dir: 返回结果按照升序或降序排列，默认为asc,降序为desc
        :type sort_dir: list[str]
        """
        
        

        self._er_id = None
        self._limit = None
        self._marker = None
        self._state = None
        self._is_default_propagation_table = None
        self._is_default_association_table = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        self.er_id = er_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if state is not None:
            self.state = state
        if is_default_propagation_table is not None:
            self.is_default_propagation_table = is_default_propagation_table
        if is_default_association_table is not None:
            self.is_default_association_table = is_default_association_table
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def er_id(self):
        r"""Gets the er_id of this ListRouteTablesRequest.

        企业路由器实例ID

        :return: The er_id of this ListRouteTablesRequest.
        :rtype: str
        """
        return self._er_id

    @er_id.setter
    def er_id(self, er_id):
        r"""Sets the er_id of this ListRouteTablesRequest.

        企业路由器实例ID

        :param er_id: The er_id of this ListRouteTablesRequest.
        :type er_id: str
        """
        self._er_id = er_id

    @property
    def limit(self):
        r"""Gets the limit of this ListRouteTablesRequest.

        每页返回的个数。 取值范围：0~2000。

        :return: The limit of this ListRouteTablesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRouteTablesRequest.

        每页返回的个数。 取值范围：0~2000。

        :param limit: The limit of this ListRouteTablesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListRouteTablesRequest.

        上一页最后一条记录的企业路由器实例的id，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :return: The marker of this ListRouteTablesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListRouteTablesRequest.

        上一页最后一条记录的企业路由器实例的id，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :param marker: The marker of this ListRouteTablesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def state(self):
        r"""Gets the state of this ListRouteTablesRequest.

        状态

        :return: The state of this ListRouteTablesRequest.
        :rtype: list[str]
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListRouteTablesRequest.

        状态

        :param state: The state of this ListRouteTablesRequest.
        :type state: list[str]
        """
        self._state = state

    @property
    def is_default_propagation_table(self):
        r"""Gets the is_default_propagation_table of this ListRouteTablesRequest.

        是否为默认传播路由表

        :return: The is_default_propagation_table of this ListRouteTablesRequest.
        :rtype: bool
        """
        return self._is_default_propagation_table

    @is_default_propagation_table.setter
    def is_default_propagation_table(self, is_default_propagation_table):
        r"""Sets the is_default_propagation_table of this ListRouteTablesRequest.

        是否为默认传播路由表

        :param is_default_propagation_table: The is_default_propagation_table of this ListRouteTablesRequest.
        :type is_default_propagation_table: bool
        """
        self._is_default_propagation_table = is_default_propagation_table

    @property
    def is_default_association_table(self):
        r"""Gets the is_default_association_table of this ListRouteTablesRequest.

        是否为默认关联路由表

        :return: The is_default_association_table of this ListRouteTablesRequest.
        :rtype: bool
        """
        return self._is_default_association_table

    @is_default_association_table.setter
    def is_default_association_table(self, is_default_association_table):
        r"""Sets the is_default_association_table of this ListRouteTablesRequest.

        是否为默认关联路由表

        :param is_default_association_table: The is_default_association_table of this ListRouteTablesRequest.
        :type is_default_association_table: bool
        """
        self._is_default_association_table = is_default_association_table

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListRouteTablesRequest.

        按关键字排序，默认按照id排序，可选值:id|name|state

        :return: The sort_key of this ListRouteTablesRequest.
        :rtype: list[str]
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListRouteTablesRequest.

        按关键字排序，默认按照id排序，可选值:id|name|state

        :param sort_key: The sort_key of this ListRouteTablesRequest.
        :type sort_key: list[str]
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListRouteTablesRequest.

        返回结果按照升序或降序排列，默认为asc,降序为desc

        :return: The sort_dir of this ListRouteTablesRequest.
        :rtype: list[str]
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListRouteTablesRequest.

        返回结果按照升序或降序排列，默认为asc,降序为desc

        :param sort_dir: The sort_dir of this ListRouteTablesRequest.
        :type sort_dir: list[str]
        """
        self._sort_dir = sort_dir

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
        if not isinstance(other, ListRouteTablesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
