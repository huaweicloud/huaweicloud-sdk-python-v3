# coding: utf-8

import re
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
        'task_count': 'int',
        'success_count': 'int',
        'failed_count': 'int',
        'updated_at': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'job_name': 'job_name',
        'job_type': 'job_type',
        'created_at': 'created_at',
        'status': 'status',
        'task_count': 'task_count',
        'success_count': 'success_count',
        'failed_count': 'failed_count',
        'updated_at': 'updated_at'
    }

    def __init__(self, job_id=None, job_name=None, job_type=None, created_at=None, status=None, task_count=None, success_count=None, failed_count=None, updated_at=None):
        """BatchJobForList

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
        :param task_count: 任务总数
        :type task_count: int
        :param success_count: 任务项执行成功数
        :type success_count: int
        :param failed_count: 任务项执行失败数
        :type failed_count: int
        :param updated_at: 状态更新时间戳
        :type updated_at: int
        """
        
        

        self._job_id = None
        self._job_name = None
        self._job_type = None
        self._created_at = None
        self._status = None
        self._task_count = None
        self._success_count = None
        self._failed_count = None
        self._updated_at = None
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
        if task_count is not None:
            self.task_count = task_count
        if success_count is not None:
            self.success_count = success_count
        if failed_count is not None:
            self.failed_count = failed_count
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def job_id(self):
        """Gets the job_id of this BatchJobForList.

        批量处理作业ID

        :return: The job_id of this BatchJobForList.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this BatchJobForList.

        批量处理作业ID

        :param job_id: The job_id of this BatchJobForList.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        """Gets the job_name of this BatchJobForList.

        批量处理作业名称

        :return: The job_name of this BatchJobForList.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this BatchJobForList.

        批量处理作业名称

        :param job_name: The job_name of this BatchJobForList.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_type(self):
        """Gets the job_type of this BatchJobForList.

        批量处理作业类型，支持以下选项： - node_upgrade： 节点升级 - deployment_deploy：应用部署 - deployment_upgrade：应用升级

        :return: The job_type of this BatchJobForList.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this BatchJobForList.

        批量处理作业类型，支持以下选项： - node_upgrade： 节点升级 - deployment_deploy：应用部署 - deployment_upgrade：应用升级

        :param job_type: The job_type of this BatchJobForList.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def created_at(self):
        """Gets the created_at of this BatchJobForList.

        创建时间戳

        :return: The created_at of this BatchJobForList.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BatchJobForList.

        创建时间戳

        :param created_at: The created_at of this BatchJobForList.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def status(self):
        """Gets the status of this BatchJobForList.

        执行状态

        :return: The status of this BatchJobForList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BatchJobForList.

        执行状态

        :param status: The status of this BatchJobForList.
        :type status: str
        """
        self._status = status

    @property
    def task_count(self):
        """Gets the task_count of this BatchJobForList.

        任务总数

        :return: The task_count of this BatchJobForList.
        :rtype: int
        """
        return self._task_count

    @task_count.setter
    def task_count(self, task_count):
        """Sets the task_count of this BatchJobForList.

        任务总数

        :param task_count: The task_count of this BatchJobForList.
        :type task_count: int
        """
        self._task_count = task_count

    @property
    def success_count(self):
        """Gets the success_count of this BatchJobForList.

        任务项执行成功数

        :return: The success_count of this BatchJobForList.
        :rtype: int
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        """Sets the success_count of this BatchJobForList.

        任务项执行成功数

        :param success_count: The success_count of this BatchJobForList.
        :type success_count: int
        """
        self._success_count = success_count

    @property
    def failed_count(self):
        """Gets the failed_count of this BatchJobForList.

        任务项执行失败数

        :return: The failed_count of this BatchJobForList.
        :rtype: int
        """
        return self._failed_count

    @failed_count.setter
    def failed_count(self, failed_count):
        """Sets the failed_count of this BatchJobForList.

        任务项执行失败数

        :param failed_count: The failed_count of this BatchJobForList.
        :type failed_count: int
        """
        self._failed_count = failed_count

    @property
    def updated_at(self):
        """Gets the updated_at of this BatchJobForList.

        状态更新时间戳

        :return: The updated_at of this BatchJobForList.
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this BatchJobForList.

        状态更新时间戳

        :param updated_at: The updated_at of this BatchJobForList.
        :type updated_at: int
        """
        self._updated_at = updated_at

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
