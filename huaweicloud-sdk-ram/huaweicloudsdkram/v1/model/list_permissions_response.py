# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPermissionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permissions': 'list[PermissionSummary]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'permissions': 'permissions',
        'page_info': 'page_info'
    }

    def __init__(self, permissions=None, page_info=None):
        r"""ListPermissionsResponse

        The model defined in huaweicloud sdk

        :param permissions: 共享资源权限的详细信息列表。
        :type permissions: list[:class:`huaweicloudsdkram.v1.PermissionSummary`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkram.v1.PageInfo`
        """
        
        super(ListPermissionsResponse, self).__init__()

        self._permissions = None
        self._page_info = None
        self.discriminator = None

        if permissions is not None:
            self.permissions = permissions
        if page_info is not None:
            self.page_info = page_info

    @property
    def permissions(self):
        r"""Gets the permissions of this ListPermissionsResponse.

        共享资源权限的详细信息列表。

        :return: The permissions of this ListPermissionsResponse.
        :rtype: list[:class:`huaweicloudsdkram.v1.PermissionSummary`]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        r"""Sets the permissions of this ListPermissionsResponse.

        共享资源权限的详细信息列表。

        :param permissions: The permissions of this ListPermissionsResponse.
        :type permissions: list[:class:`huaweicloudsdkram.v1.PermissionSummary`]
        """
        self._permissions = permissions

    @property
    def page_info(self):
        r"""Gets the page_info of this ListPermissionsResponse.

        :return: The page_info of this ListPermissionsResponse.
        :rtype: :class:`huaweicloudsdkram.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListPermissionsResponse.

        :param page_info: The page_info of this ListPermissionsResponse.
        :type page_info: :class:`huaweicloudsdkram.v1.PageInfo`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListPermissionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
