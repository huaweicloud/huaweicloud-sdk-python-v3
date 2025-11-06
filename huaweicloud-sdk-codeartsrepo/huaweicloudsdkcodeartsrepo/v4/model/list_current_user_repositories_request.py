# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCurrentUserRepositoriesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'order_by': 'str',
        'sort': 'str',
        'archived': 'bool',
        'search': 'str',
        'starred': 'bool',
        'membership': 'bool',
        'user_created': 'bool',
        'include_abnormal': 'bool'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'order_by': 'order_by',
        'sort': 'sort',
        'archived': 'archived',
        'search': 'search',
        'starred': 'starred',
        'membership': 'membership',
        'user_created': 'user_created',
        'include_abnormal': 'include_abnormal'
    }

    def __init__(self, offset=None, limit=None, order_by=None, sort=None, archived=None, search=None, starred=None, membership=None, user_created=None, include_abnormal=None):
        r"""ListCurrentUserRepositoriesRequest

        The model defined in huaweicloud sdk

        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        :param order_by: **参数解释：** 排序字段。 **取值范围：** - created_at，创建时间。 - updated_at，更新时间。 **约束限制：** 不涉及。 **默认取值：** created_at。
        :type order_by: str
        :param sort: **参数解释：** 排序字段。 **取值范围：** - asc，升序。 - desc，逆序。 **约束限制：** 不涉及。 **默认取值：** desc。
        :type sort: str
        :param archived: **参数解释：** 是否归档。 **取值范围：** - true，归档。 - false，未归档。 **约束限制：** 不涉及。 **默认取值：** false。
        :type archived: bool
        :param search: **参数解释：** 仓库搜索。 **取值范围：** 1-512。 **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type search: str
        :param starred: **参数解释：** 关注的仓库。 **取值范围：** - true，关注。 - false，未关注。 **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type starred: bool
        :param membership: **参数解释：** 参与的仓库（有仓库成员身份）。 **取值范围：** - true，筛选我参与的仓库。 - false，不筛选。 **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type membership: bool
        :param user_created: **参数解释：** 创建的仓库。 **取值范围：** - true，筛选我创建的仓库。 - false，不筛选。 **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type user_created: bool
        :param include_abnormal: **参数解释：** 包含异常状态的仓库。 **取值范围：** - true，筛选包含异常状态的仓库。 - false，不筛选。 **约束限制：** 不涉及。 **默认取值：** 不涉及。
        :type include_abnormal: bool
        """
        
        

        self._offset = None
        self._limit = None
        self._order_by = None
        self._sort = None
        self._archived = None
        self._search = None
        self._starred = None
        self._membership = None
        self._user_created = None
        self._include_abnormal = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if order_by is not None:
            self.order_by = order_by
        if sort is not None:
            self.sort = sort
        if archived is not None:
            self.archived = archived
        if search is not None:
            self.search = search
        if starred is not None:
            self.starred = starred
        if membership is not None:
            self.membership = membership
        if user_created is not None:
            self.user_created = user_created
        if include_abnormal is not None:
            self.include_abnormal = include_abnormal

    @property
    def offset(self):
        r"""Gets the offset of this ListCurrentUserRepositoriesRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListCurrentUserRepositoriesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCurrentUserRepositoriesRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListCurrentUserRepositoriesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListCurrentUserRepositoriesRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListCurrentUserRepositoriesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCurrentUserRepositoriesRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListCurrentUserRepositoriesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def order_by(self):
        r"""Gets the order_by of this ListCurrentUserRepositoriesRequest.

        **参数解释：** 排序字段。 **取值范围：** - created_at，创建时间。 - updated_at，更新时间。 **约束限制：** 不涉及。 **默认取值：** created_at。

        :return: The order_by of this ListCurrentUserRepositoriesRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListCurrentUserRepositoriesRequest.

        **参数解释：** 排序字段。 **取值范围：** - created_at，创建时间。 - updated_at，更新时间。 **约束限制：** 不涉及。 **默认取值：** created_at。

        :param order_by: The order_by of this ListCurrentUserRepositoriesRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def sort(self):
        r"""Gets the sort of this ListCurrentUserRepositoriesRequest.

        **参数解释：** 排序字段。 **取值范围：** - asc，升序。 - desc，逆序。 **约束限制：** 不涉及。 **默认取值：** desc。

        :return: The sort of this ListCurrentUserRepositoriesRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ListCurrentUserRepositoriesRequest.

        **参数解释：** 排序字段。 **取值范围：** - asc，升序。 - desc，逆序。 **约束限制：** 不涉及。 **默认取值：** desc。

        :param sort: The sort of this ListCurrentUserRepositoriesRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def archived(self):
        r"""Gets the archived of this ListCurrentUserRepositoriesRequest.

        **参数解释：** 是否归档。 **取值范围：** - true，归档。 - false，未归档。 **约束限制：** 不涉及。 **默认取值：** false。

        :return: The archived of this ListCurrentUserRepositoriesRequest.
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        r"""Sets the archived of this ListCurrentUserRepositoriesRequest.

        **参数解释：** 是否归档。 **取值范围：** - true，归档。 - false，未归档。 **约束限制：** 不涉及。 **默认取值：** false。

        :param archived: The archived of this ListCurrentUserRepositoriesRequest.
        :type archived: bool
        """
        self._archived = archived

    @property
    def search(self):
        r"""Gets the search of this ListCurrentUserRepositoriesRequest.

        **参数解释：** 仓库搜索。 **取值范围：** 1-512。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The search of this ListCurrentUserRepositoriesRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListCurrentUserRepositoriesRequest.

        **参数解释：** 仓库搜索。 **取值范围：** 1-512。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param search: The search of this ListCurrentUserRepositoriesRequest.
        :type search: str
        """
        self._search = search

    @property
    def starred(self):
        r"""Gets the starred of this ListCurrentUserRepositoriesRequest.

        **参数解释：** 关注的仓库。 **取值范围：** - true，关注。 - false，未关注。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The starred of this ListCurrentUserRepositoriesRequest.
        :rtype: bool
        """
        return self._starred

    @starred.setter
    def starred(self, starred):
        r"""Sets the starred of this ListCurrentUserRepositoriesRequest.

        **参数解释：** 关注的仓库。 **取值范围：** - true，关注。 - false，未关注。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param starred: The starred of this ListCurrentUserRepositoriesRequest.
        :type starred: bool
        """
        self._starred = starred

    @property
    def membership(self):
        r"""Gets the membership of this ListCurrentUserRepositoriesRequest.

        **参数解释：** 参与的仓库（有仓库成员身份）。 **取值范围：** - true，筛选我参与的仓库。 - false，不筛选。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The membership of this ListCurrentUserRepositoriesRequest.
        :rtype: bool
        """
        return self._membership

    @membership.setter
    def membership(self, membership):
        r"""Sets the membership of this ListCurrentUserRepositoriesRequest.

        **参数解释：** 参与的仓库（有仓库成员身份）。 **取值范围：** - true，筛选我参与的仓库。 - false，不筛选。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param membership: The membership of this ListCurrentUserRepositoriesRequest.
        :type membership: bool
        """
        self._membership = membership

    @property
    def user_created(self):
        r"""Gets the user_created of this ListCurrentUserRepositoriesRequest.

        **参数解释：** 创建的仓库。 **取值范围：** - true，筛选我创建的仓库。 - false，不筛选。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The user_created of this ListCurrentUserRepositoriesRequest.
        :rtype: bool
        """
        return self._user_created

    @user_created.setter
    def user_created(self, user_created):
        r"""Sets the user_created of this ListCurrentUserRepositoriesRequest.

        **参数解释：** 创建的仓库。 **取值范围：** - true，筛选我创建的仓库。 - false，不筛选。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param user_created: The user_created of this ListCurrentUserRepositoriesRequest.
        :type user_created: bool
        """
        self._user_created = user_created

    @property
    def include_abnormal(self):
        r"""Gets the include_abnormal of this ListCurrentUserRepositoriesRequest.

        **参数解释：** 包含异常状态的仓库。 **取值范围：** - true，筛选包含异常状态的仓库。 - false，不筛选。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The include_abnormal of this ListCurrentUserRepositoriesRequest.
        :rtype: bool
        """
        return self._include_abnormal

    @include_abnormal.setter
    def include_abnormal(self, include_abnormal):
        r"""Sets the include_abnormal of this ListCurrentUserRepositoriesRequest.

        **参数解释：** 包含异常状态的仓库。 **取值范围：** - true，筛选包含异常状态的仓库。 - false，不筛选。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param include_abnormal: The include_abnormal of this ListCurrentUserRepositoriesRequest.
        :type include_abnormal: bool
        """
        self._include_abnormal = include_abnormal

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
        if not isinstance(other, ListCurrentUserRepositoriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
