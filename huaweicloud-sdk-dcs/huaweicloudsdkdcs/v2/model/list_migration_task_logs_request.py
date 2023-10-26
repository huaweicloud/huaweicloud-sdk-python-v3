# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMigrationTaskLogsRequest:

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
        'offset': 'int',
        'limit': 'int',
        'log_level': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'offset': 'offset',
        'limit': 'limit',
        'log_level': 'log_level'
    }

    def __init__(self, task_id=None, offset=None, limit=None, log_level=None):
        """ListMigrationTaskLogsRequest

        The model defined in huaweicloud sdk

        :param task_id: 任务ID
        :type task_id: str
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param log_level: 日志级别
        :type log_level: str
        """
        
        

        self._task_id = None
        self._offset = None
        self._limit = None
        self._log_level = None
        self.discriminator = None

        self.task_id = task_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if log_level is not None:
            self.log_level = log_level

    @property
    def task_id(self):
        """Gets the task_id of this ListMigrationTaskLogsRequest.

        任务ID

        :return: The task_id of this ListMigrationTaskLogsRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ListMigrationTaskLogsRequest.

        任务ID

        :param task_id: The task_id of this ListMigrationTaskLogsRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def offset(self):
        """Gets the offset of this ListMigrationTaskLogsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :return: The offset of this ListMigrationTaskLogsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListMigrationTaskLogsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :param offset: The offset of this ListMigrationTaskLogsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListMigrationTaskLogsRequest.

        每页显示的条目数量。

        :return: The limit of this ListMigrationTaskLogsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListMigrationTaskLogsRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListMigrationTaskLogsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def log_level(self):
        """Gets the log_level of this ListMigrationTaskLogsRequest.

        日志级别

        :return: The log_level of this ListMigrationTaskLogsRequest.
        :rtype: str
        """
        return self._log_level

    @log_level.setter
    def log_level(self, log_level):
        """Sets the log_level of this ListMigrationTaskLogsRequest.

        日志级别

        :param log_level: The log_level of this ListMigrationTaskLogsRequest.
        :type log_level: str
        """
        self._log_level = log_level

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
        if not isinstance(other, ListMigrationTaskLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
