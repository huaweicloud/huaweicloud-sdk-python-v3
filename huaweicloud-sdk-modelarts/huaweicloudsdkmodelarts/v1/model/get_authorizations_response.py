# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetAuthorizationsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'float',
        'auth': 'list[AuthorizationResponse]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'auth': 'auth'
    }

    def __init__(self, total_count=None, auth=None):
        r"""GetAuthorizationsResponse

        The model defined in huaweicloud sdk

        :param total_count: **参数解释**：授权信息总数。 **取值范围**：不涉及。
        :type total_count: float
        :param auth: **参数解释**：授权信息列表。
        :type auth: list[:class:`huaweicloudsdkmodelarts.v1.AuthorizationResponse`]
        """
        
        super().__init__()

        self._total_count = None
        self._auth = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if auth is not None:
            self.auth = auth

    @property
    def total_count(self):
        r"""Gets the total_count of this GetAuthorizationsResponse.

        **参数解释**：授权信息总数。 **取值范围**：不涉及。

        :return: The total_count of this GetAuthorizationsResponse.
        :rtype: float
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this GetAuthorizationsResponse.

        **参数解释**：授权信息总数。 **取值范围**：不涉及。

        :param total_count: The total_count of this GetAuthorizationsResponse.
        :type total_count: float
        """
        self._total_count = total_count

    @property
    def auth(self):
        r"""Gets the auth of this GetAuthorizationsResponse.

        **参数解释**：授权信息列表。

        :return: The auth of this GetAuthorizationsResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.AuthorizationResponse`]
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        r"""Sets the auth of this GetAuthorizationsResponse.

        **参数解释**：授权信息列表。

        :param auth: The auth of this GetAuthorizationsResponse.
        :type auth: list[:class:`huaweicloudsdkmodelarts.v1.AuthorizationResponse`]
        """
        self._auth = auth

    def to_dict(self):
        import warnings
        warnings.warn("GetAuthorizationsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, GetAuthorizationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
