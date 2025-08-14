# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateProvisioningTenantResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'creation_time': 'float',
        'scim_endpoint': 'str',
        'tenant_id': 'str'
    }

    attribute_map = {
        'creation_time': 'creation_time',
        'scim_endpoint': 'scim_endpoint',
        'tenant_id': 'tenant_id'
    }

    def __init__(self, creation_time=None, scim_endpoint=None, tenant_id=None):
        r"""CreateProvisioningTenantResponse

        The model defined in huaweicloud sdk

        :param creation_time: 创建时间
        :type creation_time: float
        :param scim_endpoint: SCIM终端节点
        :type scim_endpoint: str
        :param tenant_id: 开启自动预配后生成的全局唯一标识符（ID）
        :type tenant_id: str
        """
        
        super(CreateProvisioningTenantResponse, self).__init__()

        self._creation_time = None
        self._scim_endpoint = None
        self._tenant_id = None
        self.discriminator = None

        if creation_time is not None:
            self.creation_time = creation_time
        if scim_endpoint is not None:
            self.scim_endpoint = scim_endpoint
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def creation_time(self):
        r"""Gets the creation_time of this CreateProvisioningTenantResponse.

        创建时间

        :return: The creation_time of this CreateProvisioningTenantResponse.
        :rtype: float
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        r"""Sets the creation_time of this CreateProvisioningTenantResponse.

        创建时间

        :param creation_time: The creation_time of this CreateProvisioningTenantResponse.
        :type creation_time: float
        """
        self._creation_time = creation_time

    @property
    def scim_endpoint(self):
        r"""Gets the scim_endpoint of this CreateProvisioningTenantResponse.

        SCIM终端节点

        :return: The scim_endpoint of this CreateProvisioningTenantResponse.
        :rtype: str
        """
        return self._scim_endpoint

    @scim_endpoint.setter
    def scim_endpoint(self, scim_endpoint):
        r"""Sets the scim_endpoint of this CreateProvisioningTenantResponse.

        SCIM终端节点

        :param scim_endpoint: The scim_endpoint of this CreateProvisioningTenantResponse.
        :type scim_endpoint: str
        """
        self._scim_endpoint = scim_endpoint

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this CreateProvisioningTenantResponse.

        开启自动预配后生成的全局唯一标识符（ID）

        :return: The tenant_id of this CreateProvisioningTenantResponse.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this CreateProvisioningTenantResponse.

        开启自动预配后生成的全局唯一标识符（ID）

        :param tenant_id: The tenant_id of this CreateProvisioningTenantResponse.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

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
        if not isinstance(other, CreateProvisioningTenantResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
