# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobsRequest:

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
        'job_type': 'str',
        'order': 'str',
        'owner': 'str',
        'page_size': 'int',
        'queue_name': 'str',
        'sql_pattern': 'str',
        'start': 'int',
        'table_name': 'str',
        'tags': 'str'
    }

    attribute_map = {
        'current_page': 'current-page',
        'db_name': 'db_name',
        'end': 'end',
        'engine_type': 'engine-type',
        'job_status': 'job-status',
        'job_type': 'job-type',
        'order': 'order',
        'owner': 'owner',
        'page_size': 'page-size',
        'queue_name': 'queue_name',
        'sql_pattern': 'sql_pattern',
        'start': 'start',
        'table_name': 'table_name',
        'tags': 'tags'
    }

    def __init__(self, current_page=None, db_name=None, end=None, engine_type=None, job_status=None, job_type=None, order=None, owner=None, page_size=None, queue_name=None, sql_pattern=None, start=None, table_name=None, tags=None):
        """ListJobsRequest

        The model defined in huaweicloud sdk

        :param current_page: 当前页码，默认为第一页。
        :type current_page: int
        :param db_name: 
        :type db_name: str
        :param end: 用于查询开始时间在该时间点之前的作业。时间格式为unix时间戳，单位：毫秒。
        :type end: int
        :param engine_type: 
        :type engine_type: str
        :param job_status: 
        :type job_status: str
        :param job_type: 指定查询的作业类型，包含DDL、DCL、IMPORT、EXPORT、QUERY、INSERT，若要查询所有类型的作业，则传入ALL。
        :type job_type: str
        :param order: 指定作业排序方式，默认为start_time_desc（作业提交时间降序），支持duration_desc（作业运行时长降序）、duration_asc（作业运行时长升序）、start_time_desc（作业提交时间降序）、start_time_asc（作业提交时间升序）四种排序方式。
        :type order: str
        :param owner: 提交作业的用户名称
        :type owner: str
        :param page_size: 每页显示的最大作业个数，范围: [1, 100]。默认值：50。
        :type page_size: int
        :param queue_name: 指定queue_name作为作业过滤条件，查询在指定queue上运行的作业。
        :type queue_name: str
        :param sql_pattern: 指定sql片段作为作业过滤条件，不区分大小写。
        :type sql_pattern: str
        :param start: 用于查询开始时间在该时间点之后的作业。时间格式为unix时间戳，单位：毫秒。
        :type start: int
        :param table_name: 
        :type table_name: str
        :param tags: 指定作业标签作为过滤条件，支持多标签过滤。格式为“key&#x3D;value”，如：GET /v1.0/{project_id}/jobs?tags&#x3D;k1%3Dv1，“&#x3D;”需要转义为“%3D”，“k1”为标签键，“v1”为标签值。
        :type tags: str
        """
        
        

        self._current_page = None
        self._db_name = None
        self._end = None
        self._engine_type = None
        self._job_status = None
        self._job_type = None
        self._order = None
        self._owner = None
        self._page_size = None
        self._queue_name = None
        self._sql_pattern = None
        self._start = None
        self._table_name = None
        self._tags = None
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

    @property
    def current_page(self):
        """Gets the current_page of this ListJobsRequest.

        当前页码，默认为第一页。

        :return: The current_page of this ListJobsRequest.
        :rtype: int
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        """Sets the current_page of this ListJobsRequest.

        当前页码，默认为第一页。

        :param current_page: The current_page of this ListJobsRequest.
        :type current_page: int
        """
        self._current_page = current_page

    @property
    def db_name(self):
        """Gets the db_name of this ListJobsRequest.

        :return: The db_name of this ListJobsRequest.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this ListJobsRequest.

        :param db_name: The db_name of this ListJobsRequest.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def end(self):
        """Gets the end of this ListJobsRequest.

        用于查询开始时间在该时间点之前的作业。时间格式为unix时间戳，单位：毫秒。

        :return: The end of this ListJobsRequest.
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this ListJobsRequest.

        用于查询开始时间在该时间点之前的作业。时间格式为unix时间戳，单位：毫秒。

        :param end: The end of this ListJobsRequest.
        :type end: int
        """
        self._end = end

    @property
    def engine_type(self):
        """Gets the engine_type of this ListJobsRequest.

        :return: The engine_type of this ListJobsRequest.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        """Sets the engine_type of this ListJobsRequest.

        :param engine_type: The engine_type of this ListJobsRequest.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def job_status(self):
        """Gets the job_status of this ListJobsRequest.

        :return: The job_status of this ListJobsRequest.
        :rtype: str
        """
        return self._job_status

    @job_status.setter
    def job_status(self, job_status):
        """Sets the job_status of this ListJobsRequest.

        :param job_status: The job_status of this ListJobsRequest.
        :type job_status: str
        """
        self._job_status = job_status

    @property
    def job_type(self):
        """Gets the job_type of this ListJobsRequest.

        指定查询的作业类型，包含DDL、DCL、IMPORT、EXPORT、QUERY、INSERT，若要查询所有类型的作业，则传入ALL。

        :return: The job_type of this ListJobsRequest.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this ListJobsRequest.

        指定查询的作业类型，包含DDL、DCL、IMPORT、EXPORT、QUERY、INSERT，若要查询所有类型的作业，则传入ALL。

        :param job_type: The job_type of this ListJobsRequest.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def order(self):
        """Gets the order of this ListJobsRequest.

        指定作业排序方式，默认为start_time_desc（作业提交时间降序），支持duration_desc（作业运行时长降序）、duration_asc（作业运行时长升序）、start_time_desc（作业提交时间降序）、start_time_asc（作业提交时间升序）四种排序方式。

        :return: The order of this ListJobsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ListJobsRequest.

        指定作业排序方式，默认为start_time_desc（作业提交时间降序），支持duration_desc（作业运行时长降序）、duration_asc（作业运行时长升序）、start_time_desc（作业提交时间降序）、start_time_asc（作业提交时间升序）四种排序方式。

        :param order: The order of this ListJobsRequest.
        :type order: str
        """
        self._order = order

    @property
    def owner(self):
        """Gets the owner of this ListJobsRequest.

        提交作业的用户名称

        :return: The owner of this ListJobsRequest.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ListJobsRequest.

        提交作业的用户名称

        :param owner: The owner of this ListJobsRequest.
        :type owner: str
        """
        self._owner = owner

    @property
    def page_size(self):
        """Gets the page_size of this ListJobsRequest.

        每页显示的最大作业个数，范围: [1, 100]。默认值：50。

        :return: The page_size of this ListJobsRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListJobsRequest.

        每页显示的最大作业个数，范围: [1, 100]。默认值：50。

        :param page_size: The page_size of this ListJobsRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def queue_name(self):
        """Gets the queue_name of this ListJobsRequest.

        指定queue_name作为作业过滤条件，查询在指定queue上运行的作业。

        :return: The queue_name of this ListJobsRequest.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this ListJobsRequest.

        指定queue_name作为作业过滤条件，查询在指定queue上运行的作业。

        :param queue_name: The queue_name of this ListJobsRequest.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def sql_pattern(self):
        """Gets the sql_pattern of this ListJobsRequest.

        指定sql片段作为作业过滤条件，不区分大小写。

        :return: The sql_pattern of this ListJobsRequest.
        :rtype: str
        """
        return self._sql_pattern

    @sql_pattern.setter
    def sql_pattern(self, sql_pattern):
        """Sets the sql_pattern of this ListJobsRequest.

        指定sql片段作为作业过滤条件，不区分大小写。

        :param sql_pattern: The sql_pattern of this ListJobsRequest.
        :type sql_pattern: str
        """
        self._sql_pattern = sql_pattern

    @property
    def start(self):
        """Gets the start of this ListJobsRequest.

        用于查询开始时间在该时间点之后的作业。时间格式为unix时间戳，单位：毫秒。

        :return: The start of this ListJobsRequest.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ListJobsRequest.

        用于查询开始时间在该时间点之后的作业。时间格式为unix时间戳，单位：毫秒。

        :param start: The start of this ListJobsRequest.
        :type start: int
        """
        self._start = start

    @property
    def table_name(self):
        """Gets the table_name of this ListJobsRequest.

        :return: The table_name of this ListJobsRequest.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this ListJobsRequest.

        :param table_name: The table_name of this ListJobsRequest.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def tags(self):
        """Gets the tags of this ListJobsRequest.

        指定作业标签作为过滤条件，支持多标签过滤。格式为“key=value”，如：GET /v1.0/{project_id}/jobs?tags=k1%3Dv1，“=”需要转义为“%3D”，“k1”为标签键，“v1”为标签值。

        :return: The tags of this ListJobsRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListJobsRequest.

        指定作业标签作为过滤条件，支持多标签过滤。格式为“key=value”，如：GET /v1.0/{project_id}/jobs?tags=k1%3Dv1，“=”需要转义为“%3D”，“k1”为标签键，“v1”为标签值。

        :param tags: The tags of this ListJobsRequest.
        :type tags: str
        """
        self._tags = tags

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
        if not isinstance(other, ListJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
