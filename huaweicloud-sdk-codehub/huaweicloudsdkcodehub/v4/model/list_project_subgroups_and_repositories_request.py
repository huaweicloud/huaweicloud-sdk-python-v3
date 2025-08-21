# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProjectSubgroupsAndRepositoriesRequest:

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
        'filter': 'int',
        'order_by': 'str',
        'sort': 'str',
        'archived': 'bool',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'filter': 'filter',
        'order_by': 'order_by',
        'sort': 'sort',
        'archived': 'archived',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, project_id=None, filter=None, order_by=None, sort=None, archived=None, offset=None, limit=None):
        r"""ListProjectSubgroupsAndRepositoriesRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **取值范围：** 字符串长度32。
        :type project_id: str
        :param filter: **参数解释：** 检索条件，名称。
        :type filter: int
        :param order_by: **参数解释：** 排序字段 id 唯一标识 name 名称 created_at 创建时间 updated_at 更新时间
        :type order_by: str
        :param sort: **参数解释：** 排序顺序 asc顺序 desc逆序
        :type sort: str
        :param archived: **参数解释：** 是否归档
        :type archived: bool
        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        """
        
        

        self._project_id = None
        self._filter = None
        self._order_by = None
        self._sort = None
        self._archived = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.project_id = project_id
        if filter is not None:
            self.filter = filter
        if order_by is not None:
            self.order_by = order_by
        if sort is not None:
            self.sort = sort
        if archived is not None:
            self.archived = archived
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def project_id(self):
        r"""Gets the project_id of this ListProjectSubgroupsAndRepositoriesRequest.

        **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **取值范围：** 字符串长度32。

        :return: The project_id of this ListProjectSubgroupsAndRepositoriesRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListProjectSubgroupsAndRepositoriesRequest.

        **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **取值范围：** 字符串长度32。

        :param project_id: The project_id of this ListProjectSubgroupsAndRepositoriesRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def filter(self):
        r"""Gets the filter of this ListProjectSubgroupsAndRepositoriesRequest.

        **参数解释：** 检索条件，名称。

        :return: The filter of this ListProjectSubgroupsAndRepositoriesRequest.
        :rtype: int
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this ListProjectSubgroupsAndRepositoriesRequest.

        **参数解释：** 检索条件，名称。

        :param filter: The filter of this ListProjectSubgroupsAndRepositoriesRequest.
        :type filter: int
        """
        self._filter = filter

    @property
    def order_by(self):
        r"""Gets the order_by of this ListProjectSubgroupsAndRepositoriesRequest.

        **参数解释：** 排序字段 id 唯一标识 name 名称 created_at 创建时间 updated_at 更新时间

        :return: The order_by of this ListProjectSubgroupsAndRepositoriesRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListProjectSubgroupsAndRepositoriesRequest.

        **参数解释：** 排序字段 id 唯一标识 name 名称 created_at 创建时间 updated_at 更新时间

        :param order_by: The order_by of this ListProjectSubgroupsAndRepositoriesRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def sort(self):
        r"""Gets the sort of this ListProjectSubgroupsAndRepositoriesRequest.

        **参数解释：** 排序顺序 asc顺序 desc逆序

        :return: The sort of this ListProjectSubgroupsAndRepositoriesRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ListProjectSubgroupsAndRepositoriesRequest.

        **参数解释：** 排序顺序 asc顺序 desc逆序

        :param sort: The sort of this ListProjectSubgroupsAndRepositoriesRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def archived(self):
        r"""Gets the archived of this ListProjectSubgroupsAndRepositoriesRequest.

        **参数解释：** 是否归档

        :return: The archived of this ListProjectSubgroupsAndRepositoriesRequest.
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        r"""Sets the archived of this ListProjectSubgroupsAndRepositoriesRequest.

        **参数解释：** 是否归档

        :param archived: The archived of this ListProjectSubgroupsAndRepositoriesRequest.
        :type archived: bool
        """
        self._archived = archived

    @property
    def offset(self):
        r"""Gets the offset of this ListProjectSubgroupsAndRepositoriesRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListProjectSubgroupsAndRepositoriesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListProjectSubgroupsAndRepositoriesRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListProjectSubgroupsAndRepositoriesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListProjectSubgroupsAndRepositoriesRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListProjectSubgroupsAndRepositoriesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListProjectSubgroupsAndRepositoriesRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListProjectSubgroupsAndRepositoriesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListProjectSubgroupsAndRepositoriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
