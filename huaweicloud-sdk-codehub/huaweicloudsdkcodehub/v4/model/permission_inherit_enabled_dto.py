# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PermissionInheritEnabledDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'inherit_parent_permission': 'bool'
    }

    attribute_map = {
        'inherit_parent_permission': 'inherit_parent_permission'
    }

    def __init__(self, inherit_parent_permission=None):
        r"""PermissionInheritEnabledDto

        The model defined in huaweicloud sdk

        :param inherit_parent_permission: **参数解释：** 权限继承设置。 **约束限制：** 不涉及。 **取值范围：** - true，使用上层权限配置，如果上层是代码组使用代码组权限配置，如果上层是项目使用项目权限配置。 - false，使用仓库权限配置。 
        :type inherit_parent_permission: bool
        """
        
        

        self._inherit_parent_permission = None
        self.discriminator = None

        self.inherit_parent_permission = inherit_parent_permission

    @property
    def inherit_parent_permission(self):
        r"""Gets the inherit_parent_permission of this PermissionInheritEnabledDto.

        **参数解释：** 权限继承设置。 **约束限制：** 不涉及。 **取值范围：** - true，使用上层权限配置，如果上层是代码组使用代码组权限配置，如果上层是项目使用项目权限配置。 - false，使用仓库权限配置。 

        :return: The inherit_parent_permission of this PermissionInheritEnabledDto.
        :rtype: bool
        """
        return self._inherit_parent_permission

    @inherit_parent_permission.setter
    def inherit_parent_permission(self, inherit_parent_permission):
        r"""Sets the inherit_parent_permission of this PermissionInheritEnabledDto.

        **参数解释：** 权限继承设置。 **约束限制：** 不涉及。 **取值范围：** - true，使用上层权限配置，如果上层是代码组使用代码组权限配置，如果上层是项目使用项目权限配置。 - false，使用仓库权限配置。 

        :param inherit_parent_permission: The inherit_parent_permission of this PermissionInheritEnabledDto.
        :type inherit_parent_permission: bool
        """
        self._inherit_parent_permission = inherit_parent_permission

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
        if not isinstance(other, PermissionInheritEnabledDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
