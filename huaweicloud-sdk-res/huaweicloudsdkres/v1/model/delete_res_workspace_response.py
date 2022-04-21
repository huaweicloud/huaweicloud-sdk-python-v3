# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteResWorkspaceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'message': 'str',
        'error_code': 'str'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'error_code': 'error_code'
    }

    def __init__(self, is_success=None, message=None, error_code=None):
        """DeleteResWorkspaceResponse

        The model defined in huaweicloud sdk

        :param is_success: 是否成功。
        :type is_success: bool
        :param message: 返回消息。
        :type message: str
        :param error_code: 错误码（请求成功时，不返回此字段）。
        :type error_code: str
        """
        
        super(DeleteResWorkspaceResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._error_code = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if error_code is not None:
            self.error_code = error_code

    @property
    def is_success(self):
        """Gets the is_success of this DeleteResWorkspaceResponse.

        是否成功。

        :return: The is_success of this DeleteResWorkspaceResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this DeleteResWorkspaceResponse.

        是否成功。

        :param is_success: The is_success of this DeleteResWorkspaceResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        """Gets the message of this DeleteResWorkspaceResponse.

        返回消息。

        :return: The message of this DeleteResWorkspaceResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this DeleteResWorkspaceResponse.

        返回消息。

        :param message: The message of this DeleteResWorkspaceResponse.
        :type message: str
        """
        self._message = message

    @property
    def error_code(self):
        """Gets the error_code of this DeleteResWorkspaceResponse.

        错误码（请求成功时，不返回此字段）。

        :return: The error_code of this DeleteResWorkspaceResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this DeleteResWorkspaceResponse.

        错误码（请求成功时，不返回此字段）。

        :param error_code: The error_code of this DeleteResWorkspaceResponse.
        :type error_code: str
        """
        self._error_code = error_code

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
        if not isinstance(other, DeleteResWorkspaceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
