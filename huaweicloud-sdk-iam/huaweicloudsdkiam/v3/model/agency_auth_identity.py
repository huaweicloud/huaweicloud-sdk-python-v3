# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgencyAuthIdentity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'methods': 'list[str]',
        'assume_role': 'IdentityAssumerole',
        'policy': 'ServicePolicy'
    }

    attribute_map = {
        'methods': 'methods',
        'assume_role': 'assume_role',
        'policy': 'policy'
    }

    def __init__(self, methods=None, assume_role=None, policy=None):
        r"""AgencyAuthIdentity

        The model defined in huaweicloud sdk

        :param methods: 认证方法，该字段内容为[\&quot;assume_role\&quot;]。
        :type methods: list[str]
        :param assume_role: 
        :type assume_role: :class:`huaweicloudsdkiam.v3.IdentityAssumerole`
        :param policy: 
        :type policy: :class:`huaweicloudsdkiam.v3.ServicePolicy`
        """
        
        

        self._methods = None
        self._assume_role = None
        self._policy = None
        self.discriminator = None

        self.methods = methods
        self.assume_role = assume_role
        if policy is not None:
            self.policy = policy

    @property
    def methods(self):
        r"""Gets the methods of this AgencyAuthIdentity.

        认证方法，该字段内容为[\"assume_role\"]。

        :return: The methods of this AgencyAuthIdentity.
        :rtype: list[str]
        """
        return self._methods

    @methods.setter
    def methods(self, methods):
        r"""Sets the methods of this AgencyAuthIdentity.

        认证方法，该字段内容为[\"assume_role\"]。

        :param methods: The methods of this AgencyAuthIdentity.
        :type methods: list[str]
        """
        self._methods = methods

    @property
    def assume_role(self):
        r"""Gets the assume_role of this AgencyAuthIdentity.

        :return: The assume_role of this AgencyAuthIdentity.
        :rtype: :class:`huaweicloudsdkiam.v3.IdentityAssumerole`
        """
        return self._assume_role

    @assume_role.setter
    def assume_role(self, assume_role):
        r"""Sets the assume_role of this AgencyAuthIdentity.

        :param assume_role: The assume_role of this AgencyAuthIdentity.
        :type assume_role: :class:`huaweicloudsdkiam.v3.IdentityAssumerole`
        """
        self._assume_role = assume_role

    @property
    def policy(self):
        r"""Gets the policy of this AgencyAuthIdentity.

        :return: The policy of this AgencyAuthIdentity.
        :rtype: :class:`huaweicloudsdkiam.v3.ServicePolicy`
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this AgencyAuthIdentity.

        :param policy: The policy of this AgencyAuthIdentity.
        :type policy: :class:`huaweicloudsdkiam.v3.ServicePolicy`
        """
        self._policy = policy

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
        if not isinstance(other, AgencyAuthIdentity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
