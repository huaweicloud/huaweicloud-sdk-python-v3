# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFeatureConfigsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'feature': 'str'
    }

    attribute_map = {
        'feature': 'feature'
    }

    def __init__(self, feature=None):
        r"""ListFeatureConfigsRequest

        The model defined in huaweicloud sdk

        :param feature: **参数解释**：特性名称。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type feature: str
        """
        
        

        self._feature = None
        self.discriminator = None

        if feature is not None:
            self.feature = feature

    @property
    def feature(self):
        r"""Gets the feature of this ListFeatureConfigsRequest.

        **参数解释**：特性名称。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The feature of this ListFeatureConfigsRequest.
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        r"""Sets the feature of this ListFeatureConfigsRequest.

        **参数解释**：特性名称。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param feature: The feature of this ListFeatureConfigsRequest.
        :type feature: str
        """
        self._feature = feature

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListFeatureConfigsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
