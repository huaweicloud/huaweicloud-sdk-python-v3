# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAuthModeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'mode': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'mode': 'mode'
    }

    def __init__(self, domain_id=None, mode=None):
        r"""UpdateAuthModeResponse

        The model defined in huaweicloud sdk

        :param domain_id: **参数解释**：账号domainId。 **取值范围**：不涉及。
        :type domain_id: str
        :param mode: **参数解释**：授权模式。 **取值范围**： - strict：严格模式。 - loose：非严格模式。
        :type mode: str
        """
        
        super().__init__()

        self._domain_id = None
        self._mode = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if mode is not None:
            self.mode = mode

    @property
    def domain_id(self):
        r"""Gets the domain_id of this UpdateAuthModeResponse.

        **参数解释**：账号domainId。 **取值范围**：不涉及。

        :return: The domain_id of this UpdateAuthModeResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this UpdateAuthModeResponse.

        **参数解释**：账号domainId。 **取值范围**：不涉及。

        :param domain_id: The domain_id of this UpdateAuthModeResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def mode(self):
        r"""Gets the mode of this UpdateAuthModeResponse.

        **参数解释**：授权模式。 **取值范围**： - strict：严格模式。 - loose：非严格模式。

        :return: The mode of this UpdateAuthModeResponse.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this UpdateAuthModeResponse.

        **参数解释**：授权模式。 **取值范围**： - strict：严格模式。 - loose：非严格模式。

        :param mode: The mode of this UpdateAuthModeResponse.
        :type mode: str
        """
        self._mode = mode

    def to_dict(self):
        import warnings
        warnings.warn("UpdateAuthModeResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdateAuthModeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
