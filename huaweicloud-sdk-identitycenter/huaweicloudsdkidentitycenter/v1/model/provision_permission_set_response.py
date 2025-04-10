# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProvisionPermissionSetResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permission_set_provisioning_status': 'PermissionSetProvisioningStatusDto'
    }

    attribute_map = {
        'permission_set_provisioning_status': 'permission_set_provisioning_status'
    }

    def __init__(self, permission_set_provisioning_status=None):
        r"""ProvisionPermissionSetResponse

        The model defined in huaweicloud sdk

        :param permission_set_provisioning_status: 
        :type permission_set_provisioning_status: :class:`huaweicloudsdkidentitycenter.v1.PermissionSetProvisioningStatusDto`
        """
        
        super(ProvisionPermissionSetResponse, self).__init__()

        self._permission_set_provisioning_status = None
        self.discriminator = None

        if permission_set_provisioning_status is not None:
            self.permission_set_provisioning_status = permission_set_provisioning_status

    @property
    def permission_set_provisioning_status(self):
        r"""Gets the permission_set_provisioning_status of this ProvisionPermissionSetResponse.

        :return: The permission_set_provisioning_status of this ProvisionPermissionSetResponse.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.PermissionSetProvisioningStatusDto`
        """
        return self._permission_set_provisioning_status

    @permission_set_provisioning_status.setter
    def permission_set_provisioning_status(self, permission_set_provisioning_status):
        r"""Sets the permission_set_provisioning_status of this ProvisionPermissionSetResponse.

        :param permission_set_provisioning_status: The permission_set_provisioning_status of this ProvisionPermissionSetResponse.
        :type permission_set_provisioning_status: :class:`huaweicloudsdkidentitycenter.v1.PermissionSetProvisioningStatusDto`
        """
        self._permission_set_provisioning_status = permission_set_provisioning_status

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
        if not isinstance(other, ProvisionPermissionSetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
