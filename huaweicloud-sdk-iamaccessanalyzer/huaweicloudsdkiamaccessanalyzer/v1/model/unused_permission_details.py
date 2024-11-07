# coding: utf-8

import six

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
        'actions': 'list[UnusedAction]'
    }

    attribute_map = {
        'service': 'service',
        'actions': 'actions'
    }

    def __init__(self, service=None, actions=None):
        """UnusedPermissionDetails

        The model defined in huaweicloud sdk

        :param service: 权限对应的云服务名称。
        :type service: str
        :param actions: 未使用的操作列表。
        :type actions: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedAction`]
        """
        
        

        self._service = None
        self._actions = None
        self.discriminator = None

        self.service = service
        self.actions = actions

    @property
    def service(self):
        """Gets the service of this UnusedPermissionDetails.

        权限对应的云服务名称。

        :return: The service of this UnusedPermissionDetails.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this UnusedPermissionDetails.

        权限对应的云服务名称。

        :param service: The service of this UnusedPermissionDetails.
        :type service: str
        """
        self._service = service

    @property
    def actions(self):
        """Gets the actions of this UnusedPermissionDetails.

        未使用的操作列表。

        :return: The actions of this UnusedPermissionDetails.
        :rtype: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedAction`]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this UnusedPermissionDetails.

        未使用的操作列表。

        :param actions: The actions of this UnusedPermissionDetails.
        :type actions: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.UnusedAction`]
        """
        self._actions = actions

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
        if not isinstance(other, UnusedPermissionDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
