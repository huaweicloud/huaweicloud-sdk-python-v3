# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrivilegeEscalationDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'actions': 'list[str]',
        'resource': 'str',
        'principal': 'FindingPrincipal',
        'active_action': 'str',
        'path': 'list[PrivilegeEscalationStep]'
    }

    attribute_map = {
        'actions': 'actions',
        'resource': 'resource',
        'principal': 'principal',
        'active_action': 'active_action',
        'path': 'path'
    }

    def __init__(self, actions=None, resource=None, principal=None, active_action=None, path=None):
        r"""PrivilegeEscalationDetails

        The model defined in huaweicloud sdk

        :param actions: 指定的待分析操作集合。
        :type actions: list[str]
        :param resource: 资源的唯一资源标识符。
        :type resource: str
        :param principal: 
        :type principal: :class:`huaweicloudsdkiamaccessanalyzer.v1.FindingPrincipal`
        :param active_action: 能够通过提权访问路径触发的操作代表。
        :type active_action: str
        :param path: 
        :type path: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.PrivilegeEscalationStep`]
        """
        
        

        self._actions = None
        self._resource = None
        self._principal = None
        self._active_action = None
        self._path = None
        self.discriminator = None

        self.actions = actions
        self.resource = resource
        self.principal = principal
        self.active_action = active_action
        self.path = path

    @property
    def actions(self):
        r"""Gets the actions of this PrivilegeEscalationDetails.

        指定的待分析操作集合。

        :return: The actions of this PrivilegeEscalationDetails.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this PrivilegeEscalationDetails.

        指定的待分析操作集合。

        :param actions: The actions of this PrivilegeEscalationDetails.
        :type actions: list[str]
        """
        self._actions = actions

    @property
    def resource(self):
        r"""Gets the resource of this PrivilegeEscalationDetails.

        资源的唯一资源标识符。

        :return: The resource of this PrivilegeEscalationDetails.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this PrivilegeEscalationDetails.

        资源的唯一资源标识符。

        :param resource: The resource of this PrivilegeEscalationDetails.
        :type resource: str
        """
        self._resource = resource

    @property
    def principal(self):
        r"""Gets the principal of this PrivilegeEscalationDetails.

        :return: The principal of this PrivilegeEscalationDetails.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.FindingPrincipal`
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        r"""Sets the principal of this PrivilegeEscalationDetails.

        :param principal: The principal of this PrivilegeEscalationDetails.
        :type principal: :class:`huaweicloudsdkiamaccessanalyzer.v1.FindingPrincipal`
        """
        self._principal = principal

    @property
    def active_action(self):
        r"""Gets the active_action of this PrivilegeEscalationDetails.

        能够通过提权访问路径触发的操作代表。

        :return: The active_action of this PrivilegeEscalationDetails.
        :rtype: str
        """
        return self._active_action

    @active_action.setter
    def active_action(self, active_action):
        r"""Sets the active_action of this PrivilegeEscalationDetails.

        能够通过提权访问路径触发的操作代表。

        :param active_action: The active_action of this PrivilegeEscalationDetails.
        :type active_action: str
        """
        self._active_action = active_action

    @property
    def path(self):
        r"""Gets the path of this PrivilegeEscalationDetails.

        :return: The path of this PrivilegeEscalationDetails.
        :rtype: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.PrivilegeEscalationStep`]
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this PrivilegeEscalationDetails.

        :param path: The path of this PrivilegeEscalationDetails.
        :type path: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.PrivilegeEscalationStep`]
        """
        self._path = path

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
        if not isinstance(other, PrivilegeEscalationDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
