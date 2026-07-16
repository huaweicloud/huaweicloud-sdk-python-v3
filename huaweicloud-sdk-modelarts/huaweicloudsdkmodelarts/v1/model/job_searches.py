# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobSearches:

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
        'sort_by': 'str',
        'order': 'str',
        'group_by': 'str',
        'workspace_id': 'str',
        'train_type': 'str',
        'filters': 'list[Filter]'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'sort_by': 'sort_by',
        'order': 'order',
        'group_by': 'group_by',
        'workspace_id': 'workspace_id',
        'train_type': 'train_type',
        'filters': 'filters'
    }

    def __init__(self, offset=None, limit=None, sort_by=None, order=None, group_by=None, workspace_id=None, train_type=None, filters=None):
        r"""JobSearches

        The model defined in huaweicloud sdk

        :param offset: 查询作业的页数，最小为0。例如设置为0，则表示从第一页开始查询。
        :type offset: int
        :param limit: 查询作业的每页条目数。最小为1，最大为50。
        :type limit: int
        :param sort_by: 查询作业排列顺序的指标。默认使用create_time排序。
        :type sort_by: str
        :param order: 查询作业排列顺序，默认为“desc”，降序排序。也可以选择对应的“asc”，升序排序。
        :type order: str
        :param group_by: 查询作业要搜索的分组条件。
        :type group_by: str
        :param workspace_id: 参数解释：工作空间ID。 约束限制：不涉及。 取值范围：0或长度为32的字符串。 默认取值：0。
        :type workspace_id: str
        :param train_type: **参数解释**：在开启自定义作业和精调作业联合查询时，只显示自定义或精调作业。 **约束限制**：不涉及。 **取值范围**：   - job: 只查自定义作业   - ftjob : 只查精调作业 **默认取值**：不涉及。
        :type train_type: str
        :param filters: 查询作业要过滤的一系列条件。
        :type filters: list[:class:`huaweicloudsdkmodelarts.v1.Filter`]
        """
        
        

        self._offset = None
        self._limit = None
        self._sort_by = None
        self._order = None
        self._group_by = None
        self._workspace_id = None
        self._train_type = None
        self._filters = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_by is not None:
            self.sort_by = sort_by
        if order is not None:
            self.order = order
        if group_by is not None:
            self.group_by = group_by
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if train_type is not None:
            self.train_type = train_type
        if filters is not None:
            self.filters = filters

    @property
    def offset(self):
        r"""Gets the offset of this JobSearches.

        查询作业的页数，最小为0。例如设置为0，则表示从第一页开始查询。

        :return: The offset of this JobSearches.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this JobSearches.

        查询作业的页数，最小为0。例如设置为0，则表示从第一页开始查询。

        :param offset: The offset of this JobSearches.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this JobSearches.

        查询作业的每页条目数。最小为1，最大为50。

        :return: The limit of this JobSearches.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this JobSearches.

        查询作业的每页条目数。最小为1，最大为50。

        :param limit: The limit of this JobSearches.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_by(self):
        r"""Gets the sort_by of this JobSearches.

        查询作业排列顺序的指标。默认使用create_time排序。

        :return: The sort_by of this JobSearches.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this JobSearches.

        查询作业排列顺序的指标。默认使用create_time排序。

        :param sort_by: The sort_by of this JobSearches.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def order(self):
        r"""Gets the order of this JobSearches.

        查询作业排列顺序，默认为“desc”，降序排序。也可以选择对应的“asc”，升序排序。

        :return: The order of this JobSearches.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this JobSearches.

        查询作业排列顺序，默认为“desc”，降序排序。也可以选择对应的“asc”，升序排序。

        :param order: The order of this JobSearches.
        :type order: str
        """
        self._order = order

    @property
    def group_by(self):
        r"""Gets the group_by of this JobSearches.

        查询作业要搜索的分组条件。

        :return: The group_by of this JobSearches.
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        r"""Sets the group_by of this JobSearches.

        查询作业要搜索的分组条件。

        :param group_by: The group_by of this JobSearches.
        :type group_by: str
        """
        self._group_by = group_by

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this JobSearches.

        参数解释：工作空间ID。 约束限制：不涉及。 取值范围：0或长度为32的字符串。 默认取值：0。

        :return: The workspace_id of this JobSearches.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this JobSearches.

        参数解释：工作空间ID。 约束限制：不涉及。 取值范围：0或长度为32的字符串。 默认取值：0。

        :param workspace_id: The workspace_id of this JobSearches.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def train_type(self):
        r"""Gets the train_type of this JobSearches.

        **参数解释**：在开启自定义作业和精调作业联合查询时，只显示自定义或精调作业。 **约束限制**：不涉及。 **取值范围**：   - job: 只查自定义作业   - ftjob : 只查精调作业 **默认取值**：不涉及。

        :return: The train_type of this JobSearches.
        :rtype: str
        """
        return self._train_type

    @train_type.setter
    def train_type(self, train_type):
        r"""Sets the train_type of this JobSearches.

        **参数解释**：在开启自定义作业和精调作业联合查询时，只显示自定义或精调作业。 **约束限制**：不涉及。 **取值范围**：   - job: 只查自定义作业   - ftjob : 只查精调作业 **默认取值**：不涉及。

        :param train_type: The train_type of this JobSearches.
        :type train_type: str
        """
        self._train_type = train_type

    @property
    def filters(self):
        r"""Gets the filters of this JobSearches.

        查询作业要过滤的一系列条件。

        :return: The filters of this JobSearches.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.Filter`]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        r"""Sets the filters of this JobSearches.

        查询作业要过滤的一系列条件。

        :param filters: The filters of this JobSearches.
        :type filters: list[:class:`huaweicloudsdkmodelarts.v1.Filter`]
        """
        self._filters = filters

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
        if not isinstance(other, JobSearches):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
