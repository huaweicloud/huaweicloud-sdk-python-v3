# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeNetwork:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc': 'str',
        'subnet': 'str',
        'security_groups': 'list[str]'
    }

    attribute_map = {
        'vpc': 'vpc',
        'subnet': 'subnet',
        'security_groups': 'securityGroups'
    }

    def __init__(self, vpc=None, subnet=None, security_groups=None):
        r"""NodeNetwork

        The model defined in huaweicloud sdk

        :param vpc: **参数解释**：vpc id。 **取值范围**：不涉及。
        :type vpc: str
        :param subnet: **参数解释**：子网id。 **取值范围**：不涉及。
        :type subnet: str
        :param security_groups: **参数解释**：安全组id集合。
        :type security_groups: list[str]
        """
        
        

        self._vpc = None
        self._subnet = None
        self._security_groups = None
        self.discriminator = None

        if vpc is not None:
            self.vpc = vpc
        if subnet is not None:
            self.subnet = subnet
        if security_groups is not None:
            self.security_groups = security_groups

    @property
    def vpc(self):
        r"""Gets the vpc of this NodeNetwork.

        **参数解释**：vpc id。 **取值范围**：不涉及。

        :return: The vpc of this NodeNetwork.
        :rtype: str
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        r"""Sets the vpc of this NodeNetwork.

        **参数解释**：vpc id。 **取值范围**：不涉及。

        :param vpc: The vpc of this NodeNetwork.
        :type vpc: str
        """
        self._vpc = vpc

    @property
    def subnet(self):
        r"""Gets the subnet of this NodeNetwork.

        **参数解释**：子网id。 **取值范围**：不涉及。

        :return: The subnet of this NodeNetwork.
        :rtype: str
        """
        return self._subnet

    @subnet.setter
    def subnet(self, subnet):
        r"""Sets the subnet of this NodeNetwork.

        **参数解释**：子网id。 **取值范围**：不涉及。

        :param subnet: The subnet of this NodeNetwork.
        :type subnet: str
        """
        self._subnet = subnet

    @property
    def security_groups(self):
        r"""Gets the security_groups of this NodeNetwork.

        **参数解释**：安全组id集合。

        :return: The security_groups of this NodeNetwork.
        :rtype: list[str]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        r"""Sets the security_groups of this NodeNetwork.

        **参数解释**：安全组id集合。

        :param security_groups: The security_groups of this NodeNetwork.
        :type security_groups: list[str]
        """
        self._security_groups = security_groups

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
        if not isinstance(other, NodeNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
