# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyAssignment:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_assignment_type': 'str',
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'policy_filter': 'PolicyFilterDefinition',
        'period': 'str',
        'state': 'str',
        'created': 'str',
        'updated': 'str',
        'policy_definition_id': 'str',
        'custom_policy': 'CustomPolicy',
        'parameters': 'dict(str, PolicyParameterValue)',
        'tags': 'list[ResourceTag]',
        'created_by': 'str'
    }

    attribute_map = {
        'policy_assignment_type': 'policy_assignment_type',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'policy_filter': 'policy_filter',
        'period': 'period',
        'state': 'state',
        'created': 'created',
        'updated': 'updated',
        'policy_definition_id': 'policy_definition_id',
        'custom_policy': 'custom_policy',
        'parameters': 'parameters',
        'tags': 'tags',
        'created_by': 'created_by'
    }

    def __init__(self, policy_assignment_type=None, id=None, name=None, description=None, policy_filter=None, period=None, state=None, created=None, updated=None, policy_definition_id=None, custom_policy=None, parameters=None, tags=None, created_by=None):
        """PolicyAssignment

        The model defined in huaweicloud sdk

        :param policy_assignment_type: 规则类型，包括预定义合规规则(builtin)和用户自定义合规规则(custom)
        :type policy_assignment_type: str
        :param id: 规则ID
        :type id: str
        :param name: 规则名字
        :type name: str
        :param description: 规则描述
        :type description: str
        :param policy_filter: 
        :type policy_filter: :class:`huaweicloudsdkconfig.v1.PolicyFilterDefinition`
        :param period: 触发周期值，可选值：One_Hour, Three_Hours, Six_Hours, Twelve_Hours, TwentyFour_Hours
        :type period: str
        :param state: 规则状态
        :type state: str
        :param created: 规则创建时间
        :type created: str
        :param updated: 规则更新时间
        :type updated: str
        :param policy_definition_id: 规则的策略ID
        :type policy_definition_id: str
        :param custom_policy: 
        :type custom_policy: :class:`huaweicloudsdkconfig.v1.CustomPolicy`
        :param parameters: 规则参数
        :type parameters: dict(str, PolicyParameterValue)
        :param tags: 
        :type tags: list[:class:`huaweicloudsdkconfig.v1.ResourceTag`]
        :param created_by: 规则的创建者
        :type created_by: str
        """
        
        

        self._policy_assignment_type = None
        self._id = None
        self._name = None
        self._description = None
        self._policy_filter = None
        self._period = None
        self._state = None
        self._created = None
        self._updated = None
        self._policy_definition_id = None
        self._custom_policy = None
        self._parameters = None
        self._tags = None
        self._created_by = None
        self.discriminator = None

        if policy_assignment_type is not None:
            self.policy_assignment_type = policy_assignment_type
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if policy_filter is not None:
            self.policy_filter = policy_filter
        if period is not None:
            self.period = period
        if state is not None:
            self.state = state
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if policy_definition_id is not None:
            self.policy_definition_id = policy_definition_id
        if custom_policy is not None:
            self.custom_policy = custom_policy
        if parameters is not None:
            self.parameters = parameters
        if tags is not None:
            self.tags = tags
        if created_by is not None:
            self.created_by = created_by

    @property
    def policy_assignment_type(self):
        """Gets the policy_assignment_type of this PolicyAssignment.

        规则类型，包括预定义合规规则(builtin)和用户自定义合规规则(custom)

        :return: The policy_assignment_type of this PolicyAssignment.
        :rtype: str
        """
        return self._policy_assignment_type

    @policy_assignment_type.setter
    def policy_assignment_type(self, policy_assignment_type):
        """Sets the policy_assignment_type of this PolicyAssignment.

        规则类型，包括预定义合规规则(builtin)和用户自定义合规规则(custom)

        :param policy_assignment_type: The policy_assignment_type of this PolicyAssignment.
        :type policy_assignment_type: str
        """
        self._policy_assignment_type = policy_assignment_type

    @property
    def id(self):
        """Gets the id of this PolicyAssignment.

        规则ID

        :return: The id of this PolicyAssignment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PolicyAssignment.

        规则ID

        :param id: The id of this PolicyAssignment.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this PolicyAssignment.

        规则名字

        :return: The name of this PolicyAssignment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PolicyAssignment.

        规则名字

        :param name: The name of this PolicyAssignment.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this PolicyAssignment.

        规则描述

        :return: The description of this PolicyAssignment.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PolicyAssignment.

        规则描述

        :param description: The description of this PolicyAssignment.
        :type description: str
        """
        self._description = description

    @property
    def policy_filter(self):
        """Gets the policy_filter of this PolicyAssignment.

        :return: The policy_filter of this PolicyAssignment.
        :rtype: :class:`huaweicloudsdkconfig.v1.PolicyFilterDefinition`
        """
        return self._policy_filter

    @policy_filter.setter
    def policy_filter(self, policy_filter):
        """Sets the policy_filter of this PolicyAssignment.

        :param policy_filter: The policy_filter of this PolicyAssignment.
        :type policy_filter: :class:`huaweicloudsdkconfig.v1.PolicyFilterDefinition`
        """
        self._policy_filter = policy_filter

    @property
    def period(self):
        """Gets the period of this PolicyAssignment.

        触发周期值，可选值：One_Hour, Three_Hours, Six_Hours, Twelve_Hours, TwentyFour_Hours

        :return: The period of this PolicyAssignment.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this PolicyAssignment.

        触发周期值，可选值：One_Hour, Three_Hours, Six_Hours, Twelve_Hours, TwentyFour_Hours

        :param period: The period of this PolicyAssignment.
        :type period: str
        """
        self._period = period

    @property
    def state(self):
        """Gets the state of this PolicyAssignment.

        规则状态

        :return: The state of this PolicyAssignment.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PolicyAssignment.

        规则状态

        :param state: The state of this PolicyAssignment.
        :type state: str
        """
        self._state = state

    @property
    def created(self):
        """Gets the created of this PolicyAssignment.

        规则创建时间

        :return: The created of this PolicyAssignment.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PolicyAssignment.

        规则创建时间

        :param created: The created of this PolicyAssignment.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this PolicyAssignment.

        规则更新时间

        :return: The updated of this PolicyAssignment.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this PolicyAssignment.

        规则更新时间

        :param updated: The updated of this PolicyAssignment.
        :type updated: str
        """
        self._updated = updated

    @property
    def policy_definition_id(self):
        """Gets the policy_definition_id of this PolicyAssignment.

        规则的策略ID

        :return: The policy_definition_id of this PolicyAssignment.
        :rtype: str
        """
        return self._policy_definition_id

    @policy_definition_id.setter
    def policy_definition_id(self, policy_definition_id):
        """Sets the policy_definition_id of this PolicyAssignment.

        规则的策略ID

        :param policy_definition_id: The policy_definition_id of this PolicyAssignment.
        :type policy_definition_id: str
        """
        self._policy_definition_id = policy_definition_id

    @property
    def custom_policy(self):
        """Gets the custom_policy of this PolicyAssignment.

        :return: The custom_policy of this PolicyAssignment.
        :rtype: :class:`huaweicloudsdkconfig.v1.CustomPolicy`
        """
        return self._custom_policy

    @custom_policy.setter
    def custom_policy(self, custom_policy):
        """Sets the custom_policy of this PolicyAssignment.

        :param custom_policy: The custom_policy of this PolicyAssignment.
        :type custom_policy: :class:`huaweicloudsdkconfig.v1.CustomPolicy`
        """
        self._custom_policy = custom_policy

    @property
    def parameters(self):
        """Gets the parameters of this PolicyAssignment.

        规则参数

        :return: The parameters of this PolicyAssignment.
        :rtype: dict(str, PolicyParameterValue)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this PolicyAssignment.

        规则参数

        :param parameters: The parameters of this PolicyAssignment.
        :type parameters: dict(str, PolicyParameterValue)
        """
        self._parameters = parameters

    @property
    def tags(self):
        """Gets the tags of this PolicyAssignment.

        :return: The tags of this PolicyAssignment.
        :rtype: list[:class:`huaweicloudsdkconfig.v1.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this PolicyAssignment.

        :param tags: The tags of this PolicyAssignment.
        :type tags: list[:class:`huaweicloudsdkconfig.v1.ResourceTag`]
        """
        self._tags = tags

    @property
    def created_by(self):
        """Gets the created_by of this PolicyAssignment.

        规则的创建者

        :return: The created_by of this PolicyAssignment.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this PolicyAssignment.

        规则的创建者

        :param created_by: The created_by of this PolicyAssignment.
        :type created_by: str
        """
        self._created_by = created_by

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
        if not isinstance(other, PolicyAssignment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
