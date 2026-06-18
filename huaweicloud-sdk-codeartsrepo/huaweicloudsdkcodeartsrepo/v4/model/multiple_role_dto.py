# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MultipleRoleDto:

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
        'role_name': 'str',
        'role_chinese_name': 'str'
    }

    attribute_map = {
        'role_id': 'role_id',
        'role_name': 'role_name',
        'role_chinese_name': 'role_chinese_name'
    }

    def __init__(self, role_id=None, role_name=None, role_chinese_name=None):
        r"""MultipleRoleDto

        The model defined in huaweicloud sdk

        :param role_id: **参数解释：** 角色id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type role_id: str
        :param role_name: **参数解释：** 角色名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type role_name: str
        :param role_chinese_name: **参数解释：** 角色中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type role_chinese_name: str
        """
        
        

        self._role_id = None
        self._role_name = None
        self._role_chinese_name = None
        self.discriminator = None

        if role_id is not None:
            self.role_id = role_id
        if role_name is not None:
            self.role_name = role_name
        if role_chinese_name is not None:
            self.role_chinese_name = role_chinese_name

    @property
    def role_id(self):
        r"""Gets the role_id of this MultipleRoleDto.

        **参数解释：** 角色id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The role_id of this MultipleRoleDto.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        r"""Sets the role_id of this MultipleRoleDto.

        **参数解释：** 角色id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param role_id: The role_id of this MultipleRoleDto.
        :type role_id: str
        """
        self._role_id = role_id

    @property
    def role_name(self):
        r"""Gets the role_name of this MultipleRoleDto.

        **参数解释：** 角色名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The role_name of this MultipleRoleDto.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        r"""Sets the role_name of this MultipleRoleDto.

        **参数解释：** 角色名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param role_name: The role_name of this MultipleRoleDto.
        :type role_name: str
        """
        self._role_name = role_name

    @property
    def role_chinese_name(self):
        r"""Gets the role_chinese_name of this MultipleRoleDto.

        **参数解释：** 角色中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The role_chinese_name of this MultipleRoleDto.
        :rtype: str
        """
        return self._role_chinese_name

    @role_chinese_name.setter
    def role_chinese_name(self, role_chinese_name):
        r"""Sets the role_chinese_name of this MultipleRoleDto.

        **参数解释：** 角色中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param role_chinese_name: The role_chinese_name of this MultipleRoleDto.
        :type role_chinese_name: str
        """
        self._role_chinese_name = role_chinese_name

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
        if not isinstance(other, MultipleRoleDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
