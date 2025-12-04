# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserPolicyResponeEntity:

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
        'access_policy': 'str',
        'acl_permission_type': 'str'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'resource_name': 'resource_name',
        'pattern_type': 'pattern_type',
        'access_policy': 'access_policy',
        'acl_permission_type': 'acl_permission_type'
    }

    def __init__(self, resource_type=None, resource_name=None, pattern_type=None, access_policy=None, acl_permission_type=None):
        r"""UserPolicyResponeEntity

        The model defined in huaweicloud sdk

        :param resource_type: **参数解释**： 资源类型。 **取值范围**： - TOPIC：表示资源类型为Topic。
        :type resource_type: str
        :param resource_name: **参数解释**： 资源名称。 **取值范围**： - 已有的Topic名称。 - 符合Topic名称规则的前缀。 - “*”表示匹配所有的Topic。
        :type resource_name: str
        :param pattern_type: **参数解释**： 匹配方式。 **取值范围**： - LITERAL：完全匹配。 - PREFIXED：前缀匹配。
        :type pattern_type: str
        :param access_policy: **参数解释**： 权限类型。 **取值范围**： - all：拥有发布、订阅权限。 - pub：拥有发布权限。 - sub：拥有订阅权限。
        :type access_policy: str
        :param acl_permission_type: **参数解释**： Acl权限类型。 **取值范围**： - ALLOW：允许用户进行某种操作。
        :type acl_permission_type: str
        """
        
        

        self._resource_type = None
        self._resource_name = None
        self._pattern_type = None
        self._access_policy = None
        self._acl_permission_type = None
        self.discriminator = None

        if resource_type is not None:
            self.resource_type = resource_type
        if resource_name is not None:
            self.resource_name = resource_name
        if pattern_type is not None:
            self.pattern_type = pattern_type
        if access_policy is not None:
            self.access_policy = access_policy
        if acl_permission_type is not None:
            self.acl_permission_type = acl_permission_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this UserPolicyResponeEntity.

        **参数解释**： 资源类型。 **取值范围**： - TOPIC：表示资源类型为Topic。

        :return: The resource_type of this UserPolicyResponeEntity.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this UserPolicyResponeEntity.

        **参数解释**： 资源类型。 **取值范围**： - TOPIC：表示资源类型为Topic。

        :param resource_type: The resource_type of this UserPolicyResponeEntity.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_name(self):
        r"""Gets the resource_name of this UserPolicyResponeEntity.

        **参数解释**： 资源名称。 **取值范围**： - 已有的Topic名称。 - 符合Topic名称规则的前缀。 - “*”表示匹配所有的Topic。

        :return: The resource_name of this UserPolicyResponeEntity.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this UserPolicyResponeEntity.

        **参数解释**： 资源名称。 **取值范围**： - 已有的Topic名称。 - 符合Topic名称规则的前缀。 - “*”表示匹配所有的Topic。

        :param resource_name: The resource_name of this UserPolicyResponeEntity.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def pattern_type(self):
        r"""Gets the pattern_type of this UserPolicyResponeEntity.

        **参数解释**： 匹配方式。 **取值范围**： - LITERAL：完全匹配。 - PREFIXED：前缀匹配。

        :return: The pattern_type of this UserPolicyResponeEntity.
        :rtype: str
        """
        return self._pattern_type

    @pattern_type.setter
    def pattern_type(self, pattern_type):
        r"""Sets the pattern_type of this UserPolicyResponeEntity.

        **参数解释**： 匹配方式。 **取值范围**： - LITERAL：完全匹配。 - PREFIXED：前缀匹配。

        :param pattern_type: The pattern_type of this UserPolicyResponeEntity.
        :type pattern_type: str
        """
        self._pattern_type = pattern_type

    @property
    def access_policy(self):
        r"""Gets the access_policy of this UserPolicyResponeEntity.

        **参数解释**： 权限类型。 **取值范围**： - all：拥有发布、订阅权限。 - pub：拥有发布权限。 - sub：拥有订阅权限。

        :return: The access_policy of this UserPolicyResponeEntity.
        :rtype: str
        """
        return self._access_policy

    @access_policy.setter
    def access_policy(self, access_policy):
        r"""Sets the access_policy of this UserPolicyResponeEntity.

        **参数解释**： 权限类型。 **取值范围**： - all：拥有发布、订阅权限。 - pub：拥有发布权限。 - sub：拥有订阅权限。

        :param access_policy: The access_policy of this UserPolicyResponeEntity.
        :type access_policy: str
        """
        self._access_policy = access_policy

    @property
    def acl_permission_type(self):
        r"""Gets the acl_permission_type of this UserPolicyResponeEntity.

        **参数解释**： Acl权限类型。 **取值范围**： - ALLOW：允许用户进行某种操作。

        :return: The acl_permission_type of this UserPolicyResponeEntity.
        :rtype: str
        """
        return self._acl_permission_type

    @acl_permission_type.setter
    def acl_permission_type(self, acl_permission_type):
        r"""Sets the acl_permission_type of this UserPolicyResponeEntity.

        **参数解释**： Acl权限类型。 **取值范围**： - ALLOW：允许用户进行某种操作。

        :param acl_permission_type: The acl_permission_type of this UserPolicyResponeEntity.
        :type acl_permission_type: str
        """
        self._acl_permission_type = acl_permission_type

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
        if not isinstance(other, UserPolicyResponeEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
