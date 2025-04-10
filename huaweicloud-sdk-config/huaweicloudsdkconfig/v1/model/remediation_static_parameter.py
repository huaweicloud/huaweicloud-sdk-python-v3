# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemediationStaticParameter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'var_key': 'str',
        'var_value': 'object'
    }

    attribute_map = {
        'var_key': 'var_key',
        'var_value': 'var_value'
    }

    def __init__(self, var_key=None, var_value=None):
        r"""RemediationStaticParameter

        The model defined in huaweicloud sdk

        :param var_key: 参数名称。
        :type var_key: str
        :param var_value: 参数的值。
        :type var_value: object
        """
        
        

        self._var_key = None
        self._var_value = None
        self.discriminator = None

        if var_key is not None:
            self.var_key = var_key
        if var_value is not None:
            self.var_value = var_value

    @property
    def var_key(self):
        r"""Gets the var_key of this RemediationStaticParameter.

        参数名称。

        :return: The var_key of this RemediationStaticParameter.
        :rtype: str
        """
        return self._var_key

    @var_key.setter
    def var_key(self, var_key):
        r"""Sets the var_key of this RemediationStaticParameter.

        参数名称。

        :param var_key: The var_key of this RemediationStaticParameter.
        :type var_key: str
        """
        self._var_key = var_key

    @property
    def var_value(self):
        r"""Gets the var_value of this RemediationStaticParameter.

        参数的值。

        :return: The var_value of this RemediationStaticParameter.
        :rtype: object
        """
        return self._var_value

    @var_value.setter
    def var_value(self, var_value):
        r"""Sets the var_value of this RemediationStaticParameter.

        参数的值。

        :param var_value: The var_value of this RemediationStaticParameter.
        :type var_value: object
        """
        self._var_value = var_value

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
        if not isinstance(other, RemediationStaticParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
