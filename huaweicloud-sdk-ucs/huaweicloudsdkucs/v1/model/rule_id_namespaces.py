# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleIDNamespaces:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_i_ds': 'list[str]',
        'namespaces': 'list[str]'
    }

    attribute_map = {
        'rule_i_ds': 'ruleIDs',
        'namespaces': 'namespaces'
    }

    def __init__(self, rule_i_ds=None, namespaces=None):
        r"""RuleIDNamespaces

        The model defined in huaweicloud sdk

        :param rule_i_ds: 权限策略id
        :type rule_i_ds: list[str]
        :param namespaces: 权限策略涉及到的命名空间
        :type namespaces: list[str]
        """
        
        

        self._rule_i_ds = None
        self._namespaces = None
        self.discriminator = None

        if rule_i_ds is not None:
            self.rule_i_ds = rule_i_ds
        if namespaces is not None:
            self.namespaces = namespaces

    @property
    def rule_i_ds(self):
        r"""Gets the rule_i_ds of this RuleIDNamespaces.

        权限策略id

        :return: The rule_i_ds of this RuleIDNamespaces.
        :rtype: list[str]
        """
        return self._rule_i_ds

    @rule_i_ds.setter
    def rule_i_ds(self, rule_i_ds):
        r"""Sets the rule_i_ds of this RuleIDNamespaces.

        权限策略id

        :param rule_i_ds: The rule_i_ds of this RuleIDNamespaces.
        :type rule_i_ds: list[str]
        """
        self._rule_i_ds = rule_i_ds

    @property
    def namespaces(self):
        r"""Gets the namespaces of this RuleIDNamespaces.

        权限策略涉及到的命名空间

        :return: The namespaces of this RuleIDNamespaces.
        :rtype: list[str]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        r"""Sets the namespaces of this RuleIDNamespaces.

        权限策略涉及到的命名空间

        :param namespaces: The namespaces of this RuleIDNamespaces.
        :type namespaces: list[str]
        """
        self._namespaces = namespaces

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RuleIDNamespaces):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
