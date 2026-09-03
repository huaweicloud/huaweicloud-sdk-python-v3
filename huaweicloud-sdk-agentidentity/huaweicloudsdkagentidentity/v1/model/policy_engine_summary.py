# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyEngineSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_engine_id': 'str',
        'name': 'str',
        'type': 'PolicyEngineType',
        'urn': 'str',
        'tags': 'list[Tag]',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'policy_engine_id': 'policy_engine_id',
        'name': 'name',
        'type': 'type',
        'urn': 'urn',
        'tags': 'tags',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, policy_engine_id=None, name=None, type=None, urn=None, tags=None, created_at=None, updated_at=None):
        r"""PolicyEngineSummary

        The model defined in huaweicloud sdk

        :param policy_engine_id: System-generated unique identifier for the policy engine.
        :type policy_engine_id: str
        :param name: Customer-assigned immutable name for the policy engine.
        :type name: str
        :param type: 
        :type type: :class:`huaweicloudsdkagentidentity.v1.PolicyEngineType`
        :param urn: The URN of the policy engine.
        :type urn: str
        :param tags: 自定义标签列表。
        :type tags: list[:class:`huaweicloudsdkagentidentity.v1.Tag`]
        :param created_at: Timestamp in RFC 3339 format (UTC)
        :type created_at: datetime
        :param updated_at: Timestamp in RFC 3339 format (UTC)
        :type updated_at: datetime
        """
        
        

        self._policy_engine_id = None
        self._name = None
        self._type = None
        self._urn = None
        self._tags = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.policy_engine_id = policy_engine_id
        self.name = name
        self.type = type
        self.urn = urn
        if tags is not None:
            self.tags = tags
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def policy_engine_id(self):
        r"""Gets the policy_engine_id of this PolicyEngineSummary.

        System-generated unique identifier for the policy engine.

        :return: The policy_engine_id of this PolicyEngineSummary.
        :rtype: str
        """
        return self._policy_engine_id

    @policy_engine_id.setter
    def policy_engine_id(self, policy_engine_id):
        r"""Sets the policy_engine_id of this PolicyEngineSummary.

        System-generated unique identifier for the policy engine.

        :param policy_engine_id: The policy_engine_id of this PolicyEngineSummary.
        :type policy_engine_id: str
        """
        self._policy_engine_id = policy_engine_id

    @property
    def name(self):
        r"""Gets the name of this PolicyEngineSummary.

        Customer-assigned immutable name for the policy engine.

        :return: The name of this PolicyEngineSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PolicyEngineSummary.

        Customer-assigned immutable name for the policy engine.

        :param name: The name of this PolicyEngineSummary.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this PolicyEngineSummary.

        :return: The type of this PolicyEngineSummary.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.PolicyEngineType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PolicyEngineSummary.

        :param type: The type of this PolicyEngineSummary.
        :type type: :class:`huaweicloudsdkagentidentity.v1.PolicyEngineType`
        """
        self._type = type

    @property
    def urn(self):
        r"""Gets the urn of this PolicyEngineSummary.

        The URN of the policy engine.

        :return: The urn of this PolicyEngineSummary.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        r"""Sets the urn of this PolicyEngineSummary.

        The URN of the policy engine.

        :param urn: The urn of this PolicyEngineSummary.
        :type urn: str
        """
        self._urn = urn

    @property
    def tags(self):
        r"""Gets the tags of this PolicyEngineSummary.

        自定义标签列表。

        :return: The tags of this PolicyEngineSummary.
        :rtype: list[:class:`huaweicloudsdkagentidentity.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this PolicyEngineSummary.

        自定义标签列表。

        :param tags: The tags of this PolicyEngineSummary.
        :type tags: list[:class:`huaweicloudsdkagentidentity.v1.Tag`]
        """
        self._tags = tags

    @property
    def created_at(self):
        r"""Gets the created_at of this PolicyEngineSummary.

        Timestamp in RFC 3339 format (UTC)

        :return: The created_at of this PolicyEngineSummary.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this PolicyEngineSummary.

        Timestamp in RFC 3339 format (UTC)

        :param created_at: The created_at of this PolicyEngineSummary.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this PolicyEngineSummary.

        Timestamp in RFC 3339 format (UTC)

        :return: The updated_at of this PolicyEngineSummary.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this PolicyEngineSummary.

        Timestamp in RFC 3339 format (UTC)

        :param updated_at: The updated_at of this PolicyEngineSummary.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, PolicyEngineSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
