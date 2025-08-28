# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoadbalancerFeature:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'feature': 'str',
        'type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'feature': 'feature',
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, feature=None, type=None, value=None):
        r"""LoadbalancerFeature

        The model defined in huaweicloud sdk

        :param feature: **参数解释**：特性名称。  **取值范围**：不涉及
        :type feature: str
        :param type: **参数解释**：特性值(value字段)的类型，如：INT，表示整型。  **取值范围**：不涉及
        :type type: str
        :param value: **参数解释**：特性值。如开关类型的特性取值true/false，表示特性开启关闭；配额类型的特性取值整数，表示限制配额。  **取值范围**：不涉及
        :type value: str
        """
        
        

        self._feature = None
        self._type = None
        self._value = None
        self.discriminator = None

        self.feature = feature
        self.type = type
        self.value = value

    @property
    def feature(self):
        r"""Gets the feature of this LoadbalancerFeature.

        **参数解释**：特性名称。  **取值范围**：不涉及

        :return: The feature of this LoadbalancerFeature.
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        r"""Sets the feature of this LoadbalancerFeature.

        **参数解释**：特性名称。  **取值范围**：不涉及

        :param feature: The feature of this LoadbalancerFeature.
        :type feature: str
        """
        self._feature = feature

    @property
    def type(self):
        r"""Gets the type of this LoadbalancerFeature.

        **参数解释**：特性值(value字段)的类型，如：INT，表示整型。  **取值范围**：不涉及

        :return: The type of this LoadbalancerFeature.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this LoadbalancerFeature.

        **参数解释**：特性值(value字段)的类型，如：INT，表示整型。  **取值范围**：不涉及

        :param type: The type of this LoadbalancerFeature.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        r"""Gets the value of this LoadbalancerFeature.

        **参数解释**：特性值。如开关类型的特性取值true/false，表示特性开启关闭；配额类型的特性取值整数，表示限制配额。  **取值范围**：不涉及

        :return: The value of this LoadbalancerFeature.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this LoadbalancerFeature.

        **参数解释**：特性值。如开关类型的特性取值true/false，表示特性开启关闭；配额类型的特性取值整数，表示限制配额。  **取值范围**：不涉及

        :param value: The value of this LoadbalancerFeature.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, LoadbalancerFeature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
