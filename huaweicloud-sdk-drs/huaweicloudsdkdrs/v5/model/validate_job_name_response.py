# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidateJobNameResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_valid': 'bool',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'is_valid': 'is_valid',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, is_valid=None, error_code=None, error_msg=None):
        r"""ValidateJobNameResponse

        The model defined in huaweicloud sdk

        :param is_valid: 任务名称是否有效。
        :type is_valid: bool
        :param error_code: 错误码。
        :type error_code: str
        :param error_msg: 错误信息。
        :type error_msg: str
        """
        
        super(ValidateJobNameResponse, self).__init__()

        self._is_valid = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if is_valid is not None:
            self.is_valid = is_valid
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def is_valid(self):
        r"""Gets the is_valid of this ValidateJobNameResponse.

        任务名称是否有效。

        :return: The is_valid of this ValidateJobNameResponse.
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        r"""Sets the is_valid of this ValidateJobNameResponse.

        任务名称是否有效。

        :param is_valid: The is_valid of this ValidateJobNameResponse.
        :type is_valid: bool
        """
        self._is_valid = is_valid

    @property
    def error_code(self):
        r"""Gets the error_code of this ValidateJobNameResponse.

        错误码。

        :return: The error_code of this ValidateJobNameResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ValidateJobNameResponse.

        错误码。

        :param error_code: The error_code of this ValidateJobNameResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ValidateJobNameResponse.

        错误信息。

        :return: The error_msg of this ValidateJobNameResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ValidateJobNameResponse.

        错误信息。

        :param error_msg: The error_msg of this ValidateJobNameResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, ValidateJobNameResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
