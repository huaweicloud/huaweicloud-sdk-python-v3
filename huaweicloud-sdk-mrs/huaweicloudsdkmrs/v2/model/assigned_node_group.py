# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssignedNodeGroup:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'assigned_roles': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'assigned_roles': 'assigned_roles'
    }

    def __init__(self, name=None, assigned_roles=None):
        """AssignedNodeGroup

        The model defined in huaweicloud sdk

        :param name: 节点组名称
        :type name: str
        :param assigned_roles: 角色部署信息。 可以指定节点组中部署的角色，该参数是一个字符串数组，每个字符串表示一个角色表达式。 角色表达式定义： - 当该角色在节点组所有节点部署时： {role name}，如“DataNode”。 - 当该角色在节点组指定下标节点部署时：{role name}:{index1},{index2}…,{indexN}，如“NameNode:1,2”，下标从1开始计数。 - 部分角色支持多实例部署（即在一个节点部署多个同角色的实例）：{role name}[{instance count}]，如“EsNode[9]”，多实例部署不需要指定角色位置，默认在节点组所有节点部署多个实例 可选的角色请参考[MRS支持的角色与组件对应表](https://support.huaweicloud.com/api-mrs/mrs_02_0106.html)。
        :type assigned_roles: list[str]
        """
        
        

        self._name = None
        self._assigned_roles = None
        self.discriminator = None

        self.name = name
        self.assigned_roles = assigned_roles

    @property
    def name(self):
        """Gets the name of this AssignedNodeGroup.

        节点组名称

        :return: The name of this AssignedNodeGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AssignedNodeGroup.

        节点组名称

        :param name: The name of this AssignedNodeGroup.
        :type name: str
        """
        self._name = name

    @property
    def assigned_roles(self):
        """Gets the assigned_roles of this AssignedNodeGroup.

        角色部署信息。 可以指定节点组中部署的角色，该参数是一个字符串数组，每个字符串表示一个角色表达式。 角色表达式定义： - 当该角色在节点组所有节点部署时： {role name}，如“DataNode”。 - 当该角色在节点组指定下标节点部署时：{role name}:{index1},{index2}…,{indexN}，如“NameNode:1,2”，下标从1开始计数。 - 部分角色支持多实例部署（即在一个节点部署多个同角色的实例）：{role name}[{instance count}]，如“EsNode[9]”，多实例部署不需要指定角色位置，默认在节点组所有节点部署多个实例 可选的角色请参考[MRS支持的角色与组件对应表](https://support.huaweicloud.com/api-mrs/mrs_02_0106.html)。

        :return: The assigned_roles of this AssignedNodeGroup.
        :rtype: list[str]
        """
        return self._assigned_roles

    @assigned_roles.setter
    def assigned_roles(self, assigned_roles):
        """Sets the assigned_roles of this AssignedNodeGroup.

        角色部署信息。 可以指定节点组中部署的角色，该参数是一个字符串数组，每个字符串表示一个角色表达式。 角色表达式定义： - 当该角色在节点组所有节点部署时： {role name}，如“DataNode”。 - 当该角色在节点组指定下标节点部署时：{role name}:{index1},{index2}…,{indexN}，如“NameNode:1,2”，下标从1开始计数。 - 部分角色支持多实例部署（即在一个节点部署多个同角色的实例）：{role name}[{instance count}]，如“EsNode[9]”，多实例部署不需要指定角色位置，默认在节点组所有节点部署多个实例 可选的角色请参考[MRS支持的角色与组件对应表](https://support.huaweicloud.com/api-mrs/mrs_02_0106.html)。

        :param assigned_roles: The assigned_roles of this AssignedNodeGroup.
        :type assigned_roles: list[str]
        """
        self._assigned_roles = assigned_roles

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
        if not isinstance(other, AssignedNodeGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
