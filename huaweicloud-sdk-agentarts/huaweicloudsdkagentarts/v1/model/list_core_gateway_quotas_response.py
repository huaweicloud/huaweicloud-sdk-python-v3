# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCoreGatewayQuotasResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'quotas': 'list[CoreGatewayQuota]',
        'size': 'int',
        'total': 'int'
    }

    attribute_map = {
        'quotas': 'quotas',
        'size': 'size',
        'total': 'total'
    }

    def __init__(self, quotas=None, size=None, total=None):
        r"""ListCoreGatewayQuotasResponse

        The model defined in huaweicloud sdk

        :param quotas: **参数解释：** 配额列表。 **取值范围：** 数组长度为 1-2。 
        :type quotas: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayQuota`]
        :param size: **参数解释：** 当前页返回的配额数量。 **取值范围：** 取值为 0-2个。 
        :type size: int
        :param total: **参数解释：** 配额总数。 **取值范围：** 取值为 0-2个。 
        :type total: int
        """
        
        super().__init__()

        self._quotas = None
        self._size = None
        self._total = None
        self.discriminator = None

        if quotas is not None:
            self.quotas = quotas
        if size is not None:
            self.size = size
        if total is not None:
            self.total = total

    @property
    def quotas(self):
        r"""Gets the quotas of this ListCoreGatewayQuotasResponse.

        **参数解释：** 配额列表。 **取值范围：** 数组长度为 1-2。 

        :return: The quotas of this ListCoreGatewayQuotasResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayQuota`]
        """
        return self._quotas

    @quotas.setter
    def quotas(self, quotas):
        r"""Sets the quotas of this ListCoreGatewayQuotasResponse.

        **参数解释：** 配额列表。 **取值范围：** 数组长度为 1-2。 

        :param quotas: The quotas of this ListCoreGatewayQuotasResponse.
        :type quotas: list[:class:`huaweicloudsdkagentarts.v1.CoreGatewayQuota`]
        """
        self._quotas = quotas

    @property
    def size(self):
        r"""Gets the size of this ListCoreGatewayQuotasResponse.

        **参数解释：** 当前页返回的配额数量。 **取值范围：** 取值为 0-2个。 

        :return: The size of this ListCoreGatewayQuotasResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListCoreGatewayQuotasResponse.

        **参数解释：** 当前页返回的配额数量。 **取值范围：** 取值为 0-2个。 

        :param size: The size of this ListCoreGatewayQuotasResponse.
        :type size: int
        """
        self._size = size

    @property
    def total(self):
        r"""Gets the total of this ListCoreGatewayQuotasResponse.

        **参数解释：** 配额总数。 **取值范围：** 取值为 0-2个。 

        :return: The total of this ListCoreGatewayQuotasResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListCoreGatewayQuotasResponse.

        **参数解释：** 配额总数。 **取值范围：** 取值为 0-2个。 

        :param total: The total of this ListCoreGatewayQuotasResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ListCoreGatewayQuotasResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListCoreGatewayQuotasResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
