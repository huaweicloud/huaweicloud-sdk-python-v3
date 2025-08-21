# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGroupsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'search': 'str',
        'all_available': 'bool',
        'order_by': 'str',
        'sort': 'str',
        'starred': 'bool',
        'offset': 'int',
        'limit': 'int',
        'owned': 'bool'
    }

    attribute_map = {
        'search': 'search',
        'all_available': 'all_available',
        'order_by': 'order_by',
        'sort': 'sort',
        'starred': 'starred',
        'offset': 'offset',
        'limit': 'limit',
        'owned': 'owned'
    }

    def __init__(self, search=None, all_available=None, order_by=None, sort=None, starred=None, offset=None, limit=None, owned=None):
        r"""ListGroupsRequest

        The model defined in huaweicloud sdk

        :param search: **参数解释：** 检索内容
        :type search: str
        :param all_available: **参数解释：** 所有可用的代码组。
        :type all_available: bool
        :param order_by: **参数解释：** 排序字段，name 名称 path 路径 id 唯一标示 created_at 创建时间 updated_at 更新时间
        :type order_by: str
        :param sort: **参数解释：** 排序顺序 asc顺序 desc逆序
        :type sort: str
        :param starred: **参数解释：** 是否关注。
        :type starred: bool
        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        :param owned: **参数解释：**
        :type owned: bool
        """
        
        

        self._search = None
        self._all_available = None
        self._order_by = None
        self._sort = None
        self._starred = None
        self._offset = None
        self._limit = None
        self._owned = None
        self.discriminator = None

        if search is not None:
            self.search = search
        if all_available is not None:
            self.all_available = all_available
        if order_by is not None:
            self.order_by = order_by
        if sort is not None:
            self.sort = sort
        if starred is not None:
            self.starred = starred
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if owned is not None:
            self.owned = owned

    @property
    def search(self):
        r"""Gets the search of this ListGroupsRequest.

        **参数解释：** 检索内容

        :return: The search of this ListGroupsRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListGroupsRequest.

        **参数解释：** 检索内容

        :param search: The search of this ListGroupsRequest.
        :type search: str
        """
        self._search = search

    @property
    def all_available(self):
        r"""Gets the all_available of this ListGroupsRequest.

        **参数解释：** 所有可用的代码组。

        :return: The all_available of this ListGroupsRequest.
        :rtype: bool
        """
        return self._all_available

    @all_available.setter
    def all_available(self, all_available):
        r"""Sets the all_available of this ListGroupsRequest.

        **参数解释：** 所有可用的代码组。

        :param all_available: The all_available of this ListGroupsRequest.
        :type all_available: bool
        """
        self._all_available = all_available

    @property
    def order_by(self):
        r"""Gets the order_by of this ListGroupsRequest.

        **参数解释：** 排序字段，name 名称 path 路径 id 唯一标示 created_at 创建时间 updated_at 更新时间

        :return: The order_by of this ListGroupsRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListGroupsRequest.

        **参数解释：** 排序字段，name 名称 path 路径 id 唯一标示 created_at 创建时间 updated_at 更新时间

        :param order_by: The order_by of this ListGroupsRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def sort(self):
        r"""Gets the sort of this ListGroupsRequest.

        **参数解释：** 排序顺序 asc顺序 desc逆序

        :return: The sort of this ListGroupsRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ListGroupsRequest.

        **参数解释：** 排序顺序 asc顺序 desc逆序

        :param sort: The sort of this ListGroupsRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def starred(self):
        r"""Gets the starred of this ListGroupsRequest.

        **参数解释：** 是否关注。

        :return: The starred of this ListGroupsRequest.
        :rtype: bool
        """
        return self._starred

    @starred.setter
    def starred(self, starred):
        r"""Sets the starred of this ListGroupsRequest.

        **参数解释：** 是否关注。

        :param starred: The starred of this ListGroupsRequest.
        :type starred: bool
        """
        self._starred = starred

    @property
    def offset(self):
        r"""Gets the offset of this ListGroupsRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListGroupsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListGroupsRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListGroupsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListGroupsRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListGroupsRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListGroupsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def owned(self):
        r"""Gets the owned of this ListGroupsRequest.

        **参数解释：**

        :return: The owned of this ListGroupsRequest.
        :rtype: bool
        """
        return self._owned

    @owned.setter
    def owned(self, owned):
        r"""Sets the owned of this ListGroupsRequest.

        **参数解释：**

        :param owned: The owned of this ListGroupsRequest.
        :type owned: bool
        """
        self._owned = owned

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
        if not isinstance(other, ListGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
