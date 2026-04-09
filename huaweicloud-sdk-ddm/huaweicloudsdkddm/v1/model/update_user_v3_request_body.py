# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateUserV3RequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'base_authority': 'list[str]',
        'description': 'str',
        'password_lifetime': 'int',
        'databases': 'list[UpdateUserRelatedLogicDbV3]'
    }

    attribute_map = {
        'base_authority': 'base_authority',
        'description': 'description',
        'password_lifetime': 'password_lifetime',
        'databases': 'databases'
    }

    def __init__(self, base_authority=None, description=None, password_lifetime=None, databases=None):
        r"""UpdateUserV3RequestBody

        The model defined in huaweicloud sdk

        :param base_authority: **参数解释**：  DDM实例账号的基础权限。  **约束限制**：  无  **取值范围**：  CREATE、DROP、ALTER、INDEX、INSERT、DELETE、UPDATE、SELECT的任意集合  **默认取值**：  不涉及。
        :type base_authority: list[str]
        :param description: **参数解释**：  实例账号的描述信息。  **约束限制**：  - 长度不超过256个字符。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type description: str
        :param password_lifetime: **参数解释**：  DDM实例账号的密码有效期。  **约束限制**：  不涉及。   **取值范围**：  取值范围为0-65535的整数，单位为天。  0与空表示密码永不过期。  **默认取值**：  默认值为空，永不过期。
        :type password_lifetime: int
        :param databases: 关联的逻辑库的集合。 databases字段可以省略，即创建用户时可以不关联逻辑库。
        :type databases: list[:class:`huaweicloudsdkddm.v1.UpdateUserRelatedLogicDbV3`]
        """
        
        

        self._base_authority = None
        self._description = None
        self._password_lifetime = None
        self._databases = None
        self.discriminator = None

        if base_authority is not None:
            self.base_authority = base_authority
        if description is not None:
            self.description = description
        if password_lifetime is not None:
            self.password_lifetime = password_lifetime
        if databases is not None:
            self.databases = databases

    @property
    def base_authority(self):
        r"""Gets the base_authority of this UpdateUserV3RequestBody.

        **参数解释**：  DDM实例账号的基础权限。  **约束限制**：  无  **取值范围**：  CREATE、DROP、ALTER、INDEX、INSERT、DELETE、UPDATE、SELECT的任意集合  **默认取值**：  不涉及。

        :return: The base_authority of this UpdateUserV3RequestBody.
        :rtype: list[str]
        """
        return self._base_authority

    @base_authority.setter
    def base_authority(self, base_authority):
        r"""Sets the base_authority of this UpdateUserV3RequestBody.

        **参数解释**：  DDM实例账号的基础权限。  **约束限制**：  无  **取值范围**：  CREATE、DROP、ALTER、INDEX、INSERT、DELETE、UPDATE、SELECT的任意集合  **默认取值**：  不涉及。

        :param base_authority: The base_authority of this UpdateUserV3RequestBody.
        :type base_authority: list[str]
        """
        self._base_authority = base_authority

    @property
    def description(self):
        r"""Gets the description of this UpdateUserV3RequestBody.

        **参数解释**：  实例账号的描述信息。  **约束限制**：  - 长度不超过256个字符。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The description of this UpdateUserV3RequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateUserV3RequestBody.

        **参数解释**：  实例账号的描述信息。  **约束限制**：  - 长度不超过256个字符。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param description: The description of this UpdateUserV3RequestBody.
        :type description: str
        """
        self._description = description

    @property
    def password_lifetime(self):
        r"""Gets the password_lifetime of this UpdateUserV3RequestBody.

        **参数解释**：  DDM实例账号的密码有效期。  **约束限制**：  不涉及。   **取值范围**：  取值范围为0-65535的整数，单位为天。  0与空表示密码永不过期。  **默认取值**：  默认值为空，永不过期。

        :return: The password_lifetime of this UpdateUserV3RequestBody.
        :rtype: int
        """
        return self._password_lifetime

    @password_lifetime.setter
    def password_lifetime(self, password_lifetime):
        r"""Sets the password_lifetime of this UpdateUserV3RequestBody.

        **参数解释**：  DDM实例账号的密码有效期。  **约束限制**：  不涉及。   **取值范围**：  取值范围为0-65535的整数，单位为天。  0与空表示密码永不过期。  **默认取值**：  默认值为空，永不过期。

        :param password_lifetime: The password_lifetime of this UpdateUserV3RequestBody.
        :type password_lifetime: int
        """
        self._password_lifetime = password_lifetime

    @property
    def databases(self):
        r"""Gets the databases of this UpdateUserV3RequestBody.

        关联的逻辑库的集合。 databases字段可以省略，即创建用户时可以不关联逻辑库。

        :return: The databases of this UpdateUserV3RequestBody.
        :rtype: list[:class:`huaweicloudsdkddm.v1.UpdateUserRelatedLogicDbV3`]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        r"""Sets the databases of this UpdateUserV3RequestBody.

        关联的逻辑库的集合。 databases字段可以省略，即创建用户时可以不关联逻辑库。

        :param databases: The databases of this UpdateUserV3RequestBody.
        :type databases: list[:class:`huaweicloudsdkddm.v1.UpdateUserRelatedLogicDbV3`]
        """
        self._databases = databases

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
        if not isinstance(other, UpdateUserV3RequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
