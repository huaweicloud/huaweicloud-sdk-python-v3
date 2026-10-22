# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListV2RayFederationsResponse(SdkResponse):

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
        'ray_federations': 'list[V2RayFederationInfo]'
    }

    attribute_map = {
        'total': 'total',
        'ray_federations': 'ray_federations'
    }

    def __init__(self, total=None, ray_federations=None):
        r"""ListV2RayFederationsResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释**：Ray联邦端点总记录数。 **取值范围**：大于等于0的整数。 
        :type total: int
        :param ray_federations: **参数解释**：Ray联邦端点列表。 
        :type ray_federations: list[:class:`huaweicloudsdkaidatalake.v2.V2RayFederationInfo`]
        """
        
        super().__init__()

        self._total = None
        self._ray_federations = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if ray_federations is not None:
            self.ray_federations = ray_federations

    @property
    def total(self):
        r"""Gets the total of this ListV2RayFederationsResponse.

        **参数解释**：Ray联邦端点总记录数。 **取值范围**：大于等于0的整数。 

        :return: The total of this ListV2RayFederationsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListV2RayFederationsResponse.

        **参数解释**：Ray联邦端点总记录数。 **取值范围**：大于等于0的整数。 

        :param total: The total of this ListV2RayFederationsResponse.
        :type total: int
        """
        self._total = total

    @property
    def ray_federations(self):
        r"""Gets the ray_federations of this ListV2RayFederationsResponse.

        **参数解释**：Ray联邦端点列表。 

        :return: The ray_federations of this ListV2RayFederationsResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.V2RayFederationInfo`]
        """
        return self._ray_federations

    @ray_federations.setter
    def ray_federations(self, ray_federations):
        r"""Sets the ray_federations of this ListV2RayFederationsResponse.

        **参数解释**：Ray联邦端点列表。 

        :param ray_federations: The ray_federations of this ListV2RayFederationsResponse.
        :type ray_federations: list[:class:`huaweicloudsdkaidatalake.v2.V2RayFederationInfo`]
        """
        self._ray_federations = ray_federations

    def to_dict(self):
        import warnings
        warnings.warn("ListV2RayFederationsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListV2RayFederationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
