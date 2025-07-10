# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPolicyGeoipMapRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'lang': 'str'
    }

    attribute_map = {
        'lang': 'lang'
    }

    def __init__(self, lang=None):
        r"""ShowPolicyGeoipMapRequest

        The model defined in huaweicloud sdk

        :param lang: **参数解释：** 语言的类型 - cn代表中文 - en代表英文  **约束限制：** 不涉及 **取值范围：** - cn - en  **默认取值：** - cn
        :type lang: str
        """
        
        

        self._lang = None
        self.discriminator = None

        if lang is not None:
            self.lang = lang

    @property
    def lang(self):
        r"""Gets the lang of this ShowPolicyGeoipMapRequest.

        **参数解释：** 语言的类型 - cn代表中文 - en代表英文  **约束限制：** 不涉及 **取值范围：** - cn - en  **默认取值：** - cn

        :return: The lang of this ShowPolicyGeoipMapRequest.
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        r"""Sets the lang of this ShowPolicyGeoipMapRequest.

        **参数解释：** 语言的类型 - cn代表中文 - en代表英文  **约束限制：** 不涉及 **取值范围：** - cn - en  **默认取值：** - cn

        :param lang: The lang of this ShowPolicyGeoipMapRequest.
        :type lang: str
        """
        self._lang = lang

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
        if not isinstance(other, ShowPolicyGeoipMapRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
