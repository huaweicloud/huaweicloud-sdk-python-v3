# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CodeVerifyReq:

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
        'method': 'str'
    }

    attribute_map = {
        'code': 'code',
        'method': 'method'
    }

    def __init__(self, code=None, method=None):
        """CodeVerifyReq

        The model defined in huaweicloud sdk

        :param code: 验证码
        :type code: str
        :param method: 认证方式
        :type method: str
        """
        
        

        self._code = None
        self._method = None
        self.discriminator = None

        self.code = code
        self.method = method

    @property
    def code(self):
        """Gets the code of this CodeVerifyReq.

        验证码

        :return: The code of this CodeVerifyReq.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CodeVerifyReq.

        验证码

        :param code: The code of this CodeVerifyReq.
        :type code: str
        """
        self._code = code

    @property
    def method(self):
        """Gets the method of this CodeVerifyReq.

        认证方式

        :return: The method of this CodeVerifyReq.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this CodeVerifyReq.

        认证方式

        :param method: The method of this CodeVerifyReq.
        :type method: str
        """
        self._method = method

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
        if not isinstance(other, CodeVerifyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
