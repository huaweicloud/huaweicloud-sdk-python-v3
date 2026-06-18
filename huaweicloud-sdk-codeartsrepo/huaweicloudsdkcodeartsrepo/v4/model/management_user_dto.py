# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ManagementUserDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'username': 'str',
        'nick_name': 'str',
        'tenant_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'username': 'username',
        'nick_name': 'nick_name',
        'tenant_name': 'tenant_name'
    }

    def __init__(self, name=None, username=None, nick_name=None, tenant_name=None):
        r"""ManagementUserDto

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 成员名称。 **取值范围：** 不涉及。
        :type name: str
        :param username: **参数解释：** 用户名。 **取值范围：** 不涉及
        :type username: str
        :param nick_name: **参数解释：** 昵称。 **取值范围：** 不涉及
        :type nick_name: str
        :param tenant_name: **参数解释：** 租户名称。 **取值范围：** 不涉及
        :type tenant_name: str
        """
        
        

        self._name = None
        self._username = None
        self._nick_name = None
        self._tenant_name = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if username is not None:
            self.username = username
        if nick_name is not None:
            self.nick_name = nick_name
        if tenant_name is not None:
            self.tenant_name = tenant_name

    @property
    def name(self):
        r"""Gets the name of this ManagementUserDto.

        **参数解释：** 成员名称。 **取值范围：** 不涉及。

        :return: The name of this ManagementUserDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ManagementUserDto.

        **参数解释：** 成员名称。 **取值范围：** 不涉及。

        :param name: The name of this ManagementUserDto.
        :type name: str
        """
        self._name = name

    @property
    def username(self):
        r"""Gets the username of this ManagementUserDto.

        **参数解释：** 用户名。 **取值范围：** 不涉及

        :return: The username of this ManagementUserDto.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        r"""Sets the username of this ManagementUserDto.

        **参数解释：** 用户名。 **取值范围：** 不涉及

        :param username: The username of this ManagementUserDto.
        :type username: str
        """
        self._username = username

    @property
    def nick_name(self):
        r"""Gets the nick_name of this ManagementUserDto.

        **参数解释：** 昵称。 **取值范围：** 不涉及

        :return: The nick_name of this ManagementUserDto.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this ManagementUserDto.

        **参数解释：** 昵称。 **取值范围：** 不涉及

        :param nick_name: The nick_name of this ManagementUserDto.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def tenant_name(self):
        r"""Gets the tenant_name of this ManagementUserDto.

        **参数解释：** 租户名称。 **取值范围：** 不涉及

        :return: The tenant_name of this ManagementUserDto.
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        r"""Sets the tenant_name of this ManagementUserDto.

        **参数解释：** 租户名称。 **取值范围：** 不涉及

        :param tenant_name: The tenant_name of this ManagementUserDto.
        :type tenant_name: str
        """
        self._tenant_name = tenant_name

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
        if not isinstance(other, ManagementUserDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
