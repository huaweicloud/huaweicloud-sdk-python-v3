# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnterpriseRoutersRequest:

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
        'enterprise_project_id': 'list[str]',
        'state': 'list[str]',
        'id': 'list[str]',
        'resource_id': 'list[str]',
        'owned_by_self': 'bool',
        'sort_key': 'list[str]',
        'sort_dir': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'enterprise_project_id': 'enterprise_project_id',
        'state': 'state',
        'id': 'id',
        'resource_id': 'resource_id',
        'owned_by_self': 'owned_by_self',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, limit=None, marker=None, enterprise_project_id=None, state=None, id=None, resource_id=None, owned_by_self=None, sort_key=None, sort_dir=None):
        r"""ListEnterpriseRoutersRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数。 取值范围：0~2000。
        :type limit: int
        :param marker: 上一页最后一条记录的企业路由器实例的id，为空时为查询第一页。 使用说明：必须与limit一起使用。
        :type marker: str
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: list[str]
        :param state: 企业路由器实例状态
        :type state: list[str]
        :param id: 根据资源ID查询，可同时查询多个。
        :type id: list[str]
        :param resource_id: 连接对应的资源ID列表
        :type resource_id: list[str]
        :param owned_by_self: 过滤资源是否属于当前租户；取值为true时，只查属于当前租户的资源，不包括共享资源；为false时，查询当前租户及共享给该租户的资源；
        :type owned_by_self: bool
        :param sort_key: 按关键字排序，默认按照id排序，可选值:id|name|state
        :type sort_key: list[str]
        :param sort_dir: 返回结果按照升序或降序排列，默认为asc,降序为desc
        :type sort_dir: list[str]
        """
        
        

        self._limit = None
        self._marker = None
        self._enterprise_project_id = None
        self._state = None
        self._id = None
        self._resource_id = None
        self._owned_by_self = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if state is not None:
            self.state = state
        if id is not None:
            self.id = id
        if resource_id is not None:
            self.resource_id = resource_id
        if owned_by_self is not None:
            self.owned_by_self = owned_by_self
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def limit(self):
        r"""Gets the limit of this ListEnterpriseRoutersRequest.

        每页返回的个数。 取值范围：0~2000。

        :return: The limit of this ListEnterpriseRoutersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListEnterpriseRoutersRequest.

        每页返回的个数。 取值范围：0~2000。

        :param limit: The limit of this ListEnterpriseRoutersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListEnterpriseRoutersRequest.

        上一页最后一条记录的企业路由器实例的id，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :return: The marker of this ListEnterpriseRoutersRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListEnterpriseRoutersRequest.

        上一页最后一条记录的企业路由器实例的id，为空时为查询第一页。 使用说明：必须与limit一起使用。

        :param marker: The marker of this ListEnterpriseRoutersRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListEnterpriseRoutersRequest.

        企业项目ID

        :return: The enterprise_project_id of this ListEnterpriseRoutersRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListEnterpriseRoutersRequest.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ListEnterpriseRoutersRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def state(self):
        r"""Gets the state of this ListEnterpriseRoutersRequest.

        企业路由器实例状态

        :return: The state of this ListEnterpriseRoutersRequest.
        :rtype: list[str]
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListEnterpriseRoutersRequest.

        企业路由器实例状态

        :param state: The state of this ListEnterpriseRoutersRequest.
        :type state: list[str]
        """
        self._state = state

    @property
    def id(self):
        r"""Gets the id of this ListEnterpriseRoutersRequest.

        根据资源ID查询，可同时查询多个。

        :return: The id of this ListEnterpriseRoutersRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListEnterpriseRoutersRequest.

        根据资源ID查询，可同时查询多个。

        :param id: The id of this ListEnterpriseRoutersRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ListEnterpriseRoutersRequest.

        连接对应的资源ID列表

        :return: The resource_id of this ListEnterpriseRoutersRequest.
        :rtype: list[str]
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ListEnterpriseRoutersRequest.

        连接对应的资源ID列表

        :param resource_id: The resource_id of this ListEnterpriseRoutersRequest.
        :type resource_id: list[str]
        """
        self._resource_id = resource_id

    @property
    def owned_by_self(self):
        r"""Gets the owned_by_self of this ListEnterpriseRoutersRequest.

        过滤资源是否属于当前租户；取值为true时，只查属于当前租户的资源，不包括共享资源；为false时，查询当前租户及共享给该租户的资源；

        :return: The owned_by_self of this ListEnterpriseRoutersRequest.
        :rtype: bool
        """
        return self._owned_by_self

    @owned_by_self.setter
    def owned_by_self(self, owned_by_self):
        r"""Sets the owned_by_self of this ListEnterpriseRoutersRequest.

        过滤资源是否属于当前租户；取值为true时，只查属于当前租户的资源，不包括共享资源；为false时，查询当前租户及共享给该租户的资源；

        :param owned_by_self: The owned_by_self of this ListEnterpriseRoutersRequest.
        :type owned_by_self: bool
        """
        self._owned_by_self = owned_by_self

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListEnterpriseRoutersRequest.

        按关键字排序，默认按照id排序，可选值:id|name|state

        :return: The sort_key of this ListEnterpriseRoutersRequest.
        :rtype: list[str]
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListEnterpriseRoutersRequest.

        按关键字排序，默认按照id排序，可选值:id|name|state

        :param sort_key: The sort_key of this ListEnterpriseRoutersRequest.
        :type sort_key: list[str]
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListEnterpriseRoutersRequest.

        返回结果按照升序或降序排列，默认为asc,降序为desc

        :return: The sort_dir of this ListEnterpriseRoutersRequest.
        :rtype: list[str]
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListEnterpriseRoutersRequest.

        返回结果按照升序或降序排列，默认为asc,降序为desc

        :param sort_dir: The sort_dir of this ListEnterpriseRoutersRequest.
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
        if not isinstance(other, ListEnterpriseRoutersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
