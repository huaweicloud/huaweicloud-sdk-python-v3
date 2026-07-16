# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiKeyFailureResponse:

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
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, key_id=None, error_code=None, error_msg=None):
        r"""ApiKeyFailureResponse

        The model defined in huaweicloud sdk

        :param key_id: **参数解释：** api-key的ID，在[创建API_KEY](CreateInferApiKey.xml)时即可在返回体中获取，也可通过[查询api-keys列表](ListInferApiKeys.xml)获取当前用户拥有的api-key，其中id字段即为api-key的ID。 **取值范围：** UUID格式。
        :type key_id: str
        :param error_code: **参数解释：** ModelArts错误码。 **取值范围：** 不涉及。
        :type error_code: str
        :param error_msg: **参数解释：** 具体错误信息。 **取值范围：** 不涉及。
        :type error_msg: str
        """
        
        

        self._key_id = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        self.key_id = key_id
        self.error_code = error_code
        self.error_msg = error_msg

    @property
    def key_id(self):
        r"""Gets the key_id of this ApiKeyFailureResponse.

        **参数解释：** api-key的ID，在[创建API_KEY](CreateInferApiKey.xml)时即可在返回体中获取，也可通过[查询api-keys列表](ListInferApiKeys.xml)获取当前用户拥有的api-key，其中id字段即为api-key的ID。 **取值范围：** UUID格式。

        :return: The key_id of this ApiKeyFailureResponse.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        r"""Sets the key_id of this ApiKeyFailureResponse.

        **参数解释：** api-key的ID，在[创建API_KEY](CreateInferApiKey.xml)时即可在返回体中获取，也可通过[查询api-keys列表](ListInferApiKeys.xml)获取当前用户拥有的api-key，其中id字段即为api-key的ID。 **取值范围：** UUID格式。

        :param key_id: The key_id of this ApiKeyFailureResponse.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def error_code(self):
        r"""Gets the error_code of this ApiKeyFailureResponse.

        **参数解释：** ModelArts错误码。 **取值范围：** 不涉及。

        :return: The error_code of this ApiKeyFailureResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ApiKeyFailureResponse.

        **参数解释：** ModelArts错误码。 **取值范围：** 不涉及。

        :param error_code: The error_code of this ApiKeyFailureResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this ApiKeyFailureResponse.

        **参数解释：** 具体错误信息。 **取值范围：** 不涉及。

        :return: The error_msg of this ApiKeyFailureResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this ApiKeyFailureResponse.

        **参数解释：** 具体错误信息。 **取值范围：** 不涉及。

        :param error_msg: The error_msg of this ApiKeyFailureResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, ApiKeyFailureResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
