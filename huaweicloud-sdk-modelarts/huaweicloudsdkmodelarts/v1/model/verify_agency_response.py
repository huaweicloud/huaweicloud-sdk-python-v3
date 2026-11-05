# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VerifyAgencyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_authorized': 'bool',
        'agency_name': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'is_authorized': 'is_authorized',
        'agency_name': 'agency_name',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, is_authorized=None, agency_name=None, x_request_id=None):
        r"""VerifyAgencyResponse

        The model defined in huaweicloud sdk

        :param is_authorized: 是否有权使用该委托，true表示有权，false表示无权
        :type is_authorized: bool
        :param agency_name: **参数解释**： 授权内容。 - 当授权类型是委托，该字段为委托名称。 - 当授权类型是访问密钥，该字段为访问密钥ID（AK）。  **取值范围**：长度限制64个字符。
        :type agency_name: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._is_authorized = None
        self._agency_name = None
        self._x_request_id = None
        self.discriminator = None

        if is_authorized is not None:
            self.is_authorized = is_authorized
        if agency_name is not None:
            self.agency_name = agency_name
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def is_authorized(self):
        r"""Gets the is_authorized of this VerifyAgencyResponse.

        是否有权使用该委托，true表示有权，false表示无权

        :return: The is_authorized of this VerifyAgencyResponse.
        :rtype: bool
        """
        return self._is_authorized

    @is_authorized.setter
    def is_authorized(self, is_authorized):
        r"""Sets the is_authorized of this VerifyAgencyResponse.

        是否有权使用该委托，true表示有权，false表示无权

        :param is_authorized: The is_authorized of this VerifyAgencyResponse.
        :type is_authorized: bool
        """
        self._is_authorized = is_authorized

    @property
    def agency_name(self):
        r"""Gets the agency_name of this VerifyAgencyResponse.

        **参数解释**： 授权内容。 - 当授权类型是委托，该字段为委托名称。 - 当授权类型是访问密钥，该字段为访问密钥ID（AK）。  **取值范围**：长度限制64个字符。

        :return: The agency_name of this VerifyAgencyResponse.
        :rtype: str
        """
        return self._agency_name

    @agency_name.setter
    def agency_name(self, agency_name):
        r"""Sets the agency_name of this VerifyAgencyResponse.

        **参数解释**： 授权内容。 - 当授权类型是委托，该字段为委托名称。 - 当授权类型是访问密钥，该字段为访问密钥ID（AK）。  **取值范围**：长度限制64个字符。

        :param agency_name: The agency_name of this VerifyAgencyResponse.
        :type agency_name: str
        """
        self._agency_name = agency_name

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this VerifyAgencyResponse.

        :return: The x_request_id of this VerifyAgencyResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this VerifyAgencyResponse.

        :param x_request_id: The x_request_id of this VerifyAgencyResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("VerifyAgencyResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, VerifyAgencyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
