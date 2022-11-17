# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'task_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'task_name': 'task_name'
    }

    def __init__(self, id=None, task_name=None):
        """CreateTaskResponse

        The model defined in huaweicloud sdk

        :param id: 任务ID。
        :type id: int
        :param task_name: 任务名称。
        :type task_name: str
        """
        
        super(CreateTaskResponse, self).__init__()

        self._id = None
        self._task_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if task_name is not None:
            self.task_name = task_name

    @property
    def id(self):
        """Gets the id of this CreateTaskResponse.

        任务ID。

        :return: The id of this CreateTaskResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateTaskResponse.

        任务ID。

        :param id: The id of this CreateTaskResponse.
        :type id: int
        """
        self._id = id

    @property
    def task_name(self):
        """Gets the task_name of this CreateTaskResponse.

        任务名称。

        :return: The task_name of this CreateTaskResponse.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this CreateTaskResponse.

        任务名称。

        :param task_name: The task_name of this CreateTaskResponse.
        :type task_name: str
        """
        self._task_name = task_name

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
        if not isinstance(other, CreateTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
