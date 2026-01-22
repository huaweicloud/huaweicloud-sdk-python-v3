# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPullTasksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'offset': 'int',
        'limit': 'int',
        'task_id': 'str'
    }

    attribute_map = {
        'region': 'region',
        'offset': 'offset',
        'limit': 'limit',
        'task_id': 'task_id'
    }

    def __init__(self, region=None, offset=None, limit=None, task_id=None):
        r"""ListPullTasksRequest

        The model defined in huaweicloud sdk

        :param region: 任务所在区域
        :type region: str
        :param offset: 偏移量
        :type offset: int
        :param limit: 每页记录数
        :type limit: int
        :param task_id: 任务id
        :type task_id: str
        """
        
        

        self._region = None
        self._offset = None
        self._limit = None
        self._task_id = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if task_id is not None:
            self.task_id = task_id

    @property
    def region(self):
        r"""Gets the region of this ListPullTasksRequest.

        任务所在区域

        :return: The region of this ListPullTasksRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListPullTasksRequest.

        任务所在区域

        :param region: The region of this ListPullTasksRequest.
        :type region: str
        """
        self._region = region

    @property
    def offset(self):
        r"""Gets the offset of this ListPullTasksRequest.

        偏移量

        :return: The offset of this ListPullTasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPullTasksRequest.

        偏移量

        :param offset: The offset of this ListPullTasksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListPullTasksRequest.

        每页记录数

        :return: The limit of this ListPullTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPullTasksRequest.

        每页记录数

        :param limit: The limit of this ListPullTasksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def task_id(self):
        r"""Gets the task_id of this ListPullTasksRequest.

        任务id

        :return: The task_id of this ListPullTasksRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ListPullTasksRequest.

        任务id

        :param task_id: The task_id of this ListPullTasksRequest.
        :type task_id: str
        """
        self._task_id = task_id

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
        if not isinstance(other, ListPullTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
