# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRepoRolesPrivilegeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role_id': 'str',
        'body': 'RolePrivilegeV5'
    }

    attribute_map = {
        'role_id': 'role_id',
        'body': 'body'
    }

    def __init__(self, role_id=None, body=None):
        r"""UpdateRepoRolesPrivilegeRequest

        The model defined in huaweicloud sdk

        :param role_id: **参数解释**: 角色id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。
        :type role_id: str
        :param body: Body of the UpdateRepoRolesPrivilegeRequest
        :type body: :class:`huaweicloudsdkcodeartsartifact.v2.RolePrivilegeV5`
        """
        
        

        self._role_id = None
        self._body = None
        self.discriminator = None

        self.role_id = role_id
        if body is not None:
            self.body = body

    @property
    def role_id(self):
        r"""Gets the role_id of this UpdateRepoRolesPrivilegeRequest.

        **参数解释**: 角色id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。

        :return: The role_id of this UpdateRepoRolesPrivilegeRequest.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        r"""Sets the role_id of this UpdateRepoRolesPrivilegeRequest.

        **参数解释**: 角色id。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 无。

        :param role_id: The role_id of this UpdateRepoRolesPrivilegeRequest.
        :type role_id: str
        """
        self._role_id = role_id

    @property
    def body(self):
        r"""Gets the body of this UpdateRepoRolesPrivilegeRequest.

        :return: The body of this UpdateRepoRolesPrivilegeRequest.
        :rtype: :class:`huaweicloudsdkcodeartsartifact.v2.RolePrivilegeV5`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateRepoRolesPrivilegeRequest.

        :param body: The body of this UpdateRepoRolesPrivilegeRequest.
        :type body: :class:`huaweicloudsdkcodeartsartifact.v2.RolePrivilegeV5`
        """
        self._body = body

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
        if not isinstance(other, UpdateRepoRolesPrivilegeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
