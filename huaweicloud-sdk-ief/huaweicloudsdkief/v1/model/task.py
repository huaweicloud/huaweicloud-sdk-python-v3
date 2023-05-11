# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Task:

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
        'status': 'str',
        'reason': 'str',
        'created_at': 'int',
        'target_id': 'str',
        'extension_info': 'list[Extension]'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_name': 'task_name',
        'status': 'status',
        'reason': 'reason',
        'created_at': 'created_at',
        'target_id': 'target_id',
        'extension_info': 'extension_info'
    }

    def __init__(self, task_id=None, task_name=None, status=None, reason=None, created_at=None, target_id=None, extension_info=None):
        """Task

        The model defined in huaweicloud sdk

        :param task_id: 任务项ID
        :type task_id: str
        :param task_name: 任务项名称
        :type task_name: str
        :param status: 任务项状态
        :type status: str
        :param reason: 任务项失败的原因
        :type reason: str
        :param created_at: 创建时间戳
        :type created_at: int
        :param target_id: 批量处理对象ID
        :type target_id: str
        :param extension_info: 批量处理对象基本信息
        :type extension_info: list[:class:`huaweicloudsdkief.v1.Extension`]
        """
        
        

        self._task_id = None
        self._task_name = None
        self._status = None
        self._reason = None
        self._created_at = None
        self._target_id = None
        self._extension_info = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if status is not None:
            self.status = status
        if reason is not None:
            self.reason = reason
        if created_at is not None:
            self.created_at = created_at
        if target_id is not None:
            self.target_id = target_id
        if extension_info is not None:
            self.extension_info = extension_info

    @property
    def task_id(self):
        """Gets the task_id of this Task.

        任务项ID

        :return: The task_id of this Task.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this Task.

        任务项ID

        :param task_id: The task_id of this Task.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        """Gets the task_name of this Task.

        任务项名称

        :return: The task_name of this Task.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this Task.

        任务项名称

        :param task_name: The task_name of this Task.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def status(self):
        """Gets the status of this Task.

        任务项状态

        :return: The status of this Task.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Task.

        任务项状态

        :param status: The status of this Task.
        :type status: str
        """
        self._status = status

    @property
    def reason(self):
        """Gets the reason of this Task.

        任务项失败的原因

        :return: The reason of this Task.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this Task.

        任务项失败的原因

        :param reason: The reason of this Task.
        :type reason: str
        """
        self._reason = reason

    @property
    def created_at(self):
        """Gets the created_at of this Task.

        创建时间戳

        :return: The created_at of this Task.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Task.

        创建时间戳

        :param created_at: The created_at of this Task.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def target_id(self):
        """Gets the target_id of this Task.

        批量处理对象ID

        :return: The target_id of this Task.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this Task.

        批量处理对象ID

        :param target_id: The target_id of this Task.
        :type target_id: str
        """
        self._target_id = target_id

    @property
    def extension_info(self):
        """Gets the extension_info of this Task.

        批量处理对象基本信息

        :return: The extension_info of this Task.
        :rtype: list[:class:`huaweicloudsdkief.v1.Extension`]
        """
        return self._extension_info

    @extension_info.setter
    def extension_info(self, extension_info):
        """Sets the extension_info of this Task.

        批量处理对象基本信息

        :param extension_info: The extension_info of this Task.
        :type extension_info: list[:class:`huaweicloudsdkief.v1.Extension`]
        """
        self._extension_info = extension_info

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
        if not isinstance(other, Task):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
