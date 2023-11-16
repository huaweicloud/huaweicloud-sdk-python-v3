# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteUnblockIpResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_code': 'str',
        'message': 'str'
    }

    attribute_map = {
        'error_code': 'error_code',
        'message': 'message'
    }

    def __init__(self, error_code=None, message=None):
        """ExecuteUnblockIpResponse

        The model defined in huaweicloud sdk

        :param error_code: 业务错误码
        :type error_code: str
        :param message: 描述信息
        :type message: str
        """
        
        super(ExecuteUnblockIpResponse, self).__init__()

        self._error_code = None
        self._message = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if message is not None:
            self.message = message

    @property
    def error_code(self):
        """Gets the error_code of this ExecuteUnblockIpResponse.

        业务错误码

        :return: The error_code of this ExecuteUnblockIpResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ExecuteUnblockIpResponse.

        业务错误码

        :param error_code: The error_code of this ExecuteUnblockIpResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def message(self):
        """Gets the message of this ExecuteUnblockIpResponse.

        描述信息

        :return: The message of this ExecuteUnblockIpResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ExecuteUnblockIpResponse.

        描述信息

        :param message: The message of this ExecuteUnblockIpResponse.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, ExecuteUnblockIpResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
