# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserRefPermissionBasicDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'has_permission': 'bool',
        'is_protect': 'bool'
    }

    attribute_map = {
        'has_permission': 'has_permission',
        'is_protect': 'is_protect'
    }

    def __init__(self, has_permission=None, is_protect=None):
        r"""UserRefPermissionBasicDto

        The model defined in huaweicloud sdk

        :param has_permission: **参数解释：** 是否有权限。 **取值范围：** true：有权限，false：没权限
        :type has_permission: bool
        :param is_protect: **参数解释：** 是否保护分支。 **取值范围：** true：是保护分支，false：非保护分支
        :type is_protect: bool
        """
        
        

        self._has_permission = None
        self._is_protect = None
        self.discriminator = None

        if has_permission is not None:
            self.has_permission = has_permission
        if is_protect is not None:
            self.is_protect = is_protect

    @property
    def has_permission(self):
        r"""Gets the has_permission of this UserRefPermissionBasicDto.

        **参数解释：** 是否有权限。 **取值范围：** true：有权限，false：没权限

        :return: The has_permission of this UserRefPermissionBasicDto.
        :rtype: bool
        """
        return self._has_permission

    @has_permission.setter
    def has_permission(self, has_permission):
        r"""Sets the has_permission of this UserRefPermissionBasicDto.

        **参数解释：** 是否有权限。 **取值范围：** true：有权限，false：没权限

        :param has_permission: The has_permission of this UserRefPermissionBasicDto.
        :type has_permission: bool
        """
        self._has_permission = has_permission

    @property
    def is_protect(self):
        r"""Gets the is_protect of this UserRefPermissionBasicDto.

        **参数解释：** 是否保护分支。 **取值范围：** true：是保护分支，false：非保护分支

        :return: The is_protect of this UserRefPermissionBasicDto.
        :rtype: bool
        """
        return self._is_protect

    @is_protect.setter
    def is_protect(self, is_protect):
        r"""Sets the is_protect of this UserRefPermissionBasicDto.

        **参数解释：** 是否保护分支。 **取值范围：** true：是保护分支，false：非保护分支

        :param is_protect: The is_protect of this UserRefPermissionBasicDto.
        :type is_protect: bool
        """
        self._is_protect = is_protect

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
        if not isinstance(other, UserRefPermissionBasicDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
