# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGlobalVariableRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'var_name': 'str',
        'var_value': 'str',
        'is_sensitive': 'bool'
    }

    attribute_map = {
        'var_name': 'var_name',
        'var_value': 'var_value',
        'is_sensitive': 'is_sensitive'
    }

    def __init__(self, var_name=None, var_value=None, is_sensitive=None):
        r"""CreateGlobalVariableRequestBody

        The model defined in huaweicloud sdk

        :param var_name: 变量名称
        :type var_name: str
        :param var_value: 变量的值
        :type var_value: str
        :param is_sensitive: 是否为敏感变量
        :type is_sensitive: bool
        """
        
        

        self._var_name = None
        self._var_value = None
        self._is_sensitive = None
        self.discriminator = None

        self.var_name = var_name
        self.var_value = var_value
        if is_sensitive is not None:
            self.is_sensitive = is_sensitive

    @property
    def var_name(self):
        r"""Gets the var_name of this CreateGlobalVariableRequestBody.

        变量名称

        :return: The var_name of this CreateGlobalVariableRequestBody.
        :rtype: str
        """
        return self._var_name

    @var_name.setter
    def var_name(self, var_name):
        r"""Sets the var_name of this CreateGlobalVariableRequestBody.

        变量名称

        :param var_name: The var_name of this CreateGlobalVariableRequestBody.
        :type var_name: str
        """
        self._var_name = var_name

    @property
    def var_value(self):
        r"""Gets the var_value of this CreateGlobalVariableRequestBody.

        变量的值

        :return: The var_value of this CreateGlobalVariableRequestBody.
        :rtype: str
        """
        return self._var_value

    @var_value.setter
    def var_value(self, var_value):
        r"""Sets the var_value of this CreateGlobalVariableRequestBody.

        变量的值

        :param var_value: The var_value of this CreateGlobalVariableRequestBody.
        :type var_value: str
        """
        self._var_value = var_value

    @property
    def is_sensitive(self):
        r"""Gets the is_sensitive of this CreateGlobalVariableRequestBody.

        是否为敏感变量

        :return: The is_sensitive of this CreateGlobalVariableRequestBody.
        :rtype: bool
        """
        return self._is_sensitive

    @is_sensitive.setter
    def is_sensitive(self, is_sensitive):
        r"""Sets the is_sensitive of this CreateGlobalVariableRequestBody.

        是否为敏感变量

        :param is_sensitive: The is_sensitive of this CreateGlobalVariableRequestBody.
        :type is_sensitive: bool
        """
        self._is_sensitive = is_sensitive

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
        if not isinstance(other, CreateGlobalVariableRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
