# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchJobForList:

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
        'created_at': 'int',
        'status': 'str',
        'task_total_count': 'int',
        'task_success_count': 'int',
        'task_failed_count': 'int',
        'status_last_updated_at': 'int',
        'description': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'job_name': 'job_name',
        'job_type': 'job_type',
        'created_at': 'created_at',
        'status': 'status',
        'task_total_count': 'task_total_count',
        'task_success_count': 'task_success_count',
        'task_failed_count': 'task_failed_count',
        'status_last_updated_at': 'status_last_updated_at',
        'description': 'description'
    }

    def __init__(self, job_id=None, job_name=None, job_type=None, created_at=None, status=None, task_total_count=None, task_success_count=None, task_failed_count=None, status_last_updated_at=None, description=None):
        r"""BatchJobForList

        The model defined in huaweicloud sdk

        :param job_id: 批量处理作业ID
        :type job_id: str
        :param job_name: 批量处理作业名称
        :type job_name: str
        :param job_type: 批量处理作业类型，支持以下选项： - node_upgrade： 节点升级 - deployment_deploy：应用部署 - deployment_upgrade：应用升级
        :type job_type: str
        :param created_at: 创建时间戳
        :type created_at: int
        :param status: 执行状态
        :type status: str
        :param task_total_count: 任务总数
        :type task_total_count: int
        :param task_success_count: 任务项执行成功数
        :type task_success_count: int
        :param task_failed_count: 任务项执行失败数
        :type task_failed_count: int
        :param status_last_updated_at: 状态更新时间戳
        :type status_last_updated_at: int
        :param description: 任务描述
        :type description: str
        """
        
        

        self._job_id = None
        self._job_name = None
        self._job_type = None
        self._created_at = None
        self._status = None
        self._task_total_count = None
        self._task_success_count = None
        self._task_failed_count = None
        self._status_last_updated_at = None
        self._description = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if job_name is not None:
            self.job_name = job_name
        if job_type is not None:
            self.job_type = job_type
        if created_at is not None:
            self.created_at = created_at
        if status is not None:
            self.status = status
        if task_total_count is not None:
            self.task_total_count = task_total_count
        if task_success_count is not None:
            self.task_success_count = task_success_count
        if task_failed_count is not None:
            self.task_failed_count = task_failed_count
        if status_last_updated_at is not None:
            self.status_last_updated_at = status_last_updated_at
        if description is not None:
            self.description = description

    @property
    def job_id(self):
        r"""Gets the job_id of this BatchJobForList.

        批量处理作业ID

        :return: The job_id of this BatchJobForList.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this BatchJobForList.

        批量处理作业ID

        :param job_id: The job_id of this BatchJobForList.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        r"""Gets the job_name of this BatchJobForList.

        批量处理作业名称

        :return: The job_name of this BatchJobForList.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this BatchJobForList.

        批量处理作业名称

        :param job_name: The job_name of this BatchJobForList.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_type(self):
        r"""Gets the job_type of this BatchJobForList.

        批量处理作业类型，支持以下选项： - node_upgrade： 节点升级 - deployment_deploy：应用部署 - deployment_upgrade：应用升级

        :return: The job_type of this BatchJobForList.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this BatchJobForList.

        批量处理作业类型，支持以下选项： - node_upgrade： 节点升级 - deployment_deploy：应用部署 - deployment_upgrade：应用升级

        :param job_type: The job_type of this BatchJobForList.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def created_at(self):
        r"""Gets the created_at of this BatchJobForList.

        创建时间戳

        :return: The created_at of this BatchJobForList.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this BatchJobForList.

        创建时间戳

        :param created_at: The created_at of this BatchJobForList.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def status(self):
        r"""Gets the status of this BatchJobForList.

        执行状态

        :return: The status of this BatchJobForList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BatchJobForList.

        执行状态

        :param status: The status of this BatchJobForList.
        :type status: str
        """
        self._status = status

    @property
    def task_total_count(self):
        r"""Gets the task_total_count of this BatchJobForList.

        任务总数

        :return: The task_total_count of this BatchJobForList.
        :rtype: int
        """
        return self._task_total_count

    @task_total_count.setter
    def task_total_count(self, task_total_count):
        r"""Sets the task_total_count of this BatchJobForList.

        任务总数

        :param task_total_count: The task_total_count of this BatchJobForList.
        :type task_total_count: int
        """
        self._task_total_count = task_total_count

    @property
    def task_success_count(self):
        r"""Gets the task_success_count of this BatchJobForList.

        任务项执行成功数

        :return: The task_success_count of this BatchJobForList.
        :rtype: int
        """
        return self._task_success_count

    @task_success_count.setter
    def task_success_count(self, task_success_count):
        r"""Sets the task_success_count of this BatchJobForList.

        任务项执行成功数

        :param task_success_count: The task_success_count of this BatchJobForList.
        :type task_success_count: int
        """
        self._task_success_count = task_success_count

    @property
    def task_failed_count(self):
        r"""Gets the task_failed_count of this BatchJobForList.

        任务项执行失败数

        :return: The task_failed_count of this BatchJobForList.
        :rtype: int
        """
        return self._task_failed_count

    @task_failed_count.setter
    def task_failed_count(self, task_failed_count):
        r"""Sets the task_failed_count of this BatchJobForList.

        任务项执行失败数

        :param task_failed_count: The task_failed_count of this BatchJobForList.
        :type task_failed_count: int
        """
        self._task_failed_count = task_failed_count

    @property
    def status_last_updated_at(self):
        r"""Gets the status_last_updated_at of this BatchJobForList.

        状态更新时间戳

        :return: The status_last_updated_at of this BatchJobForList.
        :rtype: int
        """
        return self._status_last_updated_at

    @status_last_updated_at.setter
    def status_last_updated_at(self, status_last_updated_at):
        r"""Sets the status_last_updated_at of this BatchJobForList.

        状态更新时间戳

        :param status_last_updated_at: The status_last_updated_at of this BatchJobForList.
        :type status_last_updated_at: int
        """
        self._status_last_updated_at = status_last_updated_at

    @property
    def description(self):
        r"""Gets the description of this BatchJobForList.

        任务描述

        :return: The description of this BatchJobForList.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BatchJobForList.

        任务描述

        :param description: The description of this BatchJobForList.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, BatchJobForList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
