# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyGroupForList:

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
        'update_time': 'str',
        'description': 'str',
        'policies': 'Policies',
        'targets': 'list[Target]'
    }

    attribute_map = {
        'policy_group_id': 'policy_group_id',
        'policy_group_name': 'policy_group_name',
        'priority': 'priority',
        'update_time': 'update_time',
        'description': 'description',
        'policies': 'policies',
        'targets': 'targets'
    }

    def __init__(self, policy_group_id=None, policy_group_name=None, priority=None, update_time=None, description=None, policies=None, targets=None):
        r"""PolicyGroupForList

        The model defined in huaweicloud sdk

        :param policy_group_id: 策略组ID。
        :type policy_group_id: str
        :param policy_group_name: 策略组名称。
        :type policy_group_name: str
        :param priority: 优先级。
        :type priority: int
        :param update_time: 更新日期。
        :type update_time: str
        :param description: 策略组描述。
        :type description: str
        :param policies: 
        :type policies: :class:`huaweicloudsdkworkspace.v2.Policies`
        :param targets: 应用对象列表。
        :type targets: list[:class:`huaweicloudsdkworkspace.v2.Target`]
        """
        
        

        self._policy_group_id = None
        self._policy_group_name = None
        self._priority = None
        self._update_time = None
        self._description = None
        self._policies = None
        self._targets = None
        self.discriminator = None

        if policy_group_id is not None:
            self.policy_group_id = policy_group_id
        if policy_group_name is not None:
            self.policy_group_name = policy_group_name
        if priority is not None:
            self.priority = priority
        if update_time is not None:
            self.update_time = update_time
        if description is not None:
            self.description = description
        if policies is not None:
            self.policies = policies
        if targets is not None:
            self.targets = targets

    @property
    def policy_group_id(self):
        r"""Gets the policy_group_id of this PolicyGroupForList.

        策略组ID。

        :return: The policy_group_id of this PolicyGroupForList.
        :rtype: str
        """
        return self._policy_group_id

    @policy_group_id.setter
    def policy_group_id(self, policy_group_id):
        r"""Sets the policy_group_id of this PolicyGroupForList.

        策略组ID。

        :param policy_group_id: The policy_group_id of this PolicyGroupForList.
        :type policy_group_id: str
        """
        self._policy_group_id = policy_group_id

    @property
    def policy_group_name(self):
        r"""Gets the policy_group_name of this PolicyGroupForList.

        策略组名称。

        :return: The policy_group_name of this PolicyGroupForList.
        :rtype: str
        """
        return self._policy_group_name

    @policy_group_name.setter
    def policy_group_name(self, policy_group_name):
        r"""Sets the policy_group_name of this PolicyGroupForList.

        策略组名称。

        :param policy_group_name: The policy_group_name of this PolicyGroupForList.
        :type policy_group_name: str
        """
        self._policy_group_name = policy_group_name

    @property
    def priority(self):
        r"""Gets the priority of this PolicyGroupForList.

        优先级。

        :return: The priority of this PolicyGroupForList.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this PolicyGroupForList.

        优先级。

        :param priority: The priority of this PolicyGroupForList.
        :type priority: int
        """
        self._priority = priority

    @property
    def update_time(self):
        r"""Gets the update_time of this PolicyGroupForList.

        更新日期。

        :return: The update_time of this PolicyGroupForList.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this PolicyGroupForList.

        更新日期。

        :param update_time: The update_time of this PolicyGroupForList.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def description(self):
        r"""Gets the description of this PolicyGroupForList.

        策略组描述。

        :return: The description of this PolicyGroupForList.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PolicyGroupForList.

        策略组描述。

        :param description: The description of this PolicyGroupForList.
        :type description: str
        """
        self._description = description

    @property
    def policies(self):
        r"""Gets the policies of this PolicyGroupForList.

        :return: The policies of this PolicyGroupForList.
        :rtype: :class:`huaweicloudsdkworkspace.v2.Policies`
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        r"""Sets the policies of this PolicyGroupForList.

        :param policies: The policies of this PolicyGroupForList.
        :type policies: :class:`huaweicloudsdkworkspace.v2.Policies`
        """
        self._policies = policies

    @property
    def targets(self):
        r"""Gets the targets of this PolicyGroupForList.

        应用对象列表。

        :return: The targets of this PolicyGroupForList.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Target`]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        r"""Sets the targets of this PolicyGroupForList.

        应用对象列表。

        :param targets: The targets of this PolicyGroupForList.
        :type targets: list[:class:`huaweicloudsdkworkspace.v2.Target`]
        """
        self._targets = targets

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
        if not isinstance(other, PolicyGroupForList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
