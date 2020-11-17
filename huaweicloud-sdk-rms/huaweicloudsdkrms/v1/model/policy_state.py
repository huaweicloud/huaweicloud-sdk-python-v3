# coding: utf-8

import pprint
import re

import six





class PolicyState:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'resource_provider': 'str',
        'resource_type': 'str',
        'compliance_state': 'str',
        'policy_assignment_id': 'str',
        'policy_definition_id': 'str',
        'evaluation_time': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'resource_id': 'resource_id',
        'resource_name': 'resource_name',
        'resource_provider': 'resource_provider',
        'resource_type': 'resource_type',
        'compliance_state': 'compliance_state',
        'policy_assignment_id': 'policy_assignment_id',
        'policy_definition_id': 'policy_definition_id',
        'evaluation_time': 'evaluation_time'
    }

    def __init__(self, domain_id=None, resource_id=None, resource_name=None, resource_provider=None, resource_type=None, compliance_state=None, policy_assignment_id=None, policy_definition_id=None, evaluation_time=None):
        """PolicyState - a model defined in huaweicloud sdk"""
        
        

        self._domain_id = None
        self._resource_id = None
        self._resource_name = None
        self._resource_provider = None
        self._resource_type = None
        self._compliance_state = None
        self._policy_assignment_id = None
        self._policy_definition_id = None
        self._evaluation_time = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if resource_provider is not None:
            self.resource_provider = resource_provider
        if resource_type is not None:
            self.resource_type = resource_type
        if compliance_state is not None:
            self.compliance_state = compliance_state
        if policy_assignment_id is not None:
            self.policy_assignment_id = policy_assignment_id
        if policy_definition_id is not None:
            self.policy_definition_id = policy_definition_id
        if evaluation_time is not None:
            self.evaluation_time = evaluation_time

    @property
    def domain_id(self):
        """Gets the domain_id of this PolicyState.

        合规状态所属用户ID

        :return: The domain_id of this PolicyState.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this PolicyState.

        合规状态所属用户ID

        :param domain_id: The domain_id of this PolicyState.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def resource_id(self):
        """Gets the resource_id of this PolicyState.

        合规状态所属资源ID

        :return: The resource_id of this PolicyState.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this PolicyState.

        合规状态所属资源ID

        :param resource_id: The resource_id of this PolicyState.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        """Gets the resource_name of this PolicyState.

        合规状态所属资源名字

        :return: The resource_name of this PolicyState.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this PolicyState.

        合规状态所属资源名字

        :param resource_name: The resource_name of this PolicyState.
        :type: str
        """
        self._resource_name = resource_name

    @property
    def resource_provider(self):
        """Gets the resource_provider of this PolicyState.

        合规状态所属资源provider

        :return: The resource_provider of this PolicyState.
        :rtype: str
        """
        return self._resource_provider

    @resource_provider.setter
    def resource_provider(self, resource_provider):
        """Sets the resource_provider of this PolicyState.

        合规状态所属资源provider

        :param resource_provider: The resource_provider of this PolicyState.
        :type: str
        """
        self._resource_provider = resource_provider

    @property
    def resource_type(self):
        """Gets the resource_type of this PolicyState.

        合规状态所属资源类型

        :return: The resource_type of this PolicyState.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this PolicyState.

        合规状态所属资源类型

        :param resource_type: The resource_type of this PolicyState.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def compliance_state(self):
        """Gets the compliance_state of this PolicyState.

        合规状态

        :return: The compliance_state of this PolicyState.
        :rtype: str
        """
        return self._compliance_state

    @compliance_state.setter
    def compliance_state(self, compliance_state):
        """Sets the compliance_state of this PolicyState.

        合规状态

        :param compliance_state: The compliance_state of this PolicyState.
        :type: str
        """
        self._compliance_state = compliance_state

    @property
    def policy_assignment_id(self):
        """Gets the policy_assignment_id of this PolicyState.

        合规状态所属规则ID

        :return: The policy_assignment_id of this PolicyState.
        :rtype: str
        """
        return self._policy_assignment_id

    @policy_assignment_id.setter
    def policy_assignment_id(self, policy_assignment_id):
        """Sets the policy_assignment_id of this PolicyState.

        合规状态所属规则ID

        :param policy_assignment_id: The policy_assignment_id of this PolicyState.
        :type: str
        """
        self._policy_assignment_id = policy_assignment_id

    @property
    def policy_definition_id(self):
        """Gets the policy_definition_id of this PolicyState.

        合规状态所属策略ID

        :return: The policy_definition_id of this PolicyState.
        :rtype: str
        """
        return self._policy_definition_id

    @policy_definition_id.setter
    def policy_definition_id(self, policy_definition_id):
        """Sets the policy_definition_id of this PolicyState.

        合规状态所属策略ID

        :param policy_definition_id: The policy_definition_id of this PolicyState.
        :type: str
        """
        self._policy_definition_id = policy_definition_id

    @property
    def evaluation_time(self):
        """Gets the evaluation_time of this PolicyState.

        合规状态评估时间

        :return: The evaluation_time of this PolicyState.
        :rtype: str
        """
        return self._evaluation_time

    @evaluation_time.setter
    def evaluation_time(self, evaluation_time):
        """Sets the evaluation_time of this PolicyState.

        合规状态评估时间

        :param evaluation_time: The evaluation_time of this PolicyState.
        :type: str
        """
        self._evaluation_time = evaluation_time

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PolicyState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
