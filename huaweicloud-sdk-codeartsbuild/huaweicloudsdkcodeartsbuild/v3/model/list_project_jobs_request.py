# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProjectJobsRequest:

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
        'page_index': 'int',
        'page_size': 'int',
        'search': 'str',
        'sort_field': 'str',
        'sort_order': 'str',
        'creator_id': 'str',
        'build_status': 'str',
        'by_group': 'bool',
        'group_path_id': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'page_index': 'page_index',
        'page_size': 'page_size',
        'search': 'search',
        'sort_field': 'sort_field',
        'sort_order': 'sort_order',
        'creator_id': 'creator_id',
        'build_status': 'build_status',
        'by_group': 'by_group',
        'group_path_id': 'group_path_id'
    }

    def __init__(self, project_id=None, page_index=None, page_size=None, search=None, sort_field=None, sort_order=None, creator_id=None, build_status=None, by_group=None, group_path_id=None):
        r"""ListProjectJobsRequest

        The model defined in huaweicloud sdk

        :param project_id: CodeArts项目ID，32位数字、小写字母组合。
        :type project_id: str
        :param page_index: **参数解释**： 分页页码， 表示从此页开始查询。 **约束限制**： 不涉及。 **取值范围**： 只能使用数字，大于等于0。
        :type page_index: int
        :param page_size: **参数解释**： 每页显示的条目数量。 **约束限制**： 不涉及。 **取值范围**： 只能使用数字，小于等于100。
        :type page_size: int
        :param search: 查询条件
        :type search: str
        :param sort_field: 排序的字段
        :type sort_field: str
        :param sort_order: 排序顺序
        :type sort_order: str
        :param creator_id: 创建人ID
        :type creator_id: str
        :param build_status: 构建状态过滤条件
        :type build_status: str
        :param by_group: 是否分组
        :type by_group: bool
        :param group_path_id: 分组ID
        :type group_path_id: str
        """
        
        

        self._project_id = None
        self._page_index = None
        self._page_size = None
        self._search = None
        self._sort_field = None
        self._sort_order = None
        self._creator_id = None
        self._build_status = None
        self._by_group = None
        self._group_path_id = None
        self.discriminator = None

        self.project_id = project_id
        self.page_index = page_index
        self.page_size = page_size
        if search is not None:
            self.search = search
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_order is not None:
            self.sort_order = sort_order
        if creator_id is not None:
            self.creator_id = creator_id
        if build_status is not None:
            self.build_status = build_status
        if by_group is not None:
            self.by_group = by_group
        if group_path_id is not None:
            self.group_path_id = group_path_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ListProjectJobsRequest.

        CodeArts项目ID，32位数字、小写字母组合。

        :return: The project_id of this ListProjectJobsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListProjectJobsRequest.

        CodeArts项目ID，32位数字、小写字母组合。

        :param project_id: The project_id of this ListProjectJobsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def page_index(self):
        r"""Gets the page_index of this ListProjectJobsRequest.

        **参数解释**： 分页页码， 表示从此页开始查询。 **约束限制**： 不涉及。 **取值范围**： 只能使用数字，大于等于0。

        :return: The page_index of this ListProjectJobsRequest.
        :rtype: int
        """
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        r"""Sets the page_index of this ListProjectJobsRequest.

        **参数解释**： 分页页码， 表示从此页开始查询。 **约束限制**： 不涉及。 **取值范围**： 只能使用数字，大于等于0。

        :param page_index: The page_index of this ListProjectJobsRequest.
        :type page_index: int
        """
        self._page_index = page_index

    @property
    def page_size(self):
        r"""Gets the page_size of this ListProjectJobsRequest.

        **参数解释**： 每页显示的条目数量。 **约束限制**： 不涉及。 **取值范围**： 只能使用数字，小于等于100。

        :return: The page_size of this ListProjectJobsRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListProjectJobsRequest.

        **参数解释**： 每页显示的条目数量。 **约束限制**： 不涉及。 **取值范围**： 只能使用数字，小于等于100。

        :param page_size: The page_size of this ListProjectJobsRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def search(self):
        r"""Gets the search of this ListProjectJobsRequest.

        查询条件

        :return: The search of this ListProjectJobsRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListProjectJobsRequest.

        查询条件

        :param search: The search of this ListProjectJobsRequest.
        :type search: str
        """
        self._search = search

    @property
    def sort_field(self):
        r"""Gets the sort_field of this ListProjectJobsRequest.

        排序的字段

        :return: The sort_field of this ListProjectJobsRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this ListProjectJobsRequest.

        排序的字段

        :param sort_field: The sort_field of this ListProjectJobsRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_order(self):
        r"""Gets the sort_order of this ListProjectJobsRequest.

        排序顺序

        :return: The sort_order of this ListProjectJobsRequest.
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        r"""Sets the sort_order of this ListProjectJobsRequest.

        排序顺序

        :param sort_order: The sort_order of this ListProjectJobsRequest.
        :type sort_order: str
        """
        self._sort_order = sort_order

    @property
    def creator_id(self):
        r"""Gets the creator_id of this ListProjectJobsRequest.

        创建人ID

        :return: The creator_id of this ListProjectJobsRequest.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this ListProjectJobsRequest.

        创建人ID

        :param creator_id: The creator_id of this ListProjectJobsRequest.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def build_status(self):
        r"""Gets the build_status of this ListProjectJobsRequest.

        构建状态过滤条件

        :return: The build_status of this ListProjectJobsRequest.
        :rtype: str
        """
        return self._build_status

    @build_status.setter
    def build_status(self, build_status):
        r"""Sets the build_status of this ListProjectJobsRequest.

        构建状态过滤条件

        :param build_status: The build_status of this ListProjectJobsRequest.
        :type build_status: str
        """
        self._build_status = build_status

    @property
    def by_group(self):
        r"""Gets the by_group of this ListProjectJobsRequest.

        是否分组

        :return: The by_group of this ListProjectJobsRequest.
        :rtype: bool
        """
        return self._by_group

    @by_group.setter
    def by_group(self, by_group):
        r"""Sets the by_group of this ListProjectJobsRequest.

        是否分组

        :param by_group: The by_group of this ListProjectJobsRequest.
        :type by_group: bool
        """
        self._by_group = by_group

    @property
    def group_path_id(self):
        r"""Gets the group_path_id of this ListProjectJobsRequest.

        分组ID

        :return: The group_path_id of this ListProjectJobsRequest.
        :rtype: str
        """
        return self._group_path_id

    @group_path_id.setter
    def group_path_id(self, group_path_id):
        r"""Sets the group_path_id of this ListProjectJobsRequest.

        分组ID

        :param group_path_id: The group_path_id of this ListProjectJobsRequest.
        :type group_path_id: str
        """
        self._group_path_id = group_path_id

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
        if not isinstance(other, ListProjectJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
