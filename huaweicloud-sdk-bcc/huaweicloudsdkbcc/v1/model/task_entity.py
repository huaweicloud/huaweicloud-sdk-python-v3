# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskEntity:

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
        'task_type': 'TaskTypeEnum',
        'task_status': 'TaskStatusEnum',
        'resource_name': 'str',
        'resource_id': 'str',
        'resource_type': 'ResourceTypeEnum',
        'region_id': 'str',
        'vault_name': 'str',
        'vault_id': 'str',
        'task_start_time': 'str',
        'task_end_time': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_type': 'task_type',
        'task_status': 'task_status',
        'resource_name': 'resource_name',
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'region_id': 'region_id',
        'vault_name': 'vault_name',
        'vault_id': 'vault_id',
        'task_start_time': 'task_start_time',
        'task_end_time': 'task_end_time'
    }

    def __init__(self, task_id=None, task_type=None, task_status=None, resource_name=None, resource_id=None, resource_type=None, region_id=None, vault_name=None, vault_id=None, task_start_time=None, task_end_time=None):
        r"""TaskEntity

        The model defined in huaweicloud sdk

        :param task_id: 任务ID
        :type task_id: str
        :param task_type: 
        :type task_type: :class:`huaweicloudsdkbcc.v1.TaskTypeEnum`
        :param task_status: 
        :type task_status: :class:`huaweicloudsdkbcc.v1.TaskStatusEnum`
        :param resource_name: 资源名称
        :type resource_name: str
        :param resource_id: 资源ID
        :type resource_id: str
        :param resource_type: 
        :type resource_type: :class:`huaweicloudsdkbcc.v1.ResourceTypeEnum`
        :param region_id: 任务归属的区域ID
        :type region_id: str
        :param vault_name: 存储库名称
        :type vault_name: str
        :param vault_id: 存储库ID
        :type vault_id: str
        :param task_start_time: 任务开始时间
        :type task_start_time: str
        :param task_end_time: 任务结束时间
        :type task_end_time: str
        """
        
        

        self._task_id = None
        self._task_type = None
        self._task_status = None
        self._resource_name = None
        self._resource_id = None
        self._resource_type = None
        self._region_id = None
        self._vault_name = None
        self._vault_id = None
        self._task_start_time = None
        self._task_end_time = None
        self.discriminator = None

        self.task_id = task_id
        self.task_type = task_type
        self.task_status = task_status
        self.resource_name = resource_name
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.region_id = region_id
        if vault_name is not None:
            self.vault_name = vault_name
        if vault_id is not None:
            self.vault_id = vault_id
        self.task_start_time = task_start_time
        self.task_end_time = task_end_time

    @property
    def task_id(self):
        r"""Gets the task_id of this TaskEntity.

        任务ID

        :return: The task_id of this TaskEntity.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this TaskEntity.

        任务ID

        :param task_id: The task_id of this TaskEntity.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_type(self):
        r"""Gets the task_type of this TaskEntity.

        :return: The task_type of this TaskEntity.
        :rtype: :class:`huaweicloudsdkbcc.v1.TaskTypeEnum`
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this TaskEntity.

        :param task_type: The task_type of this TaskEntity.
        :type task_type: :class:`huaweicloudsdkbcc.v1.TaskTypeEnum`
        """
        self._task_type = task_type

    @property
    def task_status(self):
        r"""Gets the task_status of this TaskEntity.

        :return: The task_status of this TaskEntity.
        :rtype: :class:`huaweicloudsdkbcc.v1.TaskStatusEnum`
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        r"""Sets the task_status of this TaskEntity.

        :param task_status: The task_status of this TaskEntity.
        :type task_status: :class:`huaweicloudsdkbcc.v1.TaskStatusEnum`
        """
        self._task_status = task_status

    @property
    def resource_name(self):
        r"""Gets the resource_name of this TaskEntity.

        资源名称

        :return: The resource_name of this TaskEntity.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this TaskEntity.

        资源名称

        :param resource_name: The resource_name of this TaskEntity.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def resource_id(self):
        r"""Gets the resource_id of this TaskEntity.

        资源ID

        :return: The resource_id of this TaskEntity.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this TaskEntity.

        资源ID

        :param resource_id: The resource_id of this TaskEntity.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this TaskEntity.

        :return: The resource_type of this TaskEntity.
        :rtype: :class:`huaweicloudsdkbcc.v1.ResourceTypeEnum`
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this TaskEntity.

        :param resource_type: The resource_type of this TaskEntity.
        :type resource_type: :class:`huaweicloudsdkbcc.v1.ResourceTypeEnum`
        """
        self._resource_type = resource_type

    @property
    def region_id(self):
        r"""Gets the region_id of this TaskEntity.

        任务归属的区域ID

        :return: The region_id of this TaskEntity.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this TaskEntity.

        任务归属的区域ID

        :param region_id: The region_id of this TaskEntity.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def vault_name(self):
        r"""Gets the vault_name of this TaskEntity.

        存储库名称

        :return: The vault_name of this TaskEntity.
        :rtype: str
        """
        return self._vault_name

    @vault_name.setter
    def vault_name(self, vault_name):
        r"""Sets the vault_name of this TaskEntity.

        存储库名称

        :param vault_name: The vault_name of this TaskEntity.
        :type vault_name: str
        """
        self._vault_name = vault_name

    @property
    def vault_id(self):
        r"""Gets the vault_id of this TaskEntity.

        存储库ID

        :return: The vault_id of this TaskEntity.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        r"""Sets the vault_id of this TaskEntity.

        存储库ID

        :param vault_id: The vault_id of this TaskEntity.
        :type vault_id: str
        """
        self._vault_id = vault_id

    @property
    def task_start_time(self):
        r"""Gets the task_start_time of this TaskEntity.

        任务开始时间

        :return: The task_start_time of this TaskEntity.
        :rtype: str
        """
        return self._task_start_time

    @task_start_time.setter
    def task_start_time(self, task_start_time):
        r"""Sets the task_start_time of this TaskEntity.

        任务开始时间

        :param task_start_time: The task_start_time of this TaskEntity.
        :type task_start_time: str
        """
        self._task_start_time = task_start_time

    @property
    def task_end_time(self):
        r"""Gets the task_end_time of this TaskEntity.

        任务结束时间

        :return: The task_end_time of this TaskEntity.
        :rtype: str
        """
        return self._task_end_time

    @task_end_time.setter
    def task_end_time(self, task_end_time):
        r"""Sets the task_end_time of this TaskEntity.

        任务结束时间

        :param task_end_time: The task_end_time of this TaskEntity.
        :type task_end_time: str
        """
        self._task_end_time = task_end_time

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
        if not isinstance(other, TaskEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
