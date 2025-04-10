# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'function_urn': 'str',
        'auth_type': 'str',
        'auth_value': 'dict(str, object)'
    }

    attribute_map = {
        'function_urn': 'function_urn',
        'auth_type': 'auth_type',
        'auth_value': 'auth_value'
    }

    def __init__(self, function_urn=None, auth_type=None, auth_value=None):
        r"""CustomPolicy

        The model defined in huaweicloud sdk

        :param function_urn: 自定义函数的urn
        :type function_urn: str
        :param auth_type: 自定义合规规则调用function方式
        :type auth_type: str
        :param auth_value: method参数值，method为agency时，为{\&quot;agency_name\&quot;:rms_fg_agency}, rms_fg_agency为授权RMS调用FunctionGraph接口的委托名称
        :type auth_value: dict(str, object)
        """
        
        

        self._function_urn = None
        self._auth_type = None
        self._auth_value = None
        self.discriminator = None

        self.function_urn = function_urn
        self.auth_type = auth_type
        if auth_value is not None:
            self.auth_value = auth_value

    @property
    def function_urn(self):
        r"""Gets the function_urn of this CustomPolicy.

        自定义函数的urn

        :return: The function_urn of this CustomPolicy.
        :rtype: str
        """
        return self._function_urn

    @function_urn.setter
    def function_urn(self, function_urn):
        r"""Sets the function_urn of this CustomPolicy.

        自定义函数的urn

        :param function_urn: The function_urn of this CustomPolicy.
        :type function_urn: str
        """
        self._function_urn = function_urn

    @property
    def auth_type(self):
        r"""Gets the auth_type of this CustomPolicy.

        自定义合规规则调用function方式

        :return: The auth_type of this CustomPolicy.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        r"""Sets the auth_type of this CustomPolicy.

        自定义合规规则调用function方式

        :param auth_type: The auth_type of this CustomPolicy.
        :type auth_type: str
        """
        self._auth_type = auth_type

    @property
    def auth_value(self):
        r"""Gets the auth_value of this CustomPolicy.

        method参数值，method为agency时，为{\"agency_name\":rms_fg_agency}, rms_fg_agency为授权RMS调用FunctionGraph接口的委托名称

        :return: The auth_value of this CustomPolicy.
        :rtype: dict(str, object)
        """
        return self._auth_value

    @auth_value.setter
    def auth_value(self, auth_value):
        r"""Sets the auth_value of this CustomPolicy.

        method参数值，method为agency时，为{\"agency_name\":rms_fg_agency}, rms_fg_agency为授权RMS调用FunctionGraph接口的委托名称

        :param auth_value: The auth_value of this CustomPolicy.
        :type auth_value: dict(str, object)
        """
        self._auth_value = auth_value

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
        if not isinstance(other, CustomPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
