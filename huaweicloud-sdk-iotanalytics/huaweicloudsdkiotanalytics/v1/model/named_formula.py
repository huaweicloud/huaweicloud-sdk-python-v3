# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NamedFormula:

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
        'formula': 'str'
    }

    attribute_map = {
        'name': 'name',
        'formula': 'formula'
    }

    def __init__(self, name=None, formula=None):
        """NamedFormula

        The model defined in huaweicloud sdk

        :param name: 公式名称，不能和输入参数名重复，正则：\&quot;^[A-Za-z][A-Za-z_]{0,31}$\&quot;
        :type name: str
        :param formula: 公式，最多1024个字符
        :type formula: str
        """
        
        

        self._name = None
        self._formula = None
        self.discriminator = None

        self.name = name
        self.formula = formula

    @property
    def name(self):
        """Gets the name of this NamedFormula.

        公式名称，不能和输入参数名重复，正则：\"^[A-Za-z][A-Za-z_]{0,31}$\"

        :return: The name of this NamedFormula.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NamedFormula.

        公式名称，不能和输入参数名重复，正则：\"^[A-Za-z][A-Za-z_]{0,31}$\"

        :param name: The name of this NamedFormula.
        :type name: str
        """
        self._name = name

    @property
    def formula(self):
        """Gets the formula of this NamedFormula.

        公式，最多1024个字符

        :return: The formula of this NamedFormula.
        :rtype: str
        """
        return self._formula

    @formula.setter
    def formula(self, formula):
        """Sets the formula of this NamedFormula.

        公式，最多1024个字符

        :param formula: The formula of this NamedFormula.
        :type formula: str
        """
        self._formula = formula

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
        if not isinstance(other, NamedFormula):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
