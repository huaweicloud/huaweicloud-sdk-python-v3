# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SharedSparkUiInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'url': 'str',
        'expired_at': 'int'
    }

    attribute_map = {
        'url': 'url',
        'expired_at': 'expired_at'
    }

    def __init__(self, url=None, expired_at=None):
        r"""SharedSparkUiInfo

        The model defined in huaweicloud sdk

        :param url: **参数解释**：共享链接凭证。 **约束限制**：不涉及。 **取值范围**：共享URL格式，长度为1~1024个字符。 **默认取值**：不涉及。
        :type url: str
        :param expired_at: **参数解释**：过期时间时间戳，共享链接使用到该时间之后不可用，毫秒。 **约束限制**：毫秒时间戳。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type expired_at: int
        """
        
        

        self._url = None
        self._expired_at = None
        self.discriminator = None

        self.url = url
        self.expired_at = expired_at

    @property
    def url(self):
        r"""Gets the url of this SharedSparkUiInfo.

        **参数解释**：共享链接凭证。 **约束限制**：不涉及。 **取值范围**：共享URL格式，长度为1~1024个字符。 **默认取值**：不涉及。

        :return: The url of this SharedSparkUiInfo.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this SharedSparkUiInfo.

        **参数解释**：共享链接凭证。 **约束限制**：不涉及。 **取值范围**：共享URL格式，长度为1~1024个字符。 **默认取值**：不涉及。

        :param url: The url of this SharedSparkUiInfo.
        :type url: str
        """
        self._url = url

    @property
    def expired_at(self):
        r"""Gets the expired_at of this SharedSparkUiInfo.

        **参数解释**：过期时间时间戳，共享链接使用到该时间之后不可用，毫秒。 **约束限制**：毫秒时间戳。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The expired_at of this SharedSparkUiInfo.
        :rtype: int
        """
        return self._expired_at

    @expired_at.setter
    def expired_at(self, expired_at):
        r"""Sets the expired_at of this SharedSparkUiInfo.

        **参数解释**：过期时间时间戳，共享链接使用到该时间之后不可用，毫秒。 **约束限制**：毫秒时间戳。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param expired_at: The expired_at of this SharedSparkUiInfo.
        :type expired_at: int
        """
        self._expired_at = expired_at

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
        if not isinstance(other, SharedSparkUiInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
