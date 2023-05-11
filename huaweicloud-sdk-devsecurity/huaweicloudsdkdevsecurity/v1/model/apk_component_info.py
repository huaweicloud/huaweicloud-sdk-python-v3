# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApkComponentInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permission': 'list[PermissionItem]',
        'activity': 'list[ApkComponentItem]',
        'service': 'list[ApkComponentItem]',
        'provider': 'list[ApkComponentItem]',
        'receive': 'list[ApkComponentItem]'
    }

    attribute_map = {
        'permission': 'permission',
        'activity': 'activity',
        'service': 'service',
        'provider': 'provider',
        'receive': 'receive'
    }

    def __init__(self, permission=None, activity=None, service=None, provider=None, receive=None):
        """ApkComponentInfo

        The model defined in huaweicloud sdk

        :param permission: 权限列表
        :type permission: list[:class:`huaweicloudsdkdevsecurity.v1.PermissionItem`]
        :param activity: 安卓activity列表，仅安卓任务存在该组件
        :type activity: list[:class:`huaweicloudsdkdevsecurity.v1.ApkComponentItem`]
        :param service: 安卓service列表，仅安卓任务存在该组件
        :type service: list[:class:`huaweicloudsdkdevsecurity.v1.ApkComponentItem`]
        :param provider: 安卓provider列表，仅安卓任务存在该组件
        :type provider: list[:class:`huaweicloudsdkdevsecurity.v1.ApkComponentItem`]
        :param receive: 安卓receive列表，仅安卓任务存在该组件
        :type receive: list[:class:`huaweicloudsdkdevsecurity.v1.ApkComponentItem`]
        """
        
        

        self._permission = None
        self._activity = None
        self._service = None
        self._provider = None
        self._receive = None
        self.discriminator = None

        if permission is not None:
            self.permission = permission
        if activity is not None:
            self.activity = activity
        if service is not None:
            self.service = service
        if provider is not None:
            self.provider = provider
        if receive is not None:
            self.receive = receive

    @property
    def permission(self):
        """Gets the permission of this ApkComponentInfo.

        权限列表

        :return: The permission of this ApkComponentInfo.
        :rtype: list[:class:`huaweicloudsdkdevsecurity.v1.PermissionItem`]
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this ApkComponentInfo.

        权限列表

        :param permission: The permission of this ApkComponentInfo.
        :type permission: list[:class:`huaweicloudsdkdevsecurity.v1.PermissionItem`]
        """
        self._permission = permission

    @property
    def activity(self):
        """Gets the activity of this ApkComponentInfo.

        安卓activity列表，仅安卓任务存在该组件

        :return: The activity of this ApkComponentInfo.
        :rtype: list[:class:`huaweicloudsdkdevsecurity.v1.ApkComponentItem`]
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this ApkComponentInfo.

        安卓activity列表，仅安卓任务存在该组件

        :param activity: The activity of this ApkComponentInfo.
        :type activity: list[:class:`huaweicloudsdkdevsecurity.v1.ApkComponentItem`]
        """
        self._activity = activity

    @property
    def service(self):
        """Gets the service of this ApkComponentInfo.

        安卓service列表，仅安卓任务存在该组件

        :return: The service of this ApkComponentInfo.
        :rtype: list[:class:`huaweicloudsdkdevsecurity.v1.ApkComponentItem`]
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this ApkComponentInfo.

        安卓service列表，仅安卓任务存在该组件

        :param service: The service of this ApkComponentInfo.
        :type service: list[:class:`huaweicloudsdkdevsecurity.v1.ApkComponentItem`]
        """
        self._service = service

    @property
    def provider(self):
        """Gets the provider of this ApkComponentInfo.

        安卓provider列表，仅安卓任务存在该组件

        :return: The provider of this ApkComponentInfo.
        :rtype: list[:class:`huaweicloudsdkdevsecurity.v1.ApkComponentItem`]
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ApkComponentInfo.

        安卓provider列表，仅安卓任务存在该组件

        :param provider: The provider of this ApkComponentInfo.
        :type provider: list[:class:`huaweicloudsdkdevsecurity.v1.ApkComponentItem`]
        """
        self._provider = provider

    @property
    def receive(self):
        """Gets the receive of this ApkComponentInfo.

        安卓receive列表，仅安卓任务存在该组件

        :return: The receive of this ApkComponentInfo.
        :rtype: list[:class:`huaweicloudsdkdevsecurity.v1.ApkComponentItem`]
        """
        return self._receive

    @receive.setter
    def receive(self, receive):
        """Sets the receive of this ApkComponentInfo.

        安卓receive列表，仅安卓任务存在该组件

        :param receive: The receive of this ApkComponentInfo.
        :type receive: list[:class:`huaweicloudsdkdevsecurity.v1.ApkComponentItem`]
        """
        self._receive = receive

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
        if not isinstance(other, ApkComponentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
