# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSecAppTaskStatusResponse(SdkResponse):

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
        'create_time': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'task_status': 'str',
        'fail_reason': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'create_time': 'create_time',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'task_status': 'task_status',
        'fail_reason': 'fail_reason'
    }

    def __init__(self, task_id=None, create_time=None, begin_time=None, end_time=None, task_status=None, fail_reason=None):
        """ShowSecAppTaskStatusResponse

        The model defined in huaweicloud sdk

        :param task_id: 任务ID
        :type task_id: str
        :param create_time: 创建任务的时间
        :type create_time: str
        :param begin_time: 任务启动的时间
        :type begin_time: str
        :param end_time: 任务结束的时间
        :type end_time: str
        :param task_status: 任务状态:   * WAITING - 等待   * RUNNING - 进行   * SUCCESS - 完成   * FAILURE - 失败   * STOP - 停止   * DELETED - 删除 
        :type task_status: str
        :param fail_reason: 任务失败时返回失败原因
        :type fail_reason: str
        """
        
        super(ShowSecAppTaskStatusResponse, self).__init__()

        self._task_id = None
        self._create_time = None
        self._begin_time = None
        self._end_time = None
        self._task_status = None
        self._fail_reason = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if create_time is not None:
            self.create_time = create_time
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if task_status is not None:
            self.task_status = task_status
        if fail_reason is not None:
            self.fail_reason = fail_reason

    @property
    def task_id(self):
        """Gets the task_id of this ShowSecAppTaskStatusResponse.

        任务ID

        :return: The task_id of this ShowSecAppTaskStatusResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ShowSecAppTaskStatusResponse.

        任务ID

        :param task_id: The task_id of this ShowSecAppTaskStatusResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def create_time(self):
        """Gets the create_time of this ShowSecAppTaskStatusResponse.

        创建任务的时间

        :return: The create_time of this ShowSecAppTaskStatusResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowSecAppTaskStatusResponse.

        创建任务的时间

        :param create_time: The create_time of this ShowSecAppTaskStatusResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def begin_time(self):
        """Gets the begin_time of this ShowSecAppTaskStatusResponse.

        任务启动的时间

        :return: The begin_time of this ShowSecAppTaskStatusResponse.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ShowSecAppTaskStatusResponse.

        任务启动的时间

        :param begin_time: The begin_time of this ShowSecAppTaskStatusResponse.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowSecAppTaskStatusResponse.

        任务结束的时间

        :return: The end_time of this ShowSecAppTaskStatusResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowSecAppTaskStatusResponse.

        任务结束的时间

        :param end_time: The end_time of this ShowSecAppTaskStatusResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def task_status(self):
        """Gets the task_status of this ShowSecAppTaskStatusResponse.

        任务状态:   * WAITING - 等待   * RUNNING - 进行   * SUCCESS - 完成   * FAILURE - 失败   * STOP - 停止   * DELETED - 删除 

        :return: The task_status of this ShowSecAppTaskStatusResponse.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this ShowSecAppTaskStatusResponse.

        任务状态:   * WAITING - 等待   * RUNNING - 进行   * SUCCESS - 完成   * FAILURE - 失败   * STOP - 停止   * DELETED - 删除 

        :param task_status: The task_status of this ShowSecAppTaskStatusResponse.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def fail_reason(self):
        """Gets the fail_reason of this ShowSecAppTaskStatusResponse.

        任务失败时返回失败原因

        :return: The fail_reason of this ShowSecAppTaskStatusResponse.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this ShowSecAppTaskStatusResponse.

        任务失败时返回失败原因

        :param fail_reason: The fail_reason of this ShowSecAppTaskStatusResponse.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

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
        if not isinstance(other, ShowSecAppTaskStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
