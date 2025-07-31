# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTasksResponseInfoDataList:

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
        'task_type': 'str',
        'task_name': 'str',
        'trigger_type': 'str',
        'task_status': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'estimated_time': 'int',
        'cluster_scan_info': 'ListTasksResponseInfoClusterScanInfo',
        'iac_scan_info': 'ListTasksResponseInfoIacScanInfo'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_type': 'task_type',
        'task_name': 'task_name',
        'trigger_type': 'trigger_type',
        'task_status': 'task_status',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'estimated_time': 'estimated_time',
        'cluster_scan_info': 'cluster_scan_info',
        'iac_scan_info': 'iac_scan_info'
    }

    def __init__(self, task_id=None, task_type=None, task_name=None, trigger_type=None, task_status=None, start_time=None, end_time=None, estimated_time=None, cluster_scan_info=None, iac_scan_info=None):
        r"""ListTasksResponseInfoDataList

        The model defined in huaweicloud sdk

        :param task_id: 本次创建任务的id
        :type task_id: str
        :param task_type: 任务类型，包含如下   - cluster_scan：集群扫描   - iac_scan：iac扫描
        :type task_type: str
        :param task_name: 任务名称
        :type task_name: str
        :param trigger_type: 任务触发类型，包含如下   - manual：手动创建的任务   - schedule：定时任务
        :type trigger_type: str
        :param task_status: 任务状态，包含如下   - ready：等待执行   - running：运行中   - finished：任务结束
        :type task_status: str
        :param start_time: 任务开始的时间
        :type start_time: int
        :param end_time: 任务结束的时间
        :type end_time: int
        :param estimated_time: 预计当前任务结束还需要的时间，单位为分钟
        :type estimated_time: int
        :param cluster_scan_info: 
        :type cluster_scan_info: :class:`huaweicloudsdkhss.v5.ListTasksResponseInfoClusterScanInfo`
        :param iac_scan_info: 
        :type iac_scan_info: :class:`huaweicloudsdkhss.v5.ListTasksResponseInfoIacScanInfo`
        """
        
        

        self._task_id = None
        self._task_type = None
        self._task_name = None
        self._trigger_type = None
        self._task_status = None
        self._start_time = None
        self._end_time = None
        self._estimated_time = None
        self._cluster_scan_info = None
        self._iac_scan_info = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_type is not None:
            self.task_type = task_type
        if task_name is not None:
            self.task_name = task_name
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if task_status is not None:
            self.task_status = task_status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if estimated_time is not None:
            self.estimated_time = estimated_time
        if cluster_scan_info is not None:
            self.cluster_scan_info = cluster_scan_info
        if iac_scan_info is not None:
            self.iac_scan_info = iac_scan_info

    @property
    def task_id(self):
        r"""Gets the task_id of this ListTasksResponseInfoDataList.

        本次创建任务的id

        :return: The task_id of this ListTasksResponseInfoDataList.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ListTasksResponseInfoDataList.

        本次创建任务的id

        :param task_id: The task_id of this ListTasksResponseInfoDataList.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_type(self):
        r"""Gets the task_type of this ListTasksResponseInfoDataList.

        任务类型，包含如下   - cluster_scan：集群扫描   - iac_scan：iac扫描

        :return: The task_type of this ListTasksResponseInfoDataList.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ListTasksResponseInfoDataList.

        任务类型，包含如下   - cluster_scan：集群扫描   - iac_scan：iac扫描

        :param task_type: The task_type of this ListTasksResponseInfoDataList.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def task_name(self):
        r"""Gets the task_name of this ListTasksResponseInfoDataList.

        任务名称

        :return: The task_name of this ListTasksResponseInfoDataList.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this ListTasksResponseInfoDataList.

        任务名称

        :param task_name: The task_name of this ListTasksResponseInfoDataList.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def trigger_type(self):
        r"""Gets the trigger_type of this ListTasksResponseInfoDataList.

        任务触发类型，包含如下   - manual：手动创建的任务   - schedule：定时任务

        :return: The trigger_type of this ListTasksResponseInfoDataList.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        r"""Sets the trigger_type of this ListTasksResponseInfoDataList.

        任务触发类型，包含如下   - manual：手动创建的任务   - schedule：定时任务

        :param trigger_type: The trigger_type of this ListTasksResponseInfoDataList.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def task_status(self):
        r"""Gets the task_status of this ListTasksResponseInfoDataList.

        任务状态，包含如下   - ready：等待执行   - running：运行中   - finished：任务结束

        :return: The task_status of this ListTasksResponseInfoDataList.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        r"""Sets the task_status of this ListTasksResponseInfoDataList.

        任务状态，包含如下   - ready：等待执行   - running：运行中   - finished：任务结束

        :param task_status: The task_status of this ListTasksResponseInfoDataList.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def start_time(self):
        r"""Gets the start_time of this ListTasksResponseInfoDataList.

        任务开始的时间

        :return: The start_time of this ListTasksResponseInfoDataList.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListTasksResponseInfoDataList.

        任务开始的时间

        :param start_time: The start_time of this ListTasksResponseInfoDataList.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListTasksResponseInfoDataList.

        任务结束的时间

        :return: The end_time of this ListTasksResponseInfoDataList.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListTasksResponseInfoDataList.

        任务结束的时间

        :param end_time: The end_time of this ListTasksResponseInfoDataList.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def estimated_time(self):
        r"""Gets the estimated_time of this ListTasksResponseInfoDataList.

        预计当前任务结束还需要的时间，单位为分钟

        :return: The estimated_time of this ListTasksResponseInfoDataList.
        :rtype: int
        """
        return self._estimated_time

    @estimated_time.setter
    def estimated_time(self, estimated_time):
        r"""Sets the estimated_time of this ListTasksResponseInfoDataList.

        预计当前任务结束还需要的时间，单位为分钟

        :param estimated_time: The estimated_time of this ListTasksResponseInfoDataList.
        :type estimated_time: int
        """
        self._estimated_time = estimated_time

    @property
    def cluster_scan_info(self):
        r"""Gets the cluster_scan_info of this ListTasksResponseInfoDataList.

        :return: The cluster_scan_info of this ListTasksResponseInfoDataList.
        :rtype: :class:`huaweicloudsdkhss.v5.ListTasksResponseInfoClusterScanInfo`
        """
        return self._cluster_scan_info

    @cluster_scan_info.setter
    def cluster_scan_info(self, cluster_scan_info):
        r"""Sets the cluster_scan_info of this ListTasksResponseInfoDataList.

        :param cluster_scan_info: The cluster_scan_info of this ListTasksResponseInfoDataList.
        :type cluster_scan_info: :class:`huaweicloudsdkhss.v5.ListTasksResponseInfoClusterScanInfo`
        """
        self._cluster_scan_info = cluster_scan_info

    @property
    def iac_scan_info(self):
        r"""Gets the iac_scan_info of this ListTasksResponseInfoDataList.

        :return: The iac_scan_info of this ListTasksResponseInfoDataList.
        :rtype: :class:`huaweicloudsdkhss.v5.ListTasksResponseInfoIacScanInfo`
        """
        return self._iac_scan_info

    @iac_scan_info.setter
    def iac_scan_info(self, iac_scan_info):
        r"""Sets the iac_scan_info of this ListTasksResponseInfoDataList.

        :param iac_scan_info: The iac_scan_info of this ListTasksResponseInfoDataList.
        :type iac_scan_info: :class:`huaweicloudsdkhss.v5.ListTasksResponseInfoIacScanInfo`
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
        if not isinstance(other, ListTasksResponseInfoDataList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
