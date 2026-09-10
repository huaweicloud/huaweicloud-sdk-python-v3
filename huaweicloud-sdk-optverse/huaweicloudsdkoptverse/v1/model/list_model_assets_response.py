# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListModelAssetsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'assets': 'list[ModelAssetRsp]',
        'count': 'int'
    }

    attribute_map = {
        'assets': 'assets',
        'count': 'count'
    }

    def __init__(self, assets=None, count=None):
        r"""ListModelAssetsResponse

        The model defined in huaweicloud sdk

        :param assets: **参数解释**： 资产列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type assets: list[:class:`huaweicloudsdkoptverse.v1.ModelAssetRsp`]
        :param count: **参数解释**： 资产总数。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type count: int
        """
        
        super().__init__()

        self._assets = None
        self._count = None
        self.discriminator = None

        if assets is not None:
            self.assets = assets
        if count is not None:
            self.count = count

    @property
    def assets(self):
        r"""Gets the assets of this ListModelAssetsResponse.

        **参数解释**： 资产列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The assets of this ListModelAssetsResponse.
        :rtype: list[:class:`huaweicloudsdkoptverse.v1.ModelAssetRsp`]
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        r"""Sets the assets of this ListModelAssetsResponse.

        **参数解释**： 资产列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param assets: The assets of this ListModelAssetsResponse.
        :type assets: list[:class:`huaweicloudsdkoptverse.v1.ModelAssetRsp`]
        """
        self._assets = assets

    @property
    def count(self):
        r"""Gets the count of this ListModelAssetsResponse.

        **参数解释**： 资产总数。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The count of this ListModelAssetsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListModelAssetsResponse.

        **参数解释**： 资产总数。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param count: The count of this ListModelAssetsResponse.
        :type count: int
        """
        self._count = count

    def to_dict(self):
        import warnings
        warnings.warn("ListModelAssetsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListModelAssetsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
