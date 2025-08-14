# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProvisioningTenantsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provisioning_tenants': 'list[ProvisioningTenant]'
    }

    attribute_map = {
        'provisioning_tenants': 'provisioning_tenants'
    }

    def __init__(self, provisioning_tenants=None):
        r"""ListProvisioningTenantsResponse

        The model defined in huaweicloud sdk

        :param provisioning_tenants: SCIM自动预配配置信息
        :type provisioning_tenants: list[:class:`huaweicloudsdkidentitycenterstore.v1.ProvisioningTenant`]
        """
        
        super(ListProvisioningTenantsResponse, self).__init__()

        self._provisioning_tenants = None
        self.discriminator = None

        if provisioning_tenants is not None:
            self.provisioning_tenants = provisioning_tenants

    @property
    def provisioning_tenants(self):
        r"""Gets the provisioning_tenants of this ListProvisioningTenantsResponse.

        SCIM自动预配配置信息

        :return: The provisioning_tenants of this ListProvisioningTenantsResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenterstore.v1.ProvisioningTenant`]
        """
        return self._provisioning_tenants

    @provisioning_tenants.setter
    def provisioning_tenants(self, provisioning_tenants):
        r"""Sets the provisioning_tenants of this ListProvisioningTenantsResponse.

        SCIM自动预配配置信息

        :param provisioning_tenants: The provisioning_tenants of this ListProvisioningTenantsResponse.
        :type provisioning_tenants: list[:class:`huaweicloudsdkidentitycenterstore.v1.ProvisioningTenant`]
        """
        self._provisioning_tenants = provisioning_tenants

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
        if not isinstance(other, ListProvisioningTenantsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
