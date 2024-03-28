# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrganizationPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'operation_type': 'str',
        'domain_id': 'str',
        'policy_name': 'str',
        'policy_enabled': 'bool',
        'policy_operation_definition': 'PolicyoODCreate',
        'policy_trigger': 'PolicyTriggerReq',
        'status': 'str',
        'domain_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'operation_type': 'operation_type',
        'domain_id': 'domain_id',
        'policy_name': 'policy_name',
        'policy_enabled': 'policy_enabled',
        'policy_operation_definition': 'policy_operation_definition',
        'policy_trigger': 'policy_trigger',
        'status': 'status',
        'domain_name': 'domain_name'
    }

    def __init__(self, id=None, name=None, description=None, operation_type=None, domain_id=None, policy_name=None, policy_enabled=None, policy_operation_definition=None, policy_trigger=None, status=None, domain_name=None):
        """OrganizationPolicy

        The model defined in huaweicloud sdk

        :param id: 组织策略ID
        :type id: str
        :param name: 组织策略名称
        :type name: str
        :param description: 组织策略描述
        :type description: str
        :param operation_type: 组织策略类型 - backup: 备份 -  replication: 复制
        :type operation_type: str
        :param domain_id: 组织策略所属账号ID
        :type domain_id: str
        :param policy_name: 策略名称
        :type policy_name: str
        :param policy_enabled: 策略是否开启
        :type policy_enabled: bool
        :param policy_operation_definition: 
        :type policy_operation_definition: :class:`huaweicloudsdkcbr.v1.PolicyoODCreate`
        :param policy_trigger: 
        :type policy_trigger: :class:`huaweicloudsdkcbr.v1.PolicyTriggerReq`
        :param status: 组织策略状态
        :type status: str
        :param domain_name: 组织策略所属账号
        :type domain_name: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._operation_type = None
        self._domain_id = None
        self._policy_name = None
        self._policy_enabled = None
        self._policy_operation_definition = None
        self._policy_trigger = None
        self._status = None
        self._domain_name = None
        self.discriminator = None

        self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.operation_type = operation_type
        self.domain_id = domain_id
        self.policy_name = policy_name
        self.policy_enabled = policy_enabled
        self.policy_operation_definition = policy_operation_definition
        self.policy_trigger = policy_trigger
        self.status = status
        if domain_name is not None:
            self.domain_name = domain_name

    @property
    def id(self):
        """Gets the id of this OrganizationPolicy.

        组织策略ID

        :return: The id of this OrganizationPolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrganizationPolicy.

        组织策略ID

        :param id: The id of this OrganizationPolicy.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this OrganizationPolicy.

        组织策略名称

        :return: The name of this OrganizationPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganizationPolicy.

        组织策略名称

        :param name: The name of this OrganizationPolicy.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this OrganizationPolicy.

        组织策略描述

        :return: The description of this OrganizationPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OrganizationPolicy.

        组织策略描述

        :param description: The description of this OrganizationPolicy.
        :type description: str
        """
        self._description = description

    @property
    def operation_type(self):
        """Gets the operation_type of this OrganizationPolicy.

        组织策略类型 - backup: 备份 -  replication: 复制

        :return: The operation_type of this OrganizationPolicy.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this OrganizationPolicy.

        组织策略类型 - backup: 备份 -  replication: 复制

        :param operation_type: The operation_type of this OrganizationPolicy.
        :type operation_type: str
        """
        self._operation_type = operation_type

    @property
    def domain_id(self):
        """Gets the domain_id of this OrganizationPolicy.

        组织策略所属账号ID

        :return: The domain_id of this OrganizationPolicy.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this OrganizationPolicy.

        组织策略所属账号ID

        :param domain_id: The domain_id of this OrganizationPolicy.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def policy_name(self):
        """Gets the policy_name of this OrganizationPolicy.

        策略名称

        :return: The policy_name of this OrganizationPolicy.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this OrganizationPolicy.

        策略名称

        :param policy_name: The policy_name of this OrganizationPolicy.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def policy_enabled(self):
        """Gets the policy_enabled of this OrganizationPolicy.

        策略是否开启

        :return: The policy_enabled of this OrganizationPolicy.
        :rtype: bool
        """
        return self._policy_enabled

    @policy_enabled.setter
    def policy_enabled(self, policy_enabled):
        """Sets the policy_enabled of this OrganizationPolicy.

        策略是否开启

        :param policy_enabled: The policy_enabled of this OrganizationPolicy.
        :type policy_enabled: bool
        """
        self._policy_enabled = policy_enabled

    @property
    def policy_operation_definition(self):
        """Gets the policy_operation_definition of this OrganizationPolicy.

        :return: The policy_operation_definition of this OrganizationPolicy.
        :rtype: :class:`huaweicloudsdkcbr.v1.PolicyoODCreate`
        """
        return self._policy_operation_definition

    @policy_operation_definition.setter
    def policy_operation_definition(self, policy_operation_definition):
        """Sets the policy_operation_definition of this OrganizationPolicy.

        :param policy_operation_definition: The policy_operation_definition of this OrganizationPolicy.
        :type policy_operation_definition: :class:`huaweicloudsdkcbr.v1.PolicyoODCreate`
        """
        self._policy_operation_definition = policy_operation_definition

    @property
    def policy_trigger(self):
        """Gets the policy_trigger of this OrganizationPolicy.

        :return: The policy_trigger of this OrganizationPolicy.
        :rtype: :class:`huaweicloudsdkcbr.v1.PolicyTriggerReq`
        """
        return self._policy_trigger

    @policy_trigger.setter
    def policy_trigger(self, policy_trigger):
        """Sets the policy_trigger of this OrganizationPolicy.

        :param policy_trigger: The policy_trigger of this OrganizationPolicy.
        :type policy_trigger: :class:`huaweicloudsdkcbr.v1.PolicyTriggerReq`
        """
        self._policy_trigger = policy_trigger

    @property
    def status(self):
        """Gets the status of this OrganizationPolicy.

        组织策略状态

        :return: The status of this OrganizationPolicy.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OrganizationPolicy.

        组织策略状态

        :param status: The status of this OrganizationPolicy.
        :type status: str
        """
        self._status = status

    @property
    def domain_name(self):
        """Gets the domain_name of this OrganizationPolicy.

        组织策略所属账号

        :return: The domain_name of this OrganizationPolicy.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this OrganizationPolicy.

        组织策略所属账号

        :param domain_name: The domain_name of this OrganizationPolicy.
        :type domain_name: str
        """
        self._domain_name = domain_name

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
        if not isinstance(other, OrganizationPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
