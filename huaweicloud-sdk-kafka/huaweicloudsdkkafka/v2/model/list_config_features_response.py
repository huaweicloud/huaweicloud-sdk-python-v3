# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConfigFeaturesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'features': 'list[ListConfigFeatures]',
        'total_record': 'int'
    }

    attribute_map = {
        'features': 'features',
        'total_record': 'totalRecord'
    }

    def __init__(self, features=None, total_record=None):
        r"""ListConfigFeaturesResponse

        The model defined in huaweicloud sdk

        :param features: **参数解释**： 特性列表。
        :type features: list[:class:`huaweicloudsdkkafka.v2.ListConfigFeatures`]
        :param total_record: **参数解释**： 总特性数量。  **取值范围**： 不涉及。
        :type total_record: int
        """
        
        super().__init__()

        self._features = None
        self._total_record = None
        self.discriminator = None

        if features is not None:
            self.features = features
        if total_record is not None:
            self.total_record = total_record

    @property
    def features(self):
        r"""Gets the features of this ListConfigFeaturesResponse.

        **参数解释**： 特性列表。

        :return: The features of this ListConfigFeaturesResponse.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.ListConfigFeatures`]
        """
        return self._features

    @features.setter
    def features(self, features):
        r"""Sets the features of this ListConfigFeaturesResponse.

        **参数解释**： 特性列表。

        :param features: The features of this ListConfigFeaturesResponse.
        :type features: list[:class:`huaweicloudsdkkafka.v2.ListConfigFeatures`]
        """
        self._features = features

    @property
    def total_record(self):
        r"""Gets the total_record of this ListConfigFeaturesResponse.

        **参数解释**： 总特性数量。  **取值范围**： 不涉及。

        :return: The total_record of this ListConfigFeaturesResponse.
        :rtype: int
        """
        return self._total_record

    @total_record.setter
    def total_record(self, total_record):
        r"""Sets the total_record of this ListConfigFeaturesResponse.

        **参数解释**： 总特性数量。  **取值范围**： 不涉及。

        :param total_record: The total_record of this ListConfigFeaturesResponse.
        :type total_record: int
        """
        self._total_record = total_record

    def to_dict(self):
        import warnings
        warnings.warn("ListConfigFeaturesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListConfigFeaturesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
