# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HapComponentInfo:

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
        'page': 'list[HapComponentItem]',
        'service': 'list[HapComponentItem]',
        'data': 'list[HapComponentItem]'
    }

    attribute_map = {
        'permission': 'permission',
        'page': 'page',
        'service': 'service',
        'data': 'data'
    }

    def __init__(self, permission=None, page=None, service=None, data=None):
        r"""HapComponentInfo

        The model defined in huaweicloud sdk

        :param permission: 权限列表
        :type permission: list[:class:`huaweicloudsdkcodeartsgovernance.v1.PermissionItem`]
        :param page: 鸿蒙Page列表，仅鸿蒙任务存在该组件
        :type page: list[:class:`huaweicloudsdkcodeartsgovernance.v1.HapComponentItem`]
        :param service: 鸿蒙service列表，仅鸿蒙任务存在该组件
        :type service: list[:class:`huaweicloudsdkcodeartsgovernance.v1.HapComponentItem`]
        :param data: 鸿蒙data息列表，仅鸿蒙任务存在该组件
        :type data: list[:class:`huaweicloudsdkcodeartsgovernance.v1.HapComponentItem`]
        """
        
        

        self._permission = None
        self._page = None
        self._service = None
        self._data = None
        self.discriminator = None

        if permission is not None:
            self.permission = permission
        if page is not None:
            self.page = page
        if service is not None:
            self.service = service
        if data is not None:
            self.data = data

    @property
    def permission(self):
        r"""Gets the permission of this HapComponentInfo.

        权限列表

        :return: The permission of this HapComponentInfo.
        :rtype: list[:class:`huaweicloudsdkcodeartsgovernance.v1.PermissionItem`]
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        r"""Sets the permission of this HapComponentInfo.

        权限列表

        :param permission: The permission of this HapComponentInfo.
        :type permission: list[:class:`huaweicloudsdkcodeartsgovernance.v1.PermissionItem`]
        """
        self._permission = permission

    @property
    def page(self):
        r"""Gets the page of this HapComponentInfo.

        鸿蒙Page列表，仅鸿蒙任务存在该组件

        :return: The page of this HapComponentInfo.
        :rtype: list[:class:`huaweicloudsdkcodeartsgovernance.v1.HapComponentItem`]
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this HapComponentInfo.

        鸿蒙Page列表，仅鸿蒙任务存在该组件

        :param page: The page of this HapComponentInfo.
        :type page: list[:class:`huaweicloudsdkcodeartsgovernance.v1.HapComponentItem`]
        """
        self._page = page

    @property
    def service(self):
        r"""Gets the service of this HapComponentInfo.

        鸿蒙service列表，仅鸿蒙任务存在该组件

        :return: The service of this HapComponentInfo.
        :rtype: list[:class:`huaweicloudsdkcodeartsgovernance.v1.HapComponentItem`]
        """
        return self._service

    @service.setter
    def service(self, service):
        r"""Sets the service of this HapComponentInfo.

        鸿蒙service列表，仅鸿蒙任务存在该组件

        :param service: The service of this HapComponentInfo.
        :type service: list[:class:`huaweicloudsdkcodeartsgovernance.v1.HapComponentItem`]
        """
        self._service = service

    @property
    def data(self):
        r"""Gets the data of this HapComponentInfo.

        鸿蒙data息列表，仅鸿蒙任务存在该组件

        :return: The data of this HapComponentInfo.
        :rtype: list[:class:`huaweicloudsdkcodeartsgovernance.v1.HapComponentItem`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this HapComponentInfo.

        鸿蒙data息列表，仅鸿蒙任务存在该组件

        :param data: The data of this HapComponentInfo.
        :type data: list[:class:`huaweicloudsdkcodeartsgovernance.v1.HapComponentItem`]
        """
        self._data = data

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
        if not isinstance(other, HapComponentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
