# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentConfigCompareResultModifyEnvs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'value': 'str',
        'change_value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'change_value': 'change_value'
    }

    def __init__(self, name=None, value=None, change_value=None):
        """ComponentConfigCompareResultModifyEnvs

        The model defined in huaweicloud sdk

        :param name: 
        :type name: str
        :param value: 
        :type value: str
        :param change_value: 
        :type change_value: str
        """
        
        

        self._name = None
        self._value = None
        self._change_value = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if change_value is not None:
            self.change_value = change_value

    @property
    def name(self):
        """Gets the name of this ComponentConfigCompareResultModifyEnvs.

        :return: The name of this ComponentConfigCompareResultModifyEnvs.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComponentConfigCompareResultModifyEnvs.

        :param name: The name of this ComponentConfigCompareResultModifyEnvs.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        """Gets the value of this ComponentConfigCompareResultModifyEnvs.

        :return: The value of this ComponentConfigCompareResultModifyEnvs.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ComponentConfigCompareResultModifyEnvs.

        :param value: The value of this ComponentConfigCompareResultModifyEnvs.
        :type value: str
        """
        self._value = value

    @property
    def change_value(self):
        """Gets the change_value of this ComponentConfigCompareResultModifyEnvs.

        :return: The change_value of this ComponentConfigCompareResultModifyEnvs.
        :rtype: str
        """
        return self._change_value

    @change_value.setter
    def change_value(self, change_value):
        """Sets the change_value of this ComponentConfigCompareResultModifyEnvs.

        :param change_value: The change_value of this ComponentConfigCompareResultModifyEnvs.
        :type change_value: str
        """
        self._change_value = change_value

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
        if not isinstance(other, ComponentConfigCompareResultModifyEnvs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
