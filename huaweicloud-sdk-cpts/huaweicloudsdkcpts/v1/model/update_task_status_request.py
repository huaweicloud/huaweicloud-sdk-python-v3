# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTaskStatusRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'test_suite_id': 'int',
        'task_id': 'int',
        'body': 'UpdateTaskStatusRequestBody'
    }

    attribute_map = {
        'test_suite_id': 'test_suite_id',
        'task_id': 'task_id',
        'body': 'body'
    }

    def __init__(self, test_suite_id=None, task_id=None, body=None):
        """UpdateTaskStatusRequest

        The model defined in huaweicloud sdk

        :param test_suite_id: 测试工程id
        :type test_suite_id: int
        :param task_id: 任务id
        :type task_id: int
        :param body: Body of the UpdateTaskStatusRequest
        :type body: :class:`huaweicloudsdkcpts.v1.UpdateTaskStatusRequestBody`
        """
        
        

        self._test_suite_id = None
        self._task_id = None
        self._body = None
        self.discriminator = None

        self.test_suite_id = test_suite_id
        self.task_id = task_id
        if body is not None:
            self.body = body

    @property
    def test_suite_id(self):
        """Gets the test_suite_id of this UpdateTaskStatusRequest.

        测试工程id

        :return: The test_suite_id of this UpdateTaskStatusRequest.
        :rtype: int
        """
        return self._test_suite_id

    @test_suite_id.setter
    def test_suite_id(self, test_suite_id):
        """Sets the test_suite_id of this UpdateTaskStatusRequest.

        测试工程id

        :param test_suite_id: The test_suite_id of this UpdateTaskStatusRequest.
        :type test_suite_id: int
        """
        self._test_suite_id = test_suite_id

    @property
    def task_id(self):
        """Gets the task_id of this UpdateTaskStatusRequest.

        任务id

        :return: The task_id of this UpdateTaskStatusRequest.
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this UpdateTaskStatusRequest.

        任务id

        :param task_id: The task_id of this UpdateTaskStatusRequest.
        :type task_id: int
        """
        self._task_id = task_id

    @property
    def body(self):
        """Gets the body of this UpdateTaskStatusRequest.

        :return: The body of this UpdateTaskStatusRequest.
        :rtype: :class:`huaweicloudsdkcpts.v1.UpdateTaskStatusRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateTaskStatusRequest.

        :param body: The body of this UpdateTaskStatusRequest.
        :type body: :class:`huaweicloudsdkcpts.v1.UpdateTaskStatusRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateTaskStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
