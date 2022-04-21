# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTakeOverTaskDetailsRequest:

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
        'page': 'int',
        'size': 'int'
    }

    attribute_map = {
        'task_id': 'task_id',
        'page': 'page',
        'size': 'size'
    }

    def __init__(self, task_id=None, page=None, size=None):
        """ShowTakeOverTaskDetailsRequest

        The model defined in huaweicloud sdk

        :param task_id: 任务ID。
        :type task_id: str
        :param page: 分页编号，默认为0。
        :type page: int
        :param size: 每页记录数。  默认10，范围[1,100]
        :type size: int
        """
        
        

        self._task_id = None
        self._page = None
        self._size = None
        self.discriminator = None

        self.task_id = task_id
        if page is not None:
            self.page = page
        if size is not None:
            self.size = size

    @property
    def task_id(self):
        """Gets the task_id of this ShowTakeOverTaskDetailsRequest.

        任务ID。

        :return: The task_id of this ShowTakeOverTaskDetailsRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ShowTakeOverTaskDetailsRequest.

        任务ID。

        :param task_id: The task_id of this ShowTakeOverTaskDetailsRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def page(self):
        """Gets the page of this ShowTakeOverTaskDetailsRequest.

        分页编号，默认为0。

        :return: The page of this ShowTakeOverTaskDetailsRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ShowTakeOverTaskDetailsRequest.

        分页编号，默认为0。

        :param page: The page of this ShowTakeOverTaskDetailsRequest.
        :type page: int
        """
        self._page = page

    @property
    def size(self):
        """Gets the size of this ShowTakeOverTaskDetailsRequest.

        每页记录数。  默认10，范围[1,100]

        :return: The size of this ShowTakeOverTaskDetailsRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ShowTakeOverTaskDetailsRequest.

        每页记录数。  默认10，范围[1,100]

        :param size: The size of this ShowTakeOverTaskDetailsRequest.
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
        if not isinstance(other, ShowTakeOverTaskDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
