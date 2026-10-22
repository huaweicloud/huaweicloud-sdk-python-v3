# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListV2NetworksResponse(SdkResponse):

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
        'networks': 'list[V2NetworkBriefInfo]'
    }

    attribute_map = {
        'total': 'total',
        'networks': 'networks'
    }

    def __init__(self, total=None, networks=None):
        r"""ListV2NetworksResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释**：总记录数。 **取值范围**：不涉及。 
        :type total: int
        :param networks: **参数解释**：网络配置列表。 
        :type networks: list[:class:`huaweicloudsdkaidatalake.v2.V2NetworkBriefInfo`]
        """
        
        super().__init__()

        self._total = None
        self._networks = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if networks is not None:
            self.networks = networks

    @property
    def total(self):
        r"""Gets the total of this ListV2NetworksResponse.

        **参数解释**：总记录数。 **取值范围**：不涉及。 

        :return: The total of this ListV2NetworksResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListV2NetworksResponse.

        **参数解释**：总记录数。 **取值范围**：不涉及。 

        :param total: The total of this ListV2NetworksResponse.
        :type total: int
        """
        self._total = total

    @property
    def networks(self):
        r"""Gets the networks of this ListV2NetworksResponse.

        **参数解释**：网络配置列表。 

        :return: The networks of this ListV2NetworksResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.V2NetworkBriefInfo`]
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        r"""Sets the networks of this ListV2NetworksResponse.

        **参数解释**：网络配置列表。 

        :param networks: The networks of this ListV2NetworksResponse.
        :type networks: list[:class:`huaweicloudsdkaidatalake.v2.V2NetworkBriefInfo`]
        """
        self._networks = networks

    def to_dict(self):
        import warnings
        warnings.warn("ListV2NetworksResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListV2NetworksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
