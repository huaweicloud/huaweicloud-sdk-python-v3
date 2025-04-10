# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentInstallMode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'component': 'str',
        'node_groups': 'list[AssignedNodeGroup]',
        'component_user_password': 'str',
        'component_default_password': 'str'
    }

    attribute_map = {
        'component': 'component',
        'node_groups': 'node_groups',
        'component_user_password': 'component_user_password',
        'component_default_password': 'component_default_password'
    }

    def __init__(self, component=None, node_groups=None, component_user_password=None, component_default_password=None):
        r"""ComponentInstallMode

        The model defined in huaweicloud sdk

        :param component: 组件名称
        :type component: str
        :param node_groups: 该组件的角色部署信息
        :type node_groups: list[:class:`huaweicloudsdkmrs.v2.AssignedNodeGroup`]
        :param component_user_password: 配置组件用户密码，该密码用于ClickHouse组件机机用户连接使用。 - 密码长度应在8～26个字符之间 - 不能与用户名或者倒序用户名相同 - 必须包含如下4种字符的组合 - 至少一个小写字母 - 至少一个大写字母 - 至少一个数字 - 至少一个特殊字符：!@$%^-_&#x3D;+[{}]:,./?
        :type component_user_password: str
        :param component_default_password: 配置组件default用户密码，该密码用于ClickHouse组件人机用户连接使用。 - 密码长度应在8～26个字符之间 - 不能与用户名或者倒序用户名相同 - 必须包含如下4种字符的组合 - 至少一个小写字母 - 至少一个大写字母 - 至少一个数字 - 至少一个特殊字符：!@$%^-_&#x3D;+[{}]:,./?
        :type component_default_password: str
        """
        
        

        self._component = None
        self._node_groups = None
        self._component_user_password = None
        self._component_default_password = None
        self.discriminator = None

        self.component = component
        self.node_groups = node_groups
        if component_user_password is not None:
            self.component_user_password = component_user_password
        if component_default_password is not None:
            self.component_default_password = component_default_password

    @property
    def component(self):
        r"""Gets the component of this ComponentInstallMode.

        组件名称

        :return: The component of this ComponentInstallMode.
        :rtype: str
        """
        return self._component

    @component.setter
    def component(self, component):
        r"""Sets the component of this ComponentInstallMode.

        组件名称

        :param component: The component of this ComponentInstallMode.
        :type component: str
        """
        self._component = component

    @property
    def node_groups(self):
        r"""Gets the node_groups of this ComponentInstallMode.

        该组件的角色部署信息

        :return: The node_groups of this ComponentInstallMode.
        :rtype: list[:class:`huaweicloudsdkmrs.v2.AssignedNodeGroup`]
        """
        return self._node_groups

    @node_groups.setter
    def node_groups(self, node_groups):
        r"""Sets the node_groups of this ComponentInstallMode.

        该组件的角色部署信息

        :param node_groups: The node_groups of this ComponentInstallMode.
        :type node_groups: list[:class:`huaweicloudsdkmrs.v2.AssignedNodeGroup`]
        """
        self._node_groups = node_groups

    @property
    def component_user_password(self):
        r"""Gets the component_user_password of this ComponentInstallMode.

        配置组件用户密码，该密码用于ClickHouse组件机机用户连接使用。 - 密码长度应在8～26个字符之间 - 不能与用户名或者倒序用户名相同 - 必须包含如下4种字符的组合 - 至少一个小写字母 - 至少一个大写字母 - 至少一个数字 - 至少一个特殊字符：!@$%^-_=+[{}]:,./?

        :return: The component_user_password of this ComponentInstallMode.
        :rtype: str
        """
        return self._component_user_password

    @component_user_password.setter
    def component_user_password(self, component_user_password):
        r"""Sets the component_user_password of this ComponentInstallMode.

        配置组件用户密码，该密码用于ClickHouse组件机机用户连接使用。 - 密码长度应在8～26个字符之间 - 不能与用户名或者倒序用户名相同 - 必须包含如下4种字符的组合 - 至少一个小写字母 - 至少一个大写字母 - 至少一个数字 - 至少一个特殊字符：!@$%^-_=+[{}]:,./?

        :param component_user_password: The component_user_password of this ComponentInstallMode.
        :type component_user_password: str
        """
        self._component_user_password = component_user_password

    @property
    def component_default_password(self):
        r"""Gets the component_default_password of this ComponentInstallMode.

        配置组件default用户密码，该密码用于ClickHouse组件人机用户连接使用。 - 密码长度应在8～26个字符之间 - 不能与用户名或者倒序用户名相同 - 必须包含如下4种字符的组合 - 至少一个小写字母 - 至少一个大写字母 - 至少一个数字 - 至少一个特殊字符：!@$%^-_=+[{}]:,./?

        :return: The component_default_password of this ComponentInstallMode.
        :rtype: str
        """
        return self._component_default_password

    @component_default_password.setter
    def component_default_password(self, component_default_password):
        r"""Sets the component_default_password of this ComponentInstallMode.

        配置组件default用户密码，该密码用于ClickHouse组件人机用户连接使用。 - 密码长度应在8～26个字符之间 - 不能与用户名或者倒序用户名相同 - 必须包含如下4种字符的组合 - 至少一个小写字母 - 至少一个大写字母 - 至少一个数字 - 至少一个特殊字符：!@$%^-_=+[{}]:,./?

        :param component_default_password: The component_default_password of this ComponentInstallMode.
        :type component_default_password: str
        """
        self._component_default_password = component_default_password

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
        if not isinstance(other, ComponentInstallMode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
