# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateKeyStoreRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keystore_id': 'str',
        'body': 'UpdateKeyStoreRequestBody'
    }

    attribute_map = {
        'keystore_id': 'keystore_id',
        'body': 'body'
    }

    def __init__(self, keystore_id=None, body=None):
        r"""UpdateKeyStoreRequest

        The model defined in huaweicloud sdk

        :param keystore_id: **参数解释：** 密钥库ID **约束限制：** 满足正则表达式\&quot;[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$\&quot; **取值范围：** 不涉及 **默认取值：** 不涉及
        :type keystore_id: str
        :param body: Body of the UpdateKeyStoreRequest
        :type body: :class:`huaweicloudsdkkms.v2.UpdateKeyStoreRequestBody`
        """
        
        

        self._keystore_id = None
        self._body = None
        self.discriminator = None

        self.keystore_id = keystore_id
        if body is not None:
            self.body = body

    @property
    def keystore_id(self):
        r"""Gets the keystore_id of this UpdateKeyStoreRequest.

        **参数解释：** 密钥库ID **约束限制：** 满足正则表达式\"[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$\" **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The keystore_id of this UpdateKeyStoreRequest.
        :rtype: str
        """
        return self._keystore_id

    @keystore_id.setter
    def keystore_id(self, keystore_id):
        r"""Sets the keystore_id of this UpdateKeyStoreRequest.

        **参数解释：** 密钥库ID **约束限制：** 满足正则表达式\"[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}$\" **取值范围：** 不涉及 **默认取值：** 不涉及

        :param keystore_id: The keystore_id of this UpdateKeyStoreRequest.
        :type keystore_id: str
        """
        self._keystore_id = keystore_id

    @property
    def body(self):
        r"""Gets the body of this UpdateKeyStoreRequest.

        :return: The body of this UpdateKeyStoreRequest.
        :rtype: :class:`huaweicloudsdkkms.v2.UpdateKeyStoreRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateKeyStoreRequest.

        :param body: The body of this UpdateKeyStoreRequest.
        :type body: :class:`huaweicloudsdkkms.v2.UpdateKeyStoreRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateKeyStoreRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
