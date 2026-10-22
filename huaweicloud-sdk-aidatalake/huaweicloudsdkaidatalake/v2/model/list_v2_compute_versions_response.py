# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListV2ComputeVersionsResponse(SdkResponse):

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
        'compute_versions': 'list[ShowV2ComputeVersionResponseBody]'
    }

    attribute_map = {
        'total': 'total',
        'compute_versions': 'compute_versions'
    }

    def __init__(self, total=None, compute_versions=None):
        r"""ListV2ComputeVersionsResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释**：总记录数。 **取值范围**：0~10000。 
        :type total: int
        :param compute_versions: **参数解释**：计算资源操作历史列表，列表元素为计算资源操作历史详情对象。 
        :type compute_versions: list[:class:`huaweicloudsdkaidatalake.v2.ShowV2ComputeVersionResponseBody`]
        """
        
        super().__init__()

        self._total = None
        self._compute_versions = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if compute_versions is not None:
            self.compute_versions = compute_versions

    @property
    def total(self):
        r"""Gets the total of this ListV2ComputeVersionsResponse.

        **参数解释**：总记录数。 **取值范围**：0~10000。 

        :return: The total of this ListV2ComputeVersionsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListV2ComputeVersionsResponse.

        **参数解释**：总记录数。 **取值范围**：0~10000。 

        :param total: The total of this ListV2ComputeVersionsResponse.
        :type total: int
        """
        self._total = total

    @property
    def compute_versions(self):
        r"""Gets the compute_versions of this ListV2ComputeVersionsResponse.

        **参数解释**：计算资源操作历史列表，列表元素为计算资源操作历史详情对象。 

        :return: The compute_versions of this ListV2ComputeVersionsResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.ShowV2ComputeVersionResponseBody`]
        """
        return self._compute_versions

    @compute_versions.setter
    def compute_versions(self, compute_versions):
        r"""Sets the compute_versions of this ListV2ComputeVersionsResponse.

        **参数解释**：计算资源操作历史列表，列表元素为计算资源操作历史详情对象。 

        :param compute_versions: The compute_versions of this ListV2ComputeVersionsResponse.
        :type compute_versions: list[:class:`huaweicloudsdkaidatalake.v2.ShowV2ComputeVersionResponseBody`]
        """
        self._compute_versions = compute_versions

    def to_dict(self):
        import warnings
        warnings.warn("ListV2ComputeVersionsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListV2ComputeVersionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
