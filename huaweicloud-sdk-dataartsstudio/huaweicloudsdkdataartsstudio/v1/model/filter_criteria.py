# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FilterCriteria:

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
        'operator': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'operator': 'operator'
    }

    def __init__(self, name=None, value=None, operator=None):
        r"""FilterCriteria

        The model defined in huaweicloud sdk

        :param name: 当前可选值：database
        :type name: str
        :param value: database的名称
        :type value: str
        :param operator: 操作者
        :type operator: str
        """
        
        

        self._name = None
        self._value = None
        self._operator = None
        self.discriminator = None

        self.name = name
        self.value = value
        self.operator = operator

    @property
    def name(self):
        r"""Gets the name of this FilterCriteria.

        当前可选值：database

        :return: The name of this FilterCriteria.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this FilterCriteria.

        当前可选值：database

        :param name: The name of this FilterCriteria.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        r"""Gets the value of this FilterCriteria.

        database的名称

        :return: The value of this FilterCriteria.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this FilterCriteria.

        database的名称

        :param value: The value of this FilterCriteria.
        :type value: str
        """
        self._value = value

    @property
    def operator(self):
        r"""Gets the operator of this FilterCriteria.

        操作者

        :return: The operator of this FilterCriteria.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this FilterCriteria.

        操作者

        :param operator: The operator of this FilterCriteria.
        :type operator: str
        """
        self._operator = operator

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
        if not isinstance(other, FilterCriteria):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
