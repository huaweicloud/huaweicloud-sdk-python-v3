# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleNamespace:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rules': 'list[RuleInfo]',
        'namespaces': 'list[str]'
    }

    attribute_map = {
        'rules': 'rules',
        'namespaces': 'namespaces'
    }

    def __init__(self, rules=None, namespaces=None):
        r"""RuleNamespace

        The model defined in huaweicloud sdk

        :param rules: 权限策略列表
        :type rules: list[:class:`huaweicloudsdkucs.v1.RuleInfo`]
        :param namespaces: 命名空间列表
        :type namespaces: list[str]
        """
        
        

        self._rules = None
        self._namespaces = None
        self.discriminator = None

        if rules is not None:
            self.rules = rules
        if namespaces is not None:
            self.namespaces = namespaces

    @property
    def rules(self):
        r"""Gets the rules of this RuleNamespace.

        权限策略列表

        :return: The rules of this RuleNamespace.
        :rtype: list[:class:`huaweicloudsdkucs.v1.RuleInfo`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        r"""Sets the rules of this RuleNamespace.

        权限策略列表

        :param rules: The rules of this RuleNamespace.
        :type rules: list[:class:`huaweicloudsdkucs.v1.RuleInfo`]
        """
        self._rules = rules

    @property
    def namespaces(self):
        r"""Gets the namespaces of this RuleNamespace.

        命名空间列表

        :return: The namespaces of this RuleNamespace.
        :rtype: list[str]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        r"""Sets the namespaces of this RuleNamespace.

        命名空间列表

        :param namespaces: The namespaces of this RuleNamespace.
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
        if not isinstance(other, RuleNamespace):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
