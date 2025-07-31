# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTasksRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_type': 'str',
        'task_id': 'str',
        'task_name': 'str',
        'start_create_time': 'int',
        'end_create_time': 'int',
        'trigger_type': 'str',
        'task_status': 'str',
        'sort_key': 'str',
        'sort_dir': 'str',
        'cluster_scan_info': 'ListTasksRequestBodyClusterScanInfo',
        'iac_scan_info': 'ListTasksRequestBodyIacScanInfo'
    }

    attribute_map = {
        'task_type': 'task_type',
        'task_id': 'task_id',
        'task_name': 'task_name',
        'start_create_time': 'start_create_time',
        'end_create_time': 'end_create_time',
        'trigger_type': 'trigger_type',
        'task_status': 'task_status',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'cluster_scan_info': 'cluster_scan_info',
        'iac_scan_info': 'iac_scan_info'
    }

    def __init__(self, task_type=None, task_id=None, task_name=None, start_create_time=None, end_create_time=None, trigger_type=None, task_status=None, sort_key=None, sort_dir=None, cluster_scan_info=None, iac_scan_info=None):
        r"""ListTasksRequestBody

        The model defined in huaweicloud sdk

        :param task_type: 任务类型，包含如下   - cluster_scan：集群扫描   - iac_scan：iac扫描
        :type task_type: str
        :param task_id: 本次创建任务的id
        :type task_id: str
        :param task_name: 模糊匹配任务名称
        :type task_name: str
        :param start_create_time: 按任务创建时间范围查询时的起始时间
        :type start_create_time: int
        :param end_create_time: 按任务创建时间范围查询时的结束时间
        :type end_create_time: int
        :param trigger_type: 任务触发类型，包含如下   - manual：手动创建的任务   - schedule：定时任务
        :type trigger_type: str
        :param task_status: 任务状态，包含如下   - ready：等待执行   - running：运行中   - finished：任务结束
        :type task_status: str
        :param sort_key: 排序字段，包含如下   - start_time：任务开始时间
        :type sort_key: str
        :param sort_dir: 排序方式，包含如下   - desc：降序   - asc: 升序
        :type sort_dir: str
        :param cluster_scan_info: 
        :type cluster_scan_info: :class:`huaweicloudsdkhss.v5.ListTasksRequestBodyClusterScanInfo`
        :param iac_scan_info: 
        :type iac_scan_info: :class:`huaweicloudsdkhss.v5.ListTasksRequestBodyIacScanInfo`
        """
        
        

        self._task_type = None
        self._task_id = None
        self._task_name = None
        self._start_create_time = None
        self._end_create_time = None
        self._trigger_type = None
        self._task_status = None
        self._sort_key = None
        self._sort_dir = None
        self._cluster_scan_info = None
        self._iac_scan_info = None
        self.discriminator = None

        self.task_type = task_type
        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if start_create_time is not None:
            self.start_create_time = start_create_time
        if end_create_time is not None:
            self.end_create_time = end_create_time
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if task_status is not None:
            self.task_status = task_status
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if cluster_scan_info is not None:
            self.cluster_scan_info = cluster_scan_info
        if iac_scan_info is not None:
            self.iac_scan_info = iac_scan_info

    @property
    def task_type(self):
        r"""Gets the task_type of this ListTasksRequestBody.

        任务类型，包含如下   - cluster_scan：集群扫描   - iac_scan：iac扫描

        :return: The task_type of this ListTasksRequestBody.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ListTasksRequestBody.

        任务类型，包含如下   - cluster_scan：集群扫描   - iac_scan：iac扫描

        :param task_type: The task_type of this ListTasksRequestBody.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def task_id(self):
        r"""Gets the task_id of this ListTasksRequestBody.

        本次创建任务的id

        :return: The task_id of this ListTasksRequestBody.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ListTasksRequestBody.

        本次创建任务的id

        :param task_id: The task_id of this ListTasksRequestBody.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        r"""Gets the task_name of this ListTasksRequestBody.

        模糊匹配任务名称

        :return: The task_name of this ListTasksRequestBody.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this ListTasksRequestBody.

        模糊匹配任务名称

        :param task_name: The task_name of this ListTasksRequestBody.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def start_create_time(self):
        r"""Gets the start_create_time of this ListTasksRequestBody.

        按任务创建时间范围查询时的起始时间

        :return: The start_create_time of this ListTasksRequestBody.
        :rtype: int
        """
        return self._start_create_time

    @start_create_time.setter
    def start_create_time(self, start_create_time):
        r"""Sets the start_create_time of this ListTasksRequestBody.

        按任务创建时间范围查询时的起始时间

        :param start_create_time: The start_create_time of this ListTasksRequestBody.
        :type start_create_time: int
        """
        self._start_create_time = start_create_time

    @property
    def end_create_time(self):
        r"""Gets the end_create_time of this ListTasksRequestBody.

        按任务创建时间范围查询时的结束时间

        :return: The end_create_time of this ListTasksRequestBody.
        :rtype: int
        """
        return self._end_create_time

    @end_create_time.setter
    def end_create_time(self, end_create_time):
        r"""Sets the end_create_time of this ListTasksRequestBody.

        按任务创建时间范围查询时的结束时间

        :param end_create_time: The end_create_time of this ListTasksRequestBody.
        :type end_create_time: int
        """
        self._end_create_time = end_create_time

    @property
    def trigger_type(self):
        r"""Gets the trigger_type of this ListTasksRequestBody.

        任务触发类型，包含如下   - manual：手动创建的任务   - schedule：定时任务

        :return: The trigger_type of this ListTasksRequestBody.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        r"""Sets the trigger_type of this ListTasksRequestBody.

        任务触发类型，包含如下   - manual：手动创建的任务   - schedule：定时任务

        :param trigger_type: The trigger_type of this ListTasksRequestBody.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def task_status(self):
        r"""Gets the task_status of this ListTasksRequestBody.

        任务状态，包含如下   - ready：等待执行   - running：运行中   - finished：任务结束

        :return: The task_status of this ListTasksRequestBody.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        r"""Sets the task_status of this ListTasksRequestBody.

        任务状态，包含如下   - ready：等待执行   - running：运行中   - finished：任务结束

        :param task_status: The task_status of this ListTasksRequestBody.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListTasksRequestBody.

        排序字段，包含如下   - start_time：任务开始时间

        :return: The sort_key of this ListTasksRequestBody.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListTasksRequestBody.

        排序字段，包含如下   - start_time：任务开始时间

        :param sort_key: The sort_key of this ListTasksRequestBody.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListTasksRequestBody.

        排序方式，包含如下   - desc：降序   - asc: 升序

        :return: The sort_dir of this ListTasksRequestBody.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListTasksRequestBody.

        排序方式，包含如下   - desc：降序   - asc: 升序

        :param sort_dir: The sort_dir of this ListTasksRequestBody.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def cluster_scan_info(self):
        r"""Gets the cluster_scan_info of this ListTasksRequestBody.

        :return: The cluster_scan_info of this ListTasksRequestBody.
        :rtype: :class:`huaweicloudsdkhss.v5.ListTasksRequestBodyClusterScanInfo`
        """
        return self._cluster_scan_info

    @cluster_scan_info.setter
    def cluster_scan_info(self, cluster_scan_info):
        r"""Sets the cluster_scan_info of this ListTasksRequestBody.

        :param cluster_scan_info: The cluster_scan_info of this ListTasksRequestBody.
        :type cluster_scan_info: :class:`huaweicloudsdkhss.v5.ListTasksRequestBodyClusterScanInfo`
        """
        self._cluster_scan_info = cluster_scan_info

    @property
    def iac_scan_info(self):
        r"""Gets the iac_scan_info of this ListTasksRequestBody.

        :return: The iac_scan_info of this ListTasksRequestBody.
        :rtype: :class:`huaweicloudsdkhss.v5.ListTasksRequestBodyIacScanInfo`
        """
        return self._iac_scan_info

    @iac_scan_info.setter
    def iac_scan_info(self, iac_scan_info):
        r"""Sets the iac_scan_info of this ListTasksRequestBody.

        :param iac_scan_info: The iac_scan_info of this ListTasksRequestBody.
        :type iac_scan_info: :class:`huaweicloudsdkhss.v5.ListTasksRequestBodyIacScanInfo`
        """
        self._iac_scan_info = iac_scan_info

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
        if not isinstance(other, ListTasksRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
