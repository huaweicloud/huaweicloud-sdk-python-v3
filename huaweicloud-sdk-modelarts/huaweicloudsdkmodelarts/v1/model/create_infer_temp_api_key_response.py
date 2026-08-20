# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInferTempApiKeyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_key': 'str',
        'expire_time': 'int',
        'create_time': 'int'
    }

    attribute_map = {
        'api_key': 'api_key',
        'expire_time': 'expire_time',
        'create_time': 'create_time'
    }

    def __init__(self, api_key=None, expire_time=None, create_time=None):
        r"""CreateInferTempApiKeyResponse

        The model defined in huaweicloud sdk

        :param api_key: **参数解释：** 临时apikey。 **取值范围：**不涉及。
        :type api_key: str
        :param expire_time: **参数解释：** 临时apikey超时时间。 **取值范围：**不涉及。
        :type expire_time: int
        :param create_time: **参数解释：** 临时apikey创建时间。 **取值范围：**不涉及。
        :type create_time: int
        """
        
        super().__init__()

        self._api_key = None
        self._expire_time = None
        self._create_time = None
        self.discriminator = None

        if api_key is not None:
            self.api_key = api_key
        if expire_time is not None:
            self.expire_time = expire_time
        if create_time is not None:
            self.create_time = create_time

    @property
    def api_key(self):
        r"""Gets the api_key of this CreateInferTempApiKeyResponse.

        **参数解释：** 临时apikey。 **取值范围：**不涉及。

        :return: The api_key of this CreateInferTempApiKeyResponse.
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        r"""Sets the api_key of this CreateInferTempApiKeyResponse.

        **参数解释：** 临时apikey。 **取值范围：**不涉及。

        :param api_key: The api_key of this CreateInferTempApiKeyResponse.
        :type api_key: str
        """
        self._api_key = api_key

    @property
    def expire_time(self):
        r"""Gets the expire_time of this CreateInferTempApiKeyResponse.

        **参数解释：** 临时apikey超时时间。 **取值范围：**不涉及。

        :return: The expire_time of this CreateInferTempApiKeyResponse.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this CreateInferTempApiKeyResponse.

        **参数解释：** 临时apikey超时时间。 **取值范围：**不涉及。

        :param expire_time: The expire_time of this CreateInferTempApiKeyResponse.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def create_time(self):
        r"""Gets the create_time of this CreateInferTempApiKeyResponse.

        **参数解释：** 临时apikey创建时间。 **取值范围：**不涉及。

        :return: The create_time of this CreateInferTempApiKeyResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this CreateInferTempApiKeyResponse.

        **参数解释：** 临时apikey创建时间。 **取值范围：**不涉及。

        :param create_time: The create_time of this CreateInferTempApiKeyResponse.
        :type create_time: int
        """
        self._create_time = create_time

    def to_dict(self):
        import warnings
        warnings.warn("CreateInferTempApiKeyResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateInferTempApiKeyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
