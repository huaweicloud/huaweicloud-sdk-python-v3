# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServicePermissionsDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permissions': 'list[PermissionObject]',
        'total_count': 'int'
    }

    attribute_map = {
        'permissions': 'permissions',
        'total_count': 'total_count'
    }

    def __init__(self, permissions=None, total_count=None):
        """ListServicePermissionsDetailsResponse

        The model defined in huaweicloud sdk

        :param permissions: permission列表。
        :type permissions: list[:class:`huaweicloudsdkvpcep.v1.PermissionObject`]
        :param total_count: 满足查询条件的终端节点服务的白名单总条数，不受分页（即limit、offset参数）影响。
        :type total_count: int
        """
        
        super(ListServicePermissionsDetailsResponse, self).__init__()

        self._permissions = None
        self._total_count = None
        self.discriminator = None

        if permissions is not None:
            self.permissions = permissions
        if total_count is not None:
            self.total_count = total_count

    @property
    def permissions(self):
        """Gets the permissions of this ListServicePermissionsDetailsResponse.

        permission列表。

        :return: The permissions of this ListServicePermissionsDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkvpcep.v1.PermissionObject`]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this ListServicePermissionsDetailsResponse.

        permission列表。

        :param permissions: The permissions of this ListServicePermissionsDetailsResponse.
        :type permissions: list[:class:`huaweicloudsdkvpcep.v1.PermissionObject`]
        """
        self._permissions = permissions

    @property
    def total_count(self):
        """Gets the total_count of this ListServicePermissionsDetailsResponse.

        满足查询条件的终端节点服务的白名单总条数，不受分页（即limit、offset参数）影响。

        :return: The total_count of this ListServicePermissionsDetailsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListServicePermissionsDetailsResponse.

        满足查询条件的终端节点服务的白名单总条数，不受分页（即limit、offset参数）影响。

        :param total_count: The total_count of this ListServicePermissionsDetailsResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListServicePermissionsDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
