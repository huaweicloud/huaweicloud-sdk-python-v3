# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MultiTaskRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_name': 'str',
        'task_id': 'str',
        'task_type': 'str',
        'description': 'str',
        'task_tag': 'str',
        'operation_types': 'list[str]',
        'source_app_id': 'str',
        'target_app_id': 'str'
    }

    attribute_map = {
        'task_name': 'task_name',
        'task_id': 'task_id',
        'task_type': 'task_type',
        'description': 'description',
        'task_tag': 'task_tag',
        'operation_types': 'operation_types',
        'source_app_id': 'source_app_id',
        'target_app_id': 'target_app_id'
    }

    def __init__(self, task_name=None, task_id=None, task_type=None, description=None, task_tag=None, operation_types=None, source_app_id=None, target_app_id=None):
        """MultiTaskRequestBody

        The model defined in huaweicloud sdk

        :param task_name: 任务名称，只能以字母、数字为开头，包含字母、数字和 . _ -  3~100个字符
        :type task_name: str
        :param task_id: 任务ID，可以为空
        :type task_id: str
        :param task_type: 任务类型，目前组合任务仅支持实时任务 - REALTIME (实时) - TIMING (定时)
        :type task_type: str
        :param description: 描述信息
        :type description: str
        :param task_tag: 任务标签,只能包含字母、数字、中划线、下划线
        :type task_tag: str
        :param operation_types: 需要支持的操作类型，支持多选，至少需要选择以下一种： - INSERT - UPDATE - DELETE
        :type operation_types: list[str]
        :param source_app_id: 源端数据源所属集成应用ID
        :type source_app_id: str
        :param target_app_id: 目标端数据源所属集成应用ID
        :type target_app_id: str
        """
        
        

        self._task_name = None
        self._task_id = None
        self._task_type = None
        self._description = None
        self._task_tag = None
        self._operation_types = None
        self._source_app_id = None
        self._target_app_id = None
        self.discriminator = None

        self.task_name = task_name
        if task_id is not None:
            self.task_id = task_id
        if task_type is not None:
            self.task_type = task_type
        if description is not None:
            self.description = description
        if task_tag is not None:
            self.task_tag = task_tag
        self.operation_types = operation_types
        if source_app_id is not None:
            self.source_app_id = source_app_id
        if target_app_id is not None:
            self.target_app_id = target_app_id

    @property
    def task_name(self):
        """Gets the task_name of this MultiTaskRequestBody.

        任务名称，只能以字母、数字为开头，包含字母、数字和 . _ -  3~100个字符

        :return: The task_name of this MultiTaskRequestBody.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this MultiTaskRequestBody.

        任务名称，只能以字母、数字为开头，包含字母、数字和 . _ -  3~100个字符

        :param task_name: The task_name of this MultiTaskRequestBody.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_id(self):
        """Gets the task_id of this MultiTaskRequestBody.

        任务ID，可以为空

        :return: The task_id of this MultiTaskRequestBody.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this MultiTaskRequestBody.

        任务ID，可以为空

        :param task_id: The task_id of this MultiTaskRequestBody.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_type(self):
        """Gets the task_type of this MultiTaskRequestBody.

        任务类型，目前组合任务仅支持实时任务 - REALTIME (实时) - TIMING (定时)

        :return: The task_type of this MultiTaskRequestBody.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this MultiTaskRequestBody.

        任务类型，目前组合任务仅支持实时任务 - REALTIME (实时) - TIMING (定时)

        :param task_type: The task_type of this MultiTaskRequestBody.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def description(self):
        """Gets the description of this MultiTaskRequestBody.

        描述信息

        :return: The description of this MultiTaskRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MultiTaskRequestBody.

        描述信息

        :param description: The description of this MultiTaskRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def task_tag(self):
        """Gets the task_tag of this MultiTaskRequestBody.

        任务标签,只能包含字母、数字、中划线、下划线

        :return: The task_tag of this MultiTaskRequestBody.
        :rtype: str
        """
        return self._task_tag

    @task_tag.setter
    def task_tag(self, task_tag):
        """Sets the task_tag of this MultiTaskRequestBody.

        任务标签,只能包含字母、数字、中划线、下划线

        :param task_tag: The task_tag of this MultiTaskRequestBody.
        :type task_tag: str
        """
        self._task_tag = task_tag

    @property
    def operation_types(self):
        """Gets the operation_types of this MultiTaskRequestBody.

        需要支持的操作类型，支持多选，至少需要选择以下一种： - INSERT - UPDATE - DELETE

        :return: The operation_types of this MultiTaskRequestBody.
        :rtype: list[str]
        """
        return self._operation_types

    @operation_types.setter
    def operation_types(self, operation_types):
        """Sets the operation_types of this MultiTaskRequestBody.

        需要支持的操作类型，支持多选，至少需要选择以下一种： - INSERT - UPDATE - DELETE

        :param operation_types: The operation_types of this MultiTaskRequestBody.
        :type operation_types: list[str]
        """
        self._operation_types = operation_types

    @property
    def source_app_id(self):
        """Gets the source_app_id of this MultiTaskRequestBody.

        源端数据源所属集成应用ID

        :return: The source_app_id of this MultiTaskRequestBody.
        :rtype: str
        """
        return self._source_app_id

    @source_app_id.setter
    def source_app_id(self, source_app_id):
        """Sets the source_app_id of this MultiTaskRequestBody.

        源端数据源所属集成应用ID

        :param source_app_id: The source_app_id of this MultiTaskRequestBody.
        :type source_app_id: str
        """
        self._source_app_id = source_app_id

    @property
    def target_app_id(self):
        """Gets the target_app_id of this MultiTaskRequestBody.

        目标端数据源所属集成应用ID

        :return: The target_app_id of this MultiTaskRequestBody.
        :rtype: str
        """
        return self._target_app_id

    @target_app_id.setter
    def target_app_id(self, target_app_id):
        """Sets the target_app_id of this MultiTaskRequestBody.

        目标端数据源所属集成应用ID

        :param target_app_id: The target_app_id of this MultiTaskRequestBody.
        :type target_app_id: str
        """
        self._target_app_id = target_app_id

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
        if not isinstance(other, MultiTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
