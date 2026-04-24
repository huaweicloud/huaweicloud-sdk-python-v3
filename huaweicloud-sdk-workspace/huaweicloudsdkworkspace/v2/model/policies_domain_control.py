# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesDomainControl:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'default_enabled': 'bool',
        'domain_rules': 'str'
    }

    attribute_map = {
        'default_enabled': 'default_enabled',
        'domain_rules': 'domain_rules'
    }

    def __init__(self, default_enabled=None, domain_rules=None):
        r"""PoliciesDomainControl

        The model defined in huaweicloud sdk

        :param default_enabled: 默认开关
        :type default_enabled: bool
        :param domain_rules: 域名
        :type domain_rules: str
        """
        
        

        self._default_enabled = None
        self._domain_rules = None
        self.discriminator = None

        if default_enabled is not None:
            self.default_enabled = default_enabled
        if domain_rules is not None:
            self.domain_rules = domain_rules

    @property
    def default_enabled(self):
        r"""Gets the default_enabled of this PoliciesDomainControl.

        默认开关

        :return: The default_enabled of this PoliciesDomainControl.
        :rtype: bool
        """
        return self._default_enabled

    @default_enabled.setter
    def default_enabled(self, default_enabled):
        r"""Sets the default_enabled of this PoliciesDomainControl.

        默认开关

        :param default_enabled: The default_enabled of this PoliciesDomainControl.
        :type default_enabled: bool
        """
        self._default_enabled = default_enabled

    @property
    def domain_rules(self):
        r"""Gets the domain_rules of this PoliciesDomainControl.

        域名

        :return: The domain_rules of this PoliciesDomainControl.
        :rtype: str
        """
        return self._domain_rules

    @domain_rules.setter
    def domain_rules(self, domain_rules):
        r"""Sets the domain_rules of this PoliciesDomainControl.

        域名

        :param domain_rules: The domain_rules of this PoliciesDomainControl.
        :type domain_rules: str
        """
        self._domain_rules = domain_rules

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
        if not isinstance(other, PoliciesDomainControl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
