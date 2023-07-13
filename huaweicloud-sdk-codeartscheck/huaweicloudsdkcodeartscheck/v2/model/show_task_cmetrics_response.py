# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskCmetricsResponse(SdkResponse):

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
        'task_name': 'str',
        'creator_id': 'str',
        'git_url': 'str',
        'git_branch': 'str',
        'last_check_time': 'str',
        'last_exec_time': 'str',
        'check_type': 'str',
        'created_at': 'str',
        'metric_info': 'MetricInfo'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_name': 'task_name',
        'creator_id': 'creator_id',
        'git_url': 'git_url',
        'git_branch': 'git_branch',
        'last_check_time': 'last_check_time',
        'last_exec_time': 'last_exec_time',
        'check_type': 'check_type',
        'created_at': 'created_at',
        'metric_info': 'metric_info'
    }

    def __init__(self, task_id=None, task_name=None, creator_id=None, git_url=None, git_branch=None, last_check_time=None, last_exec_time=None, check_type=None, created_at=None, metric_info=None):
        """ShowTaskCmetricsResponse

        The model defined in huaweicloud sdk

        :param task_id: 任务id
        :type task_id: str
        :param task_name: 任务名字
        :type task_name: str
        :param creator_id: 创建者id
        :type creator_id: str
        :param git_url: 代码仓地址
        :type git_url: str
        :param git_branch: 代码仓分支
        :type git_branch: str
        :param last_check_time: 上一次检查时间
        :type last_check_time: str
        :param last_exec_time: 上次执行时间
        :type last_exec_time: str
        :param check_type: 检查类型
        :type check_type: str
        :param created_at: 创建时间
        :type created_at: str
        :param metric_info: 
        :type metric_info: :class:`huaweicloudsdkcodeartscheck.v2.MetricInfo`
        """
        
        super(ShowTaskCmetricsResponse, self).__init__()

        self._task_id = None
        self._task_name = None
        self._creator_id = None
        self._git_url = None
        self._git_branch = None
        self._last_check_time = None
        self._last_exec_time = None
        self._check_type = None
        self._created_at = None
        self._metric_info = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if creator_id is not None:
            self.creator_id = creator_id
        if git_url is not None:
            self.git_url = git_url
        if git_branch is not None:
            self.git_branch = git_branch
        if last_check_time is not None:
            self.last_check_time = last_check_time
        if last_exec_time is not None:
            self.last_exec_time = last_exec_time
        if check_type is not None:
            self.check_type = check_type
        if created_at is not None:
            self.created_at = created_at
        if metric_info is not None:
            self.metric_info = metric_info

    @property
    def task_id(self):
        """Gets the task_id of this ShowTaskCmetricsResponse.

        任务id

        :return: The task_id of this ShowTaskCmetricsResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ShowTaskCmetricsResponse.

        任务id

        :param task_id: The task_id of this ShowTaskCmetricsResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        """Gets the task_name of this ShowTaskCmetricsResponse.

        任务名字

        :return: The task_name of this ShowTaskCmetricsResponse.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this ShowTaskCmetricsResponse.

        任务名字

        :param task_name: The task_name of this ShowTaskCmetricsResponse.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def creator_id(self):
        """Gets the creator_id of this ShowTaskCmetricsResponse.

        创建者id

        :return: The creator_id of this ShowTaskCmetricsResponse.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this ShowTaskCmetricsResponse.

        创建者id

        :param creator_id: The creator_id of this ShowTaskCmetricsResponse.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def git_url(self):
        """Gets the git_url of this ShowTaskCmetricsResponse.

        代码仓地址

        :return: The git_url of this ShowTaskCmetricsResponse.
        :rtype: str
        """
        return self._git_url

    @git_url.setter
    def git_url(self, git_url):
        """Sets the git_url of this ShowTaskCmetricsResponse.

        代码仓地址

        :param git_url: The git_url of this ShowTaskCmetricsResponse.
        :type git_url: str
        """
        self._git_url = git_url

    @property
    def git_branch(self):
        """Gets the git_branch of this ShowTaskCmetricsResponse.

        代码仓分支

        :return: The git_branch of this ShowTaskCmetricsResponse.
        :rtype: str
        """
        return self._git_branch

    @git_branch.setter
    def git_branch(self, git_branch):
        """Sets the git_branch of this ShowTaskCmetricsResponse.

        代码仓分支

        :param git_branch: The git_branch of this ShowTaskCmetricsResponse.
        :type git_branch: str
        """
        self._git_branch = git_branch

    @property
    def last_check_time(self):
        """Gets the last_check_time of this ShowTaskCmetricsResponse.

        上一次检查时间

        :return: The last_check_time of this ShowTaskCmetricsResponse.
        :rtype: str
        """
        return self._last_check_time

    @last_check_time.setter
    def last_check_time(self, last_check_time):
        """Sets the last_check_time of this ShowTaskCmetricsResponse.

        上一次检查时间

        :param last_check_time: The last_check_time of this ShowTaskCmetricsResponse.
        :type last_check_time: str
        """
        self._last_check_time = last_check_time

    @property
    def last_exec_time(self):
        """Gets the last_exec_time of this ShowTaskCmetricsResponse.

        上次执行时间

        :return: The last_exec_time of this ShowTaskCmetricsResponse.
        :rtype: str
        """
        return self._last_exec_time

    @last_exec_time.setter
    def last_exec_time(self, last_exec_time):
        """Sets the last_exec_time of this ShowTaskCmetricsResponse.

        上次执行时间

        :param last_exec_time: The last_exec_time of this ShowTaskCmetricsResponse.
        :type last_exec_time: str
        """
        self._last_exec_time = last_exec_time

    @property
    def check_type(self):
        """Gets the check_type of this ShowTaskCmetricsResponse.

        检查类型

        :return: The check_type of this ShowTaskCmetricsResponse.
        :rtype: str
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        """Sets the check_type of this ShowTaskCmetricsResponse.

        检查类型

        :param check_type: The check_type of this ShowTaskCmetricsResponse.
        :type check_type: str
        """
        self._check_type = check_type

    @property
    def created_at(self):
        """Gets the created_at of this ShowTaskCmetricsResponse.

        创建时间

        :return: The created_at of this ShowTaskCmetricsResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ShowTaskCmetricsResponse.

        创建时间

        :param created_at: The created_at of this ShowTaskCmetricsResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def metric_info(self):
        """Gets the metric_info of this ShowTaskCmetricsResponse.

        :return: The metric_info of this ShowTaskCmetricsResponse.
        :rtype: :class:`huaweicloudsdkcodeartscheck.v2.MetricInfo`
        """
        return self._metric_info

    @metric_info.setter
    def metric_info(self, metric_info):
        """Sets the metric_info of this ShowTaskCmetricsResponse.

        :param metric_info: The metric_info of this ShowTaskCmetricsResponse.
        :type metric_info: :class:`huaweicloudsdkcodeartscheck.v2.MetricInfo`
        """
        self._metric_info = metric_info

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
        if not isinstance(other, ShowTaskCmetricsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
