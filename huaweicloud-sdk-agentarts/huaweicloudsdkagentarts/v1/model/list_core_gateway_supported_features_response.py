# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCoreGatewaySupportedFeaturesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'supported_features': 'list[str]',
        'size': 'int',
        'total': 'int'
    }

    attribute_map = {
        'supported_features': 'supported_features',
        'size': 'size',
        'total': 'total'
    }

    def __init__(self, supported_features=None, size=None, total=None):
        r"""ListCoreGatewaySupportedFeaturesResponse

        The model defined in huaweicloud sdk

        :param supported_features: **参数解释：** 网关支持的特性列表。 **取值范围：** 数组长度为1-100个。 
        :type supported_features: list[str]
        :param size: **参数解释：** 当前页返回的特性数量。 **取值范围：** 取值为 0-100个。 
        :type size: int
        :param total: **参数解释：** 特性总数。 **取值范围：** 取值为 0-1000000个。 
        :type total: int
        """
        
        super().__init__()

        self._supported_features = None
        self._size = None
        self._total = None
        self.discriminator = None

        if supported_features is not None:
            self.supported_features = supported_features
        if size is not None:
            self.size = size
        if total is not None:
            self.total = total

    @property
    def supported_features(self):
        r"""Gets the supported_features of this ListCoreGatewaySupportedFeaturesResponse.

        **参数解释：** 网关支持的特性列表。 **取值范围：** 数组长度为1-100个。 

        :return: The supported_features of this ListCoreGatewaySupportedFeaturesResponse.
        :rtype: list[str]
        """
        return self._supported_features

    @supported_features.setter
    def supported_features(self, supported_features):
        r"""Sets the supported_features of this ListCoreGatewaySupportedFeaturesResponse.

        **参数解释：** 网关支持的特性列表。 **取值范围：** 数组长度为1-100个。 

        :param supported_features: The supported_features of this ListCoreGatewaySupportedFeaturesResponse.
        :type supported_features: list[str]
        """
        self._supported_features = supported_features

    @property
    def size(self):
        r"""Gets the size of this ListCoreGatewaySupportedFeaturesResponse.

        **参数解释：** 当前页返回的特性数量。 **取值范围：** 取值为 0-100个。 

        :return: The size of this ListCoreGatewaySupportedFeaturesResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListCoreGatewaySupportedFeaturesResponse.

        **参数解释：** 当前页返回的特性数量。 **取值范围：** 取值为 0-100个。 

        :param size: The size of this ListCoreGatewaySupportedFeaturesResponse.
        :type size: int
        """
        self._size = size

    @property
    def total(self):
        r"""Gets the total of this ListCoreGatewaySupportedFeaturesResponse.

        **参数解释：** 特性总数。 **取值范围：** 取值为 0-1000000个。 

        :return: The total of this ListCoreGatewaySupportedFeaturesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListCoreGatewaySupportedFeaturesResponse.

        **参数解释：** 特性总数。 **取值范围：** 取值为 0-1000000个。 

        :param total: The total of this ListCoreGatewaySupportedFeaturesResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ListCoreGatewaySupportedFeaturesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListCoreGatewaySupportedFeaturesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
