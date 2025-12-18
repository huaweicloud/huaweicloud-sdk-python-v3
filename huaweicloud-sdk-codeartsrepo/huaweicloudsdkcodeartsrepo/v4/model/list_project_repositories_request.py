# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProjectRepositoriesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'search': 'str',
        'offset': 'int',
        'limit': 'int',
        'order_by': 'str',
        'sort': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'search': 'search',
        'offset': 'offset',
        'limit': 'limit',
        'order_by': 'order_by',
        'sort': 'sort'
    }

    def __init__(self, project_id=None, search=None, offset=None, limit=None, order_by=None, sort=None):
        r"""ListProjectRepositoriesRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[[查询项目列表](https://support.huaweicloud.com/eu/api-projectman/ListProjectsV4.html)](tag:hws_eu)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **取值范围：** 字符串长度32。
        :type project_id: str
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
        
        

        self._project_id = None
        self._search = None
        self._offset = None
        self._limit = None
        self._order_by = None
        self._sort = None
        self.discriminator = None

        self.project_id = project_id
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
    def project_id(self):
        r"""Gets the project_id of this ListProjectRepositoriesRequest.

        **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[[查询项目列表](https://support.huaweicloud.com/eu/api-projectman/ListProjectsV4.html)](tag:hws_eu)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **取值范围：** 字符串长度32。

        :return: The project_id of this ListProjectRepositoriesRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListProjectRepositoriesRequest.

        **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[[查询项目列表](https://support.huaweicloud.com/eu/api-projectman/ListProjectsV4.html)](tag:hws_eu)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **取值范围：** 字符串长度32。

        :param project_id: The project_id of this ListProjectRepositoriesRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def search(self):
        r"""Gets the search of this ListProjectRepositoriesRequest.

        **参数解释：** 仓库名称搜索关键字。 **取值范围：** 不涉及。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :return: The search of this ListProjectRepositoriesRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListProjectRepositoriesRequest.

        **参数解释：** 仓库名称搜索关键字。 **取值范围：** 不涉及。 **约束限制：** 不涉及。 **默认取值：** 不涉及。

        :param search: The search of this ListProjectRepositoriesRequest.
        :type search: str
        """
        self._search = search

    @property
    def offset(self):
        r"""Gets the offset of this ListProjectRepositoriesRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListProjectRepositoriesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListProjectRepositoriesRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListProjectRepositoriesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListProjectRepositoriesRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListProjectRepositoriesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListProjectRepositoriesRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListProjectRepositoriesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def order_by(self):
        r"""Gets the order_by of this ListProjectRepositoriesRequest.

        **参数解释：** 排序字段。 **取值范围：** - id，仓库ID。 - name，仓库名称。 - created_at，创建时间。 - updated_at，更新时间。 **约束限制：** 不涉及。 **默认取值：** updated_at。

        :return: The order_by of this ListProjectRepositoriesRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListProjectRepositoriesRequest.

        **参数解释：** 排序字段。 **取值范围：** - id，仓库ID。 - name，仓库名称。 - created_at，创建时间。 - updated_at，更新时间。 **约束限制：** 不涉及。 **默认取值：** updated_at。

        :param order_by: The order_by of this ListProjectRepositoriesRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def sort(self):
        r"""Gets the sort of this ListProjectRepositoriesRequest.

        **参数解释：** 排序字段。 **取值范围：** - asc，升序。 - desc，逆序。 **约束限制：** 不涉及。 **默认取值：** desc。

        :return: The sort of this ListProjectRepositoriesRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ListProjectRepositoriesRequest.

        **参数解释：** 排序字段。 **取值范围：** - asc，升序。 - desc，逆序。 **约束限制：** 不涉及。 **默认取值：** desc。

        :param sort: The sort of this ListProjectRepositoriesRequest.
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
        if not isinstance(other, ListProjectRepositoriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
