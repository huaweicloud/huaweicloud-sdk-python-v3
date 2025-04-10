# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPermissionSetProvisioningStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permission_sets_provisioning_status': 'list[PermissionSetProvisioningStatusMetadataDto]',
        'page_info': 'PageInfoDto'
    }

    attribute_map = {
        'permission_sets_provisioning_status': 'permission_sets_provisioning_status',
        'page_info': 'page_info'
    }

    def __init__(self, permission_sets_provisioning_status=None, page_info=None):
        r"""ListPermissionSetProvisioningStatusResponse

        The model defined in huaweicloud sdk

        :param permission_sets_provisioning_status: 权限集授权状态
        :type permission_sets_provisioning_status: list[:class:`huaweicloudsdkidentitycenter.v1.PermissionSetProvisioningStatusMetadataDto`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkidentitycenter.v1.PageInfoDto`
        """
        
        super(ListPermissionSetProvisioningStatusResponse, self).__init__()

        self._permission_sets_provisioning_status = None
        self._page_info = None
        self.discriminator = None

        if permission_sets_provisioning_status is not None:
            self.permission_sets_provisioning_status = permission_sets_provisioning_status
        if page_info is not None:
            self.page_info = page_info

    @property
    def permission_sets_provisioning_status(self):
        r"""Gets the permission_sets_provisioning_status of this ListPermissionSetProvisioningStatusResponse.

        权限集授权状态

        :return: The permission_sets_provisioning_status of this ListPermissionSetProvisioningStatusResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenter.v1.PermissionSetProvisioningStatusMetadataDto`]
        """
        return self._permission_sets_provisioning_status

    @permission_sets_provisioning_status.setter
    def permission_sets_provisioning_status(self, permission_sets_provisioning_status):
        r"""Sets the permission_sets_provisioning_status of this ListPermissionSetProvisioningStatusResponse.

        权限集授权状态

        :param permission_sets_provisioning_status: The permission_sets_provisioning_status of this ListPermissionSetProvisioningStatusResponse.
        :type permission_sets_provisioning_status: list[:class:`huaweicloudsdkidentitycenter.v1.PermissionSetProvisioningStatusMetadataDto`]
        """
        self._permission_sets_provisioning_status = permission_sets_provisioning_status

    @property
    def page_info(self):
        r"""Gets the page_info of this ListPermissionSetProvisioningStatusResponse.

        :return: The page_info of this ListPermissionSetProvisioningStatusResponse.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.PageInfoDto`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListPermissionSetProvisioningStatusResponse.

        :param page_info: The page_info of this ListPermissionSetProvisioningStatusResponse.
        :type page_info: :class:`huaweicloudsdkidentitycenter.v1.PageInfoDto`
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
        if not isinstance(other, ListPermissionSetProvisioningStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
