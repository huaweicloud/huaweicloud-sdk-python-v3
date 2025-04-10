# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePostPaidVaultResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'orders': 'list[CbcOrderResult]',
        'ret_code': 'int',
        'err_text': 'str',
        'error_code': 'str'
    }

    attribute_map = {
        'orders': 'orders',
        'ret_code': 'retCode',
        'err_text': 'errText',
        'error_code': 'error_code'
    }

    def __init__(self, orders=None, ret_code=None, err_text=None, error_code=None):
        r"""CreatePostPaidVaultResponse

        The model defined in huaweicloud sdk

        :param orders: 订单详情
        :type orders: list[:class:`huaweicloudsdkcbr.v1.CbcOrderResult`]
        :param ret_code: 创建结果代码 0：成功
        :type ret_code: int
        :param err_text: 创建结果信息
        :type err_text: str
        :param error_code: 操作错误码 0：无错误
        :type error_code: str
        """
        
        super(CreatePostPaidVaultResponse, self).__init__()

        self._orders = None
        self._ret_code = None
        self._err_text = None
        self._error_code = None
        self.discriminator = None

        if orders is not None:
            self.orders = orders
        if ret_code is not None:
            self.ret_code = ret_code
        if err_text is not None:
            self.err_text = err_text
        if error_code is not None:
            self.error_code = error_code

    @property
    def orders(self):
        r"""Gets the orders of this CreatePostPaidVaultResponse.

        订单详情

        :return: The orders of this CreatePostPaidVaultResponse.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.CbcOrderResult`]
        """
        return self._orders

    @orders.setter
    def orders(self, orders):
        r"""Sets the orders of this CreatePostPaidVaultResponse.

        订单详情

        :param orders: The orders of this CreatePostPaidVaultResponse.
        :type orders: list[:class:`huaweicloudsdkcbr.v1.CbcOrderResult`]
        """
        self._orders = orders

    @property
    def ret_code(self):
        r"""Gets the ret_code of this CreatePostPaidVaultResponse.

        创建结果代码 0：成功

        :return: The ret_code of this CreatePostPaidVaultResponse.
        :rtype: int
        """
        return self._ret_code

    @ret_code.setter
    def ret_code(self, ret_code):
        r"""Sets the ret_code of this CreatePostPaidVaultResponse.

        创建结果代码 0：成功

        :param ret_code: The ret_code of this CreatePostPaidVaultResponse.
        :type ret_code: int
        """
        self._ret_code = ret_code

    @property
    def err_text(self):
        r"""Gets the err_text of this CreatePostPaidVaultResponse.

        创建结果信息

        :return: The err_text of this CreatePostPaidVaultResponse.
        :rtype: str
        """
        return self._err_text

    @err_text.setter
    def err_text(self, err_text):
        r"""Sets the err_text of this CreatePostPaidVaultResponse.

        创建结果信息

        :param err_text: The err_text of this CreatePostPaidVaultResponse.
        :type err_text: str
        """
        self._err_text = err_text

    @property
    def error_code(self):
        r"""Gets the error_code of this CreatePostPaidVaultResponse.

        操作错误码 0：无错误

        :return: The error_code of this CreatePostPaidVaultResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this CreatePostPaidVaultResponse.

        操作错误码 0：无错误

        :param error_code: The error_code of this CreatePostPaidVaultResponse.
        :type error_code: str
        """
        self._error_code = error_code

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
        if not isinstance(other, CreatePostPaidVaultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
