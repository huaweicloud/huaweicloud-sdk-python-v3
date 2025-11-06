# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGroupRepositoriesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'int',
        'search': 'str',
        'offset': 'int',
        'limit': 'int',
        'order_by': 'str',
        'sort': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'search': 'search',
        'offset': 'offset',
        'limit': 'limit',
        'order_by': 'order_by',
        'sort': 'sort'
    }

    def __init__(self, group_id=None, search=None, offset=None, limit=None, order_by=None, sort=None):
        r"""ListGroupRepositoriesRequest

        The model defined in huaweicloud sdk

        :param group_id: **参数解释：** 代码组id，代码组首页，Group ID后的数字Id
        :type group_id: int
        :param search: **参数解释：** 仓库名称搜索关键字。 **取值范围：** 不涉及。 **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type search: str
        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        :param order_by: **参数解释：** 排序字段。 **取值范围：** - id，仓库ID。 - name，仓库名称。 - created_at，创建时间。 - updated_at，更新时间。 **约束限制：** 不涉及。 **默认取值：** updated_at。
        :type order_by: str
        :param sort: **参数解释：** 排序字段。 **取值范围：** - asc，升序。 - desc，逆序。 **约束限制：** 不涉及。 **默认取值：** desc。
        :type sort: str
        """
        
        

        self._group_id = None
        self._search = None
        self._offset = None
        self._limit = None
        self._order_by = None
        self._sort = None
        self.discriminator = None

        self.group_id = group_id
        if search is not None:
            self.search = search
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if order_by is not None:
            self.order_by = order_by
        if sort is not None:
            self.sort = sort

    @property
    def group_id(self):
        r"""Gets the group_id of this ListGroupRepositoriesRequest.

        **参数解释：** 代码组id，代码组首页，Group ID后的数字Id

        :return: The group_id of this ListGroupRepositoriesRequest.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListGroupRepositoriesRequest.

        **参数解释：** 代码组id，代码组首页，Group ID后的数字Id

        :param group_id: The group_id of this ListGroupRepositoriesRequest.
        :type group_id: int
        """
        self._group_id = group_id

    @property
    def search(self):
        r"""Gets the search of this ListGroupRepositoriesRequest.

        **参数解释：** 仓库名称搜索关键字。 **取值范围：** 不涉及。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The search of this ListGroupRepositoriesRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListGroupRepositoriesRequest.

        **参数解释：** 仓库名称搜索关键字。 **取值范围：** 不涉及。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param search: The search of this ListGroupRepositoriesRequest.
        :type search: str
        """
        self._search = search

    @property
    def offset(self):
        r"""Gets the offset of this ListGroupRepositoriesRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListGroupRepositoriesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListGroupRepositoriesRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListGroupRepositoriesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListGroupRepositoriesRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListGroupRepositoriesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListGroupRepositoriesRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListGroupRepositoriesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def order_by(self):
        r"""Gets the order_by of this ListGroupRepositoriesRequest.

        **参数解释：** 排序字段。 **取值范围：** - id，仓库ID。 - name，仓库名称。 - created_at，创建时间。 - updated_at，更新时间。 **约束限制：** 不涉及。 **默认取值：** updated_at。

        :return: The order_by of this ListGroupRepositoriesRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListGroupRepositoriesRequest.

        **参数解释：** 排序字段。 **取值范围：** - id，仓库ID。 - name，仓库名称。 - created_at，创建时间。 - updated_at，更新时间。 **约束限制：** 不涉及。 **默认取值：** updated_at。

        :param order_by: The order_by of this ListGroupRepositoriesRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def sort(self):
        r"""Gets the sort of this ListGroupRepositoriesRequest.

        **参数解释：** 排序字段。 **取值范围：** - asc，升序。 - desc，逆序。 **约束限制：** 不涉及。 **默认取值：** desc。

        :return: The sort of this ListGroupRepositoriesRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ListGroupRepositoriesRequest.

        **参数解释：** 排序字段。 **取值范围：** - asc，升序。 - desc，逆序。 **约束限制：** 不涉及。 **默认取值：** desc。

        :param sort: The sort of this ListGroupRepositoriesRequest.
        :type sort: str
        """
        self._sort = sort

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
        if not isinstance(other, ListGroupRepositoriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
