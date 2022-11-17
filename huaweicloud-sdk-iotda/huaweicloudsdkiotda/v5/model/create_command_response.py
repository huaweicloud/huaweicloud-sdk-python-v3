# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCommandResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'command_id': 'str',
        'response': 'object'
    }

    attribute_map = {
        'command_id': 'command_id',
        'response': 'response'
    }

    def __init__(self, command_id=None, response=None):
        """CreateCommandResponse

        The model defined in huaweicloud sdk

        :param command_id: 设备命令ID，用于唯一标识一条命令，在下发设备命令时由物联网平台分配获得。
        :type command_id: str
        :param response: 设备上报的命令执行结果。Json格式，具体格式需要应用和设备约定。
        :type response: object
        """
        
        super(CreateCommandResponse, self).__init__()

        self._command_id = None
        self._response = None
        self.discriminator = None

        if command_id is not None:
            self.command_id = command_id
        if response is not None:
            self.response = response

    @property
    def command_id(self):
        """Gets the command_id of this CreateCommandResponse.

        设备命令ID，用于唯一标识一条命令，在下发设备命令时由物联网平台分配获得。

        :return: The command_id of this CreateCommandResponse.
        :rtype: str
        """
        return self._command_id

    @command_id.setter
    def command_id(self, command_id):
        """Sets the command_id of this CreateCommandResponse.

        设备命令ID，用于唯一标识一条命令，在下发设备命令时由物联网平台分配获得。

        :param command_id: The command_id of this CreateCommandResponse.
        :type command_id: str
        """
        self._command_id = command_id

    @property
    def response(self):
        """Gets the response of this CreateCommandResponse.

        设备上报的命令执行结果。Json格式，具体格式需要应用和设备约定。

        :return: The response of this CreateCommandResponse.
        :rtype: object
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this CreateCommandResponse.

        设备上报的命令执行结果。Json格式，具体格式需要应用和设备约定。

        :param response: The response of this CreateCommandResponse.
        :type response: object
        """
        self._response = response

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
        if not isinstance(other, CreateCommandResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
