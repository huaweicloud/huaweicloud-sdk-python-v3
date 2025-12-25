# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloudLogManagerVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tenant_managed_domain_id': 'str',
        'platform_managed_domain_id': 'str',
        'dw_region': 'str'
    }

    attribute_map = {
        'tenant_managed_domain_id': 'tenant_managed_domain_id',
        'platform_managed_domain_id': 'platform_managed_domain_id',
        'dw_region': 'dw_region'
    }

    def __init__(self, tenant_managed_domain_id=None, platform_managed_domain_id=None, dw_region=None):
        r"""CloudLogManagerVo

        The model defined in huaweicloud sdk

        :param tenant_managed_domain_id: 租户行管id
        :type tenant_managed_domain_id: str
        :param platform_managed_domain_id: 平台行管id
        :type platform_managed_domain_id: str
        :param dw_region: regionId
        :type dw_region: str
        """
        
        

        self._tenant_managed_domain_id = None
        self._platform_managed_domain_id = None
        self._dw_region = None
        self.discriminator = None

        if tenant_managed_domain_id is not None:
            self.tenant_managed_domain_id = tenant_managed_domain_id
        if platform_managed_domain_id is not None:
            self.platform_managed_domain_id = platform_managed_domain_id
        if dw_region is not None:
            self.dw_region = dw_region

    @property
    def tenant_managed_domain_id(self):
        r"""Gets the tenant_managed_domain_id of this CloudLogManagerVo.

        租户行管id

        :return: The tenant_managed_domain_id of this CloudLogManagerVo.
        :rtype: str
        """
        return self._tenant_managed_domain_id

    @tenant_managed_domain_id.setter
    def tenant_managed_domain_id(self, tenant_managed_domain_id):
        r"""Sets the tenant_managed_domain_id of this CloudLogManagerVo.

        租户行管id

        :param tenant_managed_domain_id: The tenant_managed_domain_id of this CloudLogManagerVo.
        :type tenant_managed_domain_id: str
        """
        self._tenant_managed_domain_id = tenant_managed_domain_id

    @property
    def platform_managed_domain_id(self):
        r"""Gets the platform_managed_domain_id of this CloudLogManagerVo.

        平台行管id

        :return: The platform_managed_domain_id of this CloudLogManagerVo.
        :rtype: str
        """
        return self._platform_managed_domain_id

    @platform_managed_domain_id.setter
    def platform_managed_domain_id(self, platform_managed_domain_id):
        r"""Sets the platform_managed_domain_id of this CloudLogManagerVo.

        平台行管id

        :param platform_managed_domain_id: The platform_managed_domain_id of this CloudLogManagerVo.
        :type platform_managed_domain_id: str
        """
        self._platform_managed_domain_id = platform_managed_domain_id

    @property
    def dw_region(self):
        r"""Gets the dw_region of this CloudLogManagerVo.

        regionId

        :return: The dw_region of this CloudLogManagerVo.
        :rtype: str
        """
        return self._dw_region

    @dw_region.setter
    def dw_region(self, dw_region):
        r"""Sets the dw_region of this CloudLogManagerVo.

        regionId

        :param dw_region: The dw_region of this CloudLogManagerVo.
        :type dw_region: str
        """
        self._dw_region = dw_region

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CloudLogManagerVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
