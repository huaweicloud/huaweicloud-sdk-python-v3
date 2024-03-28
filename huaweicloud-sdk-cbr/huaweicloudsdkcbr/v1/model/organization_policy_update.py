# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrganizationPolicyUpdate:

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
        'description': 'str',
        'policy_name': 'str',
        'policy_enabled': 'bool',
        'policy_operation_definition': 'PolicyoODCreate',
        'policy_trigger': 'PolicyTriggerReq'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'policy_name': 'policy_name',
        'policy_enabled': 'policy_enabled',
        'policy_operation_definition': 'policy_operation_definition',
        'policy_trigger': 'policy_trigger'
    }

    def __init__(self, name=None, description=None, policy_name=None, policy_enabled=None, policy_operation_definition=None, policy_trigger=None):
        """OrganizationPolicyUpdate

        The model defined in huaweicloud sdk

        :param name: 组织策略名称
        :type name: str
        :param description: 组织策略描述
        :type description: str
        :param policy_name: 策略名称
        :type policy_name: str
        :param policy_enabled: 策略是否开启
        :type policy_enabled: bool
        :param policy_operation_definition: 
        :type policy_operation_definition: :class:`huaweicloudsdkcbr.v1.PolicyoODCreate`
        :param policy_trigger: 
        :type policy_trigger: :class:`huaweicloudsdkcbr.v1.PolicyTriggerReq`
        """
        
        

        self._name = None
        self._description = None
        self._policy_name = None
        self._policy_enabled = None
        self._policy_operation_definition = None
        self._policy_trigger = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if policy_name is not None:
            self.policy_name = policy_name
        if policy_enabled is not None:
            self.policy_enabled = policy_enabled
        if policy_operation_definition is not None:
            self.policy_operation_definition = policy_operation_definition
        if policy_trigger is not None:
            self.policy_trigger = policy_trigger

    @property
    def name(self):
        """Gets the name of this OrganizationPolicyUpdate.

        组织策略名称

        :return: The name of this OrganizationPolicyUpdate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganizationPolicyUpdate.

        组织策略名称

        :param name: The name of this OrganizationPolicyUpdate.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this OrganizationPolicyUpdate.

        组织策略描述

        :return: The description of this OrganizationPolicyUpdate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OrganizationPolicyUpdate.

        组织策略描述

        :param description: The description of this OrganizationPolicyUpdate.
        :type description: str
        """
        self._description = description

    @property
    def policy_name(self):
        """Gets the policy_name of this OrganizationPolicyUpdate.

        策略名称

        :return: The policy_name of this OrganizationPolicyUpdate.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this OrganizationPolicyUpdate.

        策略名称

        :param policy_name: The policy_name of this OrganizationPolicyUpdate.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def policy_enabled(self):
        """Gets the policy_enabled of this OrganizationPolicyUpdate.

        策略是否开启

        :return: The policy_enabled of this OrganizationPolicyUpdate.
        :rtype: bool
        """
        return self._policy_enabled

    @policy_enabled.setter
    def policy_enabled(self, policy_enabled):
        """Sets the policy_enabled of this OrganizationPolicyUpdate.

        策略是否开启

        :param policy_enabled: The policy_enabled of this OrganizationPolicyUpdate.
        :type policy_enabled: bool
        """
        self._policy_enabled = policy_enabled

    @property
    def policy_operation_definition(self):
        """Gets the policy_operation_definition of this OrganizationPolicyUpdate.

        :return: The policy_operation_definition of this OrganizationPolicyUpdate.
        :rtype: :class:`huaweicloudsdkcbr.v1.PolicyoODCreate`
        """
        return self._policy_operation_definition

    @policy_operation_definition.setter
    def policy_operation_definition(self, policy_operation_definition):
        """Sets the policy_operation_definition of this OrganizationPolicyUpdate.

        :param policy_operation_definition: The policy_operation_definition of this OrganizationPolicyUpdate.
        :type policy_operation_definition: :class:`huaweicloudsdkcbr.v1.PolicyoODCreate`
        """
        self._policy_operation_definition = policy_operation_definition

    @property
    def policy_trigger(self):
        """Gets the policy_trigger of this OrganizationPolicyUpdate.

        :return: The policy_trigger of this OrganizationPolicyUpdate.
        :rtype: :class:`huaweicloudsdkcbr.v1.PolicyTriggerReq`
        """
        return self._policy_trigger

    @policy_trigger.setter
    def policy_trigger(self, policy_trigger):
        """Sets the policy_trigger of this OrganizationPolicyUpdate.

        :param policy_trigger: The policy_trigger of this OrganizationPolicyUpdate.
        :type policy_trigger: :class:`huaweicloudsdkcbr.v1.PolicyTriggerReq`
        """
        self._policy_trigger = policy_trigger

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
        if not isinstance(other, OrganizationPolicyUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
