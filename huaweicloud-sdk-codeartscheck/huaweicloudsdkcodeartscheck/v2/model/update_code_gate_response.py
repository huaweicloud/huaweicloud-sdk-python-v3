# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCodeGateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'str',
        'http_status': 'str',
        'status': 'str'
    }

    attribute_map = {
        'result': 'result',
        'http_status': 'httpStatus',
        'status': 'status'
    }

    def __init__(self, result=None, http_status=None, status=None):
        r"""UpdateCodeGateResponse

        The model defined in huaweicloud sdk

        :param result: **参数解释：** 更新成功时返回\&quot;更新门禁配置成功\&quot;。 **取值范围：** 不涉及。
        :type result: str
        :param http_status: **参数解释：** HTTP响应状态。 **取值范围：** - OK：请求已成功处理，服务器返回了请求的资源或操作结果。 - ACCEPTED：请求已被服务器接受，但处理尚未完成（通常用于异步操作）。 - INTERNAL_SERVER_ERROR：接口内部异常。 - BAD_REQUEST：参数校验异常。
        :type http_status: str
        :param status: **参数解释：** 接口响应状态。 **取值范围：** - success：接口响应成功。 - error：接口响应失败。
        :type status: str
        """
        
        super().__init__()

        self._result = None
        self._http_status = None
        self._status = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if http_status is not None:
            self.http_status = http_status
        if status is not None:
            self.status = status

    @property
    def result(self):
        r"""Gets the result of this UpdateCodeGateResponse.

        **参数解释：** 更新成功时返回\"更新门禁配置成功\"。 **取值范围：** 不涉及。

        :return: The result of this UpdateCodeGateResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this UpdateCodeGateResponse.

        **参数解释：** 更新成功时返回\"更新门禁配置成功\"。 **取值范围：** 不涉及。

        :param result: The result of this UpdateCodeGateResponse.
        :type result: str
        """
        self._result = result

    @property
    def http_status(self):
        r"""Gets the http_status of this UpdateCodeGateResponse.

        **参数解释：** HTTP响应状态。 **取值范围：** - OK：请求已成功处理，服务器返回了请求的资源或操作结果。 - ACCEPTED：请求已被服务器接受，但处理尚未完成（通常用于异步操作）。 - INTERNAL_SERVER_ERROR：接口内部异常。 - BAD_REQUEST：参数校验异常。

        :return: The http_status of this UpdateCodeGateResponse.
        :rtype: str
        """
        return self._http_status

    @http_status.setter
    def http_status(self, http_status):
        r"""Sets the http_status of this UpdateCodeGateResponse.

        **参数解释：** HTTP响应状态。 **取值范围：** - OK：请求已成功处理，服务器返回了请求的资源或操作结果。 - ACCEPTED：请求已被服务器接受，但处理尚未完成（通常用于异步操作）。 - INTERNAL_SERVER_ERROR：接口内部异常。 - BAD_REQUEST：参数校验异常。

        :param http_status: The http_status of this UpdateCodeGateResponse.
        :type http_status: str
        """
        self._http_status = http_status

    @property
    def status(self):
        r"""Gets the status of this UpdateCodeGateResponse.

        **参数解释：** 接口响应状态。 **取值范围：** - success：接口响应成功。 - error：接口响应失败。

        :return: The status of this UpdateCodeGateResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateCodeGateResponse.

        **参数解释：** 接口响应状态。 **取值范围：** - success：接口响应成功。 - error：接口响应失败。

        :param status: The status of this UpdateCodeGateResponse.
        :type status: str
        """
        self._status = status

    def to_dict(self):
        import warnings
        warnings.warn("UpdateCodeGateResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdateCodeGateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
