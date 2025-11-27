# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListExportTasksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'task_id': 'str',
        'task_name': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'task_id': 'task_id',
        'task_name': 'task_name'
    }

    def __init__(self, limit=None, offset=None, task_id=None, task_name=None):
        r"""ListExportTasksRequest

        The model defined in huaweicloud sdk

        :param limit: - 每页显示的条目数量, 默认为10
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0
        :type offset: int
        :param task_id: 任务id
        :type task_id: str
        :param task_name: 任务名称
        :type task_name: str
        """
        
        

        self._limit = None
        self._offset = None
        self._task_id = None
        self._task_name = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.task_id = task_id
        self.task_name = task_name

    @property
    def limit(self):
        r"""Gets the limit of this ListExportTasksRequest.

        - 每页显示的条目数量, 默认为10

        :return: The limit of this ListExportTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListExportTasksRequest.

        - 每页显示的条目数量, 默认为10

        :param limit: The limit of this ListExportTasksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListExportTasksRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0

        :return: The offset of this ListExportTasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListExportTasksRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0

        :param offset: The offset of this ListExportTasksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def task_id(self):
        r"""Gets the task_id of this ListExportTasksRequest.

        任务id

        :return: The task_id of this ListExportTasksRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ListExportTasksRequest.

        任务id

        :param task_id: The task_id of this ListExportTasksRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        r"""Gets the task_name of this ListExportTasksRequest.

        任务名称

        :return: The task_name of this ListExportTasksRequest.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this ListExportTasksRequest.

        任务名称

        :param task_name: The task_name of this ListExportTasksRequest.
        :type task_name: str
        """
        self._task_name = task_name

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListExportTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
