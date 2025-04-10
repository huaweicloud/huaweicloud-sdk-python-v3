# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScheduledTaskHistoryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'id': 'str',
        'region': 'str',
        'status': 'str',
        'started_start_time': 'int',
        'started_end_time': 'int',
        'finished_start_time': 'int',
        'finished_end_time': 'int',
        'marker': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'id': 'id',
        'region': 'region',
        'status': 'status',
        'started_start_time': 'started_start_time',
        'started_end_time': 'started_end_time',
        'finished_start_time': 'finished_start_time',
        'finished_end_time': 'finished_end_time',
        'marker': 'marker',
        'offset': 'offset',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, task_id=None, id=None, region=None, status=None, started_start_time=None, started_end_time=None, finished_start_time=None, finished_end_time=None, marker=None, offset=None, limit=None, sort_key=None, sort_dir=None):
        r"""ListScheduledTaskHistoryRequest

        The model defined in huaweicloud sdk

        :param task_id: ID of ScheduledTask
        :type task_id: str
        :param id: 工单ID
        :type id: str
        :param region: 区域
        :type region: str
        :param status: 状态
        :type status: str
        :param started_start_time: 开始时间参数的查询开始区间时间戳
        :type started_start_time: int
        :param started_end_time: 开始时间参数的查询结束区间时间戳
        :type started_end_time: int
        :param finished_start_time: 结束时间参数的查询开始区间时间戳
        :type finished_start_time: int
        :param finished_end_time: 结束时间参数的查询结束区间时间戳
        :type finished_end_time: int
        :param marker: 上一页数据的最后一条记录的id
        :type marker: str
        :param offset: 分页指针
        :type offset: int
        :param limit: 每页数量
        :type limit: int
        :param sort_key: 排序字段名：支持 started_time,finished_time
        :type sort_key: str
        :param sort_dir: 排序方式，asc升序，desc降序
        :type sort_dir: str
        """
        
        

        self._task_id = None
        self._id = None
        self._region = None
        self._status = None
        self._started_start_time = None
        self._started_end_time = None
        self._finished_start_time = None
        self._finished_end_time = None
        self._marker = None
        self._offset = None
        self._limit = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        self.task_id = task_id
        if id is not None:
            self.id = id
        if region is not None:
            self.region = region
        if status is not None:
            self.status = status
        if started_start_time is not None:
            self.started_start_time = started_start_time
        if started_end_time is not None:
            self.started_end_time = started_end_time
        if finished_start_time is not None:
            self.finished_start_time = finished_start_time
        if finished_end_time is not None:
            self.finished_end_time = finished_end_time
        if marker is not None:
            self.marker = marker
        if offset is not None:
            self.offset = offset
        self.limit = limit
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def task_id(self):
        r"""Gets the task_id of this ListScheduledTaskHistoryRequest.

        ID of ScheduledTask

        :return: The task_id of this ListScheduledTaskHistoryRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ListScheduledTaskHistoryRequest.

        ID of ScheduledTask

        :param task_id: The task_id of this ListScheduledTaskHistoryRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def id(self):
        r"""Gets the id of this ListScheduledTaskHistoryRequest.

        工单ID

        :return: The id of this ListScheduledTaskHistoryRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListScheduledTaskHistoryRequest.

        工单ID

        :param id: The id of this ListScheduledTaskHistoryRequest.
        :type id: str
        """
        self._id = id

    @property
    def region(self):
        r"""Gets the region of this ListScheduledTaskHistoryRequest.

        区域

        :return: The region of this ListScheduledTaskHistoryRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListScheduledTaskHistoryRequest.

        区域

        :param region: The region of this ListScheduledTaskHistoryRequest.
        :type region: str
        """
        self._region = region

    @property
    def status(self):
        r"""Gets the status of this ListScheduledTaskHistoryRequest.

        状态

        :return: The status of this ListScheduledTaskHistoryRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListScheduledTaskHistoryRequest.

        状态

        :param status: The status of this ListScheduledTaskHistoryRequest.
        :type status: str
        """
        self._status = status

    @property
    def started_start_time(self):
        r"""Gets the started_start_time of this ListScheduledTaskHistoryRequest.

        开始时间参数的查询开始区间时间戳

        :return: The started_start_time of this ListScheduledTaskHistoryRequest.
        :rtype: int
        """
        return self._started_start_time

    @started_start_time.setter
    def started_start_time(self, started_start_time):
        r"""Sets the started_start_time of this ListScheduledTaskHistoryRequest.

        开始时间参数的查询开始区间时间戳

        :param started_start_time: The started_start_time of this ListScheduledTaskHistoryRequest.
        :type started_start_time: int
        """
        self._started_start_time = started_start_time

    @property
    def started_end_time(self):
        r"""Gets the started_end_time of this ListScheduledTaskHistoryRequest.

        开始时间参数的查询结束区间时间戳

        :return: The started_end_time of this ListScheduledTaskHistoryRequest.
        :rtype: int
        """
        return self._started_end_time

    @started_end_time.setter
    def started_end_time(self, started_end_time):
        r"""Sets the started_end_time of this ListScheduledTaskHistoryRequest.

        开始时间参数的查询结束区间时间戳

        :param started_end_time: The started_end_time of this ListScheduledTaskHistoryRequest.
        :type started_end_time: int
        """
        self._started_end_time = started_end_time

    @property
    def finished_start_time(self):
        r"""Gets the finished_start_time of this ListScheduledTaskHistoryRequest.

        结束时间参数的查询开始区间时间戳

        :return: The finished_start_time of this ListScheduledTaskHistoryRequest.
        :rtype: int
        """
        return self._finished_start_time

    @finished_start_time.setter
    def finished_start_time(self, finished_start_time):
        r"""Sets the finished_start_time of this ListScheduledTaskHistoryRequest.

        结束时间参数的查询开始区间时间戳

        :param finished_start_time: The finished_start_time of this ListScheduledTaskHistoryRequest.
        :type finished_start_time: int
        """
        self._finished_start_time = finished_start_time

    @property
    def finished_end_time(self):
        r"""Gets the finished_end_time of this ListScheduledTaskHistoryRequest.

        结束时间参数的查询结束区间时间戳

        :return: The finished_end_time of this ListScheduledTaskHistoryRequest.
        :rtype: int
        """
        return self._finished_end_time

    @finished_end_time.setter
    def finished_end_time(self, finished_end_time):
        r"""Sets the finished_end_time of this ListScheduledTaskHistoryRequest.

        结束时间参数的查询结束区间时间戳

        :param finished_end_time: The finished_end_time of this ListScheduledTaskHistoryRequest.
        :type finished_end_time: int
        """
        self._finished_end_time = finished_end_time

    @property
    def marker(self):
        r"""Gets the marker of this ListScheduledTaskHistoryRequest.

        上一页数据的最后一条记录的id

        :return: The marker of this ListScheduledTaskHistoryRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListScheduledTaskHistoryRequest.

        上一页数据的最后一条记录的id

        :param marker: The marker of this ListScheduledTaskHistoryRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def offset(self):
        r"""Gets the offset of this ListScheduledTaskHistoryRequest.

        分页指针

        :return: The offset of this ListScheduledTaskHistoryRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListScheduledTaskHistoryRequest.

        分页指针

        :param offset: The offset of this ListScheduledTaskHistoryRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListScheduledTaskHistoryRequest.

        每页数量

        :return: The limit of this ListScheduledTaskHistoryRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListScheduledTaskHistoryRequest.

        每页数量

        :param limit: The limit of this ListScheduledTaskHistoryRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListScheduledTaskHistoryRequest.

        排序字段名：支持 started_time,finished_time

        :return: The sort_key of this ListScheduledTaskHistoryRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListScheduledTaskHistoryRequest.

        排序字段名：支持 started_time,finished_time

        :param sort_key: The sort_key of this ListScheduledTaskHistoryRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListScheduledTaskHistoryRequest.

        排序方式，asc升序，desc降序

        :return: The sort_dir of this ListScheduledTaskHistoryRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListScheduledTaskHistoryRequest.

        排序方式，asc升序，desc降序

        :param sort_dir: The sort_dir of this ListScheduledTaskHistoryRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

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
        if not isinstance(other, ListScheduledTaskHistoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
