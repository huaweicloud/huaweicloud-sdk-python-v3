# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecognizeInvoiceVerificationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'object',
        'x_request_id': 'str'
    }

    attribute_map = {
        'result': 'result',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, result=None, x_request_id=None):
        r"""RecognizeInvoiceVerificationResponse

        The model defined in huaweicloud sdk

        :param result: 调用成功时表示调用结果，详情参见[响应参数](https://support.huaweicloud.com/api-ocr/ocr_03_0134.html#ocr_03_0134__table266mcpsimp)。  调用失败时无此字段。 依据发票类型不同，返回参数不同。 - 增值税发票   含增值税专用发票、增值税普通发票、增值税普通发票（卷式）、增值税电子专用发票、增值税电子普通发票、增值税电子普通发票（通行费）、区块链电子发票。 - 机动车销售统一发票 - 二手车销售统一发票 - 航空运输电子客票行程单 - 铁路电子客票 
        :type result: object
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(RecognizeInvoiceVerificationResponse, self).__init__()

        self._result = None
        self._x_request_id = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def result(self):
        r"""Gets the result of this RecognizeInvoiceVerificationResponse.

        调用成功时表示调用结果，详情参见[响应参数](https://support.huaweicloud.com/api-ocr/ocr_03_0134.html#ocr_03_0134__table266mcpsimp)。  调用失败时无此字段。 依据发票类型不同，返回参数不同。 - 增值税发票   含增值税专用发票、增值税普通发票、增值税普通发票（卷式）、增值税电子专用发票、增值税电子普通发票、增值税电子普通发票（通行费）、区块链电子发票。 - 机动车销售统一发票 - 二手车销售统一发票 - 航空运输电子客票行程单 - 铁路电子客票 

        :return: The result of this RecognizeInvoiceVerificationResponse.
        :rtype: object
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this RecognizeInvoiceVerificationResponse.

        调用成功时表示调用结果，详情参见[响应参数](https://support.huaweicloud.com/api-ocr/ocr_03_0134.html#ocr_03_0134__table266mcpsimp)。  调用失败时无此字段。 依据发票类型不同，返回参数不同。 - 增值税发票   含增值税专用发票、增值税普通发票、增值税普通发票（卷式）、增值税电子专用发票、增值税电子普通发票、增值税电子普通发票（通行费）、区块链电子发票。 - 机动车销售统一发票 - 二手车销售统一发票 - 航空运输电子客票行程单 - 铁路电子客票 

        :param result: The result of this RecognizeInvoiceVerificationResponse.
        :type result: object
        """
        self._result = result

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this RecognizeInvoiceVerificationResponse.

        :return: The x_request_id of this RecognizeInvoiceVerificationResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this RecognizeInvoiceVerificationResponse.

        :param x_request_id: The x_request_id of this RecognizeInvoiceVerificationResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RecognizeInvoiceVerificationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
