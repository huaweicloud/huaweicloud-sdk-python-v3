# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowQueryParam:

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
        'type': 'str',
        'tags': 'dict(str, str)',
        'page': 'int',
        'size': 'int',
        'enterprise_project_id': 'str',
        'create_by': 'str',
        'sort_field': 'str',
        'sort_type': 'str',
        'search_time_start': 'int',
        'search_time_end': 'int',
        'status': 'str'
    }

    attribute_map = {
        'search': 'search',
        'type': 'type',
        'tags': 'tags',
        'page': 'page',
        'size': 'size',
        'enterprise_project_id': 'enterprise_project_id',
        'create_by': 'create_by',
        'sort_field': 'sort_field',
        'sort_type': 'sort_type',
        'search_time_start': 'search_time_start',
        'search_time_end': 'search_time_end',
        'status': 'status'
    }

    def __init__(self, search=None, type=None, tags=None, page=None, size=None, enterprise_project_id=None, create_by=None, sort_field=None, sort_type=None, search_time_start=None, search_time_end=None, status=None):
        r"""WorkflowQueryParam

        The model defined in huaweicloud sdk

        :param search: 搜索内容，可以针对工作流名称和描述内容进行搜索。
        :type search: str
        :param type: 工作流分类，可以取值[\&quot;cron\&quot;,\&quot;event\&quot;,\&quot;manual\&quot;]。
        :type type: str
        :param tags: 工作流标签，最多支持10个。
        :type tags: dict(str, str)
        :param page: 查询当前的页数，默认值为0。
        :type page: int
        :param size: 查询当前页的大小，默认值为10。
        :type size: int
        :param enterprise_project_id: 企业项目id。
        :type enterprise_project_id: str
        :param create_by: 工作流创建人。
        :type create_by: str
        :param sort_field: 排序字段，取值[\&quot;create_time\&quot;，\&quot;last_execution_start_time\&quot;，\&quot;update_time\&quot;]。
        :type sort_field: str
        :param sort_type: 排序类型，取值[\&quot;ASC\&quot;，\&quot;DESC\&quot;]。
        :type sort_type: str
        :param search_time_start: 时间范围查询的开始时间。
        :type search_time_start: int
        :param search_time_end: 时间范围查询的结束时间。
        :type search_time_end: int
        :param status: 任务的状态 [\&quot;success\&quot;,\&quot;fail\&quot;,\&quot;executing\&quot;,\&quot;cancel\&quot;,\&quot;waitExecute\&quot;,\&quot;waitApproval\&quot;,\&quot;approvalFailed\&quot;,\&quot;pausing\&quot;,\&quot;canceling\&quot;]
        :type status: str
        """
        
        

        self._search = None
        self._type = None
        self._tags = None
        self._page = None
        self._size = None
        self._enterprise_project_id = None
        self._create_by = None
        self._sort_field = None
        self._sort_type = None
        self._search_time_start = None
        self._search_time_end = None
        self._status = None
        self.discriminator = None

        if search is not None:
            self.search = search
        if type is not None:
            self.type = type
        if tags is not None:
            self.tags = tags
        if page is not None:
            self.page = page
        if size is not None:
            self.size = size
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if create_by is not None:
            self.create_by = create_by
        self.sort_field = sort_field
        self.sort_type = sort_type
        if search_time_start is not None:
            self.search_time_start = search_time_start
        if search_time_end is not None:
            self.search_time_end = search_time_end
        if status is not None:
            self.status = status

    @property
    def search(self):
        r"""Gets the search of this WorkflowQueryParam.

        搜索内容，可以针对工作流名称和描述内容进行搜索。

        :return: The search of this WorkflowQueryParam.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this WorkflowQueryParam.

        搜索内容，可以针对工作流名称和描述内容进行搜索。

        :param search: The search of this WorkflowQueryParam.
        :type search: str
        """
        self._search = search

    @property
    def type(self):
        r"""Gets the type of this WorkflowQueryParam.

        工作流分类，可以取值[\"cron\",\"event\",\"manual\"]。

        :return: The type of this WorkflowQueryParam.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this WorkflowQueryParam.

        工作流分类，可以取值[\"cron\",\"event\",\"manual\"]。

        :param type: The type of this WorkflowQueryParam.
        :type type: str
        """
        self._type = type

    @property
    def tags(self):
        r"""Gets the tags of this WorkflowQueryParam.

        工作流标签，最多支持10个。

        :return: The tags of this WorkflowQueryParam.
        :rtype: dict(str, str)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this WorkflowQueryParam.

        工作流标签，最多支持10个。

        :param tags: The tags of this WorkflowQueryParam.
        :type tags: dict(str, str)
        """
        self._tags = tags

    @property
    def page(self):
        r"""Gets the page of this WorkflowQueryParam.

        查询当前的页数，默认值为0。

        :return: The page of this WorkflowQueryParam.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this WorkflowQueryParam.

        查询当前的页数，默认值为0。

        :param page: The page of this WorkflowQueryParam.
        :type page: int
        """
        self._page = page

    @property
    def size(self):
        r"""Gets the size of this WorkflowQueryParam.

        查询当前页的大小，默认值为10。

        :return: The size of this WorkflowQueryParam.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this WorkflowQueryParam.

        查询当前页的大小，默认值为10。

        :param size: The size of this WorkflowQueryParam.
        :type size: int
        """
        self._size = size

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this WorkflowQueryParam.

        企业项目id。

        :return: The enterprise_project_id of this WorkflowQueryParam.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this WorkflowQueryParam.

        企业项目id。

        :param enterprise_project_id: The enterprise_project_id of this WorkflowQueryParam.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def create_by(self):
        r"""Gets the create_by of this WorkflowQueryParam.

        工作流创建人。

        :return: The create_by of this WorkflowQueryParam.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        r"""Sets the create_by of this WorkflowQueryParam.

        工作流创建人。

        :param create_by: The create_by of this WorkflowQueryParam.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def sort_field(self):
        r"""Gets the sort_field of this WorkflowQueryParam.

        排序字段，取值[\"create_time\"，\"last_execution_start_time\"，\"update_time\"]。

        :return: The sort_field of this WorkflowQueryParam.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this WorkflowQueryParam.

        排序字段，取值[\"create_time\"，\"last_execution_start_time\"，\"update_time\"]。

        :param sort_field: The sort_field of this WorkflowQueryParam.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_type(self):
        r"""Gets the sort_type of this WorkflowQueryParam.

        排序类型，取值[\"ASC\"，\"DESC\"]。

        :return: The sort_type of this WorkflowQueryParam.
        :rtype: str
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type):
        r"""Sets the sort_type of this WorkflowQueryParam.

        排序类型，取值[\"ASC\"，\"DESC\"]。

        :param sort_type: The sort_type of this WorkflowQueryParam.
        :type sort_type: str
        """
        self._sort_type = sort_type

    @property
    def search_time_start(self):
        r"""Gets the search_time_start of this WorkflowQueryParam.

        时间范围查询的开始时间。

        :return: The search_time_start of this WorkflowQueryParam.
        :rtype: int
        """
        return self._search_time_start

    @search_time_start.setter
    def search_time_start(self, search_time_start):
        r"""Sets the search_time_start of this WorkflowQueryParam.

        时间范围查询的开始时间。

        :param search_time_start: The search_time_start of this WorkflowQueryParam.
        :type search_time_start: int
        """
        self._search_time_start = search_time_start

    @property
    def search_time_end(self):
        r"""Gets the search_time_end of this WorkflowQueryParam.

        时间范围查询的结束时间。

        :return: The search_time_end of this WorkflowQueryParam.
        :rtype: int
        """
        return self._search_time_end

    @search_time_end.setter
    def search_time_end(self, search_time_end):
        r"""Sets the search_time_end of this WorkflowQueryParam.

        时间范围查询的结束时间。

        :param search_time_end: The search_time_end of this WorkflowQueryParam.
        :type search_time_end: int
        """
        self._search_time_end = search_time_end

    @property
    def status(self):
        r"""Gets the status of this WorkflowQueryParam.

        任务的状态 [\"success\",\"fail\",\"executing\",\"cancel\",\"waitExecute\",\"waitApproval\",\"approvalFailed\",\"pausing\",\"canceling\"]

        :return: The status of this WorkflowQueryParam.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this WorkflowQueryParam.

        任务的状态 [\"success\",\"fail\",\"executing\",\"cancel\",\"waitExecute\",\"waitApproval\",\"approvalFailed\",\"pausing\",\"canceling\"]

        :param status: The status of this WorkflowQueryParam.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, WorkflowQueryParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
