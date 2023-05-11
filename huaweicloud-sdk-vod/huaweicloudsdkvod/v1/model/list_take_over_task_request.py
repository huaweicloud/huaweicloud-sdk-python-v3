# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTakeOverTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'task_id': 'str',
        'page': 'int',
        'size': 'int'
    }

    attribute_map = {
        'status': 'status',
        'task_id': 'task_id',
        'page': 'page',
        'size': 'size'
    }

    def __init__(self, status=None, task_id=None, page=None, size=None):
        """ListTakeOverTaskRequest

        The model defined in huaweicloud sdk

        :param status: 任务状态。
        :type status: str
        :param task_id: 任务ID。
        :type task_id: str
        :param page: 分页编号，默认为0。
        :type page: int
        :param size: 每页记录数。  默认10，范围[1,100]，指定task_id时该参数无效。
        :type size: int
        """
        
        

        self._status = None
        self._task_id = None
        self._page = None
        self._size = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if task_id is not None:
            self.task_id = task_id
        if page is not None:
            self.page = page
        if size is not None:
            self.size = size

    @property
    def status(self):
        """Gets the status of this ListTakeOverTaskRequest.

        任务状态。

        :return: The status of this ListTakeOverTaskRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListTakeOverTaskRequest.

        任务状态。

        :param status: The status of this ListTakeOverTaskRequest.
        :type status: str
        """
        self._status = status

    @property
    def task_id(self):
        """Gets the task_id of this ListTakeOverTaskRequest.

        任务ID。

        :return: The task_id of this ListTakeOverTaskRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ListTakeOverTaskRequest.

        任务ID。

        :param task_id: The task_id of this ListTakeOverTaskRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def page(self):
        """Gets the page of this ListTakeOverTaskRequest.

        分页编号，默认为0。

        :return: The page of this ListTakeOverTaskRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListTakeOverTaskRequest.

        分页编号，默认为0。

        :param page: The page of this ListTakeOverTaskRequest.
        :type page: int
        """
        self._page = page

    @property
    def size(self):
        """Gets the size of this ListTakeOverTaskRequest.

        每页记录数。  默认10，范围[1,100]，指定task_id时该参数无效。

        :return: The size of this ListTakeOverTaskRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListTakeOverTaskRequest.

        每页记录数。  默认10，范围[1,100]，指定task_id时该参数无效。

        :param size: The size of this ListTakeOverTaskRequest.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, ListTakeOverTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
