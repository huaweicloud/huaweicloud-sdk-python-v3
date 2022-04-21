# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskBasicRequestBody:

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
        'task_type': 'str',
        'source_datasource_id': 'str',
        'target_datasource_id': 'str',
        'description': 'str',
        'task_tag': 'str'
    }

    attribute_map = {
        'task_name': 'task_name',
        'task_type': 'task_type',
        'source_datasource_id': 'source_datasource_id',
        'target_datasource_id': 'target_datasource_id',
        'description': 'description',
        'task_tag': 'task_tag'
    }

    def __init__(self, task_name=None, task_type=None, source_datasource_id=None, target_datasource_id=None, description=None, task_tag=None):
        """TaskBasicRequestBody

        The model defined in huaweicloud sdk

        :param task_name: 任务名称，只能以字母、数字为开头，包含字母、数字和 . _ -  3~100个字符
        :type task_name: str
        :param task_type: 任务类型 - REALTIME (实时) - TIMING (定时)
        :type task_type: str
        :param source_datasource_id: 源端数据源ID
        :type source_datasource_id: str
        :param target_datasource_id: 目标端数据源ID
        :type target_datasource_id: str
        :param description: 描述信息
        :type description: str
        :param task_tag: 任务标签,只能包含字母、数字、中划线、下划线
        :type task_tag: str
        """
        
        

        self._task_name = None
        self._task_type = None
        self._source_datasource_id = None
        self._target_datasource_id = None
        self._description = None
        self._task_tag = None
        self.discriminator = None

        if task_name is not None:
            self.task_name = task_name
        if task_type is not None:
            self.task_type = task_type
        if source_datasource_id is not None:
            self.source_datasource_id = source_datasource_id
        if target_datasource_id is not None:
            self.target_datasource_id = target_datasource_id
        if description is not None:
            self.description = description
        if task_tag is not None:
            self.task_tag = task_tag

    @property
    def task_name(self):
        """Gets the task_name of this TaskBasicRequestBody.

        任务名称，只能以字母、数字为开头，包含字母、数字和 . _ -  3~100个字符

        :return: The task_name of this TaskBasicRequestBody.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this TaskBasicRequestBody.

        任务名称，只能以字母、数字为开头，包含字母、数字和 . _ -  3~100个字符

        :param task_name: The task_name of this TaskBasicRequestBody.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_type(self):
        """Gets the task_type of this TaskBasicRequestBody.

        任务类型 - REALTIME (实时) - TIMING (定时)

        :return: The task_type of this TaskBasicRequestBody.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this TaskBasicRequestBody.

        任务类型 - REALTIME (实时) - TIMING (定时)

        :param task_type: The task_type of this TaskBasicRequestBody.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def source_datasource_id(self):
        """Gets the source_datasource_id of this TaskBasicRequestBody.

        源端数据源ID

        :return: The source_datasource_id of this TaskBasicRequestBody.
        :rtype: str
        """
        return self._source_datasource_id

    @source_datasource_id.setter
    def source_datasource_id(self, source_datasource_id):
        """Sets the source_datasource_id of this TaskBasicRequestBody.

        源端数据源ID

        :param source_datasource_id: The source_datasource_id of this TaskBasicRequestBody.
        :type source_datasource_id: str
        """
        self._source_datasource_id = source_datasource_id

    @property
    def target_datasource_id(self):
        """Gets the target_datasource_id of this TaskBasicRequestBody.

        目标端数据源ID

        :return: The target_datasource_id of this TaskBasicRequestBody.
        :rtype: str
        """
        return self._target_datasource_id

    @target_datasource_id.setter
    def target_datasource_id(self, target_datasource_id):
        """Sets the target_datasource_id of this TaskBasicRequestBody.

        目标端数据源ID

        :param target_datasource_id: The target_datasource_id of this TaskBasicRequestBody.
        :type target_datasource_id: str
        """
        self._target_datasource_id = target_datasource_id

    @property
    def description(self):
        """Gets the description of this TaskBasicRequestBody.

        描述信息

        :return: The description of this TaskBasicRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaskBasicRequestBody.

        描述信息

        :param description: The description of this TaskBasicRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def task_tag(self):
        """Gets the task_tag of this TaskBasicRequestBody.

        任务标签,只能包含字母、数字、中划线、下划线

        :return: The task_tag of this TaskBasicRequestBody.
        :rtype: str
        """
        return self._task_tag

    @task_tag.setter
    def task_tag(self, task_tag):
        """Sets the task_tag of this TaskBasicRequestBody.

        任务标签,只能包含字母、数字、中划线、下划线

        :param task_tag: The task_tag of this TaskBasicRequestBody.
        :type task_tag: str
        """
        self._task_tag = task_tag

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
        if not isinstance(other, TaskBasicRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
