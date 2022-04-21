# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomizeFormula:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'alias': 'str',
        'formula': 'str'
    }

    attribute_map = {
        'alias': 'alias',
        'formula': 'formula'
    }

    def __init__(self, alias=None, formula=None):
        """CustomizeFormula

        The model defined in huaweicloud sdk

        :param alias: 别名。
        :type alias: str
        :param formula: 公式。
        :type formula: str
        """
        
        

        self._alias = None
        self._formula = None
        self.discriminator = None

        if alias is not None:
            self.alias = alias
        if formula is not None:
            self.formula = formula

    @property
    def alias(self):
        """Gets the alias of this CustomizeFormula.

        别名。

        :return: The alias of this CustomizeFormula.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this CustomizeFormula.

        别名。

        :param alias: The alias of this CustomizeFormula.
        :type alias: str
        """
        self._alias = alias

    @property
    def formula(self):
        """Gets the formula of this CustomizeFormula.

        公式。

        :return: The formula of this CustomizeFormula.
        :rtype: str
        """
        return self._formula

    @formula.setter
    def formula(self, formula):
        """Sets the formula of this CustomizeFormula.

        公式。

        :param formula: The formula of this CustomizeFormula.
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
        if not isinstance(other, CustomizeFormula):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
