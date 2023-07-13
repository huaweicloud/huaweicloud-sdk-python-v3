# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCaseRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'int',
        'task_id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'task_id': 'task_id'
    }

    def __init__(self, name=None, type=None, task_id=None):
        """CreateCaseRequestBody

        The model defined in huaweicloud sdk

        :param name: name
        :type name: str
        :param type: type（0-常规用例，1-视频流用例，2-预制用例）
        :type type: int
        :param task_id: task_id
        :type task_id: int
        """
        
        

        self._name = None
        self._type = None
        self._task_id = None
        self.discriminator = None

        self.name = name
        self.type = type
        self.task_id = task_id

    @property
    def name(self):
        """Gets the name of this CreateCaseRequestBody.

        name

        :return: The name of this CreateCaseRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateCaseRequestBody.

        name

        :param name: The name of this CreateCaseRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this CreateCaseRequestBody.

        type（0-常规用例，1-视频流用例，2-预制用例）

        :return: The type of this CreateCaseRequestBody.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateCaseRequestBody.

        type（0-常规用例，1-视频流用例，2-预制用例）

        :param type: The type of this CreateCaseRequestBody.
        :type type: int
        """
        self._type = type

    @property
    def task_id(self):
        """Gets the task_id of this CreateCaseRequestBody.

        task_id

        :return: The task_id of this CreateCaseRequestBody.
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this CreateCaseRequestBody.

        task_id

        :param task_id: The task_id of this CreateCaseRequestBody.
        :type task_id: int
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
        if not isinstance(other, CreateCaseRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
