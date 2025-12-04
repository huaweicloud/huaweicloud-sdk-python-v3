# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUserPoliciesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_name': 'str',
        'total': 'int',
        'policies': 'list[UserPolicyResponeEntity]'
    }

    attribute_map = {
        'user_name': 'user_name',
        'total': 'total',
        'policies': 'policies'
    }

    def __init__(self, user_name=None, total=None, policies=None):
        r"""ListUserPoliciesResponse

        The model defined in huaweicloud sdk

        :param user_name: **参数解释**： 用户名。 **取值范围**： 不涉及。
        :type user_name: str
        :param total: **参数解释**： 用户权限总数。 **取值范围**： 不涉及。
        :type total: int
        :param policies: **参数解释**： 用户权限列表。
        :type policies: list[:class:`huaweicloudsdkkafka.v2.UserPolicyResponeEntity`]
        """
        
        super().__init__()

        self._user_name = None
        self._total = None
        self._policies = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        if total is not None:
            self.total = total
        if policies is not None:
            self.policies = policies

    @property
    def user_name(self):
        r"""Gets the user_name of this ListUserPoliciesResponse.

        **参数解释**： 用户名。 **取值范围**： 不涉及。

        :return: The user_name of this ListUserPoliciesResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ListUserPoliciesResponse.

        **参数解释**： 用户名。 **取值范围**： 不涉及。

        :param user_name: The user_name of this ListUserPoliciesResponse.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def total(self):
        r"""Gets the total of this ListUserPoliciesResponse.

        **参数解释**： 用户权限总数。 **取值范围**： 不涉及。

        :return: The total of this ListUserPoliciesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListUserPoliciesResponse.

        **参数解释**： 用户权限总数。 **取值范围**： 不涉及。

        :param total: The total of this ListUserPoliciesResponse.
        :type total: int
        """
        self._total = total

    @property
    def policies(self):
        r"""Gets the policies of this ListUserPoliciesResponse.

        **参数解释**： 用户权限列表。

        :return: The policies of this ListUserPoliciesResponse.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.UserPolicyResponeEntity`]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        r"""Sets the policies of this ListUserPoliciesResponse.

        **参数解释**： 用户权限列表。

        :param policies: The policies of this ListUserPoliciesResponse.
        :type policies: list[:class:`huaweicloudsdkkafka.v2.UserPolicyResponeEntity`]
        """
        self._policies = policies

    def to_dict(self):
        import warnings
        warnings.warn("ListUserPoliciesResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListUserPoliciesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
