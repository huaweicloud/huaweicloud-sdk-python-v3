# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResponsePermissionInfo:

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
        'role_name_cn': 'str',
        'resource_permissions': 'dict(str, object)'
    }

    attribute_map = {
        'role_id': 'role_id',
        'role_name': 'role_name',
        'role_name_cn': 'role_name_cn',
        'resource_permissions': 'resource_permissions'
    }

    def __init__(self, role_id=None, role_name=None, role_name_cn=None, resource_permissions=None):
        r"""ResponsePermissionInfo

        The model defined in huaweicloud sdk

        :param role_id: **参数解释：** 角色id **取值范围：** 不涉及。
        :type role_id: str
        :param role_name: **参数解释：** 角色名称 **取值范围：** 不涉及。
        :type role_name: str
        :param role_name_cn: **参数解释：** 角色中文名称 **取值范围：** 不涉及。
        :type role_name_cn: str
        :param resource_permissions: 
        :type resource_permissions: dict(str, object)
        """
        
        

        self._role_id = None
        self._role_name = None
        self._role_name_cn = None
        self._resource_permissions = None
        self.discriminator = None

        if role_id is not None:
            self.role_id = role_id
        if role_name is not None:
            self.role_name = role_name
        if role_name_cn is not None:
            self.role_name_cn = role_name_cn
        if resource_permissions is not None:
            self.resource_permissions = resource_permissions

    @property
    def role_id(self):
        r"""Gets the role_id of this ResponsePermissionInfo.

        **参数解释：** 角色id **取值范围：** 不涉及。

        :return: The role_id of this ResponsePermissionInfo.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        r"""Sets the role_id of this ResponsePermissionInfo.

        **参数解释：** 角色id **取值范围：** 不涉及。

        :param role_id: The role_id of this ResponsePermissionInfo.
        :type role_id: str
        """
        self._role_id = role_id

    @property
    def role_name(self):
        r"""Gets the role_name of this ResponsePermissionInfo.

        **参数解释：** 角色名称 **取值范围：** 不涉及。

        :return: The role_name of this ResponsePermissionInfo.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        r"""Sets the role_name of this ResponsePermissionInfo.

        **参数解释：** 角色名称 **取值范围：** 不涉及。

        :param role_name: The role_name of this ResponsePermissionInfo.
        :type role_name: str
        """
        self._role_name = role_name

    @property
    def role_name_cn(self):
        r"""Gets the role_name_cn of this ResponsePermissionInfo.

        **参数解释：** 角色中文名称 **取值范围：** 不涉及。

        :return: The role_name_cn of this ResponsePermissionInfo.
        :rtype: str
        """
        return self._role_name_cn

    @role_name_cn.setter
    def role_name_cn(self, role_name_cn):
        r"""Sets the role_name_cn of this ResponsePermissionInfo.

        **参数解释：** 角色中文名称 **取值范围：** 不涉及。

        :param role_name_cn: The role_name_cn of this ResponsePermissionInfo.
        :type role_name_cn: str
        """
        self._role_name_cn = role_name_cn

    @property
    def resource_permissions(self):
        r"""Gets the resource_permissions of this ResponsePermissionInfo.

        :return: The resource_permissions of this ResponsePermissionInfo.
        :rtype: dict(str, object)
        """
        return self._resource_permissions

    @resource_permissions.setter
    def resource_permissions(self, resource_permissions):
        r"""Sets the resource_permissions of this ResponsePermissionInfo.

        :param resource_permissions: The resource_permissions of this ResponsePermissionInfo.
        :type resource_permissions: dict(str, object)
        """
        self._resource_permissions = resource_permissions

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
        if not isinstance(other, ResponsePermissionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
