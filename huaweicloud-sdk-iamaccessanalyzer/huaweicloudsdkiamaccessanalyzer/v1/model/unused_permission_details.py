# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnusedPermissionDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service': 'str',
        'last_accessed': 'datetime',
        'actions': 'list[UnusedAction]'
    }

    attribute_map = {
        'service': 'service',
        'last_accessed': 'last_accessed',
        'actions': 'actions'
    }

    def __init__(self, service=None, last_accessed=None, actions=None):
        r"""UnusedPermissionDetails

        The model defined in huaweicloud sdk

        :param service: 权限对应的云服务名称。
        :type service: str
        :param last_accessed: 用户使用云服务的最后访问时间。
        :type last_accessed: datetime
        :param actions: 未使用的操作列表。
        :type actions: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedAction`]
        """
        
        

        self._service = None
        self._last_accessed = None
        self._actions = None
        self.discriminator = None

        self.service = service
        if last_accessed is not None:
            self.last_accessed = last_accessed
        self.actions = actions

    @property
    def service(self):
        r"""Gets the service of this UnusedPermissionDetails.

        权限对应的云服务名称。

        :return: The service of this UnusedPermissionDetails.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        r"""Sets the service of this UnusedPermissionDetails.

        权限对应的云服务名称。

        :param service: The service of this UnusedPermissionDetails.
        :type service: str
        """
        self._service = service

    @property
    def last_accessed(self):
        r"""Gets the last_accessed of this UnusedPermissionDetails.

        用户使用云服务的最后访问时间。

        :return: The last_accessed of this UnusedPermissionDetails.
        :rtype: datetime
        """
        return self._last_accessed

    @last_accessed.setter
    def last_accessed(self, last_accessed):
        r"""Sets the last_accessed of this UnusedPermissionDetails.

        用户使用云服务的最后访问时间。

        :param last_accessed: The last_accessed of this UnusedPermissionDetails.
        :type last_accessed: datetime
        """
        self._last_accessed = last_accessed

    @property
    def actions(self):
        r"""Gets the actions of this UnusedPermissionDetails.

        未使用的操作列表。

        :return: The actions of this UnusedPermissionDetails.
        :rtype: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedAction`]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this UnusedPermissionDetails.

        未使用的操作列表。

        :param actions: The actions of this UnusedPermissionDetails.
        :type actions: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedAction`]
        """
        self._actions = actions

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
        if not isinstance(other, UnusedPermissionDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
