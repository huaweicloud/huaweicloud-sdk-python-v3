# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteScheduleTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'task_id': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'task_id': 'task_id'
    }

    def __init__(self, x_language=None, task_id=None):
        r"""DeleteScheduleTaskRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言。
        :type x_language: str
        :param task_id: 任务id。
        :type task_id: str
        """
        
        

        self._x_language = None
        self._task_id = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.task_id = task_id

    @property
    def x_language(self):
        r"""Gets the x_language of this DeleteScheduleTaskRequest.

        语言。

        :return: The x_language of this DeleteScheduleTaskRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this DeleteScheduleTaskRequest.

        语言。

        :param x_language: The x_language of this DeleteScheduleTaskRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def task_id(self):
        r"""Gets the task_id of this DeleteScheduleTaskRequest.

        任务id。

        :return: The task_id of this DeleteScheduleTaskRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this DeleteScheduleTaskRequest.

        任务id。

        :param task_id: The task_id of this DeleteScheduleTaskRequest.
        :type task_id: str
        """
        self._task_id = task_id

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
        if not isinstance(other, DeleteScheduleTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
