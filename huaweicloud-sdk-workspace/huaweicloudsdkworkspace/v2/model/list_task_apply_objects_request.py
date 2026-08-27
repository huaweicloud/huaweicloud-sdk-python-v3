# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTaskApplyObjectsRequest:

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
        'object_name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'task_id': 'task_id',
        'object_name': 'object_name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, task_id=None, object_name=None, offset=None, limit=None):
        r"""ListTaskApplyObjectsRequest

        The model defined in huaweicloud sdk

        :param task_id: 任务ID（精确查询）
        :type task_id: str
        :param object_name: 应用对象名称（支持模糊查询）
        :type object_name: str
        :param offset: 偏移量，默认0
        :type offset: int
        :param limit: 每页数量，默认10，最大100
        :type limit: int
        """
        
        

        self._task_id = None
        self._object_name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.task_id = task_id
        if object_name is not None:
            self.object_name = object_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def task_id(self):
        r"""Gets the task_id of this ListTaskApplyObjectsRequest.

        任务ID（精确查询）

        :return: The task_id of this ListTaskApplyObjectsRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ListTaskApplyObjectsRequest.

        任务ID（精确查询）

        :param task_id: The task_id of this ListTaskApplyObjectsRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def object_name(self):
        r"""Gets the object_name of this ListTaskApplyObjectsRequest.

        应用对象名称（支持模糊查询）

        :return: The object_name of this ListTaskApplyObjectsRequest.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        r"""Sets the object_name of this ListTaskApplyObjectsRequest.

        应用对象名称（支持模糊查询）

        :param object_name: The object_name of this ListTaskApplyObjectsRequest.
        :type object_name: str
        """
        self._object_name = object_name

    @property
    def offset(self):
        r"""Gets the offset of this ListTaskApplyObjectsRequest.

        偏移量，默认0

        :return: The offset of this ListTaskApplyObjectsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTaskApplyObjectsRequest.

        偏移量，默认0

        :param offset: The offset of this ListTaskApplyObjectsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListTaskApplyObjectsRequest.

        每页数量，默认10，最大100

        :return: The limit of this ListTaskApplyObjectsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTaskApplyObjectsRequest.

        每页数量，默认10，最大100

        :param limit: The limit of this ListTaskApplyObjectsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListTaskApplyObjectsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
