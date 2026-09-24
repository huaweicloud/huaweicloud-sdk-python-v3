# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PermissionItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'permission': 'str',
        'permission_type': 'str',
        'created_at': 'str',
        'protected': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'permission': 'permission',
        'permission_type': 'permission_type',
        'created_at': 'created_at',
        'protected': 'protected'
    }

    def __init__(self, id=None, permission=None, permission_type=None, created_at=None, protected=None):
        r"""PermissionItem

        The model defined in huaweicloud sdk

        :param id: 权限uuid
        :type id: str
        :param permission: 权限内容。权限格式为： - iam:domain::domain_id。其中：\&quot;iam:domain::\&quot;为固定格式，\&quot;domain_id\&quot;为可连接用户的账号ID。domain_id类型支持输入包括\&quot;a~z\&quot;、\&quot;A~Z\&quot;、\&quot;0~9\&quot;或者\&quot;*\&quot;，最大长度可以传64。 - iam:domainName::domain_name_reg。其中：\&quot;iam:domainName::\&quot;为固定格式，\&quot;domain_name_reg\&quot;为可连接用户的账号名。domain_name_reg类型支持输入包括\&quot;a~z\&quot;、\&quot;A~Z\&quot;、\&quot;0~9\&quot;, \&quot;_+*.-?{},\&quot;，最大长度可以传80。 - organizations:orgPath::org_path。其中: \&quot;organizations:orgPath::\&quot;为固定格式，org_path为可连接用户的组织路径。 org_path类型支持\&quot;a~z\&quot;、\&quot;A~Z\&quot;、\&quot;0~9\&quot;、\&quot;/-?\&quot;或者\&quot;*\&quot;，最大长度可以传1024。 - \&quot;*\&quot; (表示所有终端节点可连接)  示例： - iam:domain::6e9dfd51d1124e8d8498dce894923a0dd - iam:domainName::op_svc_vpcep.* - organizations:orgPath::o-3j59d1231uprgk9yuvlidra7zbzfi578/r-rldbu1vmxdw5ahdkknxnvd5rgag77m2z/ou-7tuddd8nh99rebxltawsm6qct5z7rklv/* - \&quot;*\&quot; (表示所有终端节点可连接)
        :type permission: str
        :param permission_type: 权限类型。取值范围： - domainId：基于账户ID配置终端节点服务白名单 - orgPath：基于账户所在组织路径配置终端节点服务白名单
        :type permission_type: str
        :param created_at: 白名单的添加时间。采用UTC时间格式，格式为：YYYY-MM-DDTHH:MM:SSZ
        :type created_at: str
        :param protected: 是否为保护内网访问白名单；如果为true则不允许添加或者移除
        :type protected: bool
        """
        
        

        self._id = None
        self._permission = None
        self._permission_type = None
        self._created_at = None
        self._protected = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if permission is not None:
            self.permission = permission
        if permission_type is not None:
            self.permission_type = permission_type
        if created_at is not None:
            self.created_at = created_at
        if protected is not None:
            self.protected = protected

    @property
    def id(self):
        r"""Gets the id of this PermissionItem.

        权限uuid

        :return: The id of this PermissionItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PermissionItem.

        权限uuid

        :param id: The id of this PermissionItem.
        :type id: str
        """
        self._id = id

    @property
    def permission(self):
        r"""Gets the permission of this PermissionItem.

        权限内容。权限格式为： - iam:domain::domain_id。其中：\"iam:domain::\"为固定格式，\"domain_id\"为可连接用户的账号ID。domain_id类型支持输入包括\"a~z\"、\"A~Z\"、\"0~9\"或者\"*\"，最大长度可以传64。 - iam:domainName::domain_name_reg。其中：\"iam:domainName::\"为固定格式，\"domain_name_reg\"为可连接用户的账号名。domain_name_reg类型支持输入包括\"a~z\"、\"A~Z\"、\"0~9\", \"_+*.-?{},\"，最大长度可以传80。 - organizations:orgPath::org_path。其中: \"organizations:orgPath::\"为固定格式，org_path为可连接用户的组织路径。 org_path类型支持\"a~z\"、\"A~Z\"、\"0~9\"、\"/-?\"或者\"*\"，最大长度可以传1024。 - \"*\" (表示所有终端节点可连接)  示例： - iam:domain::6e9dfd51d1124e8d8498dce894923a0dd - iam:domainName::op_svc_vpcep.* - organizations:orgPath::o-3j59d1231uprgk9yuvlidra7zbzfi578/r-rldbu1vmxdw5ahdkknxnvd5rgag77m2z/ou-7tuddd8nh99rebxltawsm6qct5z7rklv/* - \"*\" (表示所有终端节点可连接)

        :return: The permission of this PermissionItem.
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        r"""Sets the permission of this PermissionItem.

        权限内容。权限格式为： - iam:domain::domain_id。其中：\"iam:domain::\"为固定格式，\"domain_id\"为可连接用户的账号ID。domain_id类型支持输入包括\"a~z\"、\"A~Z\"、\"0~9\"或者\"*\"，最大长度可以传64。 - iam:domainName::domain_name_reg。其中：\"iam:domainName::\"为固定格式，\"domain_name_reg\"为可连接用户的账号名。domain_name_reg类型支持输入包括\"a~z\"、\"A~Z\"、\"0~9\", \"_+*.-?{},\"，最大长度可以传80。 - organizations:orgPath::org_path。其中: \"organizations:orgPath::\"为固定格式，org_path为可连接用户的组织路径。 org_path类型支持\"a~z\"、\"A~Z\"、\"0~9\"、\"/-?\"或者\"*\"，最大长度可以传1024。 - \"*\" (表示所有终端节点可连接)  示例： - iam:domain::6e9dfd51d1124e8d8498dce894923a0dd - iam:domainName::op_svc_vpcep.* - organizations:orgPath::o-3j59d1231uprgk9yuvlidra7zbzfi578/r-rldbu1vmxdw5ahdkknxnvd5rgag77m2z/ou-7tuddd8nh99rebxltawsm6qct5z7rklv/* - \"*\" (表示所有终端节点可连接)

        :param permission: The permission of this PermissionItem.
        :type permission: str
        """
        self._permission = permission

    @property
    def permission_type(self):
        r"""Gets the permission_type of this PermissionItem.

        权限类型。取值范围： - domainId：基于账户ID配置终端节点服务白名单 - orgPath：基于账户所在组织路径配置终端节点服务白名单

        :return: The permission_type of this PermissionItem.
        :rtype: str
        """
        return self._permission_type

    @permission_type.setter
    def permission_type(self, permission_type):
        r"""Sets the permission_type of this PermissionItem.

        权限类型。取值范围： - domainId：基于账户ID配置终端节点服务白名单 - orgPath：基于账户所在组织路径配置终端节点服务白名单

        :param permission_type: The permission_type of this PermissionItem.
        :type permission_type: str
        """
        self._permission_type = permission_type

    @property
    def created_at(self):
        r"""Gets the created_at of this PermissionItem.

        白名单的添加时间。采用UTC时间格式，格式为：YYYY-MM-DDTHH:MM:SSZ

        :return: The created_at of this PermissionItem.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this PermissionItem.

        白名单的添加时间。采用UTC时间格式，格式为：YYYY-MM-DDTHH:MM:SSZ

        :param created_at: The created_at of this PermissionItem.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def protected(self):
        r"""Gets the protected of this PermissionItem.

        是否为保护内网访问白名单；如果为true则不允许添加或者移除

        :return: The protected of this PermissionItem.
        :rtype: bool
        """
        return self._protected

    @protected.setter
    def protected(self, protected):
        r"""Sets the protected of this PermissionItem.

        是否为保护内网访问白名单；如果为true则不允许添加或者移除

        :param protected: The protected of this PermissionItem.
        :type protected: bool
        """
        self._protected = protected

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
        if not isinstance(other, PermissionItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
