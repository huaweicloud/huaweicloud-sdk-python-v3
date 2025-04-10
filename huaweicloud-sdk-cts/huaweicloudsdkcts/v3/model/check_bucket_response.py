# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckBucketResponse:

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
        'error_message': 'str',
        'response_code': 'int',
        'success': 'bool'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_message': 'error_message',
        'response_code': 'response_code',
        'success': 'success'
    }

    def __init__(self, error_code=None, error_message=None, response_code=None, success=None):
        r"""CheckBucketResponse

        The model defined in huaweicloud sdk

        :param error_code: 错误码。
        :type error_code: str
        :param error_message: 错误信息。
        :type error_message: str
        :param response_code: 返回的http状态码。
        :type response_code: int
        :param success: 是否成功转储。
        :type success: bool
        """
        
        

        self._error_code = None
        self._error_message = None
        self._response_code = None
        self._success = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message
        if response_code is not None:
            self.response_code = response_code
        if success is not None:
            self.success = success

    @property
    def error_code(self):
        r"""Gets the error_code of this CheckBucketResponse.

        错误码。

        :return: The error_code of this CheckBucketResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this CheckBucketResponse.

        错误码。

        :param error_code: The error_code of this CheckBucketResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_message(self):
        r"""Gets the error_message of this CheckBucketResponse.

        错误信息。

        :return: The error_message of this CheckBucketResponse.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this CheckBucketResponse.

        错误信息。

        :param error_message: The error_message of this CheckBucketResponse.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def response_code(self):
        r"""Gets the response_code of this CheckBucketResponse.

        返回的http状态码。

        :return: The response_code of this CheckBucketResponse.
        :rtype: int
        """
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        r"""Sets the response_code of this CheckBucketResponse.

        返回的http状态码。

        :param response_code: The response_code of this CheckBucketResponse.
        :type response_code: int
        """
        self._response_code = response_code

    @property
    def success(self):
        r"""Gets the success of this CheckBucketResponse.

        是否成功转储。

        :return: The success of this CheckBucketResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this CheckBucketResponse.

        是否成功转储。

        :param success: The success of this CheckBucketResponse.
        :type success: bool
        """
        self._success = success

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
        if not isinstance(other, CheckBucketResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
