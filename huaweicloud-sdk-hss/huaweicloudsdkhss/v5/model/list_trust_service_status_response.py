# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTrustServiceStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trusted_services_enabled': 'bool',
        'x_request_id': 'str'
    }

    attribute_map = {
        'trusted_services_enabled': 'trusted_services_enabled',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, trusted_services_enabled=None, x_request_id=None):
        r"""ListTrustServiceStatusResponse

        The model defined in huaweicloud sdk

        :param trusted_services_enabled: **参数解释**: 可信服务状态 **取值范围**: - true：是。 - false：否。 
        :type trusted_services_enabled: bool
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._trusted_services_enabled = None
        self._x_request_id = None
        self.discriminator = None

        if trusted_services_enabled is not None:
            self.trusted_services_enabled = trusted_services_enabled
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def trusted_services_enabled(self):
        r"""Gets the trusted_services_enabled of this ListTrustServiceStatusResponse.

        **参数解释**: 可信服务状态 **取值范围**: - true：是。 - false：否。 

        :return: The trusted_services_enabled of this ListTrustServiceStatusResponse.
        :rtype: bool
        """
        return self._trusted_services_enabled

    @trusted_services_enabled.setter
    def trusted_services_enabled(self, trusted_services_enabled):
        r"""Sets the trusted_services_enabled of this ListTrustServiceStatusResponse.

        **参数解释**: 可信服务状态 **取值范围**: - true：是。 - false：否。 

        :param trusted_services_enabled: The trusted_services_enabled of this ListTrustServiceStatusResponse.
        :type trusted_services_enabled: bool
        """
        self._trusted_services_enabled = trusted_services_enabled

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListTrustServiceStatusResponse.

        :return: The x_request_id of this ListTrustServiceStatusResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListTrustServiceStatusResponse.

        :param x_request_id: The x_request_id of this ListTrustServiceStatusResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ListTrustServiceStatusResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListTrustServiceStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
