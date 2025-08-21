# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGroupPermissionResourcesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'use_project_permission': 'bool',
        'resources': 'list[PermissionResourcesDto]'
    }

    attribute_map = {
        'use_project_permission': 'use_project_permission',
        'resources': 'resources'
    }

    def __init__(self, use_project_permission=None, resources=None):
        r"""ListGroupPermissionResourcesResponse

        The model defined in huaweicloud sdk

        :param use_project_permission: **参数解释：** 是否使用项目权限。
        :type use_project_permission: bool
        :param resources: **参数解释：** 资源列表。
        :type resources: list[:class:`huaweicloudsdkcodehub.v4.PermissionResourcesDto`]
        """
        
        super(ListGroupPermissionResourcesResponse, self).__init__()

        self._use_project_permission = None
        self._resources = None
        self.discriminator = None

        if use_project_permission is not None:
            self.use_project_permission = use_project_permission
        if resources is not None:
            self.resources = resources

    @property
    def use_project_permission(self):
        r"""Gets the use_project_permission of this ListGroupPermissionResourcesResponse.

        **参数解释：** 是否使用项目权限。

        :return: The use_project_permission of this ListGroupPermissionResourcesResponse.
        :rtype: bool
        """
        return self._use_project_permission

    @use_project_permission.setter
    def use_project_permission(self, use_project_permission):
        r"""Sets the use_project_permission of this ListGroupPermissionResourcesResponse.

        **参数解释：** 是否使用项目权限。

        :param use_project_permission: The use_project_permission of this ListGroupPermissionResourcesResponse.
        :type use_project_permission: bool
        """
        self._use_project_permission = use_project_permission

    @property
    def resources(self):
        r"""Gets the resources of this ListGroupPermissionResourcesResponse.

        **参数解释：** 资源列表。

        :return: The resources of this ListGroupPermissionResourcesResponse.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.PermissionResourcesDto`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this ListGroupPermissionResourcesResponse.

        **参数解释：** 资源列表。

        :param resources: The resources of this ListGroupPermissionResourcesResponse.
        :type resources: list[:class:`huaweicloudsdkcodehub.v4.PermissionResourcesDto`]
        """
        self._resources = resources

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
        if not isinstance(other, ListGroupPermissionResourcesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
