# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVariablesResponse(SdkResponse):

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
        'variable_list': 'list[VariableDetail]'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'variable_list': 'variable_list'
    }

    def __init__(self, code=None, message=None, variable_list=None):
        """ListVariablesResponse

        The model defined in huaweicloud sdk

        :param code: 响应吗
        :type code: str
        :param message: 响应消息
        :type message: str
        :param variable_list: 变量列表
        :type variable_list: list[:class:`huaweicloudsdkcpts.v1.VariableDetail`]
        """
        
        super(ListVariablesResponse, self).__init__()

        self._code = None
        self._message = None
        self._variable_list = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if variable_list is not None:
            self.variable_list = variable_list

    @property
    def code(self):
        """Gets the code of this ListVariablesResponse.

        响应吗

        :return: The code of this ListVariablesResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ListVariablesResponse.

        响应吗

        :param code: The code of this ListVariablesResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        """Gets the message of this ListVariablesResponse.

        响应消息

        :return: The message of this ListVariablesResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ListVariablesResponse.

        响应消息

        :param message: The message of this ListVariablesResponse.
        :type message: str
        """
        self._message = message

    @property
    def variable_list(self):
        """Gets the variable_list of this ListVariablesResponse.

        变量列表

        :return: The variable_list of this ListVariablesResponse.
        :rtype: list[:class:`huaweicloudsdkcpts.v1.VariableDetail`]
        """
        return self._variable_list

    @variable_list.setter
    def variable_list(self, variable_list):
        """Sets the variable_list of this ListVariablesResponse.

        变量列表

        :param variable_list: The variable_list of this ListVariablesResponse.
        :type variable_list: list[:class:`huaweicloudsdkcpts.v1.VariableDetail`]
        """
        self._variable_list = variable_list

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
        if not isinstance(other, ListVariablesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
