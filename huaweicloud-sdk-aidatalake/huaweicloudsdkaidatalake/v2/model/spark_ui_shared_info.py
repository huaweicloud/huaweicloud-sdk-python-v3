# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SparkUiSharedInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'shared_url': 'str',
        'expired_at': 'int'
    }

    attribute_map = {
        'shared_url': 'shared_url',
        'expired_at': 'expired_at'
    }

    def __init__(self, shared_url=None, expired_at=None):
        r"""SparkUiSharedInfo

        The model defined in huaweicloud sdk

        :param shared_url: **参数解释**：共享链接凭证。 **约束限制**：不涉及。 **取值范围**：共享URL格式，长度为1~1024个字符。 **默认取值**：不涉及。
        :type shared_url: str
        :param expired_at: **参数解释**：过期时间时间戳，共享链接使用到该时间之后不可用，毫秒。 **约束限制**：毫秒时间戳。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type expired_at: int
        """
        
        

        self._shared_url = None
        self._expired_at = None
        self.discriminator = None

        self.shared_url = shared_url
        self.expired_at = expired_at

    @property
    def shared_url(self):
        r"""Gets the shared_url of this SparkUiSharedInfo.

        **参数解释**：共享链接凭证。 **约束限制**：不涉及。 **取值范围**：共享URL格式，长度为1~1024个字符。 **默认取值**：不涉及。

        :return: The shared_url of this SparkUiSharedInfo.
        :rtype: str
        """
        return self._shared_url

    @shared_url.setter
    def shared_url(self, shared_url):
        r"""Sets the shared_url of this SparkUiSharedInfo.

        **参数解释**：共享链接凭证。 **约束限制**：不涉及。 **取值范围**：共享URL格式，长度为1~1024个字符。 **默认取值**：不涉及。

        :param shared_url: The shared_url of this SparkUiSharedInfo.
        :type shared_url: str
        """
        self._shared_url = shared_url

    @property
    def expired_at(self):
        r"""Gets the expired_at of this SparkUiSharedInfo.

        **参数解释**：过期时间时间戳，共享链接使用到该时间之后不可用，毫秒。 **约束限制**：毫秒时间戳。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The expired_at of this SparkUiSharedInfo.
        :rtype: int
        """
        return self._expired_at

    @expired_at.setter
    def expired_at(self, expired_at):
        r"""Sets the expired_at of this SparkUiSharedInfo.

        **参数解释**：过期时间时间戳，共享链接使用到该时间之后不可用，毫秒。 **约束限制**：毫秒时间戳。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param expired_at: The expired_at of this SparkUiSharedInfo.
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
        if not isinstance(other, SparkUiSharedInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
