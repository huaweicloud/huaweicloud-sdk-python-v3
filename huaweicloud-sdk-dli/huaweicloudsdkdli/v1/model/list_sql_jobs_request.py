# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSqlJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'current_page': 'int',
        'db_name': 'str',
        'end': 'int',
        'engine_type': 'str',
        'job_status': 'str',
        'job_id': 'str',
        'job_type': 'str',
        'order': 'str',
        'owner': 'str',
        'page_size': 'int',
        'queue_name': 'str',
        'sql_pattern': 'str',
        'start': 'int',
        'table_name': 'str',
        'tags': 'str',
        'job_types': 'list[str]'
    }

    attribute_map = {
        'current_page': 'current-page',
        'db_name': 'db_name',
        'end': 'end',
        'engine_type': 'engine-type',
        'job_status': 'job-status',
        'job_id': 'job-id',
        'job_type': 'job-type',
        'order': 'order',
        'owner': 'owner',
        'page_size': 'page-size',
        'queue_name': 'queue_name',
        'sql_pattern': 'sql_pattern',
        'start': 'start',
        'table_name': 'table_name',
        'tags': 'tags',
        'job_types': 'job_types'
    }

    def __init__(self, current_page=None, db_name=None, end=None, engine_type=None, job_status=None, job_id=None, job_type=None, order=None, owner=None, page_size=None, queue_name=None, sql_pattern=None, start=None, table_name=None, tags=None, job_types=None):
        r"""ListSqlJobsRequest

        The model defined in huaweicloud sdk

        :param current_page: 参数解释:  当前页码，默认为第一页 示例: 55 约束限制:  无 取值范围: 大于1的整数 默认取值: 1
        :type current_page: int
        :param db_name: 参数解释:  数据库名称 示例: UQuery 约束限制:  长度小于等于16 取值范围: 无 默认取值: 无
        :type db_name: str
        :param end: 参数解释:  用于查询开始时间在该时间点之前的作业。时间格式为unix时间戳，单位：毫秒 示例: 156789546456 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type end: int
        :param engine_type: 参数解释:  引擎类型。支持配置spark引擎或hetuEngine引擎 示例: spark 约束限制:  无 取值范围: spark、hetuEngine 默认取值: 无
        :type engine_type: str
        :param job_status: 参数解释:  指定查询的作业状态 示例: FINISHED 约束限制:  长度小于等于16 取值范围: LAUNCHING RUNNING FAILED CANCELLED COMPUTED SUSPENDED ACTIVE DELETED CREATING FINISHED SCALING 默认取值: 无
        :type job_status: str
        :param job_id: 参数解释:  作业id 示例: bac76d9b-2891-4c50-a920-b98d8634fd0f 约束限制:  无 取值范围: 无 默认取值: 无
        :type job_id: str
        :param job_type: 参数解释:  指定查询的作业类型，包含DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE，若要查询所有类型的作业，则传入ALL。 示例: QUERY 约束限制:  无 取值范围: DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE、ALL 默认取值: 无
        :type job_type: str
        :param order: 参数解释:  指定作业排序方式 示例: duration_desc 约束限制:  无 取值范围: start_time_desc（作业提交时间降序） start_time_asc（作业提交时间升序） duration_desc（作业运行时长降序） duration_asc（作业运行时长升序） 默认取值: start_time_desc
        :type order: str
        :param owner: 参数解释:  提交作业的用户名称 示例: ei_dlics_d00352431 约束限制:  无 取值范围: 无 默认取值: 无
        :type owner: str
        :param page_size: 参数解释:  每页显示的最大作业个数 示例: 5 约束限制:  无 取值范围: [1, 100] 默认取值: 50
        :type page_size: int
        :param queue_name: 参数解释:  指定queue_name作为作业过滤条件，查询在指定queue上运行的作业 示例: q1 约束限制:  匹配正则表达式^(?!_)(?![0-9]+$)[A-Za-z0-9_]*$且长度在[1, 128]范围内的字符串 取值范围: 无 默认取值: 无
        :type queue_name: str
        :param sql_pattern: 参数解释:  指定sql片段作为作业过滤条件，不区分大小写 示例: .*? 约束限制:  长度在[0, 1024]范围内的字符串 取值范围: 无 默认取值: 无
        :type sql_pattern: str
        :param start: 参数解释:  用于查询开始时间在该时间点之后的作业。时间格式为unix时间戳，单位：毫秒 示例: 156456784655 约束限制:  无 取值范围: 大于等于1的整数 默认取值: 无
        :type start: int
        :param table_name: 参数解释:  记录其操作的表名称。类型为Import和Export作业才有“table_name”属性 示例: CS_JOB 约束限制:  无 取值范围: 无 默认取值: 无
        :type table_name: str
        :param tags: 参数解释:  指定作业标签作为过滤条件，支持多标签过滤。格式为“key&#x3D;value”，如：GET /v1.0/{project_id}/jobs?tags&#x3D;k1%3Dv1，“&#x3D;”需要转义为“%3D”，“k1”为标签键，“v1”为标签值 示例: key&#x3D;value 约束限制:  格式为“key&#x3D;value”的字符串 取值范围: 无 默认取值: 无
        :type tags: str
        :param job_types: 参数解释:  指定查询的作业类型列表，包含DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE，若要查询所有类型的作业，则传入ALL。 示例: QUERY 约束限制:  无 取值范围: DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE、ALL 默认取值: 无
        :type job_types: list[str]
        """
        
        

        self._current_page = None
        self._db_name = None
        self._end = None
        self._engine_type = None
        self._job_status = None
        self._job_id = None
        self._job_type = None
        self._order = None
        self._owner = None
        self._page_size = None
        self._queue_name = None
        self._sql_pattern = None
        self._start = None
        self._table_name = None
        self._tags = None
        self._job_types = None
        self.discriminator = None

        if current_page is not None:
            self.current_page = current_page
        if db_name is not None:
            self.db_name = db_name
        if end is not None:
            self.end = end
        if engine_type is not None:
            self.engine_type = engine_type
        if job_status is not None:
            self.job_status = job_status
        if job_id is not None:
            self.job_id = job_id
        if job_type is not None:
            self.job_type = job_type
        if order is not None:
            self.order = order
        if owner is not None:
            self.owner = owner
        if page_size is not None:
            self.page_size = page_size
        if queue_name is not None:
            self.queue_name = queue_name
        if sql_pattern is not None:
            self.sql_pattern = sql_pattern
        if start is not None:
            self.start = start
        if table_name is not None:
            self.table_name = table_name
        if tags is not None:
            self.tags = tags
        if job_types is not None:
            self.job_types = job_types

    @property
    def current_page(self):
        r"""Gets the current_page of this ListSqlJobsRequest.

        参数解释:  当前页码，默认为第一页 示例: 55 约束限制:  无 取值范围: 大于1的整数 默认取值: 1

        :return: The current_page of this ListSqlJobsRequest.
        :rtype: int
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        r"""Sets the current_page of this ListSqlJobsRequest.

        参数解释:  当前页码，默认为第一页 示例: 55 约束限制:  无 取值范围: 大于1的整数 默认取值: 1

        :param current_page: The current_page of this ListSqlJobsRequest.
        :type current_page: int
        """
        self._current_page = current_page

    @property
    def db_name(self):
        r"""Gets the db_name of this ListSqlJobsRequest.

        参数解释:  数据库名称 示例: UQuery 约束限制:  长度小于等于16 取值范围: 无 默认取值: 无

        :return: The db_name of this ListSqlJobsRequest.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this ListSqlJobsRequest.

        参数解释:  数据库名称 示例: UQuery 约束限制:  长度小于等于16 取值范围: 无 默认取值: 无

        :param db_name: The db_name of this ListSqlJobsRequest.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def end(self):
        r"""Gets the end of this ListSqlJobsRequest.

        参数解释:  用于查询开始时间在该时间点之前的作业。时间格式为unix时间戳，单位：毫秒 示例: 156789546456 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The end of this ListSqlJobsRequest.
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        r"""Sets the end of this ListSqlJobsRequest.

        参数解释:  用于查询开始时间在该时间点之前的作业。时间格式为unix时间戳，单位：毫秒 示例: 156789546456 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param end: The end of this ListSqlJobsRequest.
        :type end: int
        """
        self._end = end

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ListSqlJobsRequest.

        参数解释:  引擎类型。支持配置spark引擎或hetuEngine引擎 示例: spark 约束限制:  无 取值范围: spark、hetuEngine 默认取值: 无

        :return: The engine_type of this ListSqlJobsRequest.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ListSqlJobsRequest.

        参数解释:  引擎类型。支持配置spark引擎或hetuEngine引擎 示例: spark 约束限制:  无 取值范围: spark、hetuEngine 默认取值: 无

        :param engine_type: The engine_type of this ListSqlJobsRequest.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def job_status(self):
        r"""Gets the job_status of this ListSqlJobsRequest.

        参数解释:  指定查询的作业状态 示例: FINISHED 约束限制:  长度小于等于16 取值范围: LAUNCHING RUNNING FAILED CANCELLED COMPUTED SUSPENDED ACTIVE DELETED CREATING FINISHED SCALING 默认取值: 无

        :return: The job_status of this ListSqlJobsRequest.
        :rtype: str
        """
        return self._job_status

    @job_status.setter
    def job_status(self, job_status):
        r"""Sets the job_status of this ListSqlJobsRequest.

        参数解释:  指定查询的作业状态 示例: FINISHED 约束限制:  长度小于等于16 取值范围: LAUNCHING RUNNING FAILED CANCELLED COMPUTED SUSPENDED ACTIVE DELETED CREATING FINISHED SCALING 默认取值: 无

        :param job_status: The job_status of this ListSqlJobsRequest.
        :type job_status: str
        """
        self._job_status = job_status

    @property
    def job_id(self):
        r"""Gets the job_id of this ListSqlJobsRequest.

        参数解释:  作业id 示例: bac76d9b-2891-4c50-a920-b98d8634fd0f 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The job_id of this ListSqlJobsRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ListSqlJobsRequest.

        参数解释:  作业id 示例: bac76d9b-2891-4c50-a920-b98d8634fd0f 约束限制:  无 取值范围: 无 默认取值: 无

        :param job_id: The job_id of this ListSqlJobsRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_type(self):
        r"""Gets the job_type of this ListSqlJobsRequest.

        参数解释:  指定查询的作业类型，包含DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE，若要查询所有类型的作业，则传入ALL。 示例: QUERY 约束限制:  无 取值范围: DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE、ALL 默认取值: 无

        :return: The job_type of this ListSqlJobsRequest.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this ListSqlJobsRequest.

        参数解释:  指定查询的作业类型，包含DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE，若要查询所有类型的作业，则传入ALL。 示例: QUERY 约束限制:  无 取值范围: DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE、ALL 默认取值: 无

        :param job_type: The job_type of this ListSqlJobsRequest.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def order(self):
        r"""Gets the order of this ListSqlJobsRequest.

        参数解释:  指定作业排序方式 示例: duration_desc 约束限制:  无 取值范围: start_time_desc（作业提交时间降序） start_time_asc（作业提交时间升序） duration_desc（作业运行时长降序） duration_asc（作业运行时长升序） 默认取值: start_time_desc

        :return: The order of this ListSqlJobsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListSqlJobsRequest.

        参数解释:  指定作业排序方式 示例: duration_desc 约束限制:  无 取值范围: start_time_desc（作业提交时间降序） start_time_asc（作业提交时间升序） duration_desc（作业运行时长降序） duration_asc（作业运行时长升序） 默认取值: start_time_desc

        :param order: The order of this ListSqlJobsRequest.
        :type order: str
        """
        self._order = order

    @property
    def owner(self):
        r"""Gets the owner of this ListSqlJobsRequest.

        参数解释:  提交作业的用户名称 示例: ei_dlics_d00352431 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The owner of this ListSqlJobsRequest.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this ListSqlJobsRequest.

        参数解释:  提交作业的用户名称 示例: ei_dlics_d00352431 约束限制:  无 取值范围: 无 默认取值: 无

        :param owner: The owner of this ListSqlJobsRequest.
        :type owner: str
        """
        self._owner = owner

    @property
    def page_size(self):
        r"""Gets the page_size of this ListSqlJobsRequest.

        参数解释:  每页显示的最大作业个数 示例: 5 约束限制:  无 取值范围: [1, 100] 默认取值: 50

        :return: The page_size of this ListSqlJobsRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListSqlJobsRequest.

        参数解释:  每页显示的最大作业个数 示例: 5 约束限制:  无 取值范围: [1, 100] 默认取值: 50

        :param page_size: The page_size of this ListSqlJobsRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def queue_name(self):
        r"""Gets the queue_name of this ListSqlJobsRequest.

        参数解释:  指定queue_name作为作业过滤条件，查询在指定queue上运行的作业 示例: q1 约束限制:  匹配正则表达式^(?!_)(?![0-9]+$)[A-Za-z0-9_]*$且长度在[1, 128]范围内的字符串 取值范围: 无 默认取值: 无

        :return: The queue_name of this ListSqlJobsRequest.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        r"""Sets the queue_name of this ListSqlJobsRequest.

        参数解释:  指定queue_name作为作业过滤条件，查询在指定queue上运行的作业 示例: q1 约束限制:  匹配正则表达式^(?!_)(?![0-9]+$)[A-Za-z0-9_]*$且长度在[1, 128]范围内的字符串 取值范围: 无 默认取值: 无

        :param queue_name: The queue_name of this ListSqlJobsRequest.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def sql_pattern(self):
        r"""Gets the sql_pattern of this ListSqlJobsRequest.

        参数解释:  指定sql片段作为作业过滤条件，不区分大小写 示例: .*? 约束限制:  长度在[0, 1024]范围内的字符串 取值范围: 无 默认取值: 无

        :return: The sql_pattern of this ListSqlJobsRequest.
        :rtype: str
        """
        return self._sql_pattern

    @sql_pattern.setter
    def sql_pattern(self, sql_pattern):
        r"""Sets the sql_pattern of this ListSqlJobsRequest.

        参数解释:  指定sql片段作为作业过滤条件，不区分大小写 示例: .*? 约束限制:  长度在[0, 1024]范围内的字符串 取值范围: 无 默认取值: 无

        :param sql_pattern: The sql_pattern of this ListSqlJobsRequest.
        :type sql_pattern: str
        """
        self._sql_pattern = sql_pattern

    @property
    def start(self):
        r"""Gets the start of this ListSqlJobsRequest.

        参数解释:  用于查询开始时间在该时间点之后的作业。时间格式为unix时间戳，单位：毫秒 示例: 156456784655 约束限制:  无 取值范围: 大于等于1的整数 默认取值: 无

        :return: The start of this ListSqlJobsRequest.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this ListSqlJobsRequest.

        参数解释:  用于查询开始时间在该时间点之后的作业。时间格式为unix时间戳，单位：毫秒 示例: 156456784655 约束限制:  无 取值范围: 大于等于1的整数 默认取值: 无

        :param start: The start of this ListSqlJobsRequest.
        :type start: int
        """
        self._start = start

    @property
    def table_name(self):
        r"""Gets the table_name of this ListSqlJobsRequest.

        参数解释:  记录其操作的表名称。类型为Import和Export作业才有“table_name”属性 示例: CS_JOB 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The table_name of this ListSqlJobsRequest.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ListSqlJobsRequest.

        参数解释:  记录其操作的表名称。类型为Import和Export作业才有“table_name”属性 示例: CS_JOB 约束限制:  无 取值范围: 无 默认取值: 无

        :param table_name: The table_name of this ListSqlJobsRequest.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def tags(self):
        r"""Gets the tags of this ListSqlJobsRequest.

        参数解释:  指定作业标签作为过滤条件，支持多标签过滤。格式为“key=value”，如：GET /v1.0/{project_id}/jobs?tags=k1%3Dv1，“=”需要转义为“%3D”，“k1”为标签键，“v1”为标签值 示例: key=value 约束限制:  格式为“key=value”的字符串 取值范围: 无 默认取值: 无

        :return: The tags of this ListSqlJobsRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListSqlJobsRequest.

        参数解释:  指定作业标签作为过滤条件，支持多标签过滤。格式为“key=value”，如：GET /v1.0/{project_id}/jobs?tags=k1%3Dv1，“=”需要转义为“%3D”，“k1”为标签键，“v1”为标签值 示例: key=value 约束限制:  格式为“key=value”的字符串 取值范围: 无 默认取值: 无

        :param tags: The tags of this ListSqlJobsRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def job_types(self):
        r"""Gets the job_types of this ListSqlJobsRequest.

        参数解释:  指定查询的作业类型列表，包含DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE，若要查询所有类型的作业，则传入ALL。 示例: QUERY 约束限制:  无 取值范围: DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE、ALL 默认取值: 无

        :return: The job_types of this ListSqlJobsRequest.
        :rtype: list[str]
        """
        return self._job_types

    @job_types.setter
    def job_types(self, job_types):
        r"""Sets the job_types of this ListSqlJobsRequest.

        参数解释:  指定查询的作业类型列表，包含DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE，若要查询所有类型的作业，则传入ALL。 示例: QUERY 约束限制:  无 取值范围: DDL、DCL、IMPORT、EXPORT、QUERY、INSERT、DATA_MIGRATION、UPDATE、DELETE、RESTART_QUEUE、SCALE_QUEUE、ALL 默认取值: 无

        :param job_types: The job_types of this ListSqlJobsRequest.
        :type job_types: list[str]
        """
        self._job_types = job_types

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
        if not isinstance(other, ListSqlJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
