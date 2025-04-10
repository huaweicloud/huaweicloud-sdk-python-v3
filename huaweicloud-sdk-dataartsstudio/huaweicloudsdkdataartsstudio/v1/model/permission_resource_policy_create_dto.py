# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PermissionResourcePolicyCreateDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_name': 'str',
        'resources': 'list[ResourcePolicyItem]',
        'members': 'list[MemberPolicyItem]'
    }

    attribute_map = {
        'policy_name': 'policy_name',
        'resources': 'resources',
        'members': 'members'
    }

    def __init__(self, policy_name=None, resources=None, members=None):
        r"""PermissionResourcePolicyCreateDTO

        The model defined in huaweicloud sdk

        :param policy_name: 策略名称：英文和汉字开头, 支持英文、汉字、数字、下划线, 2-64字符
        :type policy_name: str
        :param resources: 资源对象列表。资源对象包含 数据连接, 连接获取方法详见[查询数据连接列表](ListDataconnections.xml)
        :type resources: list[:class:`huaweicloudsdkdataartsstudio.v1.ResourcePolicyItem`]
        :param members: 成员列表。 成员包含空间用户、空间用户组、空间用户角色。空间用户、用户组获取方法请参见[获取工作空间用户信息](ListWorkspaceusers.xml),空间角色获取方法参见[获取工作空间用户角色](ListWorkspaceRoles.xml)
        :type members: list[:class:`huaweicloudsdkdataartsstudio.v1.MemberPolicyItem`]
        """
        
        

        self._policy_name = None
        self._resources = None
        self._members = None
        self.discriminator = None

        self.policy_name = policy_name
        self.resources = resources
        self.members = members

    @property
    def policy_name(self):
        r"""Gets the policy_name of this PermissionResourcePolicyCreateDTO.

        策略名称：英文和汉字开头, 支持英文、汉字、数字、下划线, 2-64字符

        :return: The policy_name of this PermissionResourcePolicyCreateDTO.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this PermissionResourcePolicyCreateDTO.

        策略名称：英文和汉字开头, 支持英文、汉字、数字、下划线, 2-64字符

        :param policy_name: The policy_name of this PermissionResourcePolicyCreateDTO.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def resources(self):
        r"""Gets the resources of this PermissionResourcePolicyCreateDTO.

        资源对象列表。资源对象包含 数据连接, 连接获取方法详见[查询数据连接列表](ListDataconnections.xml)

        :return: The resources of this PermissionResourcePolicyCreateDTO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ResourcePolicyItem`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this PermissionResourcePolicyCreateDTO.

        资源对象列表。资源对象包含 数据连接, 连接获取方法详见[查询数据连接列表](ListDataconnections.xml)

        :param resources: The resources of this PermissionResourcePolicyCreateDTO.
        :type resources: list[:class:`huaweicloudsdkdataartsstudio.v1.ResourcePolicyItem`]
        """
        self._resources = resources

    @property
    def members(self):
        r"""Gets the members of this PermissionResourcePolicyCreateDTO.

        成员列表。 成员包含空间用户、空间用户组、空间用户角色。空间用户、用户组获取方法请参见[获取工作空间用户信息](ListWorkspaceusers.xml),空间角色获取方法参见[获取工作空间用户角色](ListWorkspaceRoles.xml)

        :return: The members of this PermissionResourcePolicyCreateDTO.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.MemberPolicyItem`]
        """
        return self._members

    @members.setter
    def members(self, members):
        r"""Sets the members of this PermissionResourcePolicyCreateDTO.

        成员列表。 成员包含空间用户、空间用户组、空间用户角色。空间用户、用户组获取方法请参见[获取工作空间用户信息](ListWorkspaceusers.xml),空间角色获取方法参见[获取工作空间用户角色](ListWorkspaceRoles.xml)

        :param members: The members of this PermissionResourcePolicyCreateDTO.
        :type members: list[:class:`huaweicloudsdkdataartsstudio.v1.MemberPolicyItem`]
        """
        self._members = members

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
        if not isinstance(other, PermissionResourcePolicyCreateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
