# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MultiTaskUpdateBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'task_tag': 'str',
        'operation_types': 'list[str]',
        'repulling_snapshot': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'task_tag': 'task_tag',
        'operation_types': 'operation_types',
        'repulling_snapshot': 'repulling_snapshot'
    }

    def __init__(self, description=None, task_tag=None, operation_types=None, repulling_snapshot=None):
        """MultiTaskUpdateBody

        The model defined in huaweicloud sdk

        :param description: 描述信息
        :type description: str
        :param task_tag: 任务标签,只能包含字母、数字、中划线、下划线
        :type task_tag: str
        :param operation_types: 需要支持的操作类型，支持多选，至少需要选择以下一种： - INSERT - UPDATE - DELETE
        :type operation_types: list[str]
        :param repulling_snapshot: 是否同步已有数据，仅在编辑任务时生效
        :type repulling_snapshot: bool
        """
        
        

        self._description = None
        self._task_tag = None
        self._operation_types = None
        self._repulling_snapshot = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if task_tag is not None:
            self.task_tag = task_tag
        if operation_types is not None:
            self.operation_types = operation_types
        if repulling_snapshot is not None:
            self.repulling_snapshot = repulling_snapshot

    @property
    def description(self):
        """Gets the description of this MultiTaskUpdateBody.

        描述信息

        :return: The description of this MultiTaskUpdateBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MultiTaskUpdateBody.

        描述信息

        :param description: The description of this MultiTaskUpdateBody.
        :type description: str
        """
        self._description = description

    @property
    def task_tag(self):
        """Gets the task_tag of this MultiTaskUpdateBody.

        任务标签,只能包含字母、数字、中划线、下划线

        :return: The task_tag of this MultiTaskUpdateBody.
        :rtype: str
        """
        return self._task_tag

    @task_tag.setter
    def task_tag(self, task_tag):
        """Sets the task_tag of this MultiTaskUpdateBody.

        任务标签,只能包含字母、数字、中划线、下划线

        :param task_tag: The task_tag of this MultiTaskUpdateBody.
        :type task_tag: str
        """
        self._task_tag = task_tag

    @property
    def operation_types(self):
        """Gets the operation_types of this MultiTaskUpdateBody.

        需要支持的操作类型，支持多选，至少需要选择以下一种： - INSERT - UPDATE - DELETE

        :return: The operation_types of this MultiTaskUpdateBody.
        :rtype: list[str]
        """
        return self._operation_types

    @operation_types.setter
    def operation_types(self, operation_types):
        """Sets the operation_types of this MultiTaskUpdateBody.

        需要支持的操作类型，支持多选，至少需要选择以下一种： - INSERT - UPDATE - DELETE

        :param operation_types: The operation_types of this MultiTaskUpdateBody.
        :type operation_types: list[str]
        """
        self._operation_types = operation_types

    @property
    def repulling_snapshot(self):
        """Gets the repulling_snapshot of this MultiTaskUpdateBody.

        是否同步已有数据，仅在编辑任务时生效

        :return: The repulling_snapshot of this MultiTaskUpdateBody.
        :rtype: bool
        """
        return self._repulling_snapshot

    @repulling_snapshot.setter
    def repulling_snapshot(self, repulling_snapshot):
        """Sets the repulling_snapshot of this MultiTaskUpdateBody.

        是否同步已有数据，仅在编辑任务时生效

        :param repulling_snapshot: The repulling_snapshot of this MultiTaskUpdateBody.
        :type repulling_snapshot: bool
        """
        self._repulling_snapshot = repulling_snapshot

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
        if not isinstance(other, MultiTaskUpdateBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
