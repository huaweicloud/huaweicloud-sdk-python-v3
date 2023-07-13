# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VarsStructure:

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
        'var_value': 'str',
        'encryption': 'EncryptionStructure'
    }

    attribute_map = {
        'var_key': 'var_key',
        'var_value': 'var_value',
        'encryption': 'encryption'
    }

    def __init__(self, var_key=None, var_value=None, encryption=None):
        """VarsStructure

        The model defined in huaweicloud sdk

        :param var_key: 参数的名字
        :type var_key: str
        :param var_value: 参数的值。  注意，参数需要以字符串形式存在，如果是数字，也需要以字符串形式存在，如&#39;10&#39;。  如果需要支持不同类型，或者复杂结构，请使用vars_uri或vars_body
        :type var_value: str
        :param encryption: 
        :type encryption: :class:`huaweicloudsdkaos.v1.EncryptionStructure`
        """
        
        

        self._var_key = None
        self._var_value = None
        self._encryption = None
        self.discriminator = None

        self.var_key = var_key
        self.var_value = var_value
        if encryption is not None:
            self.encryption = encryption

    @property
    def var_key(self):
        """Gets the var_key of this VarsStructure.

        参数的名字

        :return: The var_key of this VarsStructure.
        :rtype: str
        """
        return self._var_key

    @var_key.setter
    def var_key(self, var_key):
        """Sets the var_key of this VarsStructure.

        参数的名字

        :param var_key: The var_key of this VarsStructure.
        :type var_key: str
        """
        self._var_key = var_key

    @property
    def var_value(self):
        """Gets the var_value of this VarsStructure.

        参数的值。  注意，参数需要以字符串形式存在，如果是数字，也需要以字符串形式存在，如'10'。  如果需要支持不同类型，或者复杂结构，请使用vars_uri或vars_body

        :return: The var_value of this VarsStructure.
        :rtype: str
        """
        return self._var_value

    @var_value.setter
    def var_value(self, var_value):
        """Sets the var_value of this VarsStructure.

        参数的值。  注意，参数需要以字符串形式存在，如果是数字，也需要以字符串形式存在，如'10'。  如果需要支持不同类型，或者复杂结构，请使用vars_uri或vars_body

        :param var_value: The var_value of this VarsStructure.
        :type var_value: str
        """
        self._var_value = var_value

    @property
    def encryption(self):
        """Gets the encryption of this VarsStructure.

        :return: The encryption of this VarsStructure.
        :rtype: :class:`huaweicloudsdkaos.v1.EncryptionStructure`
        """
        return self._encryption

    @encryption.setter
    def encryption(self, encryption):
        """Sets the encryption of this VarsStructure.

        :param encryption: The encryption of this VarsStructure.
        :type encryption: :class:`huaweicloudsdkaos.v1.EncryptionStructure`
        """
        self._encryption = encryption

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
        if not isinstance(other, VarsStructure):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
