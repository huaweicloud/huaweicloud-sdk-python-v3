# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTenantKmsGrantResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tenant_id': 'str',
        'assumed': 'bool'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'assumed': 'assumed'
    }

    def __init__(self, tenant_id=None, assumed=None):
        r"""ShowTenantKmsGrantResponse

        The model defined in huaweicloud sdk

        :param tenant_id: **参数解释：** 租户id。 **取值范围：** 字符串长度不少于1，不超过1000。
        :type tenant_id: str
        :param assumed: **参数解释：** 是否有委托和授权。
        :type assumed: bool
        """
        
        super().__init__()

        self._tenant_id = None
        self._assumed = None
        self.discriminator = None

        if tenant_id is not None:
            self.tenant_id = tenant_id
        if assumed is not None:
            self.assumed = assumed

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ShowTenantKmsGrantResponse.

        **参数解释：** 租户id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :return: The tenant_id of this ShowTenantKmsGrantResponse.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ShowTenantKmsGrantResponse.

        **参数解释：** 租户id。 **取值范围：** 字符串长度不少于1，不超过1000。

        :param tenant_id: The tenant_id of this ShowTenantKmsGrantResponse.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def assumed(self):
        r"""Gets the assumed of this ShowTenantKmsGrantResponse.

        **参数解释：** 是否有委托和授权。

        :return: The assumed of this ShowTenantKmsGrantResponse.
        :rtype: bool
        """
        return self._assumed

    @assumed.setter
    def assumed(self, assumed):
        r"""Sets the assumed of this ShowTenantKmsGrantResponse.

        **参数解释：** 是否有委托和授权。

        :param assumed: The assumed of this ShowTenantKmsGrantResponse.
        :type assumed: bool
        """
        self._assumed = assumed

    def to_dict(self):
        import warnings
        warnings.warn("ShowTenantKmsGrantResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowTenantKmsGrantResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
