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
        """ShowTaskSetResponse

        The model defined in huaweicloud sdk

        :param code: code
        :type code: str
        :param extend: extend
        :type extend: list[str]
        :param message: message
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
        """Gets the code of this ShowTaskSetResponse.

        code

        :return: The code of this ShowTaskSetResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ShowTaskSetResponse.

        code

        :param code: The code of this ShowTaskSetResponse.
        :type code: str
        """
        self._code = code

    @property
    def extend(self):
        """Gets the extend of this ShowTaskSetResponse.

        extend

        :return: The extend of this ShowTaskSetResponse.
        :rtype: list[str]
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        """Sets the extend of this ShowTaskSetResponse.

        extend

        :param extend: The extend of this ShowTaskSetResponse.
        :type extend: list[str]
        """
        self._extend = extend

    @property
    def message(self):
        """Gets the message of this ShowTaskSetResponse.

        message

        :return: The message of this ShowTaskSetResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ShowTaskSetResponse.

        message

        :param message: The message of this ShowTaskSetResponse.
        :type message: str
        """
        self._message = message

    @property
    def tasks(self):
        """Gets the tasks of this ShowTaskSetResponse.

        工程集详细信息

        :return: The tasks of this ShowTaskSetResponse.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.Task`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this ShowTaskSetResponse.

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
