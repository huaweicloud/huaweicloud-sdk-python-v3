# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRunsRequest:

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
        'start_time': 'str',
        'end_time': 'str',
        'sql_pattern': 'str',
        'sql_type': 'str',
        'job_type': 'str',
        'status': 'str',
        'order_by': 'str',
        'order': 'str',
        'job_name': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'sql_pattern': 'sql_pattern',
        'sql_type': 'sql_type',
        'job_type': 'job_type',
        'status': 'status',
        'order_by': 'order_by',
        'order': 'order',
        'job_name': 'job_name'
    }

    def __init__(self, offset=None, limit=None, start_time=None, end_time=None, sql_pattern=None, sql_type=None, job_type=None, status=None, order_by=None, order=None, job_name=None):
        """ListRunsRequest

        The model defined in huaweicloud sdk

        :param offset: 当前偏移量，默认为0。
        :type offset: int
        :param limit: 每页显示的最大作业个数，范围: [1, 100]。默认值：10。
        :type limit: int
        :param start_time: 用于查询开始时间在该时间点之后的作业。时间格式为ISO日期时间格式yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS。
        :type start_time: str
        :param end_time: 用于查询开始时间在该时间点之前的作业。时间格式为ISO日期时间格式yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS。
        :type end_time: str
        :param sql_pattern: 仅当作业类型为SqlJob时可用。指定sql片段作为作业过滤条件，不区分大小写。
        :type sql_pattern: str
        :param sql_type: 仅当作业类型为SqlJob时可用。SQL作业类型。DDL, DCL, IMPORT, EXPORT, QUERY, INSERT, SELECT, DATA_MIGRATION, ANALYZE, OBS_SELECT, COMPLEX
        :type sql_type: str
        :param job_type: 作业类型。目前仅支持SqlJob
        :type job_type: str
        :param status: 此作业的当前状态，包含提交（LAUNCHING）、运行中（RUNNING）、完成（FINISHED）、失败（FAILED）、取消（CANCELLED）
        :type status: str
        :param order_by: 指定作业排序字段，默认为从created_time（作业提交时间），支持duration（作业运行时长）、created_time（作业提交时间） 、job_name（作业名称）三种排序字段。
        :type order_by: str
        :param order: 指定作业排序的升降序，默认为desc（降序），支持asc（升序）、desc（降序）两种排序方式。
        :type order: str
        :param job_name: 作业名称
        :type job_name: str
        """
        
        

        self._offset = None
        self._limit = None
        self._start_time = None
        self._end_time = None
        self._sql_pattern = None
        self._sql_type = None
        self._job_type = None
        self._status = None
        self._order_by = None
        self._order = None
        self._job_name = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if sql_pattern is not None:
            self.sql_pattern = sql_pattern
        if sql_type is not None:
            self.sql_type = sql_type
        if job_type is not None:
            self.job_type = job_type
        if status is not None:
            self.status = status
        if order_by is not None:
            self.order_by = order_by
        if order is not None:
            self.order = order
        if job_name is not None:
            self.job_name = job_name

    @property
    def offset(self):
        """Gets the offset of this ListRunsRequest.

        当前偏移量，默认为0。

        :return: The offset of this ListRunsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListRunsRequest.

        当前偏移量，默认为0。

        :param offset: The offset of this ListRunsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListRunsRequest.

        每页显示的最大作业个数，范围: [1, 100]。默认值：10。

        :return: The limit of this ListRunsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRunsRequest.

        每页显示的最大作业个数，范围: [1, 100]。默认值：10。

        :param limit: The limit of this ListRunsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def start_time(self):
        """Gets the start_time of this ListRunsRequest.

        用于查询开始时间在该时间点之后的作业。时间格式为ISO日期时间格式yyyy-MM-dd'T'HH:mm:ss.SSS。

        :return: The start_time of this ListRunsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListRunsRequest.

        用于查询开始时间在该时间点之后的作业。时间格式为ISO日期时间格式yyyy-MM-dd'T'HH:mm:ss.SSS。

        :param start_time: The start_time of this ListRunsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListRunsRequest.

        用于查询开始时间在该时间点之前的作业。时间格式为ISO日期时间格式yyyy-MM-dd'T'HH:mm:ss.SSS。

        :return: The end_time of this ListRunsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListRunsRequest.

        用于查询开始时间在该时间点之前的作业。时间格式为ISO日期时间格式yyyy-MM-dd'T'HH:mm:ss.SSS。

        :param end_time: The end_time of this ListRunsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def sql_pattern(self):
        """Gets the sql_pattern of this ListRunsRequest.

        仅当作业类型为SqlJob时可用。指定sql片段作为作业过滤条件，不区分大小写。

        :return: The sql_pattern of this ListRunsRequest.
        :rtype: str
        """
        return self._sql_pattern

    @sql_pattern.setter
    def sql_pattern(self, sql_pattern):
        """Sets the sql_pattern of this ListRunsRequest.

        仅当作业类型为SqlJob时可用。指定sql片段作为作业过滤条件，不区分大小写。

        :param sql_pattern: The sql_pattern of this ListRunsRequest.
        :type sql_pattern: str
        """
        self._sql_pattern = sql_pattern

    @property
    def sql_type(self):
        """Gets the sql_type of this ListRunsRequest.

        仅当作业类型为SqlJob时可用。SQL作业类型。DDL, DCL, IMPORT, EXPORT, QUERY, INSERT, SELECT, DATA_MIGRATION, ANALYZE, OBS_SELECT, COMPLEX

        :return: The sql_type of this ListRunsRequest.
        :rtype: str
        """
        return self._sql_type

    @sql_type.setter
    def sql_type(self, sql_type):
        """Sets the sql_type of this ListRunsRequest.

        仅当作业类型为SqlJob时可用。SQL作业类型。DDL, DCL, IMPORT, EXPORT, QUERY, INSERT, SELECT, DATA_MIGRATION, ANALYZE, OBS_SELECT, COMPLEX

        :param sql_type: The sql_type of this ListRunsRequest.
        :type sql_type: str
        """
        self._sql_type = sql_type

    @property
    def job_type(self):
        """Gets the job_type of this ListRunsRequest.

        作业类型。目前仅支持SqlJob

        :return: The job_type of this ListRunsRequest.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this ListRunsRequest.

        作业类型。目前仅支持SqlJob

        :param job_type: The job_type of this ListRunsRequest.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def status(self):
        """Gets the status of this ListRunsRequest.

        此作业的当前状态，包含提交（LAUNCHING）、运行中（RUNNING）、完成（FINISHED）、失败（FAILED）、取消（CANCELLED）

        :return: The status of this ListRunsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListRunsRequest.

        此作业的当前状态，包含提交（LAUNCHING）、运行中（RUNNING）、完成（FINISHED）、失败（FAILED）、取消（CANCELLED）

        :param status: The status of this ListRunsRequest.
        :type status: str
        """
        self._status = status

    @property
    def order_by(self):
        """Gets the order_by of this ListRunsRequest.

        指定作业排序字段，默认为从created_time（作业提交时间），支持duration（作业运行时长）、created_time（作业提交时间） 、job_name（作业名称）三种排序字段。

        :return: The order_by of this ListRunsRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this ListRunsRequest.

        指定作业排序字段，默认为从created_time（作业提交时间），支持duration（作业运行时长）、created_time（作业提交时间） 、job_name（作业名称）三种排序字段。

        :param order_by: The order_by of this ListRunsRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def order(self):
        """Gets the order of this ListRunsRequest.

        指定作业排序的升降序，默认为desc（降序），支持asc（升序）、desc（降序）两种排序方式。

        :return: The order of this ListRunsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ListRunsRequest.

        指定作业排序的升降序，默认为desc（降序），支持asc（升序）、desc（降序）两种排序方式。

        :param order: The order of this ListRunsRequest.
        :type order: str
        """
        self._order = order

    @property
    def job_name(self):
        """Gets the job_name of this ListRunsRequest.

        作业名称

        :return: The job_name of this ListRunsRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this ListRunsRequest.

        作业名称

        :param job_name: The job_name of this ListRunsRequest.
        :type job_name: str
        """
        self._job_name = job_name

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
        if not isinstance(other, ListRunsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
