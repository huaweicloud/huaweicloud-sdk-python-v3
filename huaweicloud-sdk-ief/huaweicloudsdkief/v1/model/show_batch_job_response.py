# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBatchJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'job_name': 'str',
        'job_type': 'str',
        'description': 'str',
        'created_at': 'int',
        'status': 'str',
        'task_total_count': 'int',
        'task_failed_count': 'int',
        'task_success_count': 'int',
        'target_type': 'str',
        'task_data': 'str',
        'tasks': 'list[Task]',
        'targets': 'list[Target]',
        'status_last_updated_at': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'job_name': 'job_name',
        'job_type': 'job_type',
        'description': 'description',
        'created_at': 'created_at',
        'status': 'status',
        'task_total_count': 'task_total_count',
        'task_failed_count': 'task_failed_count',
        'task_success_count': 'task_success_count',
        'target_type': 'target_type',
        'task_data': 'task_data',
        'tasks': 'tasks',
        'targets': 'targets',
        'status_last_updated_at': 'status_last_updated_at'
    }

    def __init__(self, job_id=None, job_name=None, job_type=None, description=None, created_at=None, status=None, task_total_count=None, task_failed_count=None, task_success_count=None, target_type=None, task_data=None, tasks=None, targets=None, status_last_updated_at=None):
        """ShowBatchJobResponse

        The model defined in huaweicloud sdk

        :param job_id: 批量处理作业ID
        :type job_id: str
        :param job_name: 批量处理作业名称
        :type job_name: str
        :param job_type: 批量作业类型，支持以下选项： - node_upgrade： 节点升级 - deployment_deploy：应用部署 - deployment_upgrade：应用升级
        :type job_type: str
        :param description: 描述
        :type description: str
        :param created_at: 创建时间戳
        :type created_at: int
        :param status: 执行状态
        :type status: str
        :param task_total_count: 任务总数
        :type task_total_count: int
        :param task_failed_count: 任务项执行成功数
        :type task_failed_count: int
        :param task_success_count: 任务项执行失败数
        :type task_success_count: int
        :param target_type: 批量作业对象类型，支持如下选项： - node：边缘节点 - node_group：边缘节点组 - deployment：边缘应用
        :type target_type: str
        :param task_data: 批量作业内容，仅在批量应用部署和批量应用升级时需要填写，填入的内容为：使用json结构体编写的创建应用部署接口请求体deployment参数，并将其转换为字符串
        :type task_data: str
        :param tasks: 任务项详情
        :type tasks: list[:class:`huaweicloudsdkief.v1.Task`]
        :param targets: 批量处理对象详情
        :type targets: list[:class:`huaweicloudsdkief.v1.Target`]
        :param status_last_updated_at: 状态更新时间戳
        :type status_last_updated_at: int
        """
        
        super(ShowBatchJobResponse, self).__init__()

        self._job_id = None
        self._job_name = None
        self._job_type = None
        self._description = None
        self._created_at = None
        self._status = None
        self._task_total_count = None
        self._task_failed_count = None
        self._task_success_count = None
        self._target_type = None
        self._task_data = None
        self._tasks = None
        self._targets = None
        self._status_last_updated_at = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if job_name is not None:
            self.job_name = job_name
        if job_type is not None:
            self.job_type = job_type
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if status is not None:
            self.status = status
        if task_total_count is not None:
            self.task_total_count = task_total_count
        if task_failed_count is not None:
            self.task_failed_count = task_failed_count
        if task_success_count is not None:
            self.task_success_count = task_success_count
        if target_type is not None:
            self.target_type = target_type
        if task_data is not None:
            self.task_data = task_data
        if tasks is not None:
            self.tasks = tasks
        if targets is not None:
            self.targets = targets
        if status_last_updated_at is not None:
            self.status_last_updated_at = status_last_updated_at

    @property
    def job_id(self):
        """Gets the job_id of this ShowBatchJobResponse.

        批量处理作业ID

        :return: The job_id of this ShowBatchJobResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ShowBatchJobResponse.

        批量处理作业ID

        :param job_id: The job_id of this ShowBatchJobResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        """Gets the job_name of this ShowBatchJobResponse.

        批量处理作业名称

        :return: The job_name of this ShowBatchJobResponse.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this ShowBatchJobResponse.

        批量处理作业名称

        :param job_name: The job_name of this ShowBatchJobResponse.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_type(self):
        """Gets the job_type of this ShowBatchJobResponse.

        批量作业类型，支持以下选项： - node_upgrade： 节点升级 - deployment_deploy：应用部署 - deployment_upgrade：应用升级

        :return: The job_type of this ShowBatchJobResponse.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this ShowBatchJobResponse.

        批量作业类型，支持以下选项： - node_upgrade： 节点升级 - deployment_deploy：应用部署 - deployment_upgrade：应用升级

        :param job_type: The job_type of this ShowBatchJobResponse.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def description(self):
        """Gets the description of this ShowBatchJobResponse.

        描述

        :return: The description of this ShowBatchJobResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowBatchJobResponse.

        描述

        :param description: The description of this ShowBatchJobResponse.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this ShowBatchJobResponse.

        创建时间戳

        :return: The created_at of this ShowBatchJobResponse.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ShowBatchJobResponse.

        创建时间戳

        :param created_at: The created_at of this ShowBatchJobResponse.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def status(self):
        """Gets the status of this ShowBatchJobResponse.

        执行状态

        :return: The status of this ShowBatchJobResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowBatchJobResponse.

        执行状态

        :param status: The status of this ShowBatchJobResponse.
        :type status: str
        """
        self._status = status

    @property
    def task_total_count(self):
        """Gets the task_total_count of this ShowBatchJobResponse.

        任务总数

        :return: The task_total_count of this ShowBatchJobResponse.
        :rtype: int
        """
        return self._task_total_count

    @task_total_count.setter
    def task_total_count(self, task_total_count):
        """Sets the task_total_count of this ShowBatchJobResponse.

        任务总数

        :param task_total_count: The task_total_count of this ShowBatchJobResponse.
        :type task_total_count: int
        """
        self._task_total_count = task_total_count

    @property
    def task_failed_count(self):
        """Gets the task_failed_count of this ShowBatchJobResponse.

        任务项执行成功数

        :return: The task_failed_count of this ShowBatchJobResponse.
        :rtype: int
        """
        return self._task_failed_count

    @task_failed_count.setter
    def task_failed_count(self, task_failed_count):
        """Sets the task_failed_count of this ShowBatchJobResponse.

        任务项执行成功数

        :param task_failed_count: The task_failed_count of this ShowBatchJobResponse.
        :type task_failed_count: int
        """
        self._task_failed_count = task_failed_count

    @property
    def task_success_count(self):
        """Gets the task_success_count of this ShowBatchJobResponse.

        任务项执行失败数

        :return: The task_success_count of this ShowBatchJobResponse.
        :rtype: int
        """
        return self._task_success_count

    @task_success_count.setter
    def task_success_count(self, task_success_count):
        """Sets the task_success_count of this ShowBatchJobResponse.

        任务项执行失败数

        :param task_success_count: The task_success_count of this ShowBatchJobResponse.
        :type task_success_count: int
        """
        self._task_success_count = task_success_count

    @property
    def target_type(self):
        """Gets the target_type of this ShowBatchJobResponse.

        批量作业对象类型，支持如下选项： - node：边缘节点 - node_group：边缘节点组 - deployment：边缘应用

        :return: The target_type of this ShowBatchJobResponse.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """Sets the target_type of this ShowBatchJobResponse.

        批量作业对象类型，支持如下选项： - node：边缘节点 - node_group：边缘节点组 - deployment：边缘应用

        :param target_type: The target_type of this ShowBatchJobResponse.
        :type target_type: str
        """
        self._target_type = target_type

    @property
    def task_data(self):
        """Gets the task_data of this ShowBatchJobResponse.

        批量作业内容，仅在批量应用部署和批量应用升级时需要填写，填入的内容为：使用json结构体编写的创建应用部署接口请求体deployment参数，并将其转换为字符串

        :return: The task_data of this ShowBatchJobResponse.
        :rtype: str
        """
        return self._task_data

    @task_data.setter
    def task_data(self, task_data):
        """Sets the task_data of this ShowBatchJobResponse.

        批量作业内容，仅在批量应用部署和批量应用升级时需要填写，填入的内容为：使用json结构体编写的创建应用部署接口请求体deployment参数，并将其转换为字符串

        :param task_data: The task_data of this ShowBatchJobResponse.
        :type task_data: str
        """
        self._task_data = task_data

    @property
    def tasks(self):
        """Gets the tasks of this ShowBatchJobResponse.

        任务项详情

        :return: The tasks of this ShowBatchJobResponse.
        :rtype: list[:class:`huaweicloudsdkief.v1.Task`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this ShowBatchJobResponse.

        任务项详情

        :param tasks: The tasks of this ShowBatchJobResponse.
        :type tasks: list[:class:`huaweicloudsdkief.v1.Task`]
        """
        self._tasks = tasks

    @property
    def targets(self):
        """Gets the targets of this ShowBatchJobResponse.

        批量处理对象详情

        :return: The targets of this ShowBatchJobResponse.
        :rtype: list[:class:`huaweicloudsdkief.v1.Target`]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this ShowBatchJobResponse.

        批量处理对象详情

        :param targets: The targets of this ShowBatchJobResponse.
        :type targets: list[:class:`huaweicloudsdkief.v1.Target`]
        """
        self._targets = targets

    @property
    def status_last_updated_at(self):
        """Gets the status_last_updated_at of this ShowBatchJobResponse.

        状态更新时间戳

        :return: The status_last_updated_at of this ShowBatchJobResponse.
        :rtype: int
        """
        return self._status_last_updated_at

    @status_last_updated_at.setter
    def status_last_updated_at(self, status_last_updated_at):
        """Sets the status_last_updated_at of this ShowBatchJobResponse.

        状态更新时间戳

        :param status_last_updated_at: The status_last_updated_at of this ShowBatchJobResponse.
        :type status_last_updated_at: int
        """
        self._status_last_updated_at = status_last_updated_at

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
        if not isinstance(other, ShowBatchJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
