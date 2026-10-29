# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTasksListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page': 'int',
        'page_size': 'int',
        'search': 'str',
        'project_id': 'str',
        'review_result_types': 'str',
        'job_status_types': 'str',
        'order_by_execute_time': 'str',
        'task_classification_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort_field': 'str',
        'sort_order': 'str',
        'operator': 'str',
        'repo_url': 'str',
        'branch': 'str',
        'repo_url_full_match': 'str'
    }

    attribute_map = {
        'page': 'page',
        'page_size': 'page_size',
        'search': 'search',
        'project_id': 'project_id',
        'review_result_types': 'review_result_types',
        'job_status_types': 'job_status_types',
        'order_by_execute_time': 'order_by_execute_time',
        'task_classification_id': 'task_classification_id',
        'offset': 'offset',
        'limit': 'limit',
        'sort_field': 'sort_field',
        'sort_order': 'sort_order',
        'operator': 'operator',
        'repo_url': 'repo_url',
        'branch': 'branch',
        'repo_url_full_match': 'repo_url_full_match'
    }

    def __init__(self, page=None, page_size=None, search=None, project_id=None, review_result_types=None, job_status_types=None, order_by_execute_time=None, task_classification_id=None, offset=None, limit=None, sort_field=None, sort_order=None, operator=None, repo_url=None, branch=None, repo_url_full_match=None):
        r"""ShowTasksListRequest

        The model defined in huaweicloud sdk

        :param page: **参数解释：** 分页页码。 **约束限制：** 分页页码≥1。 **取值范围:** 1-2147483647 **默认取值：**  不涉及。
        :type page: int
        :param page_size: **参数解释：** 分页大小。 **约束限制：** 数字1-200之间。 **取值范围:** 1-200 **默认取值：** 不涉及。
        :type page_size: int
        :param search: **参数解释：** 需要搜索的任务名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type search: str
        :param project_id: **参数解释：** 项目的32位UUID，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/zh-cn/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)接口获取。 **约束条件：** 不涉及。 **取值范围：** 长度为[1~32]个字符。 **默认取值：** 不涉及。
        :type project_id: str
        :param review_result_types: **参数解释：** 门禁结果。 **约束限制：** 不涉及。 **取值范围：** - success：门禁通过。 - error：门禁不通过。 **默认取值：** 不涉及。
        :type review_result_types: str
        :param job_status_types: **参数解释：** 检查状态。 **约束限制：** 不涉及。 **取值范围：** - success：检查成功。 - failed：检查失败。 - aborted：检查终止。 - executing：检查中。 - never_execute：未检查。 **默认取值：** 不涉及。
        :type job_status_types: str
        :param order_by_execute_time: **参数解释：** 是否按照执行时间排序。 **约束限制：** 不涉及。 **取值范围：** - up：按照执行时间升序排序。 - down：按照执行时间降序排序。 **默认取值：** 不涉及。
        :type order_by_execute_time: str
        :param task_classification_id: **参数解释：** 任务的分组ID，可通过列出项目下的分组信息接口获取任务的分组ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type task_classification_id: str
        :param offset: 列表类接口参数
        :type offset: int
        :param limit: 列表类接口参数
        :type limit: int
        :param sort_field: **参数解释：** 排序字段,任务列表每次只能根据一个字段进行排序。 **约束限制：** 不涉及。
        :type sort_field: str
        :param sort_order: **参数解释：** 排序顺序，取值范围：\&quot;up\&quot;（升序）、\&quot;down\&quot;（降序） **约束限制：** 不涉及。
        :type sort_order: str
        :param operator: **参数解释：** 操作人，填写账号用户名。 **约束限制：** 不涉及。 **取值范围：** 长度为[1~128]个字符。 **默认取值：** 不涉及。
        :type operator: str
        :param repo_url: **参数解释：** 代码仓地址。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type repo_url: str
        :param branch: **参数解释：** 分支。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type branch: str
        :param repo_url_full_match: **参数解释：** 和repo_url配合使用，查询任务时是否完全匹配repo_url。 **约束限制：** 不涉及。 **取值范围：** - true：只查询代码仓地址为repo_url的任务。 - false：查询ssh协议的代码仓地址或http协议的代码仓地址和repo_url匹配的任务。 **默认取值：** false。
        :type repo_url_full_match: str
        """
        
        

        self._page = None
        self._page_size = None
        self._search = None
        self._project_id = None
        self._review_result_types = None
        self._job_status_types = None
        self._order_by_execute_time = None
        self._task_classification_id = None
        self._offset = None
        self._limit = None
        self._sort_field = None
        self._sort_order = None
        self._operator = None
        self._repo_url = None
        self._branch = None
        self._repo_url_full_match = None
        self.discriminator = None

        if page is not None:
            self.page = page
        if page_size is not None:
            self.page_size = page_size
        if search is not None:
            self.search = search
        if project_id is not None:
            self.project_id = project_id
        if review_result_types is not None:
            self.review_result_types = review_result_types
        if job_status_types is not None:
            self.job_status_types = job_status_types
        if order_by_execute_time is not None:
            self.order_by_execute_time = order_by_execute_time
        if task_classification_id is not None:
            self.task_classification_id = task_classification_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_order is not None:
            self.sort_order = sort_order
        if operator is not None:
            self.operator = operator
        if repo_url is not None:
            self.repo_url = repo_url
        if branch is not None:
            self.branch = branch
        if repo_url_full_match is not None:
            self.repo_url_full_match = repo_url_full_match

    @property
    def page(self):
        r"""Gets the page of this ShowTasksListRequest.

        **参数解释：** 分页页码。 **约束限制：** 分页页码≥1。 **取值范围:** 1-2147483647 **默认取值：**  不涉及。

        :return: The page of this ShowTasksListRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ShowTasksListRequest.

        **参数解释：** 分页页码。 **约束限制：** 分页页码≥1。 **取值范围:** 1-2147483647 **默认取值：**  不涉及。

        :param page: The page of this ShowTasksListRequest.
        :type page: int
        """
        self._page = page

    @property
    def page_size(self):
        r"""Gets the page_size of this ShowTasksListRequest.

        **参数解释：** 分页大小。 **约束限制：** 数字1-200之间。 **取值范围:** 1-200 **默认取值：** 不涉及。

        :return: The page_size of this ShowTasksListRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ShowTasksListRequest.

        **参数解释：** 分页大小。 **约束限制：** 数字1-200之间。 **取值范围:** 1-200 **默认取值：** 不涉及。

        :param page_size: The page_size of this ShowTasksListRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def search(self):
        r"""Gets the search of this ShowTasksListRequest.

        **参数解释：** 需要搜索的任务名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The search of this ShowTasksListRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ShowTasksListRequest.

        **参数解释：** 需要搜索的任务名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param search: The search of this ShowTasksListRequest.
        :type search: str
        """
        self._search = search

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowTasksListRequest.

        **参数解释：** 项目的32位UUID，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/zh-cn/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)接口获取。 **约束条件：** 不涉及。 **取值范围：** 长度为[1~32]个字符。 **默认取值：** 不涉及。

        :return: The project_id of this ShowTasksListRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowTasksListRequest.

        **参数解释：** 项目的32位UUID，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/zh-cn/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm,hcs_site,hcs_sitesm,fcs)接口获取。 **约束条件：** 不涉及。 **取值范围：** 长度为[1~32]个字符。 **默认取值：** 不涉及。

        :param project_id: The project_id of this ShowTasksListRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def review_result_types(self):
        r"""Gets the review_result_types of this ShowTasksListRequest.

        **参数解释：** 门禁结果。 **约束限制：** 不涉及。 **取值范围：** - success：门禁通过。 - error：门禁不通过。 **默认取值：** 不涉及。

        :return: The review_result_types of this ShowTasksListRequest.
        :rtype: str
        """
        return self._review_result_types

    @review_result_types.setter
    def review_result_types(self, review_result_types):
        r"""Sets the review_result_types of this ShowTasksListRequest.

        **参数解释：** 门禁结果。 **约束限制：** 不涉及。 **取值范围：** - success：门禁通过。 - error：门禁不通过。 **默认取值：** 不涉及。

        :param review_result_types: The review_result_types of this ShowTasksListRequest.
        :type review_result_types: str
        """
        self._review_result_types = review_result_types

    @property
    def job_status_types(self):
        r"""Gets the job_status_types of this ShowTasksListRequest.

        **参数解释：** 检查状态。 **约束限制：** 不涉及。 **取值范围：** - success：检查成功。 - failed：检查失败。 - aborted：检查终止。 - executing：检查中。 - never_execute：未检查。 **默认取值：** 不涉及。

        :return: The job_status_types of this ShowTasksListRequest.
        :rtype: str
        """
        return self._job_status_types

    @job_status_types.setter
    def job_status_types(self, job_status_types):
        r"""Sets the job_status_types of this ShowTasksListRequest.

        **参数解释：** 检查状态。 **约束限制：** 不涉及。 **取值范围：** - success：检查成功。 - failed：检查失败。 - aborted：检查终止。 - executing：检查中。 - never_execute：未检查。 **默认取值：** 不涉及。

        :param job_status_types: The job_status_types of this ShowTasksListRequest.
        :type job_status_types: str
        """
        self._job_status_types = job_status_types

    @property
    def order_by_execute_time(self):
        r"""Gets the order_by_execute_time of this ShowTasksListRequest.

        **参数解释：** 是否按照执行时间排序。 **约束限制：** 不涉及。 **取值范围：** - up：按照执行时间升序排序。 - down：按照执行时间降序排序。 **默认取值：** 不涉及。

        :return: The order_by_execute_time of this ShowTasksListRequest.
        :rtype: str
        """
        return self._order_by_execute_time

    @order_by_execute_time.setter
    def order_by_execute_time(self, order_by_execute_time):
        r"""Sets the order_by_execute_time of this ShowTasksListRequest.

        **参数解释：** 是否按照执行时间排序。 **约束限制：** 不涉及。 **取值范围：** - up：按照执行时间升序排序。 - down：按照执行时间降序排序。 **默认取值：** 不涉及。

        :param order_by_execute_time: The order_by_execute_time of this ShowTasksListRequest.
        :type order_by_execute_time: str
        """
        self._order_by_execute_time = order_by_execute_time

    @property
    def task_classification_id(self):
        r"""Gets the task_classification_id of this ShowTasksListRequest.

        **参数解释：** 任务的分组ID，可通过列出项目下的分组信息接口获取任务的分组ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The task_classification_id of this ShowTasksListRequest.
        :rtype: str
        """
        return self._task_classification_id

    @task_classification_id.setter
    def task_classification_id(self, task_classification_id):
        r"""Sets the task_classification_id of this ShowTasksListRequest.

        **参数解释：** 任务的分组ID，可通过列出项目下的分组信息接口获取任务的分组ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param task_classification_id: The task_classification_id of this ShowTasksListRequest.
        :type task_classification_id: str
        """
        self._task_classification_id = task_classification_id

    @property
    def offset(self):
        r"""Gets the offset of this ShowTasksListRequest.

        列表类接口参数

        :return: The offset of this ShowTasksListRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowTasksListRequest.

        列表类接口参数

        :param offset: The offset of this ShowTasksListRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowTasksListRequest.

        列表类接口参数

        :return: The limit of this ShowTasksListRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowTasksListRequest.

        列表类接口参数

        :param limit: The limit of this ShowTasksListRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_field(self):
        r"""Gets the sort_field of this ShowTasksListRequest.

        **参数解释：** 排序字段,任务列表每次只能根据一个字段进行排序。 **约束限制：** 不涉及。

        :return: The sort_field of this ShowTasksListRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this ShowTasksListRequest.

        **参数解释：** 排序字段,任务列表每次只能根据一个字段进行排序。 **约束限制：** 不涉及。

        :param sort_field: The sort_field of this ShowTasksListRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_order(self):
        r"""Gets the sort_order of this ShowTasksListRequest.

        **参数解释：** 排序顺序，取值范围：\"up\"（升序）、\"down\"（降序） **约束限制：** 不涉及。

        :return: The sort_order of this ShowTasksListRequest.
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        r"""Sets the sort_order of this ShowTasksListRequest.

        **参数解释：** 排序顺序，取值范围：\"up\"（升序）、\"down\"（降序） **约束限制：** 不涉及。

        :param sort_order: The sort_order of this ShowTasksListRequest.
        :type sort_order: str
        """
        self._sort_order = sort_order

    @property
    def operator(self):
        r"""Gets the operator of this ShowTasksListRequest.

        **参数解释：** 操作人，填写账号用户名。 **约束限制：** 不涉及。 **取值范围：** 长度为[1~128]个字符。 **默认取值：** 不涉及。

        :return: The operator of this ShowTasksListRequest.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this ShowTasksListRequest.

        **参数解释：** 操作人，填写账号用户名。 **约束限制：** 不涉及。 **取值范围：** 长度为[1~128]个字符。 **默认取值：** 不涉及。

        :param operator: The operator of this ShowTasksListRequest.
        :type operator: str
        """
        self._operator = operator

    @property
    def repo_url(self):
        r"""Gets the repo_url of this ShowTasksListRequest.

        **参数解释：** 代码仓地址。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The repo_url of this ShowTasksListRequest.
        :rtype: str
        """
        return self._repo_url

    @repo_url.setter
    def repo_url(self, repo_url):
        r"""Sets the repo_url of this ShowTasksListRequest.

        **参数解释：** 代码仓地址。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param repo_url: The repo_url of this ShowTasksListRequest.
        :type repo_url: str
        """
        self._repo_url = repo_url

    @property
    def branch(self):
        r"""Gets the branch of this ShowTasksListRequest.

        **参数解释：** 分支。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The branch of this ShowTasksListRequest.
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        r"""Sets the branch of this ShowTasksListRequest.

        **参数解释：** 分支。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param branch: The branch of this ShowTasksListRequest.
        :type branch: str
        """
        self._branch = branch

    @property
    def repo_url_full_match(self):
        r"""Gets the repo_url_full_match of this ShowTasksListRequest.

        **参数解释：** 和repo_url配合使用，查询任务时是否完全匹配repo_url。 **约束限制：** 不涉及。 **取值范围：** - true：只查询代码仓地址为repo_url的任务。 - false：查询ssh协议的代码仓地址或http协议的代码仓地址和repo_url匹配的任务。 **默认取值：** false。

        :return: The repo_url_full_match of this ShowTasksListRequest.
        :rtype: str
        """
        return self._repo_url_full_match

    @repo_url_full_match.setter
    def repo_url_full_match(self, repo_url_full_match):
        r"""Sets the repo_url_full_match of this ShowTasksListRequest.

        **参数解释：** 和repo_url配合使用，查询任务时是否完全匹配repo_url。 **约束限制：** 不涉及。 **取值范围：** - true：只查询代码仓地址为repo_url的任务。 - false：查询ssh协议的代码仓地址或http协议的代码仓地址和repo_url匹配的任务。 **默认取值：** false。

        :param repo_url_full_match: The repo_url_full_match of this ShowTasksListRequest.
        :type repo_url_full_match: str
        """
        self._repo_url_full_match = repo_url_full_match

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
        if not isinstance(other, ShowTasksListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
