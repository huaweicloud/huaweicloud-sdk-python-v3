# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScheduledTasksRecordsDetailsRequest:

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
        'record_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'task_id': 'task_id',
        'record_id': 'record_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, task_id=None, record_id=None, offset=None, limit=None):
        r"""ListScheduledTasksRecordsDetailsRequest

        The model defined in huaweicloud sdk

        :param task_id: 任务ID。
        :type task_id: str
        :param record_id: 任务执行记录ID。
        :type record_id: str
        :param offset: 用于分页查询，查询的起始记录序号，从0开始。
        :type offset: int
        :param limit: 用于分页查询，每页返回的个数，取值范围0~100。
        :type limit: int
        """
        
        

        self._task_id = None
        self._record_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.task_id = task_id
        self.record_id = record_id
        self.offset = offset
        self.limit = limit

    @property
    def task_id(self):
        r"""Gets the task_id of this ListScheduledTasksRecordsDetailsRequest.

        任务ID。

        :return: The task_id of this ListScheduledTasksRecordsDetailsRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ListScheduledTasksRecordsDetailsRequest.

        任务ID。

        :param task_id: The task_id of this ListScheduledTasksRecordsDetailsRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def record_id(self):
        r"""Gets the record_id of this ListScheduledTasksRecordsDetailsRequest.

        任务执行记录ID。

        :return: The record_id of this ListScheduledTasksRecordsDetailsRequest.
        :rtype: str
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        r"""Sets the record_id of this ListScheduledTasksRecordsDetailsRequest.

        任务执行记录ID。

        :param record_id: The record_id of this ListScheduledTasksRecordsDetailsRequest.
        :type record_id: str
        """
        self._record_id = record_id

    @property
    def offset(self):
        r"""Gets the offset of this ListScheduledTasksRecordsDetailsRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :return: The offset of this ListScheduledTasksRecordsDetailsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListScheduledTasksRecordsDetailsRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :param offset: The offset of this ListScheduledTasksRecordsDetailsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListScheduledTasksRecordsDetailsRequest.

        用于分页查询，每页返回的个数，取值范围0~100。

        :return: The limit of this ListScheduledTasksRecordsDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListScheduledTasksRecordsDetailsRequest.

        用于分页查询，每页返回的个数，取值范围0~100。

        :param limit: The limit of this ListScheduledTasksRecordsDetailsRequest.
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
        if not isinstance(other, ListScheduledTasksRecordsDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
