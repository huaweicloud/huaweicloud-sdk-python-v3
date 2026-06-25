# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InlineResponse200PrivateKeys:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key_id': 'str',
        'timestamp': 'datetime'
    }

    attribute_map = {
        'key_id': 'key_id',
        'timestamp': 'timestamp'
    }

    def __init__(self, key_id=None, timestamp=None):
        r"""InlineResponse200PrivateKeys

        The model defined in huaweicloud sdk

        :param key_id: **参数解释**： 解密 SAML 断言私钥的 ID。  **取值范围**： 不涉及。
        :type key_id: str
        :param timestamp: **参数解释**： 上传解密 SAML 断言私钥的时间，符合 ISO 8601 格式。  **取值范围**： 不涉及。
        :type timestamp: datetime
        """
        
        

        self._key_id = None
        self._timestamp = None
        self.discriminator = None

        self.key_id = key_id
        self.timestamp = timestamp

    @property
    def key_id(self):
        r"""Gets the key_id of this InlineResponse200PrivateKeys.

        **参数解释**： 解密 SAML 断言私钥的 ID。  **取值范围**： 不涉及。

        :return: The key_id of this InlineResponse200PrivateKeys.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        r"""Sets the key_id of this InlineResponse200PrivateKeys.

        **参数解释**： 解密 SAML 断言私钥的 ID。  **取值范围**： 不涉及。

        :param key_id: The key_id of this InlineResponse200PrivateKeys.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def timestamp(self):
        r"""Gets the timestamp of this InlineResponse200PrivateKeys.

        **参数解释**： 上传解密 SAML 断言私钥的时间，符合 ISO 8601 格式。  **取值范围**： 不涉及。

        :return: The timestamp of this InlineResponse200PrivateKeys.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this InlineResponse200PrivateKeys.

        **参数解释**： 上传解密 SAML 断言私钥的时间，符合 ISO 8601 格式。  **取值范围**： 不涉及。

        :param timestamp: The timestamp of this InlineResponse200PrivateKeys.
        :type timestamp: datetime
        """
        self._timestamp = timestamp

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
        if not isinstance(other, InlineResponse200PrivateKeys):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
