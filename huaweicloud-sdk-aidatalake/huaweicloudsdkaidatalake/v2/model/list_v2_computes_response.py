# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListV2ComputesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'computes': 'list[V2ComputeInfo]'
    }

    attribute_map = {
        'total': 'total',
        'computes': 'computes'
    }

    def __init__(self, total=None, computes=None):
        r"""ListV2ComputesResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释**：总记录数。 **取值范围**：0~10000。 
        :type total: int
        :param computes: **参数解释**：计算资源列表，每个元素为一个V2ComputeInfo对象，包含计算资源ID、名称、计费模式、容量配置、标签等详细信息。 
        :type computes: list[:class:`huaweicloudsdkaidatalake.v2.V2ComputeInfo`]
        """
        
        super().__init__()

        self._total = None
        self._computes = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if computes is not None:
            self.computes = computes

    @property
    def total(self):
        r"""Gets the total of this ListV2ComputesResponse.

        **参数解释**：总记录数。 **取值范围**：0~10000。 

        :return: The total of this ListV2ComputesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListV2ComputesResponse.

        **参数解释**：总记录数。 **取值范围**：0~10000。 

        :param total: The total of this ListV2ComputesResponse.
        :type total: int
        """
        self._total = total

    @property
    def computes(self):
        r"""Gets the computes of this ListV2ComputesResponse.

        **参数解释**：计算资源列表，每个元素为一个V2ComputeInfo对象，包含计算资源ID、名称、计费模式、容量配置、标签等详细信息。 

        :return: The computes of this ListV2ComputesResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.V2ComputeInfo`]
        """
        return self._computes

    @computes.setter
    def computes(self, computes):
        r"""Sets the computes of this ListV2ComputesResponse.

        **参数解释**：计算资源列表，每个元素为一个V2ComputeInfo对象，包含计算资源ID、名称、计费模式、容量配置、标签等详细信息。 

        :param computes: The computes of this ListV2ComputesResponse.
        :type computes: list[:class:`huaweicloudsdkaidatalake.v2.V2ComputeInfo`]
        """
        self._computes = computes

    def to_dict(self):
        import warnings
        warnings.warn("ListV2ComputesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListV2ComputesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
