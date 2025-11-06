# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePermissionDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permission_id': 'int',
        'enabled': 'bool'
    }

    attribute_map = {
        'permission_id': 'permission_id',
        'enabled': 'enabled'
    }

    def __init__(self, permission_id=None, enabled=None):
        r"""UpdatePermissionDetail

        The model defined in huaweicloud sdk

        :param permission_id: **参数解释：** 权限点id **取值范围：** 不涉及。
        :type permission_id: int
        :param enabled: **参数解释：** 权限点状态 **取值范围：** - true, 开启。 - false, 关闭。  
        :type enabled: bool
        """
        
        

        self._permission_id = None
        self._enabled = None
        self.discriminator = None

        if permission_id is not None:
            self.permission_id = permission_id
        if enabled is not None:
            self.enabled = enabled

    @property
    def permission_id(self):
        r"""Gets the permission_id of this UpdatePermissionDetail.

        **参数解释：** 权限点id **取值范围：** 不涉及。

        :return: The permission_id of this UpdatePermissionDetail.
        :rtype: int
        """
        return self._permission_id

    @permission_id.setter
    def permission_id(self, permission_id):
        r"""Sets the permission_id of this UpdatePermissionDetail.

        **参数解释：** 权限点id **取值范围：** 不涉及。

        :param permission_id: The permission_id of this UpdatePermissionDetail.
        :type permission_id: int
        """
        self._permission_id = permission_id

    @property
    def enabled(self):
        r"""Gets the enabled of this UpdatePermissionDetail.

        **参数解释：** 权限点状态 **取值范围：** - true, 开启。 - false, 关闭。  

        :return: The enabled of this UpdatePermissionDetail.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this UpdatePermissionDetail.

        **参数解释：** 权限点状态 **取值范围：** - true, 开启。 - false, 关闭。  

        :param enabled: The enabled of this UpdatePermissionDetail.
        :type enabled: bool
        """
        self._enabled = enabled

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
        if not isinstance(other, UpdatePermissionDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
