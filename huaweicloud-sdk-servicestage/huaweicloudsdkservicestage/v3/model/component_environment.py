# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentEnvironment:

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
        'value_from': 'ComponentEnvironmentValueFrom'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'value_from': 'value_from'
    }

    def __init__(self, name=None, value=None, value_from=None):
        """ComponentEnvironment

        The model defined in huaweicloud sdk

        :param name: 
        :type name: str
        :param value: 
        :type value: str
        :param value_from: 
        :type value_from: :class:`huaweicloudsdkservicestage.v3.ComponentEnvironmentValueFrom`
        """
        
        

        self._name = None
        self._value = None
        self._value_from = None
        self.discriminator = None

        self.name = name
        if value is not None:
            self.value = value
        if value_from is not None:
            self.value_from = value_from

    @property
    def name(self):
        """Gets the name of this ComponentEnvironment.

        :return: The name of this ComponentEnvironment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComponentEnvironment.

        :param name: The name of this ComponentEnvironment.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        """Gets the value of this ComponentEnvironment.

        :return: The value of this ComponentEnvironment.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ComponentEnvironment.

        :param value: The value of this ComponentEnvironment.
        :type value: str
        """
        self._value = value

    @property
    def value_from(self):
        """Gets the value_from of this ComponentEnvironment.

        :return: The value_from of this ComponentEnvironment.
        :rtype: :class:`huaweicloudsdkservicestage.v3.ComponentEnvironmentValueFrom`
        """
        return self._value_from

    @value_from.setter
    def value_from(self, value_from):
        """Sets the value_from of this ComponentEnvironment.

        :param value_from: The value_from of this ComponentEnvironment.
        :type value_from: :class:`huaweicloudsdkservicestage.v3.ComponentEnvironmentValueFrom`
        """
        self._value_from = value_from

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
        if not isinstance(other, ComponentEnvironment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
