# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateIpReputationRuleRequestBody:

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
        'type': 'str',
        'tags': 'list[str]',
        'action': 'BatchCreateIpReputationRuleRequestBodyAction',
        'description': 'str',
        'policy_ids': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'tags': 'tags',
        'action': 'action',
        'description': 'description',
        'policy_ids': 'policy_ids'
    }

    def __init__(self, name=None, type=None, tags=None, action=None, description=None, policy_ids=None):
        r"""BatchCreateIpReputationRuleRequestBody

        The model defined in huaweicloud sdk

        :param name: name
        :type name: str
        :param type: type
        :type type: str
        :param tags: tags
        :type tags: list[str]
        :param action: 
        :type action: :class:`huaweicloudsdkwaf.v1.BatchCreateIpReputationRuleRequestBodyAction`
        :param description: description
        :type description: str
        :param policy_ids: 策略id
        :type policy_ids: list[str]
        """
        
        

        self._name = None
        self._type = None
        self._tags = None
        self._action = None
        self._description = None
        self._policy_ids = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if tags is not None:
            self.tags = tags
        if action is not None:
            self.action = action
        if description is not None:
            self.description = description
        if policy_ids is not None:
            self.policy_ids = policy_ids

    @property
    def name(self):
        r"""Gets the name of this BatchCreateIpReputationRuleRequestBody.

        name

        :return: The name of this BatchCreateIpReputationRuleRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BatchCreateIpReputationRuleRequestBody.

        name

        :param name: The name of this BatchCreateIpReputationRuleRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this BatchCreateIpReputationRuleRequestBody.

        type

        :return: The type of this BatchCreateIpReputationRuleRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this BatchCreateIpReputationRuleRequestBody.

        type

        :param type: The type of this BatchCreateIpReputationRuleRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def tags(self):
        r"""Gets the tags of this BatchCreateIpReputationRuleRequestBody.

        tags

        :return: The tags of this BatchCreateIpReputationRuleRequestBody.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this BatchCreateIpReputationRuleRequestBody.

        tags

        :param tags: The tags of this BatchCreateIpReputationRuleRequestBody.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def action(self):
        r"""Gets the action of this BatchCreateIpReputationRuleRequestBody.

        :return: The action of this BatchCreateIpReputationRuleRequestBody.
        :rtype: :class:`huaweicloudsdkwaf.v1.BatchCreateIpReputationRuleRequestBodyAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this BatchCreateIpReputationRuleRequestBody.

        :param action: The action of this BatchCreateIpReputationRuleRequestBody.
        :type action: :class:`huaweicloudsdkwaf.v1.BatchCreateIpReputationRuleRequestBodyAction`
        """
        self._action = action

    @property
    def description(self):
        r"""Gets the description of this BatchCreateIpReputationRuleRequestBody.

        description

        :return: The description of this BatchCreateIpReputationRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BatchCreateIpReputationRuleRequestBody.

        description

        :param description: The description of this BatchCreateIpReputationRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def policy_ids(self):
        r"""Gets the policy_ids of this BatchCreateIpReputationRuleRequestBody.

        策略id

        :return: The policy_ids of this BatchCreateIpReputationRuleRequestBody.
        :rtype: list[str]
        """
        return self._policy_ids

    @policy_ids.setter
    def policy_ids(self, policy_ids):
        r"""Sets the policy_ids of this BatchCreateIpReputationRuleRequestBody.

        策略id

        :param policy_ids: The policy_ids of this BatchCreateIpReputationRuleRequestBody.
        :type policy_ids: list[str]
        """
        self._policy_ids = policy_ids

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
        if not isinstance(other, BatchCreateIpReputationRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
