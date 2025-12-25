# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepoFileQueryDTOV5:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_no': 'int',
        'page_size': 'int',
        'parent_id': 'str',
        'project_id': 'str',
        'search_name': 'str',
        'search_type': 'str',
        'extension': 'str',
        'order_by': 'str',
        'sort': 'str',
        'status': 'str',
        'category': 'str'
    }

    attribute_map = {
        'page_no': 'page_no',
        'page_size': 'page_size',
        'parent_id': 'parent_id',
        'project_id': 'project_id',
        'search_name': 'search_name',
        'search_type': 'search_type',
        'extension': 'extension',
        'order_by': 'order_by',
        'sort': 'sort',
        'status': 'status',
        'category': 'category'
    }

    def __init__(self, page_no=None, page_size=None, parent_id=None, project_id=None, search_name=None, search_type=None, extension=None, order_by=None, sort=None, status=None, category=None):
        r"""RepoFileQueryDTOV5

        The model defined in huaweicloud sdk

        :param page_no: **参数解释**: 页码。 **约束限制**: 不涉及。 **取值范围**: 最小值1。 **默认取值**: 1
        :type page_no: int
        :param page_size: **参数解释**: 每页大小。 **约束限制**: 不涉及。 **取值范围**: 最小值1，最大值100。 **默认取值**: 10
        :type page_size: int
        :param parent_id: **参数解释**: 父级目录id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type parent_id: str
        :param project_id: **参数解释**: 项目id，对应\&quot;需求管理 CodeArts Req\&quot;项目唯一标识，私有依赖库首页地址栏url https://{host}/cloudartifact/project/{project_id}/repository中project_id变量的值。 **约束限制**: 不涉及。 **取值范围**: 只能使用小写英文字符及数字，字符串长度为32位。 **默认取值**: 不涉及。
        :type project_id: str
        :param search_name: **参数解释**: 搜索关键字。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type search_name: str
        :param search_type: **参数解释**: 搜索类型。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type search_type: str
        :param extension: **参数解释**: 后缀名。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type extension: str
        :param order_by: **参数解释**: 排序字段。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type order_by: str
        :param sort: **参数解释**: 排序方式。 **约束限制**: 不涉及。 **取值范围**: 升序或降序。 **默认取值**: 不涉及。
        :type sort: str
        :param status: **参数解释**: 文件状态。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type status: str
        :param category: **参数解释**: 发布包状态。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type category: str
        """
        
        

        self._page_no = None
        self._page_size = None
        self._parent_id = None
        self._project_id = None
        self._search_name = None
        self._search_type = None
        self._extension = None
        self._order_by = None
        self._sort = None
        self._status = None
        self._category = None
        self.discriminator = None

        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size
        if parent_id is not None:
            self.parent_id = parent_id
        if project_id is not None:
            self.project_id = project_id
        if search_name is not None:
            self.search_name = search_name
        if search_type is not None:
            self.search_type = search_type
        if extension is not None:
            self.extension = extension
        if order_by is not None:
            self.order_by = order_by
        if sort is not None:
            self.sort = sort
        if status is not None:
            self.status = status
        if category is not None:
            self.category = category

    @property
    def page_no(self):
        r"""Gets the page_no of this RepoFileQueryDTOV5.

        **参数解释**: 页码。 **约束限制**: 不涉及。 **取值范围**: 最小值1。 **默认取值**: 1

        :return: The page_no of this RepoFileQueryDTOV5.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this RepoFileQueryDTOV5.

        **参数解释**: 页码。 **约束限制**: 不涉及。 **取值范围**: 最小值1。 **默认取值**: 1

        :param page_no: The page_no of this RepoFileQueryDTOV5.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        r"""Gets the page_size of this RepoFileQueryDTOV5.

        **参数解释**: 每页大小。 **约束限制**: 不涉及。 **取值范围**: 最小值1，最大值100。 **默认取值**: 10

        :return: The page_size of this RepoFileQueryDTOV5.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this RepoFileQueryDTOV5.

        **参数解释**: 每页大小。 **约束限制**: 不涉及。 **取值范围**: 最小值1，最大值100。 **默认取值**: 10

        :param page_size: The page_size of this RepoFileQueryDTOV5.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def parent_id(self):
        r"""Gets the parent_id of this RepoFileQueryDTOV5.

        **参数解释**: 父级目录id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The parent_id of this RepoFileQueryDTOV5.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this RepoFileQueryDTOV5.

        **参数解释**: 父级目录id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param parent_id: The parent_id of this RepoFileQueryDTOV5.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def project_id(self):
        r"""Gets the project_id of this RepoFileQueryDTOV5.

        **参数解释**: 项目id，对应\"需求管理 CodeArts Req\"项目唯一标识，私有依赖库首页地址栏url https://{host}/cloudartifact/project/{project_id}/repository中project_id变量的值。 **约束限制**: 不涉及。 **取值范围**: 只能使用小写英文字符及数字，字符串长度为32位。 **默认取值**: 不涉及。

        :return: The project_id of this RepoFileQueryDTOV5.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this RepoFileQueryDTOV5.

        **参数解释**: 项目id，对应\"需求管理 CodeArts Req\"项目唯一标识，私有依赖库首页地址栏url https://{host}/cloudartifact/project/{project_id}/repository中project_id变量的值。 **约束限制**: 不涉及。 **取值范围**: 只能使用小写英文字符及数字，字符串长度为32位。 **默认取值**: 不涉及。

        :param project_id: The project_id of this RepoFileQueryDTOV5.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def search_name(self):
        r"""Gets the search_name of this RepoFileQueryDTOV5.

        **参数解释**: 搜索关键字。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The search_name of this RepoFileQueryDTOV5.
        :rtype: str
        """
        return self._search_name

    @search_name.setter
    def search_name(self, search_name):
        r"""Sets the search_name of this RepoFileQueryDTOV5.

        **参数解释**: 搜索关键字。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param search_name: The search_name of this RepoFileQueryDTOV5.
        :type search_name: str
        """
        self._search_name = search_name

    @property
    def search_type(self):
        r"""Gets the search_type of this RepoFileQueryDTOV5.

        **参数解释**: 搜索类型。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The search_type of this RepoFileQueryDTOV5.
        :rtype: str
        """
        return self._search_type

    @search_type.setter
    def search_type(self, search_type):
        r"""Sets the search_type of this RepoFileQueryDTOV5.

        **参数解释**: 搜索类型。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param search_type: The search_type of this RepoFileQueryDTOV5.
        :type search_type: str
        """
        self._search_type = search_type

    @property
    def extension(self):
        r"""Gets the extension of this RepoFileQueryDTOV5.

        **参数解释**: 后缀名。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The extension of this RepoFileQueryDTOV5.
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        r"""Sets the extension of this RepoFileQueryDTOV5.

        **参数解释**: 后缀名。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param extension: The extension of this RepoFileQueryDTOV5.
        :type extension: str
        """
        self._extension = extension

    @property
    def order_by(self):
        r"""Gets the order_by of this RepoFileQueryDTOV5.

        **参数解释**: 排序字段。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The order_by of this RepoFileQueryDTOV5.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this RepoFileQueryDTOV5.

        **参数解释**: 排序字段。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param order_by: The order_by of this RepoFileQueryDTOV5.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def sort(self):
        r"""Gets the sort of this RepoFileQueryDTOV5.

        **参数解释**: 排序方式。 **约束限制**: 不涉及。 **取值范围**: 升序或降序。 **默认取值**: 不涉及。

        :return: The sort of this RepoFileQueryDTOV5.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this RepoFileQueryDTOV5.

        **参数解释**: 排序方式。 **约束限制**: 不涉及。 **取值范围**: 升序或降序。 **默认取值**: 不涉及。

        :param sort: The sort of this RepoFileQueryDTOV5.
        :type sort: str
        """
        self._sort = sort

    @property
    def status(self):
        r"""Gets the status of this RepoFileQueryDTOV5.

        **参数解释**: 文件状态。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The status of this RepoFileQueryDTOV5.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RepoFileQueryDTOV5.

        **参数解释**: 文件状态。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param status: The status of this RepoFileQueryDTOV5.
        :type status: str
        """
        self._status = status

    @property
    def category(self):
        r"""Gets the category of this RepoFileQueryDTOV5.

        **参数解释**: 发布包状态。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The category of this RepoFileQueryDTOV5.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this RepoFileQueryDTOV5.

        **参数解释**: 发布包状态。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param category: The category of this RepoFileQueryDTOV5.
        :type category: str
        """
        self._category = category

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
        if not isinstance(other, RepoFileQueryDTOV5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
