# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidateAuthResults:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'verdict': 'str',
        'action_id': 'str',
        'resource': 'str',
        'cause': 'list[Cause]'
    }

    attribute_map = {
        'action': 'action',
        'verdict': 'verdict',
        'action_id': 'action_id',
        'resource': 'resource',
        'cause': 'cause'
    }

    def __init__(self, action=None, verdict=None, action_id=None, resource=None, cause=None):
        r"""ValidateAuthResults

        The model defined in huaweicloud sdk

        :param action: **参数解释**：细粒度权限。 **取值范围**：不涉及。
        :type action: str
        :param verdict: **参数解释**：鉴权通过与否。 **取值范围**： - allow：通过。 - deny：不通过。
        :type verdict: str
        :param action_id: **参数解释**：随机的uuid，用来定位问题使用。 **取值范围**：不涉及。
        :type action_id: str
        :param resource: **参数解释**：请求资源。 **取值范围**：不涉及。
        :type resource: str
        :param cause: **参数解释**：失败情况下原因。
        :type cause: list[:class:`huaweicloudsdkmodelarts.v1.Cause`]
        """
        
        

        self._action = None
        self._verdict = None
        self._action_id = None
        self._resource = None
        self._cause = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if verdict is not None:
            self.verdict = verdict
        if action_id is not None:
            self.action_id = action_id
        if resource is not None:
            self.resource = resource
        if cause is not None:
            self.cause = cause

    @property
    def action(self):
        r"""Gets the action of this ValidateAuthResults.

        **参数解释**：细粒度权限。 **取值范围**：不涉及。

        :return: The action of this ValidateAuthResults.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ValidateAuthResults.

        **参数解释**：细粒度权限。 **取值范围**：不涉及。

        :param action: The action of this ValidateAuthResults.
        :type action: str
        """
        self._action = action

    @property
    def verdict(self):
        r"""Gets the verdict of this ValidateAuthResults.

        **参数解释**：鉴权通过与否。 **取值范围**： - allow：通过。 - deny：不通过。

        :return: The verdict of this ValidateAuthResults.
        :rtype: str
        """
        return self._verdict

    @verdict.setter
    def verdict(self, verdict):
        r"""Sets the verdict of this ValidateAuthResults.

        **参数解释**：鉴权通过与否。 **取值范围**： - allow：通过。 - deny：不通过。

        :param verdict: The verdict of this ValidateAuthResults.
        :type verdict: str
        """
        self._verdict = verdict

    @property
    def action_id(self):
        r"""Gets the action_id of this ValidateAuthResults.

        **参数解释**：随机的uuid，用来定位问题使用。 **取值范围**：不涉及。

        :return: The action_id of this ValidateAuthResults.
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        r"""Sets the action_id of this ValidateAuthResults.

        **参数解释**：随机的uuid，用来定位问题使用。 **取值范围**：不涉及。

        :param action_id: The action_id of this ValidateAuthResults.
        :type action_id: str
        """
        self._action_id = action_id

    @property
    def resource(self):
        r"""Gets the resource of this ValidateAuthResults.

        **参数解释**：请求资源。 **取值范围**：不涉及。

        :return: The resource of this ValidateAuthResults.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this ValidateAuthResults.

        **参数解释**：请求资源。 **取值范围**：不涉及。

        :param resource: The resource of this ValidateAuthResults.
        :type resource: str
        """
        self._resource = resource

    @property
    def cause(self):
        r"""Gets the cause of this ValidateAuthResults.

        **参数解释**：失败情况下原因。

        :return: The cause of this ValidateAuthResults.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.Cause`]
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        r"""Sets the cause of this ValidateAuthResults.

        **参数解释**：失败情况下原因。

        :param cause: The cause of this ValidateAuthResults.
        :type cause: list[:class:`huaweicloudsdkmodelarts.v1.Cause`]
        """
        self._cause = cause

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
        if not isinstance(other, ValidateAuthResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
