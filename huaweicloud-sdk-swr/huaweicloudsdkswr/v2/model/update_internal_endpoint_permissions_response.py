# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInternalEndpointPermissionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permissions': 'list[str]',
        'permission_type': 'str'
    }

    attribute_map = {
        'permissions': 'permissions',
        'permission_type': 'permission_type'
    }

    def __init__(self, permissions=None, permission_type=None):
        r"""UpdateInternalEndpointPermissionsResponse

        The model defined in huaweicloud sdk

        :param permissions: 权限列表
        :type permissions: list[str]
        :param permission_type: 权限类型 取值范围： - domainId：基于账户ID配置终端节点服务白名单 - orgPath：基于账户所在组织路径配置终端节点服务白名单
        :type permission_type: str
        """
        
        super().__init__()

        self._permissions = None
        self._permission_type = None
        self.discriminator = None

        if permissions is not None:
            self.permissions = permissions
        if permission_type is not None:
            self.permission_type = permission_type

    @property
    def permissions(self):
        r"""Gets the permissions of this UpdateInternalEndpointPermissionsResponse.

        权限列表

        :return: The permissions of this UpdateInternalEndpointPermissionsResponse.
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        r"""Sets the permissions of this UpdateInternalEndpointPermissionsResponse.

        权限列表

        :param permissions: The permissions of this UpdateInternalEndpointPermissionsResponse.
        :type permissions: list[str]
        """
        self._permissions = permissions

    @property
    def permission_type(self):
        r"""Gets the permission_type of this UpdateInternalEndpointPermissionsResponse.

        权限类型 取值范围： - domainId：基于账户ID配置终端节点服务白名单 - orgPath：基于账户所在组织路径配置终端节点服务白名单

        :return: The permission_type of this UpdateInternalEndpointPermissionsResponse.
        :rtype: str
        """
        return self._permission_type

    @permission_type.setter
    def permission_type(self, permission_type):
        r"""Sets the permission_type of this UpdateInternalEndpointPermissionsResponse.

        权限类型 取值范围： - domainId：基于账户ID配置终端节点服务白名单 - orgPath：基于账户所在组织路径配置终端节点服务白名单

        :param permission_type: The permission_type of this UpdateInternalEndpointPermissionsResponse.
        :type permission_type: str
        """
        self._permission_type = permission_type

    def to_dict(self):
        import warnings
        warnings.warn("UpdateInternalEndpointPermissionsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, UpdateInternalEndpointPermissionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
