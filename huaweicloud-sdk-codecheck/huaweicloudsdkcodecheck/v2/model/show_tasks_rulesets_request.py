# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTasksRulesetsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'task_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'task_id': 'task_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, project_id=None, task_id=None, offset=None, limit=None):
        """ShowTasksRulesetsRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param task_id: 任务ID
        :type task_id: str
        :param offset: 分页索引，偏移量
        :type offset: int
        :param limit: 每页显示的数量,每页最多显示1000条
        :type limit: int
        """
        
        

        self._project_id = None
        self._task_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.project_id = project_id
        self.task_id = task_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def project_id(self):
        """Gets the project_id of this ShowTasksRulesetsRequest.

        项目ID

        :return: The project_id of this ShowTasksRulesetsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ShowTasksRulesetsRequest.

        项目ID

        :param project_id: The project_id of this ShowTasksRulesetsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def task_id(self):
        """Gets the task_id of this ShowTasksRulesetsRequest.

        任务ID

        :return: The task_id of this ShowTasksRulesetsRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ShowTasksRulesetsRequest.

        任务ID

        :param task_id: The task_id of this ShowTasksRulesetsRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def offset(self):
        """Gets the offset of this ShowTasksRulesetsRequest.

        分页索引，偏移量

        :return: The offset of this ShowTasksRulesetsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowTasksRulesetsRequest.

        分页索引，偏移量

        :param offset: The offset of this ShowTasksRulesetsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowTasksRulesetsRequest.

        每页显示的数量,每页最多显示1000条

        :return: The limit of this ShowTasksRulesetsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowTasksRulesetsRequest.

        每页显示的数量,每页最多显示1000条

        :param limit: The limit of this ShowTasksRulesetsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ShowTasksRulesetsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
