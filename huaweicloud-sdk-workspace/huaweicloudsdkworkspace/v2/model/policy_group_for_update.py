# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyGroupForUpdate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_group_name': 'str',
        'description': 'str',
        'scope_flag': 'int',
        'priority': 'int',
        'targets': 'list[Target]',
        'policies': 'Policies'
    }

    attribute_map = {
        'policy_group_name': 'policy_group_name',
        'description': 'description',
        'scope_flag': 'scope_flag',
        'priority': 'priority',
        'targets': 'targets',
        'policies': 'policies'
    }

    def __init__(self, policy_group_name=None, description=None, scope_flag=None, priority=None, targets=None, policies=None):
        """PolicyGroupForUpdate

        The model defined in huaweicloud sdk

        :param policy_group_name: 策略组名称。
        :type policy_group_name: str
        :param description: 策略组描述。
        :type description: str
        :param scope_flag: 策略来源。
        :type scope_flag: int
        :param priority: 优先级。
        :type priority: int
        :param targets: 应用对象列表。
        :type targets: list[:class:`huaweicloudsdkworkspace.v2.Target`]
        :param policies: 
        :type policies: :class:`huaweicloudsdkworkspace.v2.Policies`
        """
        
        

        self._policy_group_name = None
        self._description = None
        self._scope_flag = None
        self._priority = None
        self._targets = None
        self._policies = None
        self.discriminator = None

        if policy_group_name is not None:
            self.policy_group_name = policy_group_name
        if description is not None:
            self.description = description
        if scope_flag is not None:
            self.scope_flag = scope_flag
        if priority is not None:
            self.priority = priority
        if targets is not None:
            self.targets = targets
        if policies is not None:
            self.policies = policies

    @property
    def policy_group_name(self):
        """Gets the policy_group_name of this PolicyGroupForUpdate.

        策略组名称。

        :return: The policy_group_name of this PolicyGroupForUpdate.
        :rtype: str
        """
        return self._policy_group_name

    @policy_group_name.setter
    def policy_group_name(self, policy_group_name):
        """Sets the policy_group_name of this PolicyGroupForUpdate.

        策略组名称。

        :param policy_group_name: The policy_group_name of this PolicyGroupForUpdate.
        :type policy_group_name: str
        """
        self._policy_group_name = policy_group_name

    @property
    def description(self):
        """Gets the description of this PolicyGroupForUpdate.

        策略组描述。

        :return: The description of this PolicyGroupForUpdate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PolicyGroupForUpdate.

        策略组描述。

        :param description: The description of this PolicyGroupForUpdate.
        :type description: str
        """
        self._description = description

    @property
    def scope_flag(self):
        """Gets the scope_flag of this PolicyGroupForUpdate.

        策略来源。

        :return: The scope_flag of this PolicyGroupForUpdate.
        :rtype: int
        """
        return self._scope_flag

    @scope_flag.setter
    def scope_flag(self, scope_flag):
        """Sets the scope_flag of this PolicyGroupForUpdate.

        策略来源。

        :param scope_flag: The scope_flag of this PolicyGroupForUpdate.
        :type scope_flag: int
        """
        self._scope_flag = scope_flag

    @property
    def priority(self):
        """Gets the priority of this PolicyGroupForUpdate.

        优先级。

        :return: The priority of this PolicyGroupForUpdate.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this PolicyGroupForUpdate.

        优先级。

        :param priority: The priority of this PolicyGroupForUpdate.
        :type priority: int
        """
        self._priority = priority

    @property
    def targets(self):
        """Gets the targets of this PolicyGroupForUpdate.

        应用对象列表。

        :return: The targets of this PolicyGroupForUpdate.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Target`]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this PolicyGroupForUpdate.

        应用对象列表。

        :param targets: The targets of this PolicyGroupForUpdate.
        :type targets: list[:class:`huaweicloudsdkworkspace.v2.Target`]
        """
        self._targets = targets

    @property
    def policies(self):
        """Gets the policies of this PolicyGroupForUpdate.

        :return: The policies of this PolicyGroupForUpdate.
        :rtype: :class:`huaweicloudsdkworkspace.v2.Policies`
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this PolicyGroupForUpdate.

        :param policies: The policies of this PolicyGroupForUpdate.
        :type policies: :class:`huaweicloudsdkworkspace.v2.Policies`
        """
        self._policies = policies

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
        if not isinstance(other, PolicyGroupForUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
