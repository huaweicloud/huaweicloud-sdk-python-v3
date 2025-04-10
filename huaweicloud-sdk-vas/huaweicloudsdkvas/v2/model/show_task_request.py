# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_name': 'str',
        'task_id': 'str'
    }

    attribute_map = {
        'service_name': 'service_name',
        'task_id': 'task_id'
    }

    def __init__(self, service_name=None, task_id=None):
        r"""ShowTaskRequest

        The model defined in huaweicloud sdk

        :param service_name: 服务名称
        :type service_name: str
        :param task_id: 指定的服务作业ID
        :type task_id: str
        """
        
        

        self._service_name = None
        self._task_id = None
        self.discriminator = None

        self.service_name = service_name
        self.task_id = task_id

    @property
    def service_name(self):
        r"""Gets the service_name of this ShowTaskRequest.

        服务名称

        :return: The service_name of this ShowTaskRequest.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this ShowTaskRequest.

        服务名称

        :param service_name: The service_name of this ShowTaskRequest.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowTaskRequest.

        指定的服务作业ID

        :return: The task_id of this ShowTaskRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowTaskRequest.

        指定的服务作业ID

        :param task_id: The task_id of this ShowTaskRequest.
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
        if not isinstance(other, ShowTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
