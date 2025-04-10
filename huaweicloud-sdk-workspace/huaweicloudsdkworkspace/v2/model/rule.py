# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Rule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scope': 'RuleScope',
        'product_rule': 'ProductRule',
        'path_rule': 'PathRule'
    }

    attribute_map = {
        'scope': 'scope',
        'product_rule': 'product_rule',
        'path_rule': 'path_rule'
    }

    def __init__(self, scope=None, product_rule=None, path_rule=None):
        r"""Rule

        The model defined in huaweicloud sdk

        :param scope: 
        :type scope: :class:`huaweicloudsdkworkspace.v2.RuleScope`
        :param product_rule: 
        :type product_rule: :class:`huaweicloudsdkworkspace.v2.ProductRule`
        :param path_rule: 
        :type path_rule: :class:`huaweicloudsdkworkspace.v2.PathRule`
        """
        
        

        self._scope = None
        self._product_rule = None
        self._path_rule = None
        self.discriminator = None

        self.scope = scope
        if product_rule is not None:
            self.product_rule = product_rule
        if path_rule is not None:
            self.path_rule = path_rule

    @property
    def scope(self):
        r"""Gets the scope of this Rule.

        :return: The scope of this Rule.
        :rtype: :class:`huaweicloudsdkworkspace.v2.RuleScope`
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this Rule.

        :param scope: The scope of this Rule.
        :type scope: :class:`huaweicloudsdkworkspace.v2.RuleScope`
        """
        self._scope = scope

    @property
    def product_rule(self):
        r"""Gets the product_rule of this Rule.

        :return: The product_rule of this Rule.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ProductRule`
        """
        return self._product_rule

    @product_rule.setter
    def product_rule(self, product_rule):
        r"""Sets the product_rule of this Rule.

        :param product_rule: The product_rule of this Rule.
        :type product_rule: :class:`huaweicloudsdkworkspace.v2.ProductRule`
        """
        self._product_rule = product_rule

    @property
    def path_rule(self):
        r"""Gets the path_rule of this Rule.

        :return: The path_rule of this Rule.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PathRule`
        """
        return self._path_rule

    @path_rule.setter
    def path_rule(self, path_rule):
        r"""Sets the path_rule of this Rule.

        :param path_rule: The path_rule of this Rule.
        :type path_rule: :class:`huaweicloudsdkworkspace.v2.PathRule`
        """
        self._path_rule = path_rule

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
        if not isinstance(other, Rule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
