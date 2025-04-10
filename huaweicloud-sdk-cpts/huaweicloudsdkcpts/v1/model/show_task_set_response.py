# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskSetResponse(SdkResponse):

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
        'extend': 'list[str]',
        'message': 'str',
        'tasks': 'list[Task]'
    }

    attribute_map = {
        'code': 'code',
        'extend': 'extend',
        'message': 'message',
        'tasks': 'tasks'
    }

    def __init__(self, code=None, extend=None, message=None, tasks=None):
        r"""ShowTaskSetResponse

        The model defined in huaweicloud sdk

        :param code: 响应码
        :type code: str
        :param extend: 扩展信息
        :type extend: list[str]
        :param message: 响应消息
        :type message: str
        :param tasks: 工程集详细信息
        :type tasks: list[:class:`huaweicloudsdkcpts.v1.Task`]
        """
        
        super(ShowTaskSetResponse, self).__init__()

        self._code = None
        self._extend = None
        self._message = None
        self._tasks = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if extend is not None:
            self.extend = extend
        if message is not None:
            self.message = message
        if tasks is not None:
            self.tasks = tasks

    @property
    def code(self):
        r"""Gets the code of this ShowTaskSetResponse.

        响应码

        :return: The code of this ShowTaskSetResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ShowTaskSetResponse.

        响应码

        :param code: The code of this ShowTaskSetResponse.
        :type code: str
        """
        self._code = code

    @property
    def extend(self):
        r"""Gets the extend of this ShowTaskSetResponse.

        扩展信息

        :return: The extend of this ShowTaskSetResponse.
        :rtype: list[str]
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        r"""Sets the extend of this ShowTaskSetResponse.

        扩展信息

        :param extend: The extend of this ShowTaskSetResponse.
        :type extend: list[str]
        """
        self._extend = extend

    @property
    def message(self):
        r"""Gets the message of this ShowTaskSetResponse.

        响应消息

        :return: The message of this ShowTaskSetResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ShowTaskSetResponse.

        响应消息

        :param message: The message of this ShowTaskSetResponse.
        :type message: str
        """
        self._message = message

    @property
    def tasks(self):
        r"""Gets the tasks of this ShowTaskSetResponse.

        工程集详细信息

        :return: The tasks of this ShowTaskSetResponse.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.Task`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        r"""Sets the tasks of this ShowTaskSetResponse.

        工程集详细信息

        :param tasks: The tasks of this ShowTaskSetResponse.
        :type tasks: list[:class:`huaweicloudsdkcpts.v1.Task`]
        """
        self._tasks = tasks

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
        if not isinstance(other, ShowTaskSetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
