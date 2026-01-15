# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckCidrRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tenant_cidrs': 'list[str]',
        'availability_zone': 'str'
    }

    attribute_map = {
        'tenant_cidrs': 'tenant_cidrs',
        'availability_zone': 'availability_zone'
    }

    def __init__(self, tenant_cidrs=None, availability_zone=None):
        r"""CheckCidrRequestBody

        The model defined in huaweicloud sdk

        :param tenant_cidrs: 租户网段
        :type tenant_cidrs: list[str]
        :param availability_zone: 开通服务资源使用的可用分区。
        :type availability_zone: str
        """
        
        

        self._tenant_cidrs = None
        self._availability_zone = None
        self.discriminator = None

        if tenant_cidrs is not None:
            self.tenant_cidrs = tenant_cidrs
        if availability_zone is not None:
            self.availability_zone = availability_zone

    @property
    def tenant_cidrs(self):
        r"""Gets the tenant_cidrs of this CheckCidrRequestBody.

        租户网段

        :return: The tenant_cidrs of this CheckCidrRequestBody.
        :rtype: list[str]
        """
        return self._tenant_cidrs

    @tenant_cidrs.setter
    def tenant_cidrs(self, tenant_cidrs):
        r"""Sets the tenant_cidrs of this CheckCidrRequestBody.

        租户网段

        :param tenant_cidrs: The tenant_cidrs of this CheckCidrRequestBody.
        :type tenant_cidrs: list[str]
        """
        self._tenant_cidrs = tenant_cidrs

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this CheckCidrRequestBody.

        开通服务资源使用的可用分区。

        :return: The availability_zone of this CheckCidrRequestBody.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this CheckCidrRequestBody.

        开通服务资源使用的可用分区。

        :param availability_zone: The availability_zone of this CheckCidrRequestBody.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

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
        if not isinstance(other, CheckCidrRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
