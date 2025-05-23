# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTaskResponse(SdkResponse):

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
        r"""UpdateTaskResponse

        The model defined in huaweicloud sdk

        :param code: 响应码
        :type code: str
        :param message: 响应消息
        :type message: str
        :param task_info: 
        :type task_info: :class:`huaweicloudsdkcpts.v1.TaskInfo`
        """
        
        super(UpdateTaskResponse, self).__init__()

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
        r"""Gets the code of this UpdateTaskResponse.

        响应码

        :return: The code of this UpdateTaskResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this UpdateTaskResponse.

        响应码

        :param code: The code of this UpdateTaskResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        r"""Gets the message of this UpdateTaskResponse.

        响应消息

        :return: The message of this UpdateTaskResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this UpdateTaskResponse.

        响应消息

        :param message: The message of this UpdateTaskResponse.
        :type message: str
        """
        self._message = message

    @property
    def task_info(self):
        r"""Gets the task_info of this UpdateTaskResponse.

        :return: The task_info of this UpdateTaskResponse.
        :rtype: :class:`huaweicloudsdkcpts.v1.TaskInfo`
        """
        return self._task_info

    @task_info.setter
    def task_info(self, task_info):
        r"""Sets the task_info of this UpdateTaskResponse.

        :param task_info: The task_info of this UpdateTaskResponse.
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
        if not isinstance(other, UpdateTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
