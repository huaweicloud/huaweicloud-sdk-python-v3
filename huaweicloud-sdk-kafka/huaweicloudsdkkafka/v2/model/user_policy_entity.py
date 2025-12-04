# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserPolicyEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'resource_name': 'str',
        'pattern_type': 'str',
        'access_policy': 'str'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'resource_name': 'resource_name',
        'pattern_type': 'pattern_type',
        'access_policy': 'access_policy'
    }

    def __init__(self, resource_type=None, resource_name=None, pattern_type=None, access_policy=None):
        r"""UserPolicyEntity

        The model defined in huaweicloud sdk

        :param resource_type: **参数解释**： 资源类型。 **约束限制**： 不涉及。 **取值范围**： - TOPIC：表示资源类型为Topic。 **默认取值**： TOPIC
        :type resource_type: str
        :param resource_name: **参数解释**： 资源名称。 **约束限制**： 不涉及。 **取值范围**： - 已有的Topic名称。 - 符合Topic名称规则的前缀。 - “*”表示匹配所有的Topic。 **默认取值**： 不涉及。
        :type resource_name: str
        :param pattern_type: **参数解释**： 匹配方式。 **约束限制**： 不涉及。 **取值范围**： - LITERAL：完全匹配。 - PREFIXED：前缀匹配。 **默认取值**： 不涉及。
        :type pattern_type: str
        :param access_policy: **参数解释**： 权限类型。 **约束限制**： 不涉及。 **取值范围**： - all：拥有发布、订阅权限。 - pub：拥有发布权限。 - sub：拥有订阅权限。 **默认取值**： 不涉及。
        :type access_policy: str
        """
        
        

        self._resource_type = None
        self._resource_name = None
        self._pattern_type = None
        self._access_policy = None
        self.discriminator = None

        if resource_type is not None:
            self.resource_type = resource_type
        if resource_name is not None:
            self.resource_name = resource_name
        if pattern_type is not None:
            self.pattern_type = pattern_type
        if access_policy is not None:
            self.access_policy = access_policy

    @property
    def resource_type(self):
        r"""Gets the resource_type of this UserPolicyEntity.

        **参数解释**： 资源类型。 **约束限制**： 不涉及。 **取值范围**： - TOPIC：表示资源类型为Topic。 **默认取值**： TOPIC

        :return: The resource_type of this UserPolicyEntity.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this UserPolicyEntity.

        **参数解释**： 资源类型。 **约束限制**： 不涉及。 **取值范围**： - TOPIC：表示资源类型为Topic。 **默认取值**： TOPIC

        :param resource_type: The resource_type of this UserPolicyEntity.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_name(self):
        r"""Gets the resource_name of this UserPolicyEntity.

        **参数解释**： 资源名称。 **约束限制**： 不涉及。 **取值范围**： - 已有的Topic名称。 - 符合Topic名称规则的前缀。 - “*”表示匹配所有的Topic。 **默认取值**： 不涉及。

        :return: The resource_name of this UserPolicyEntity.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this UserPolicyEntity.

        **参数解释**： 资源名称。 **约束限制**： 不涉及。 **取值范围**： - 已有的Topic名称。 - 符合Topic名称规则的前缀。 - “*”表示匹配所有的Topic。 **默认取值**： 不涉及。

        :param resource_name: The resource_name of this UserPolicyEntity.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def pattern_type(self):
        r"""Gets the pattern_type of this UserPolicyEntity.

        **参数解释**： 匹配方式。 **约束限制**： 不涉及。 **取值范围**： - LITERAL：完全匹配。 - PREFIXED：前缀匹配。 **默认取值**： 不涉及。

        :return: The pattern_type of this UserPolicyEntity.
        :rtype: str
        """
        return self._pattern_type

    @pattern_type.setter
    def pattern_type(self, pattern_type):
        r"""Sets the pattern_type of this UserPolicyEntity.

        **参数解释**： 匹配方式。 **约束限制**： 不涉及。 **取值范围**： - LITERAL：完全匹配。 - PREFIXED：前缀匹配。 **默认取值**： 不涉及。

        :param pattern_type: The pattern_type of this UserPolicyEntity.
        :type pattern_type: str
        """
        self._pattern_type = pattern_type

    @property
    def access_policy(self):
        r"""Gets the access_policy of this UserPolicyEntity.

        **参数解释**： 权限类型。 **约束限制**： 不涉及。 **取值范围**： - all：拥有发布、订阅权限。 - pub：拥有发布权限。 - sub：拥有订阅权限。 **默认取值**： 不涉及。

        :return: The access_policy of this UserPolicyEntity.
        :rtype: str
        """
        return self._access_policy

    @access_policy.setter
    def access_policy(self, access_policy):
        r"""Sets the access_policy of this UserPolicyEntity.

        **参数解释**： 权限类型。 **约束限制**： 不涉及。 **取值范围**： - all：拥有发布、订阅权限。 - pub：拥有发布权限。 - sub：拥有订阅权限。 **默认取值**： 不涉及。

        :param access_policy: The access_policy of this UserPolicyEntity.
        :type access_policy: str
        """
        self._access_policy = access_policy

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
        if not isinstance(other, UserPolicyEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
