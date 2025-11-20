# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrivilegeEscalationStep:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'principal': 'FindingPrincipal',
        'resources': 'list[str]',
        'action': 'str'
    }

    attribute_map = {
        'principal': 'principal',
        'resources': 'resources',
        'action': 'action'
    }

    def __init__(self, principal=None, resources=None, action=None):
        r"""PrivilegeEscalationStep

        The model defined in huaweicloud sdk

        :param principal: 
        :type principal: :class:`huaweicloudsdkiamaccessanalyzer.v1.FindingPrincipal`
        :param resources: 本步骤涉及到的资源。
        :type resources: list[str]
        :param action: 本步骤涉及到的操作。
        :type action: str
        """
        
        

        self._principal = None
        self._resources = None
        self._action = None
        self.discriminator = None

        self.principal = principal
        self.resources = resources
        self.action = action

    @property
    def principal(self):
        r"""Gets the principal of this PrivilegeEscalationStep.

        :return: The principal of this PrivilegeEscalationStep.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.FindingPrincipal`
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        r"""Sets the principal of this PrivilegeEscalationStep.

        :param principal: The principal of this PrivilegeEscalationStep.
        :type principal: :class:`huaweicloudsdkiamaccessanalyzer.v1.FindingPrincipal`
        """
        self._principal = principal

    @property
    def resources(self):
        r"""Gets the resources of this PrivilegeEscalationStep.

        本步骤涉及到的资源。

        :return: The resources of this PrivilegeEscalationStep.
        :rtype: list[str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this PrivilegeEscalationStep.

        本步骤涉及到的资源。

        :param resources: The resources of this PrivilegeEscalationStep.
        :type resources: list[str]
        """
        self._resources = resources

    @property
    def action(self):
        r"""Gets the action of this PrivilegeEscalationStep.

        本步骤涉及到的操作。

        :return: The action of this PrivilegeEscalationStep.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this PrivilegeEscalationStep.

        本步骤涉及到的操作。

        :param action: The action of this PrivilegeEscalationStep.
        :type action: str
        """
        self._action = action

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
        if not isinstance(other, PrivilegeEscalationStep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
