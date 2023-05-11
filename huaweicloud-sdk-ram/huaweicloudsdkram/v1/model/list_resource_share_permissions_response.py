# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceSharePermissionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'associated_permissions': 'list[AssociatedPermission]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'associated_permissions': 'associated_permissions',
        'page_info': 'page_info'
    }

    def __init__(self, associated_permissions=None, page_info=None):
        """ListResourceSharePermissionsResponse

        The model defined in huaweicloud sdk

        :param associated_permissions: 资源共享实例关联的共享资源权限信息列表。
        :type associated_permissions: list[:class:`huaweicloudsdkram.v1.AssociatedPermission`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkram.v1.PageInfo`
        """
        
        super(ListResourceSharePermissionsResponse, self).__init__()

        self._associated_permissions = None
        self._page_info = None
        self.discriminator = None

        if associated_permissions is not None:
            self.associated_permissions = associated_permissions
        if page_info is not None:
            self.page_info = page_info

    @property
    def associated_permissions(self):
        """Gets the associated_permissions of this ListResourceSharePermissionsResponse.

        资源共享实例关联的共享资源权限信息列表。

        :return: The associated_permissions of this ListResourceSharePermissionsResponse.
        :rtype: list[:class:`huaweicloudsdkram.v1.AssociatedPermission`]
        """
        return self._associated_permissions

    @associated_permissions.setter
    def associated_permissions(self, associated_permissions):
        """Sets the associated_permissions of this ListResourceSharePermissionsResponse.

        资源共享实例关联的共享资源权限信息列表。

        :param associated_permissions: The associated_permissions of this ListResourceSharePermissionsResponse.
        :type associated_permissions: list[:class:`huaweicloudsdkram.v1.AssociatedPermission`]
        """
        self._associated_permissions = associated_permissions

    @property
    def page_info(self):
        """Gets the page_info of this ListResourceSharePermissionsResponse.

        :return: The page_info of this ListResourceSharePermissionsResponse.
        :rtype: :class:`huaweicloudsdkram.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListResourceSharePermissionsResponse.

        :param page_info: The page_info of this ListResourceSharePermissionsResponse.
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
        if not isinstance(other, ListResourceSharePermissionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
