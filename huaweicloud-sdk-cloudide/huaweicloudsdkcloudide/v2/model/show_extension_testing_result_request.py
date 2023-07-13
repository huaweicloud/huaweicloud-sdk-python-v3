# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowExtensionTestingResultRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_publisher_token')

    openapi_types = {
        'x_publisher_token': 'str',
        'task_id': 'str'
    }

    attribute_map = {
        'x_publisher_token': 'x-publisher-token',
        'task_id': 'task_id'
    }

    def __init__(self, x_publisher_token=None, task_id=None):
        """ShowExtensionTestingResultRequest

        The model defined in huaweicloud sdk

        :param x_publisher_token: 发布商凭证,x-publisher-token和X-Auth-Token必传一个
        :type x_publisher_token: str
        :param task_id: 任务id
        :type task_id: str
        """
        
        

        self._x_publisher_token = None
        self._task_id = None
        self.discriminator = None

        if x_publisher_token is not None:
            self.x_publisher_token = x_publisher_token
        self.task_id = task_id

    @property
    def x_publisher_token(self):
        """Gets the x_publisher_token of this ShowExtensionTestingResultRequest.

        发布商凭证,x-publisher-token和X-Auth-Token必传一个

        :return: The x_publisher_token of this ShowExtensionTestingResultRequest.
        :rtype: str
        """
        return self._x_publisher_token

    @x_publisher_token.setter
    def x_publisher_token(self, x_publisher_token):
        """Sets the x_publisher_token of this ShowExtensionTestingResultRequest.

        发布商凭证,x-publisher-token和X-Auth-Token必传一个

        :param x_publisher_token: The x_publisher_token of this ShowExtensionTestingResultRequest.
        :type x_publisher_token: str
        """
        self._x_publisher_token = x_publisher_token

    @property
    def task_id(self):
        """Gets the task_id of this ShowExtensionTestingResultRequest.

        任务id

        :return: The task_id of this ShowExtensionTestingResultRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ShowExtensionTestingResultRequest.

        任务id

        :param task_id: The task_id of this ShowExtensionTestingResultRequest.
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
        if not isinstance(other, ShowExtensionTestingResultRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
