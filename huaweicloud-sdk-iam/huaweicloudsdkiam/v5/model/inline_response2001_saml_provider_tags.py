# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InlineResponse2001SamlProviderTags:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tag_key': 'str',
        'tag_value': 'str'
    }

    attribute_map = {
        'tag_key': 'tag_key',
        'tag_value': 'tag_value'
    }

    def __init__(self, tag_key=None, tag_value=None):
        r"""InlineResponse2001SamlProviderTags

        The model defined in huaweicloud sdk

        :param tag_key: **参数解释**： 标签键。  **取值范围**： 字符串长度在 1 到 64 之间，可以包含任意语种字母、数字、空格以及\&quot;_\&quot;、\&quot;.\&quot;、\&quot;:\&quot;、\&quot;&#x3D;\&quot;、\&quot;+\&quot;、\&quot;-\&quot;、\&quot;@\&quot;符号；首尾不能包含空格，且不能以\&quot;_sys_\&quot;开头。
        :type tag_key: str
        :param tag_value: **参数解释**： 标签值。  **取值范围**： 字符串长度在 0 到 128 之间，可以包含任意语种字母、数字、空格以及\&quot;_\&quot;、\&quot;.\&quot;、\&quot;:\&quot;、\&quot;/\&quot;、\&quot;&#x3D;\&quot;、\&quot;+\&quot;、\&quot;-\&quot;、\&quot;@\&quot;符号，可以为空字符串。
        :type tag_value: str
        """
        
        

        self._tag_key = None
        self._tag_value = None
        self.discriminator = None

        self.tag_key = tag_key
        self.tag_value = tag_value

    @property
    def tag_key(self):
        r"""Gets the tag_key of this InlineResponse2001SamlProviderTags.

        **参数解释**： 标签键。  **取值范围**： 字符串长度在 1 到 64 之间，可以包含任意语种字母、数字、空格以及\"_\"、\".\"、\":\"、\"=\"、\"+\"、\"-\"、\"@\"符号；首尾不能包含空格，且不能以\"_sys_\"开头。

        :return: The tag_key of this InlineResponse2001SamlProviderTags.
        :rtype: str
        """
        return self._tag_key

    @tag_key.setter
    def tag_key(self, tag_key):
        r"""Sets the tag_key of this InlineResponse2001SamlProviderTags.

        **参数解释**： 标签键。  **取值范围**： 字符串长度在 1 到 64 之间，可以包含任意语种字母、数字、空格以及\"_\"、\".\"、\":\"、\"=\"、\"+\"、\"-\"、\"@\"符号；首尾不能包含空格，且不能以\"_sys_\"开头。

        :param tag_key: The tag_key of this InlineResponse2001SamlProviderTags.
        :type tag_key: str
        """
        self._tag_key = tag_key

    @property
    def tag_value(self):
        r"""Gets the tag_value of this InlineResponse2001SamlProviderTags.

        **参数解释**： 标签值。  **取值范围**： 字符串长度在 0 到 128 之间，可以包含任意语种字母、数字、空格以及\"_\"、\".\"、\":\"、\"/\"、\"=\"、\"+\"、\"-\"、\"@\"符号，可以为空字符串。

        :return: The tag_value of this InlineResponse2001SamlProviderTags.
        :rtype: str
        """
        return self._tag_value

    @tag_value.setter
    def tag_value(self, tag_value):
        r"""Sets the tag_value of this InlineResponse2001SamlProviderTags.

        **参数解释**： 标签值。  **取值范围**： 字符串长度在 0 到 128 之间，可以包含任意语种字母、数字、空格以及\"_\"、\".\"、\":\"、\"/\"、\"=\"、\"+\"、\"-\"、\"@\"符号，可以为空字符串。

        :param tag_value: The tag_value of this InlineResponse2001SamlProviderTags.
        :type tag_value: str
        """
        self._tag_value = tag_value

    def to_dict(self):
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
        if not isinstance(other, InlineResponse2001SamlProviderTags):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
