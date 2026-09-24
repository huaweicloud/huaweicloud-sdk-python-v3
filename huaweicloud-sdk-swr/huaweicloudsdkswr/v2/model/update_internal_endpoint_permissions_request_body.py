# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInternalEndpointPermissionsRequestBody:

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
        'action': 'str',
        'permission_type': 'str'
    }

    attribute_map = {
        'permissions': 'permissions',
        'action': 'action',
        'permission_type': 'permission_type'
    }

    def __init__(self, permissions=None, action=None, permission_type=None):
        r"""UpdateInternalEndpointPermissionsRequestBody

        The model defined in huaweicloud sdk

        :param permissions: 权限格式为： - iam:domain::domain_id。其中：\&quot;iam:domain::\&quot;为固定格式，\&quot;domain_id\&quot;为可连接用户的账号ID。domain_id类型支持输入包括\&quot;a~z\&quot;、\&quot;A~Z\&quot;、\&quot;0~9\&quot;或者\&quot;*\&quot;，最大长度可以传64。 - iam:domainName::domain_name_reg。其中：\&quot;iam:domainName::\&quot;为固定格式，\&quot;domain_name_reg\&quot;为可连接用户的账号名。domain_name_reg类型支持输入包括\&quot;a~z\&quot;、\&quot;A~Z\&quot;、\&quot;0~9\&quot;, \&quot;_+*.-?{},\&quot;，最大长度可以传80。 - organizations:orgPath::org_path。其中: \&quot;organizations:orgPath::\&quot;为固定格式，org_path为可连接用户的组织路径。 org_path类型支持\&quot;a~z\&quot;、\&quot;A~Z\&quot;、\&quot;0~9\&quot;、\&quot;/-?\&quot;或者\&quot;*\&quot;，最大长度可以传1024。 - \&quot;*\&quot; (表示所有终端节点可连接)  示例： - iam:domain::6e9dfd51d1124e8d8498dce894923a0dd - iam:domainName::op_svc_vpcep.* - organizations:orgPath::o-3j59d1231uprgk9yuvlidra7zbzfi578/r-rldbu1vmxdw5ahdkknxnvd5rgag77m2z/ou-7tuddd8nh99rebxltawsm6qct5z7rklv/* - \&quot;*\&quot;（表示所有终端节点可连接）
        :type permissions: list[str]
        :param action: 操作类型。取值范围: - add:增加内网白名单操作 - remove:删除内网白名单操作
        :type action: str
        :param permission_type: 权限类型。取值范围: - domainId：基于账户ID配置终端节点服务白名单 - orgPath：基于账户所在组织路径配置终端节点服务白名单
        :type permission_type: str
        """
        
        

        self._permissions = None
        self._action = None
        self._permission_type = None
        self.discriminator = None

        self.permissions = permissions
        self.action = action
        if permission_type is not None:
            self.permission_type = permission_type

    @property
    def permissions(self):
        r"""Gets the permissions of this UpdateInternalEndpointPermissionsRequestBody.

        权限格式为： - iam:domain::domain_id。其中：\"iam:domain::\"为固定格式，\"domain_id\"为可连接用户的账号ID。domain_id类型支持输入包括\"a~z\"、\"A~Z\"、\"0~9\"或者\"*\"，最大长度可以传64。 - iam:domainName::domain_name_reg。其中：\"iam:domainName::\"为固定格式，\"domain_name_reg\"为可连接用户的账号名。domain_name_reg类型支持输入包括\"a~z\"、\"A~Z\"、\"0~9\", \"_+*.-?{},\"，最大长度可以传80。 - organizations:orgPath::org_path。其中: \"organizations:orgPath::\"为固定格式，org_path为可连接用户的组织路径。 org_path类型支持\"a~z\"、\"A~Z\"、\"0~9\"、\"/-?\"或者\"*\"，最大长度可以传1024。 - \"*\" (表示所有终端节点可连接)  示例： - iam:domain::6e9dfd51d1124e8d8498dce894923a0dd - iam:domainName::op_svc_vpcep.* - organizations:orgPath::o-3j59d1231uprgk9yuvlidra7zbzfi578/r-rldbu1vmxdw5ahdkknxnvd5rgag77m2z/ou-7tuddd8nh99rebxltawsm6qct5z7rklv/* - \"*\"（表示所有终端节点可连接）

        :return: The permissions of this UpdateInternalEndpointPermissionsRequestBody.
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        r"""Sets the permissions of this UpdateInternalEndpointPermissionsRequestBody.

        权限格式为： - iam:domain::domain_id。其中：\"iam:domain::\"为固定格式，\"domain_id\"为可连接用户的账号ID。domain_id类型支持输入包括\"a~z\"、\"A~Z\"、\"0~9\"或者\"*\"，最大长度可以传64。 - iam:domainName::domain_name_reg。其中：\"iam:domainName::\"为固定格式，\"domain_name_reg\"为可连接用户的账号名。domain_name_reg类型支持输入包括\"a~z\"、\"A~Z\"、\"0~9\", \"_+*.-?{},\"，最大长度可以传80。 - organizations:orgPath::org_path。其中: \"organizations:orgPath::\"为固定格式，org_path为可连接用户的组织路径。 org_path类型支持\"a~z\"、\"A~Z\"、\"0~9\"、\"/-?\"或者\"*\"，最大长度可以传1024。 - \"*\" (表示所有终端节点可连接)  示例： - iam:domain::6e9dfd51d1124e8d8498dce894923a0dd - iam:domainName::op_svc_vpcep.* - organizations:orgPath::o-3j59d1231uprgk9yuvlidra7zbzfi578/r-rldbu1vmxdw5ahdkknxnvd5rgag77m2z/ou-7tuddd8nh99rebxltawsm6qct5z7rklv/* - \"*\"（表示所有终端节点可连接）

        :param permissions: The permissions of this UpdateInternalEndpointPermissionsRequestBody.
        :type permissions: list[str]
        """
        self._permissions = permissions

    @property
    def action(self):
        r"""Gets the action of this UpdateInternalEndpointPermissionsRequestBody.

        操作类型。取值范围: - add:增加内网白名单操作 - remove:删除内网白名单操作

        :return: The action of this UpdateInternalEndpointPermissionsRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this UpdateInternalEndpointPermissionsRequestBody.

        操作类型。取值范围: - add:增加内网白名单操作 - remove:删除内网白名单操作

        :param action: The action of this UpdateInternalEndpointPermissionsRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def permission_type(self):
        r"""Gets the permission_type of this UpdateInternalEndpointPermissionsRequestBody.

        权限类型。取值范围: - domainId：基于账户ID配置终端节点服务白名单 - orgPath：基于账户所在组织路径配置终端节点服务白名单

        :return: The permission_type of this UpdateInternalEndpointPermissionsRequestBody.
        :rtype: str
        """
        return self._permission_type

    @permission_type.setter
    def permission_type(self, permission_type):
        r"""Sets the permission_type of this UpdateInternalEndpointPermissionsRequestBody.

        权限类型。取值范围: - domainId：基于账户ID配置终端节点服务白名单 - orgPath：基于账户所在组织路径配置终端节点服务白名单

        :param permission_type: The permission_type of this UpdateInternalEndpointPermissionsRequestBody.
        :type permission_type: str
        """
        self._permission_type = permission_type

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
        if not isinstance(other, UpdateInternalEndpointPermissionsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
