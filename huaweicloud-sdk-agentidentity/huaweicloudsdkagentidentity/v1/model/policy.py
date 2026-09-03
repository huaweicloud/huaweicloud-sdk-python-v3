# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Policy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_id': 'str',
        'name': 'str',
        'description': 'str',
        'urn': 'str',
        'pending_definition': 'PolicyDefinition',
        'active_definition': 'PolicyDefinition',
        'status': 'PolicyStatus',
        'status_reasons': 'list[str]',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'policy_engine_id': 'str'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'name': 'name',
        'description': 'description',
        'urn': 'urn',
        'pending_definition': 'pending_definition',
        'active_definition': 'active_definition',
        'status': 'status',
        'status_reasons': 'status_reasons',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'policy_engine_id': 'policy_engine_id'
    }

    def __init__(self, policy_id=None, name=None, description=None, urn=None, pending_definition=None, active_definition=None, status=None, status_reasons=None, created_at=None, updated_at=None, policy_engine_id=None):
        r"""Policy

        The model defined in huaweicloud sdk

        :param policy_id: System-generated unique identifier for the policy.
        :type policy_id: str
        :param name: Human-readable display name for the policy
        :type name: str
        :param description: 策略的可读描述。
        :type description: str
        :param urn: The URN of the policy.
        :type urn: str
        :param pending_definition: 
        :type pending_definition: :class:`huaweicloudsdkagentidentity.v1.PolicyDefinition`
        :param active_definition: 
        :type active_definition: :class:`huaweicloudsdkagentidentity.v1.PolicyDefinition`
        :param status: 
        :type status: :class:`huaweicloudsdkagentidentity.v1.PolicyStatus`
        :param status_reasons: 关于策略状态的额外信息，提供关于任何失败或策略创建过程当前状态的详细信息。
        :type status_reasons: list[str]
        :param created_at: Timestamp in RFC 3339 format (UTC)
        :type created_at: datetime
        :param updated_at: Timestamp in RFC 3339 format (UTC)
        :type updated_at: datetime
        :param policy_engine_id: System-generated unique identifier for the policy engine.
        :type policy_engine_id: str
        """
        
        

        self._policy_id = None
        self._name = None
        self._description = None
        self._urn = None
        self._pending_definition = None
        self._active_definition = None
        self._status = None
        self._status_reasons = None
        self._created_at = None
        self._updated_at = None
        self._policy_engine_id = None
        self.discriminator = None

        self.policy_id = policy_id
        self.name = name
        if description is not None:
            self.description = description
        self.urn = urn
        if pending_definition is not None:
            self.pending_definition = pending_definition
        if active_definition is not None:
            self.active_definition = active_definition
        self.status = status
        if status_reasons is not None:
            self.status_reasons = status_reasons
        self.created_at = created_at
        self.updated_at = updated_at
        self.policy_engine_id = policy_engine_id

    @property
    def policy_id(self):
        r"""Gets the policy_id of this Policy.

        System-generated unique identifier for the policy.

        :return: The policy_id of this Policy.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this Policy.

        System-generated unique identifier for the policy.

        :param policy_id: The policy_id of this Policy.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def name(self):
        r"""Gets the name of this Policy.

        Human-readable display name for the policy

        :return: The name of this Policy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Policy.

        Human-readable display name for the policy

        :param name: The name of this Policy.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this Policy.

        策略的可读描述。

        :return: The description of this Policy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Policy.

        策略的可读描述。

        :param description: The description of this Policy.
        :type description: str
        """
        self._description = description

    @property
    def urn(self):
        r"""Gets the urn of this Policy.

        The URN of the policy.

        :return: The urn of this Policy.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        r"""Sets the urn of this Policy.

        The URN of the policy.

        :param urn: The urn of this Policy.
        :type urn: str
        """
        self._urn = urn

    @property
    def pending_definition(self):
        r"""Gets the pending_definition of this Policy.

        :return: The pending_definition of this Policy.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.PolicyDefinition`
        """
        return self._pending_definition

    @pending_definition.setter
    def pending_definition(self, pending_definition):
        r"""Sets the pending_definition of this Policy.

        :param pending_definition: The pending_definition of this Policy.
        :type pending_definition: :class:`huaweicloudsdkagentidentity.v1.PolicyDefinition`
        """
        self._pending_definition = pending_definition

    @property
    def active_definition(self):
        r"""Gets the active_definition of this Policy.

        :return: The active_definition of this Policy.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.PolicyDefinition`
        """
        return self._active_definition

    @active_definition.setter
    def active_definition(self, active_definition):
        r"""Sets the active_definition of this Policy.

        :param active_definition: The active_definition of this Policy.
        :type active_definition: :class:`huaweicloudsdkagentidentity.v1.PolicyDefinition`
        """
        self._active_definition = active_definition

    @property
    def status(self):
        r"""Gets the status of this Policy.

        :return: The status of this Policy.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.PolicyStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Policy.

        :param status: The status of this Policy.
        :type status: :class:`huaweicloudsdkagentidentity.v1.PolicyStatus`
        """
        self._status = status

    @property
    def status_reasons(self):
        r"""Gets the status_reasons of this Policy.

        关于策略状态的额外信息，提供关于任何失败或策略创建过程当前状态的详细信息。

        :return: The status_reasons of this Policy.
        :rtype: list[str]
        """
        return self._status_reasons

    @status_reasons.setter
    def status_reasons(self, status_reasons):
        r"""Sets the status_reasons of this Policy.

        关于策略状态的额外信息，提供关于任何失败或策略创建过程当前状态的详细信息。

        :param status_reasons: The status_reasons of this Policy.
        :type status_reasons: list[str]
        """
        self._status_reasons = status_reasons

    @property
    def created_at(self):
        r"""Gets the created_at of this Policy.

        Timestamp in RFC 3339 format (UTC)

        :return: The created_at of this Policy.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this Policy.

        Timestamp in RFC 3339 format (UTC)

        :param created_at: The created_at of this Policy.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this Policy.

        Timestamp in RFC 3339 format (UTC)

        :return: The updated_at of this Policy.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this Policy.

        Timestamp in RFC 3339 format (UTC)

        :param updated_at: The updated_at of this Policy.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def policy_engine_id(self):
        r"""Gets the policy_engine_id of this Policy.

        System-generated unique identifier for the policy engine.

        :return: The policy_engine_id of this Policy.
        :rtype: str
        """
        return self._policy_engine_id

    @policy_engine_id.setter
    def policy_engine_id(self, policy_engine_id):
        r"""Sets the policy_engine_id of this Policy.

        System-generated unique identifier for the policy engine.

        :param policy_engine_id: The policy_engine_id of this Policy.
        :type policy_engine_id: str
        """
        self._policy_engine_id = policy_engine_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Policy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
