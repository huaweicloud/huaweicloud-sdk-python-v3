# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RoleSyncDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'role_id': 'str',
        'role_sync_enabled': 'bool',
        'role_name': 'str',
        'role_type': 'str',
        'role_chinese_name': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'role_id': 'role_id',
        'role_sync_enabled': 'role_sync_enabled',
        'role_name': 'role_name',
        'role_type': 'role_type',
        'role_chinese_name': 'role_chinese_name',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, role_id=None, role_sync_enabled=None, role_name=None, role_type=None, role_chinese_name=None, created_at=None, updated_at=None):
        r"""RoleSyncDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 角色记录id。
        :type id: int
        :param role_id: **参数解释：** 角色id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type role_id: str
        :param role_sync_enabled: **参数解释：** 角色同步开关。
        :type role_sync_enabled: bool
        :param role_name: **参数解释：** 角色名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type role_name: str
        :param role_type: **参数解释：** 角色类型。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type role_type: str
        :param role_chinese_name: **参数解释：** 角色中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type role_chinese_name: str
        :param created_at: **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type created_at: str
        :param updated_at: **参数解释：** 更新时间。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type updated_at: str
        """
        
        

        self._id = None
        self._role_id = None
        self._role_sync_enabled = None
        self._role_name = None
        self._role_type = None
        self._role_chinese_name = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if role_id is not None:
            self.role_id = role_id
        if role_sync_enabled is not None:
            self.role_sync_enabled = role_sync_enabled
        if role_name is not None:
            self.role_name = role_name
        if role_type is not None:
            self.role_type = role_type
        if role_chinese_name is not None:
            self.role_chinese_name = role_chinese_name
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this RoleSyncDto.

        **参数解释：** 角色记录id。

        :return: The id of this RoleSyncDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RoleSyncDto.

        **参数解释：** 角色记录id。

        :param id: The id of this RoleSyncDto.
        :type id: int
        """
        self._id = id

    @property
    def role_id(self):
        r"""Gets the role_id of this RoleSyncDto.

        **参数解释：** 角色id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The role_id of this RoleSyncDto.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        r"""Sets the role_id of this RoleSyncDto.

        **参数解释：** 角色id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param role_id: The role_id of this RoleSyncDto.
        :type role_id: str
        """
        self._role_id = role_id

    @property
    def role_sync_enabled(self):
        r"""Gets the role_sync_enabled of this RoleSyncDto.

        **参数解释：** 角色同步开关。

        :return: The role_sync_enabled of this RoleSyncDto.
        :rtype: bool
        """
        return self._role_sync_enabled

    @role_sync_enabled.setter
    def role_sync_enabled(self, role_sync_enabled):
        r"""Sets the role_sync_enabled of this RoleSyncDto.

        **参数解释：** 角色同步开关。

        :param role_sync_enabled: The role_sync_enabled of this RoleSyncDto.
        :type role_sync_enabled: bool
        """
        self._role_sync_enabled = role_sync_enabled

    @property
    def role_name(self):
        r"""Gets the role_name of this RoleSyncDto.

        **参数解释：** 角色名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The role_name of this RoleSyncDto.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        r"""Sets the role_name of this RoleSyncDto.

        **参数解释：** 角色名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param role_name: The role_name of this RoleSyncDto.
        :type role_name: str
        """
        self._role_name = role_name

    @property
    def role_type(self):
        r"""Gets the role_type of this RoleSyncDto.

        **参数解释：** 角色类型。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The role_type of this RoleSyncDto.
        :rtype: str
        """
        return self._role_type

    @role_type.setter
    def role_type(self, role_type):
        r"""Sets the role_type of this RoleSyncDto.

        **参数解释：** 角色类型。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param role_type: The role_type of this RoleSyncDto.
        :type role_type: str
        """
        self._role_type = role_type

    @property
    def role_chinese_name(self):
        r"""Gets the role_chinese_name of this RoleSyncDto.

        **参数解释：** 角色中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The role_chinese_name of this RoleSyncDto.
        :rtype: str
        """
        return self._role_chinese_name

    @role_chinese_name.setter
    def role_chinese_name(self, role_chinese_name):
        r"""Sets the role_chinese_name of this RoleSyncDto.

        **参数解释：** 角色中文名称。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param role_chinese_name: The role_chinese_name of this RoleSyncDto.
        :type role_chinese_name: str
        """
        self._role_chinese_name = role_chinese_name

    @property
    def created_at(self):
        r"""Gets the created_at of this RoleSyncDto.

        **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The created_at of this RoleSyncDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this RoleSyncDto.

        **参数解释：** 创建时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param created_at: The created_at of this RoleSyncDto.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this RoleSyncDto.

        **参数解释：** 更新时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The updated_at of this RoleSyncDto.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this RoleSyncDto.

        **参数解释：** 更新时间。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param updated_at: The updated_at of this RoleSyncDto.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, RoleSyncDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
