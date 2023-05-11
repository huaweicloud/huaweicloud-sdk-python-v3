# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFunctionConfigRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'function_urn': 'str'
    }

    attribute_map = {
        'function_urn': 'function_urn'
    }

    def __init__(self, function_urn=None):
        """ShowFunctionConfigRequest

        The model defined in huaweicloud sdk

        :param function_urn: 函数的URN，详细解释见FunctionGraph函数模型的描述。
        :type function_urn: str
        """
        
        

        self._function_urn = None
        self.discriminator = None

        self.function_urn = function_urn

    @property
    def function_urn(self):
        """Gets the function_urn of this ShowFunctionConfigRequest.

        函数的URN，详细解释见FunctionGraph函数模型的描述。

        :return: The function_urn of this ShowFunctionConfigRequest.
        :rtype: str
        """
        return self._function_urn

    @function_urn.setter
    def function_urn(self, function_urn):
        """Sets the function_urn of this ShowFunctionConfigRequest.

        函数的URN，详细解释见FunctionGraph函数模型的描述。

        :param function_urn: The function_urn of this ShowFunctionConfigRequest.
        :type function_urn: str
        """
        self._function_urn = function_urn

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
        if not isinstance(other, ShowFunctionConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
