# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBatchJobsRequest:

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
        'has_schedule': 'bool',
        'job_name': 'str',
        'schedule_status': 'str',
        'order_by': 'str',
        'order': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'has_schedule': 'has_schedule',
        'job_name': 'job_name',
        'schedule_status': 'schedule_status',
        'order_by': 'order_by',
        'order': 'order'
    }

    def __init__(self, offset=None, limit=None, has_schedule=None, job_name=None, schedule_status=None, order_by=None, order=None):
        """ListBatchJobsRequest

        The model defined in huaweicloud sdk

        :param offset: 当前偏移量，默认为0。
        :type offset: int
        :param limit: 每页显示的最大作业个数，范围: [1, 100]。默认值：10。
        :type limit: int
        :param has_schedule: 是否定时作业。true：定时作业：false：不是定时作业。为空时：所有作业。
        :type has_schedule: bool
        :param job_name: 作业名称
        :type job_name: str
        :param schedule_status: 调度状态。1:NORMAL, 2:PAUSED, 3:COMPLETE, 4:ERROR, 5:BLOCKED
        :type schedule_status: str
        :param order_by: 指定作业排序字段，默认为created_time（作业创建时间），支持created_time(作业创建时间)、modified_time（作业更新时间） 、job_name（作业名称）三种排序字段。
        :type order_by: str
        :param order: 指定作业排序的升降序，默认为desc（降序），支持asc（升序）、desc（降序）两种排序方式。
        :type order: str
        """
        
        

        self._offset = None
        self._limit = None
        self._has_schedule = None
        self._job_name = None
        self._schedule_status = None
        self._order_by = None
        self._order = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if has_schedule is not None:
            self.has_schedule = has_schedule
        if job_name is not None:
            self.job_name = job_name
        if schedule_status is not None:
            self.schedule_status = schedule_status
        if order_by is not None:
            self.order_by = order_by
        if order is not None:
            self.order = order

    @property
    def offset(self):
        """Gets the offset of this ListBatchJobsRequest.

        当前偏移量，默认为0。

        :return: The offset of this ListBatchJobsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListBatchJobsRequest.

        当前偏移量，默认为0。

        :param offset: The offset of this ListBatchJobsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListBatchJobsRequest.

        每页显示的最大作业个数，范围: [1, 100]。默认值：10。

        :return: The limit of this ListBatchJobsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListBatchJobsRequest.

        每页显示的最大作业个数，范围: [1, 100]。默认值：10。

        :param limit: The limit of this ListBatchJobsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def has_schedule(self):
        """Gets the has_schedule of this ListBatchJobsRequest.

        是否定时作业。true：定时作业：false：不是定时作业。为空时：所有作业。

        :return: The has_schedule of this ListBatchJobsRequest.
        :rtype: bool
        """
        return self._has_schedule

    @has_schedule.setter
    def has_schedule(self, has_schedule):
        """Sets the has_schedule of this ListBatchJobsRequest.

        是否定时作业。true：定时作业：false：不是定时作业。为空时：所有作业。

        :param has_schedule: The has_schedule of this ListBatchJobsRequest.
        :type has_schedule: bool
        """
        self._has_schedule = has_schedule

    @property
    def job_name(self):
        """Gets the job_name of this ListBatchJobsRequest.

        作业名称

        :return: The job_name of this ListBatchJobsRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this ListBatchJobsRequest.

        作业名称

        :param job_name: The job_name of this ListBatchJobsRequest.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def schedule_status(self):
        """Gets the schedule_status of this ListBatchJobsRequest.

        调度状态。1:NORMAL, 2:PAUSED, 3:COMPLETE, 4:ERROR, 5:BLOCKED

        :return: The schedule_status of this ListBatchJobsRequest.
        :rtype: str
        """
        return self._schedule_status

    @schedule_status.setter
    def schedule_status(self, schedule_status):
        """Sets the schedule_status of this ListBatchJobsRequest.

        调度状态。1:NORMAL, 2:PAUSED, 3:COMPLETE, 4:ERROR, 5:BLOCKED

        :param schedule_status: The schedule_status of this ListBatchJobsRequest.
        :type schedule_status: str
        """
        self._schedule_status = schedule_status

    @property
    def order_by(self):
        """Gets the order_by of this ListBatchJobsRequest.

        指定作业排序字段，默认为created_time（作业创建时间），支持created_time(作业创建时间)、modified_time（作业更新时间） 、job_name（作业名称）三种排序字段。

        :return: The order_by of this ListBatchJobsRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this ListBatchJobsRequest.

        指定作业排序字段，默认为created_time（作业创建时间），支持created_time(作业创建时间)、modified_time（作业更新时间） 、job_name（作业名称）三种排序字段。

        :param order_by: The order_by of this ListBatchJobsRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def order(self):
        """Gets the order of this ListBatchJobsRequest.

        指定作业排序的升降序，默认为desc（降序），支持asc（升序）、desc（降序）两种排序方式。

        :return: The order of this ListBatchJobsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ListBatchJobsRequest.

        指定作业排序的升降序，默认为desc（降序），支持asc（升序）、desc（降序）两种排序方式。

        :param order: The order of this ListBatchJobsRequest.
        :type order: str
        """
        self._order = order

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
        if not isinstance(other, ListBatchJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
