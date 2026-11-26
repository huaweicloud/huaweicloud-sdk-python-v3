# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VerifyDomainOwnerResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'bool',
        'status': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'result': 'result',
        'status': 'status',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, result=None, status=None, x_request_id=None):
        r"""VerifyDomainOwnerResponse

        The model defined in huaweicloud sdk

        :param result: 验证是否通过，true：通过，false：不通过。
        :type result: bool
        :param status: **参数解释：** 域名校验状态，表示当前账号下是否存在该域名 **约束限制：** 不涉及 **取值范围：** - DomainExist: 该域名已存在 - DomainNotExist: 该域名不存在  **默认取值：** 不涉及
        :type status: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._result = None
        self._status = None
        self._x_request_id = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if status is not None:
            self.status = status
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def result(self):
        r"""Gets the result of this VerifyDomainOwnerResponse.

        验证是否通过，true：通过，false：不通过。

        :return: The result of this VerifyDomainOwnerResponse.
        :rtype: bool
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this VerifyDomainOwnerResponse.

        验证是否通过，true：通过，false：不通过。

        :param result: The result of this VerifyDomainOwnerResponse.
        :type result: bool
        """
        self._result = result

    @property
    def status(self):
        r"""Gets the status of this VerifyDomainOwnerResponse.

        **参数解释：** 域名校验状态，表示当前账号下是否存在该域名 **约束限制：** 不涉及 **取值范围：** - DomainExist: 该域名已存在 - DomainNotExist: 该域名不存在  **默认取值：** 不涉及

        :return: The status of this VerifyDomainOwnerResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this VerifyDomainOwnerResponse.

        **参数解释：** 域名校验状态，表示当前账号下是否存在该域名 **约束限制：** 不涉及 **取值范围：** - DomainExist: 该域名已存在 - DomainNotExist: 该域名不存在  **默认取值：** 不涉及

        :param status: The status of this VerifyDomainOwnerResponse.
        :type status: str
        """
        self._status = status

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this VerifyDomainOwnerResponse.

        :return: The x_request_id of this VerifyDomainOwnerResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this VerifyDomainOwnerResponse.

        :param x_request_id: The x_request_id of this VerifyDomainOwnerResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("VerifyDomainOwnerResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, VerifyDomainOwnerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
