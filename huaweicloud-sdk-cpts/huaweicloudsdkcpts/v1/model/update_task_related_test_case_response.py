# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTaskRelatedTestCaseResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'message': 'str',
        'task_info': 'TaskInfo'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'task_info': 'taskInfo'
    }

    def __init__(self, code=None, message=None, task_info=None):
        """UpdateTaskRelatedTestCaseResponse

        The model defined in huaweicloud sdk

        :param code: code
        :type code: str
        :param message: message
        :type message: str
        :param task_info: 
        :type task_info: :class:`huaweicloudsdkcpts.v1.TaskInfo`
        """
        
        super(UpdateTaskRelatedTestCaseResponse, self).__init__()

        self._code = None
        self._message = None
        self._task_info = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if task_info is not None:
            self.task_info = task_info

    @property
    def code(self):
        """Gets the code of this UpdateTaskRelatedTestCaseResponse.

        code

        :return: The code of this UpdateTaskRelatedTestCaseResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this UpdateTaskRelatedTestCaseResponse.

        code

        :param code: The code of this UpdateTaskRelatedTestCaseResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        """Gets the message of this UpdateTaskRelatedTestCaseResponse.

        message

        :return: The message of this UpdateTaskRelatedTestCaseResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this UpdateTaskRelatedTestCaseResponse.

        message

        :param message: The message of this UpdateTaskRelatedTestCaseResponse.
        :type message: str
        """
        self._message = message

    @property
    def task_info(self):
        """Gets the task_info of this UpdateTaskRelatedTestCaseResponse.


        :return: The task_info of this UpdateTaskRelatedTestCaseResponse.
        :rtype: :class:`huaweicloudsdkcpts.v1.TaskInfo`
        """
        return self._task_info

    @task_info.setter
    def task_info(self, task_info):
        """Sets the task_info of this UpdateTaskRelatedTestCaseResponse.


        :param task_info: The task_info of this UpdateTaskRelatedTestCaseResponse.
        :type task_info: :class:`huaweicloudsdkcpts.v1.TaskInfo`
        """
        self._task_info = task_info

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
        if not isinstance(other, UpdateTaskRelatedTestCaseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
