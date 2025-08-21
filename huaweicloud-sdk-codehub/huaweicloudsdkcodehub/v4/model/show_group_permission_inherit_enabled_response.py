# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGroupPermissionInheritEnabledResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permission_inherit_enabled': 'bool'
    }

    attribute_map = {
        'permission_inherit_enabled': 'permission_inherit_enabled'
    }

    def __init__(self, permission_inherit_enabled=None):
        r"""ShowGroupPermissionInheritEnabledResponse

        The model defined in huaweicloud sdk

        :param permission_inherit_enabled: **参数解释：** 使用项目权限配置开关是否开启。
        :type permission_inherit_enabled: bool
        """
        
        super(ShowGroupPermissionInheritEnabledResponse, self).__init__()

        self._permission_inherit_enabled = None
        self.discriminator = None

        if permission_inherit_enabled is not None:
            self.permission_inherit_enabled = permission_inherit_enabled

    @property
    def permission_inherit_enabled(self):
        r"""Gets the permission_inherit_enabled of this ShowGroupPermissionInheritEnabledResponse.

        **参数解释：** 使用项目权限配置开关是否开启。

        :return: The permission_inherit_enabled of this ShowGroupPermissionInheritEnabledResponse.
        :rtype: bool
        """
        return self._permission_inherit_enabled

    @permission_inherit_enabled.setter
    def permission_inherit_enabled(self, permission_inherit_enabled):
        r"""Sets the permission_inherit_enabled of this ShowGroupPermissionInheritEnabledResponse.

        **参数解释：** 使用项目权限配置开关是否开启。

        :param permission_inherit_enabled: The permission_inherit_enabled of this ShowGroupPermissionInheritEnabledResponse.
        :type permission_inherit_enabled: bool
        """
        self._permission_inherit_enabled = permission_inherit_enabled

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
        if not isinstance(other, ShowGroupPermissionInheritEnabledResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
