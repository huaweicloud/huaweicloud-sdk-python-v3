# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Action:

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
        'access_level': 'str',
        'permission_only': 'bool',
        'description': 'Description',
        'aliases': 'list[str]',
        'resources': 'list[ActionAssociatedResource]',
        'condition_keys': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'access_level': 'access_level',
        'permission_only': 'permission_only',
        'description': 'description',
        'aliases': 'aliases',
        'resources': 'resources',
        'condition_keys': 'condition_keys'
    }

    def __init__(self, name=None, access_level=None, permission_only=None, description=None, aliases=None, resources=None, condition_keys=None):
        r"""Action

        The model defined in huaweicloud sdk

        :param name: 三段式的授权项名称，例如\&quot;iam:policies:createV5\&quot;。
        :type name: str
        :param access_level: 在策略中使用此授权项时授予的访问级别。
        :type access_level: str
        :param permission_only: 该授权项是否仅作为权限点，不对应任何操作。
        :type permission_only: bool
        :param description: 
        :type description: :class:`huaweicloudsdkiam.v5.Description`
        :param aliases: 授权项别名列表，用以兼容授权项改名或者拆分新授权项的场景。
        :type aliases: list[str]
        :param resources: 与该授权项关联的资源列表，用于定义授权项的资源级权限。
        :type resources: list[:class:`huaweicloudsdkiam.v5.ActionAssociatedResource`]
        :param condition_keys: 该授权项支持的，且与资源无关的服务自定义条件属性以及部分全局属性。
        :type condition_keys: list[str]
        """
        
        

        self._name = None
        self._access_level = None
        self._permission_only = None
        self._description = None
        self._aliases = None
        self._resources = None
        self._condition_keys = None
        self.discriminator = None

        self.name = name
        self.access_level = access_level
        self.permission_only = permission_only
        self.description = description
        if aliases is not None:
            self.aliases = aliases
        if resources is not None:
            self.resources = resources
        if condition_keys is not None:
            self.condition_keys = condition_keys

    @property
    def name(self):
        r"""Gets the name of this Action.

        三段式的授权项名称，例如\"iam:policies:createV5\"。

        :return: The name of this Action.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Action.

        三段式的授权项名称，例如\"iam:policies:createV5\"。

        :param name: The name of this Action.
        :type name: str
        """
        self._name = name

    @property
    def access_level(self):
        r"""Gets the access_level of this Action.

        在策略中使用此授权项时授予的访问级别。

        :return: The access_level of this Action.
        :rtype: str
        """
        return self._access_level

    @access_level.setter
    def access_level(self, access_level):
        r"""Sets the access_level of this Action.

        在策略中使用此授权项时授予的访问级别。

        :param access_level: The access_level of this Action.
        :type access_level: str
        """
        self._access_level = access_level

    @property
    def permission_only(self):
        r"""Gets the permission_only of this Action.

        该授权项是否仅作为权限点，不对应任何操作。

        :return: The permission_only of this Action.
        :rtype: bool
        """
        return self._permission_only

    @permission_only.setter
    def permission_only(self, permission_only):
        r"""Sets the permission_only of this Action.

        该授权项是否仅作为权限点，不对应任何操作。

        :param permission_only: The permission_only of this Action.
        :type permission_only: bool
        """
        self._permission_only = permission_only

    @property
    def description(self):
        r"""Gets the description of this Action.

        :return: The description of this Action.
        :rtype: :class:`huaweicloudsdkiam.v5.Description`
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Action.

        :param description: The description of this Action.
        :type description: :class:`huaweicloudsdkiam.v5.Description`
        """
        self._description = description

    @property
    def aliases(self):
        r"""Gets the aliases of this Action.

        授权项别名列表，用以兼容授权项改名或者拆分新授权项的场景。

        :return: The aliases of this Action.
        :rtype: list[str]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        r"""Sets the aliases of this Action.

        授权项别名列表，用以兼容授权项改名或者拆分新授权项的场景。

        :param aliases: The aliases of this Action.
        :type aliases: list[str]
        """
        self._aliases = aliases

    @property
    def resources(self):
        r"""Gets the resources of this Action.

        与该授权项关联的资源列表，用于定义授权项的资源级权限。

        :return: The resources of this Action.
        :rtype: list[:class:`huaweicloudsdkiam.v5.ActionAssociatedResource`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this Action.

        与该授权项关联的资源列表，用于定义授权项的资源级权限。

        :param resources: The resources of this Action.
        :type resources: list[:class:`huaweicloudsdkiam.v5.ActionAssociatedResource`]
        """
        self._resources = resources

    @property
    def condition_keys(self):
        r"""Gets the condition_keys of this Action.

        该授权项支持的，且与资源无关的服务自定义条件属性以及部分全局属性。

        :return: The condition_keys of this Action.
        :rtype: list[str]
        """
        return self._condition_keys

    @condition_keys.setter
    def condition_keys(self, condition_keys):
        r"""Sets the condition_keys of this Action.

        该授权项支持的，且与资源无关的服务自定义条件属性以及部分全局属性。

        :param condition_keys: The condition_keys of this Action.
        :type condition_keys: list[str]
        """
        self._condition_keys = condition_keys

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
        if not isinstance(other, Action):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
