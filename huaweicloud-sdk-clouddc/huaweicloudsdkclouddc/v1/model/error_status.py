# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ErrorStatus:

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
        'error_msg': 'str',
        'error_type': 'str'
    }

    attribute_map = {
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'error_type': 'error_type'
    }

    def __init__(self, error_code=None, error_msg=None, error_type=None):
        r"""ErrorStatus

        The model defined in huaweicloud sdk

        :param error_code: 错误码
        :type error_code: str
        :param error_msg: 错误描述
        :type error_msg: str
        :param error_type: 错误类型
        :type error_type: str
        """
        
        

        self._error_code = None
        self._error_msg = None
        self._error_type = None
        self.discriminator = None

        self.error_code = error_code
        self.error_msg = error_msg
        self.error_type = error_type

    @property
    def error_code(self):
        r"""Gets the error_code of this ErrorStatus.

        错误码

        :return: The error_code of this ErrorStatus.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ErrorStatus.

        错误码

        :param error_code: The error_code of this ErrorStatus.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ErrorStatus.

        错误描述

        :return: The error_msg of this ErrorStatus.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ErrorStatus.

        错误描述

        :param error_msg: The error_msg of this ErrorStatus.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def error_type(self):
        r"""Gets the error_type of this ErrorStatus.

        错误类型

        :return: The error_type of this ErrorStatus.
        :rtype: str
        """
        return self._error_type

    @error_type.setter
    def error_type(self, error_type):
        r"""Sets the error_type of this ErrorStatus.

        错误类型

        :param error_type: The error_type of this ErrorStatus.
        :type error_type: str
        """
        self._error_type = error_type

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
        if not isinstance(other, ErrorStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
