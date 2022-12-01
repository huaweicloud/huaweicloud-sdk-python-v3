# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AcceptanceSchema:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'task_id': 'int'
    }

    attribute_map = {
        'request_id': 'request_id',
        'task_id': 'task_id'
    }

    def __init__(self, request_id=None, task_id=None):
        """AcceptanceSchema

        The model defined in huaweicloud sdk

        :param request_id: request_id
        :type request_id: str
        :param task_id: task_id
        :type task_id: int
        """
        
        

        self._request_id = None
        self._task_id = None
        self.discriminator = None

        self.request_id = request_id
        self.task_id = task_id

    @property
    def request_id(self):
        """Gets the request_id of this AcceptanceSchema.

        request_id

        :return: The request_id of this AcceptanceSchema.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this AcceptanceSchema.

        request_id

        :param request_id: The request_id of this AcceptanceSchema.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def task_id(self):
        """Gets the task_id of this AcceptanceSchema.

        task_id

        :return: The task_id of this AcceptanceSchema.
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this AcceptanceSchema.

        task_id

        :param task_id: The task_id of this AcceptanceSchema.
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
        if not isinstance(other, AcceptanceSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
