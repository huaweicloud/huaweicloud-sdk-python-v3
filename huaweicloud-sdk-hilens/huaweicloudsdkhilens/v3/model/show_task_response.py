# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'timestamp': 'str',
        'description': 'str',
        'streams': 'list[TaskStream]',
        'ok_pod_number': 'int',
        'cur_pod_number': 'int',
        'sum_pod_number': 'int',
        'fail_pod_number': 'int',
        'pending_pod_number': 'int',
        'task_status': 'list[TaskStatus]',
        'task_id': 'str',
        'user_task_id': 'str',
        'start_time_info': 'StartTimeInfo',
        'source_usage_estimate': 'TaskSourceUsageEstimate'
    }

    attribute_map = {
        'name': 'name',
        'timestamp': 'timestamp',
        'description': 'description',
        'streams': 'streams',
        'ok_pod_number': 'ok_pod_number',
        'cur_pod_number': 'cur_pod_number',
        'sum_pod_number': 'sum_pod_number',
        'fail_pod_number': 'fail_pod_number',
        'pending_pod_number': 'pending_pod_number',
        'task_status': 'task_status',
        'task_id': 'task_id',
        'user_task_id': 'user_task_id',
        'start_time_info': 'start_time_info',
        'source_usage_estimate': 'source_usage_estimate'
    }

    def __init__(self, name=None, timestamp=None, description=None, streams=None, ok_pod_number=None, cur_pod_number=None, sum_pod_number=None, fail_pod_number=None, pending_pod_number=None, task_status=None, task_id=None, user_task_id=None, start_time_info=None, source_usage_estimate=None):
        """ShowTaskResponse

        The model defined in huaweicloud sdk

        :param name: 作业名称
        :type name: str
        :param timestamp: 作业创建时间
        :type timestamp: str
        :param description: 作业描述
        :type description: str
        :param streams: 作业流详情
        :type streams: list[:class:`huaweicloudsdkhilens.v3.TaskStream`]
        :param ok_pod_number: 在实例上运行成功的作业数
        :type ok_pod_number: int
        :param cur_pod_number: 在实例上正在运行的作业数
        :type cur_pod_number: int
        :param sum_pod_number: 在实例上运行过的作业总数
        :type sum_pod_number: int
        :param fail_pod_number: 在实例上运行失败的作业数
        :type fail_pod_number: int
        :param pending_pod_number: 在实例上等待运行的作业数
        :type pending_pod_number: int
        :param task_status: 作业状态信息
        :type task_status: list[:class:`huaweicloudsdkhilens.v3.TaskStatus`]
        :param task_id: 作业id
        :type task_id: str
        :param user_task_id: 用户作业id
        :type user_task_id: str
        :param start_time_info: 
        :type start_time_info: :class:`huaweicloudsdkhilens.v3.StartTimeInfo`
        :param source_usage_estimate: 
        :type source_usage_estimate: :class:`huaweicloudsdkhilens.v3.TaskSourceUsageEstimate`
        """
        
        super(ShowTaskResponse, self).__init__()

        self._name = None
        self._timestamp = None
        self._description = None
        self._streams = None
        self._ok_pod_number = None
        self._cur_pod_number = None
        self._sum_pod_number = None
        self._fail_pod_number = None
        self._pending_pod_number = None
        self._task_status = None
        self._task_id = None
        self._user_task_id = None
        self._start_time_info = None
        self._source_usage_estimate = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if timestamp is not None:
            self.timestamp = timestamp
        if description is not None:
            self.description = description
        if streams is not None:
            self.streams = streams
        if ok_pod_number is not None:
            self.ok_pod_number = ok_pod_number
        if cur_pod_number is not None:
            self.cur_pod_number = cur_pod_number
        if sum_pod_number is not None:
            self.sum_pod_number = sum_pod_number
        if fail_pod_number is not None:
            self.fail_pod_number = fail_pod_number
        if pending_pod_number is not None:
            self.pending_pod_number = pending_pod_number
        if task_status is not None:
            self.task_status = task_status
        if task_id is not None:
            self.task_id = task_id
        if user_task_id is not None:
            self.user_task_id = user_task_id
        if start_time_info is not None:
            self.start_time_info = start_time_info
        if source_usage_estimate is not None:
            self.source_usage_estimate = source_usage_estimate

    @property
    def name(self):
        """Gets the name of this ShowTaskResponse.

        作业名称

        :return: The name of this ShowTaskResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowTaskResponse.

        作业名称

        :param name: The name of this ShowTaskResponse.
        :type name: str
        """
        self._name = name

    @property
    def timestamp(self):
        """Gets the timestamp of this ShowTaskResponse.

        作业创建时间

        :return: The timestamp of this ShowTaskResponse.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ShowTaskResponse.

        作业创建时间

        :param timestamp: The timestamp of this ShowTaskResponse.
        :type timestamp: str
        """
        self._timestamp = timestamp

    @property
    def description(self):
        """Gets the description of this ShowTaskResponse.

        作业描述

        :return: The description of this ShowTaskResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowTaskResponse.

        作业描述

        :param description: The description of this ShowTaskResponse.
        :type description: str
        """
        self._description = description

    @property
    def streams(self):
        """Gets the streams of this ShowTaskResponse.

        作业流详情

        :return: The streams of this ShowTaskResponse.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.TaskStream`]
        """
        return self._streams

    @streams.setter
    def streams(self, streams):
        """Sets the streams of this ShowTaskResponse.

        作业流详情

        :param streams: The streams of this ShowTaskResponse.
        :type streams: list[:class:`huaweicloudsdkhilens.v3.TaskStream`]
        """
        self._streams = streams

    @property
    def ok_pod_number(self):
        """Gets the ok_pod_number of this ShowTaskResponse.

        在实例上运行成功的作业数

        :return: The ok_pod_number of this ShowTaskResponse.
        :rtype: int
        """
        return self._ok_pod_number

    @ok_pod_number.setter
    def ok_pod_number(self, ok_pod_number):
        """Sets the ok_pod_number of this ShowTaskResponse.

        在实例上运行成功的作业数

        :param ok_pod_number: The ok_pod_number of this ShowTaskResponse.
        :type ok_pod_number: int
        """
        self._ok_pod_number = ok_pod_number

    @property
    def cur_pod_number(self):
        """Gets the cur_pod_number of this ShowTaskResponse.

        在实例上正在运行的作业数

        :return: The cur_pod_number of this ShowTaskResponse.
        :rtype: int
        """
        return self._cur_pod_number

    @cur_pod_number.setter
    def cur_pod_number(self, cur_pod_number):
        """Sets the cur_pod_number of this ShowTaskResponse.

        在实例上正在运行的作业数

        :param cur_pod_number: The cur_pod_number of this ShowTaskResponse.
        :type cur_pod_number: int
        """
        self._cur_pod_number = cur_pod_number

    @property
    def sum_pod_number(self):
        """Gets the sum_pod_number of this ShowTaskResponse.

        在实例上运行过的作业总数

        :return: The sum_pod_number of this ShowTaskResponse.
        :rtype: int
        """
        return self._sum_pod_number

    @sum_pod_number.setter
    def sum_pod_number(self, sum_pod_number):
        """Sets the sum_pod_number of this ShowTaskResponse.

        在实例上运行过的作业总数

        :param sum_pod_number: The sum_pod_number of this ShowTaskResponse.
        :type sum_pod_number: int
        """
        self._sum_pod_number = sum_pod_number

    @property
    def fail_pod_number(self):
        """Gets the fail_pod_number of this ShowTaskResponse.

        在实例上运行失败的作业数

        :return: The fail_pod_number of this ShowTaskResponse.
        :rtype: int
        """
        return self._fail_pod_number

    @fail_pod_number.setter
    def fail_pod_number(self, fail_pod_number):
        """Sets the fail_pod_number of this ShowTaskResponse.

        在实例上运行失败的作业数

        :param fail_pod_number: The fail_pod_number of this ShowTaskResponse.
        :type fail_pod_number: int
        """
        self._fail_pod_number = fail_pod_number

    @property
    def pending_pod_number(self):
        """Gets the pending_pod_number of this ShowTaskResponse.

        在实例上等待运行的作业数

        :return: The pending_pod_number of this ShowTaskResponse.
        :rtype: int
        """
        return self._pending_pod_number

    @pending_pod_number.setter
    def pending_pod_number(self, pending_pod_number):
        """Sets the pending_pod_number of this ShowTaskResponse.

        在实例上等待运行的作业数

        :param pending_pod_number: The pending_pod_number of this ShowTaskResponse.
        :type pending_pod_number: int
        """
        self._pending_pod_number = pending_pod_number

    @property
    def task_status(self):
        """Gets the task_status of this ShowTaskResponse.

        作业状态信息

        :return: The task_status of this ShowTaskResponse.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.TaskStatus`]
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this ShowTaskResponse.

        作业状态信息

        :param task_status: The task_status of this ShowTaskResponse.
        :type task_status: list[:class:`huaweicloudsdkhilens.v3.TaskStatus`]
        """
        self._task_status = task_status

    @property
    def task_id(self):
        """Gets the task_id of this ShowTaskResponse.

        作业id

        :return: The task_id of this ShowTaskResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ShowTaskResponse.

        作业id

        :param task_id: The task_id of this ShowTaskResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def user_task_id(self):
        """Gets the user_task_id of this ShowTaskResponse.

        用户作业id

        :return: The user_task_id of this ShowTaskResponse.
        :rtype: str
        """
        return self._user_task_id

    @user_task_id.setter
    def user_task_id(self, user_task_id):
        """Sets the user_task_id of this ShowTaskResponse.

        用户作业id

        :param user_task_id: The user_task_id of this ShowTaskResponse.
        :type user_task_id: str
        """
        self._user_task_id = user_task_id

    @property
    def start_time_info(self):
        """Gets the start_time_info of this ShowTaskResponse.

        :return: The start_time_info of this ShowTaskResponse.
        :rtype: :class:`huaweicloudsdkhilens.v3.StartTimeInfo`
        """
        return self._start_time_info

    @start_time_info.setter
    def start_time_info(self, start_time_info):
        """Sets the start_time_info of this ShowTaskResponse.

        :param start_time_info: The start_time_info of this ShowTaskResponse.
        :type start_time_info: :class:`huaweicloudsdkhilens.v3.StartTimeInfo`
        """
        self._start_time_info = start_time_info

    @property
    def source_usage_estimate(self):
        """Gets the source_usage_estimate of this ShowTaskResponse.

        :return: The source_usage_estimate of this ShowTaskResponse.
        :rtype: :class:`huaweicloudsdkhilens.v3.TaskSourceUsageEstimate`
        """
        return self._source_usage_estimate

    @source_usage_estimate.setter
    def source_usage_estimate(self, source_usage_estimate):
        """Sets the source_usage_estimate of this ShowTaskResponse.

        :param source_usage_estimate: The source_usage_estimate of this ShowTaskResponse.
        :type source_usage_estimate: :class:`huaweicloudsdkhilens.v3.TaskSourceUsageEstimate`
        """
        self._source_usage_estimate = source_usage_estimate

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
        if not isinstance(other, ShowTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
