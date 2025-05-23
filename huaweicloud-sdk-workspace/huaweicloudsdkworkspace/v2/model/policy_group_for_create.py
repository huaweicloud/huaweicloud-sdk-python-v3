# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyGroupForCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_group_id': 'str',
        'policy_group_name': 'str',
        'priority': 'int',
        'description': 'str',
        'scope_flag': 'int',
        'update_time': 'str',
        'targets': 'list[Target]',
        'policies': 'Policies'
    }

    attribute_map = {
        'policy_group_id': 'policy_group_id',
        'policy_group_name': 'policy_group_name',
        'priority': 'priority',
        'description': 'description',
        'scope_flag': 'scope_flag',
        'update_time': 'update_time',
        'targets': 'targets',
        'policies': 'policies'
    }

    def __init__(self, policy_group_id=None, policy_group_name=None, priority=None, description=None, scope_flag=None, update_time=None, targets=None, policies=None):
        r"""PolicyGroupForCreate

        The model defined in huaweicloud sdk

        :param policy_group_id: 策略组id。
        :type policy_group_id: str
        :param policy_group_name: 策略组名称。
        :type policy_group_name: str
        :param priority: 优先级。
        :type priority: int
        :param description: 策略组描述。
        :type description: str
        :param scope_flag: 策略来源。
        :type scope_flag: int
        :param update_time: 更新时间。
        :type update_time: str
        :param targets: 应用对象列表。
        :type targets: list[:class:`huaweicloudsdkworkspace.v2.Target`]
        :param policies: 
        :type policies: :class:`huaweicloudsdkworkspace.v2.Policies`
        """
        
        

        self._policy_group_id = None
        self._policy_group_name = None
        self._priority = None
        self._description = None
        self._scope_flag = None
        self._update_time = None
        self._targets = None
        self._policies = None
        self.discriminator = None

        if policy_group_id is not None:
            self.policy_group_id = policy_group_id
        if policy_group_name is not None:
            self.policy_group_name = policy_group_name
        if priority is not None:
            self.priority = priority
        if description is not None:
            self.description = description
        if scope_flag is not None:
            self.scope_flag = scope_flag
        if update_time is not None:
            self.update_time = update_time
        if targets is not None:
            self.targets = targets
        if policies is not None:
            self.policies = policies

    @property
    def policy_group_id(self):
        r"""Gets the policy_group_id of this PolicyGroupForCreate.

        策略组id。

        :return: The policy_group_id of this PolicyGroupForCreate.
        :rtype: str
        """
        return self._policy_group_id

    @policy_group_id.setter
    def policy_group_id(self, policy_group_id):
        r"""Sets the policy_group_id of this PolicyGroupForCreate.

        策略组id。

        :param policy_group_id: The policy_group_id of this PolicyGroupForCreate.
        :type policy_group_id: str
        """
        self._policy_group_id = policy_group_id

    @property
    def policy_group_name(self):
        r"""Gets the policy_group_name of this PolicyGroupForCreate.

        策略组名称。

        :return: The policy_group_name of this PolicyGroupForCreate.
        :rtype: str
        """
        return self._policy_group_name

    @policy_group_name.setter
    def policy_group_name(self, policy_group_name):
        r"""Sets the policy_group_name of this PolicyGroupForCreate.

        策略组名称。

        :param policy_group_name: The policy_group_name of this PolicyGroupForCreate.
        :type policy_group_name: str
        """
        self._policy_group_name = policy_group_name

    @property
    def priority(self):
        r"""Gets the priority of this PolicyGroupForCreate.

        优先级。

        :return: The priority of this PolicyGroupForCreate.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this PolicyGroupForCreate.

        优先级。

        :param priority: The priority of this PolicyGroupForCreate.
        :type priority: int
        """
        self._priority = priority

    @property
    def description(self):
        r"""Gets the description of this PolicyGroupForCreate.

        策略组描述。

        :return: The description of this PolicyGroupForCreate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PolicyGroupForCreate.

        策略组描述。

        :param description: The description of this PolicyGroupForCreate.
        :type description: str
        """
        self._description = description

    @property
    def scope_flag(self):
        r"""Gets the scope_flag of this PolicyGroupForCreate.

        策略来源。

        :return: The scope_flag of this PolicyGroupForCreate.
        :rtype: int
        """
        return self._scope_flag

    @scope_flag.setter
    def scope_flag(self, scope_flag):
        r"""Sets the scope_flag of this PolicyGroupForCreate.

        策略来源。

        :param scope_flag: The scope_flag of this PolicyGroupForCreate.
        :type scope_flag: int
        """
        self._scope_flag = scope_flag

    @property
    def update_time(self):
        r"""Gets the update_time of this PolicyGroupForCreate.

        更新时间。

        :return: The update_time of this PolicyGroupForCreate.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this PolicyGroupForCreate.

        更新时间。

        :param update_time: The update_time of this PolicyGroupForCreate.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def targets(self):
        r"""Gets the targets of this PolicyGroupForCreate.

        应用对象列表。

        :return: The targets of this PolicyGroupForCreate.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Target`]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        r"""Sets the targets of this PolicyGroupForCreate.

        应用对象列表。

        :param targets: The targets of this PolicyGroupForCreate.
        :type targets: list[:class:`huaweicloudsdkworkspace.v2.Target`]
        """
        self._targets = targets

    @property
    def policies(self):
        r"""Gets the policies of this PolicyGroupForCreate.

        :return: The policies of this PolicyGroupForCreate.
        :rtype: :class:`huaweicloudsdkworkspace.v2.Policies`
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        r"""Sets the policies of this PolicyGroupForCreate.

        :param policies: The policies of this PolicyGroupForCreate.
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
        if not isinstance(other, PolicyGroupForCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
