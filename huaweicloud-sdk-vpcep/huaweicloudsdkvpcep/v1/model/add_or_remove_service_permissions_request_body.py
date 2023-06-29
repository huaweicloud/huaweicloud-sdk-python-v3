# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddOrRemoveServicePermissionsRequestBody:

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
        'permission_type': 'str',
        'action': 'str'
    }

    attribute_map = {
        'permissions': 'permissions',
        'permission_type': 'permission_type',
        'action': 'action'
    }

    def __init__(self, permissions=None, permission_type=None, action=None):
        """AddOrRemoveServicePermissionsRequestBody

        The model defined in huaweicloud sdk

        :param permissions: permission列表。 权限格式为：iam:domain::domain_id或者organizations:orgPath::org_path其中， ● “iam:domain::”和“organizations:orgPath::”为固定格式。 ● “domain_id”为可连接用户的帐号ID，org_path可连接用户的组织路径 domain_id类型支持输入包括“a~z”、“A~Z”、“0~9”或者“*，最大长度可以传64； org_path类型支持“a~z”、“A~Z”、“0~9”、“/-*?”或者“*”，最大长度可以传1024； “*”表示所有终端节点可连接。 例如：iam:domain::6e9dfd51d1124e8d8498dce894923a0dd或者organizations:orgPath::o-3j59d1231uprgk9yuvlidra7zbzfi578/r-rldbu1vmxdw5ahdkknxnvd5rgag77m2z/ou-7tuddd8nh99rebxltawsm6qct5z7rklv/*
        :type permissions: list[str]
        :param permission_type: 终端节点服务白名单类型。 ● domainId：基于账户ID配置终端节点服务白名单。 ● orgPath：基于账户所在组织路径配置终端节点服务白名单。
        :type permission_type: str
        :param action: 要执行的操作。 add/remove。
        :type action: str
        """
        
        

        self._permissions = None
        self._permission_type = None
        self._action = None
        self.discriminator = None

        self.permissions = permissions
        if permission_type is not None:
            self.permission_type = permission_type
        self.action = action

    @property
    def permissions(self):
        """Gets the permissions of this AddOrRemoveServicePermissionsRequestBody.

        permission列表。 权限格式为：iam:domain::domain_id或者organizations:orgPath::org_path其中， ● “iam:domain::”和“organizations:orgPath::”为固定格式。 ● “domain_id”为可连接用户的帐号ID，org_path可连接用户的组织路径 domain_id类型支持输入包括“a~z”、“A~Z”、“0~9”或者“*，最大长度可以传64； org_path类型支持“a~z”、“A~Z”、“0~9”、“/-*?”或者“*”，最大长度可以传1024； “*”表示所有终端节点可连接。 例如：iam:domain::6e9dfd51d1124e8d8498dce894923a0dd或者organizations:orgPath::o-3j59d1231uprgk9yuvlidra7zbzfi578/r-rldbu1vmxdw5ahdkknxnvd5rgag77m2z/ou-7tuddd8nh99rebxltawsm6qct5z7rklv/*

        :return: The permissions of this AddOrRemoveServicePermissionsRequestBody.
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this AddOrRemoveServicePermissionsRequestBody.

        permission列表。 权限格式为：iam:domain::domain_id或者organizations:orgPath::org_path其中， ● “iam:domain::”和“organizations:orgPath::”为固定格式。 ● “domain_id”为可连接用户的帐号ID，org_path可连接用户的组织路径 domain_id类型支持输入包括“a~z”、“A~Z”、“0~9”或者“*，最大长度可以传64； org_path类型支持“a~z”、“A~Z”、“0~9”、“/-*?”或者“*”，最大长度可以传1024； “*”表示所有终端节点可连接。 例如：iam:domain::6e9dfd51d1124e8d8498dce894923a0dd或者organizations:orgPath::o-3j59d1231uprgk9yuvlidra7zbzfi578/r-rldbu1vmxdw5ahdkknxnvd5rgag77m2z/ou-7tuddd8nh99rebxltawsm6qct5z7rklv/*

        :param permissions: The permissions of this AddOrRemoveServicePermissionsRequestBody.
        :type permissions: list[str]
        """
        self._permissions = permissions

    @property
    def permission_type(self):
        """Gets the permission_type of this AddOrRemoveServicePermissionsRequestBody.

        终端节点服务白名单类型。 ● domainId：基于账户ID配置终端节点服务白名单。 ● orgPath：基于账户所在组织路径配置终端节点服务白名单。

        :return: The permission_type of this AddOrRemoveServicePermissionsRequestBody.
        :rtype: str
        """
        return self._permission_type

    @permission_type.setter
    def permission_type(self, permission_type):
        """Sets the permission_type of this AddOrRemoveServicePermissionsRequestBody.

        终端节点服务白名单类型。 ● domainId：基于账户ID配置终端节点服务白名单。 ● orgPath：基于账户所在组织路径配置终端节点服务白名单。

        :param permission_type: The permission_type of this AddOrRemoveServicePermissionsRequestBody.
        :type permission_type: str
        """
        self._permission_type = permission_type

    @property
    def action(self):
        """Gets the action of this AddOrRemoveServicePermissionsRequestBody.

        要执行的操作。 add/remove。

        :return: The action of this AddOrRemoveServicePermissionsRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this AddOrRemoveServicePermissionsRequestBody.

        要执行的操作。 add/remove。

        :param action: The action of this AddOrRemoveServicePermissionsRequestBody.
        :type action: str
        """
        self._action = action

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
        if not isinstance(other, AddOrRemoveServicePermissionsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
