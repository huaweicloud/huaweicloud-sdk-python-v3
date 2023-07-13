# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiError:

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
        'reason': 'str'
    }

    attribute_map = {
        'code': 'code',
        'reason': 'reason'
    }

    def __init__(self, code=None, reason=None):
        """ApiError

        The model defined in huaweicloud sdk

        :param code: 只有对外的接口才会返回此内容
        :type code: str
        :param reason: 业务失败的提示内容
        :type reason: str
        """
        
        

        self._code = None
        self._reason = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if reason is not None:
            self.reason = reason

    @property
    def code(self):
        """Gets the code of this ApiError.

        只有对外的接口才会返回此内容

        :return: The code of this ApiError.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ApiError.

        只有对外的接口才会返回此内容

        :param code: The code of this ApiError.
        :type code: str
        """
        self._code = code

    @property
    def reason(self):
        """Gets the reason of this ApiError.

        业务失败的提示内容

        :return: The reason of this ApiError.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ApiError.

        业务失败的提示内容

        :param reason: The reason of this ApiError.
        :type reason: str
        """
        self._reason = reason

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
        if not isinstance(other, ApiError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
