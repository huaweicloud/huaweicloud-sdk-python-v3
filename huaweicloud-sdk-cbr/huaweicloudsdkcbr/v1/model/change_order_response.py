# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeOrderResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'order_id': 'str',
        'ret_code': 'float',
        'ret_msg': 'str'
    }

    attribute_map = {
        'order_id': 'orderId',
        'ret_code': 'retCode',
        'ret_msg': 'retMsg'
    }

    def __init__(self, order_id=None, ret_code=None, ret_msg=None):
        r"""ChangeOrderResponse

        The model defined in huaweicloud sdk

        :param order_id: 订单ID
        :type order_id: str
        :param ret_code: 变更状态码
        :type ret_code: float
        :param ret_msg: 变更信息
        :type ret_msg: str
        """
        
        super(ChangeOrderResponse, self).__init__()

        self._order_id = None
        self._ret_code = None
        self._ret_msg = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        if ret_code is not None:
            self.ret_code = ret_code
        if ret_msg is not None:
            self.ret_msg = ret_msg

    @property
    def order_id(self):
        r"""Gets the order_id of this ChangeOrderResponse.

        订单ID

        :return: The order_id of this ChangeOrderResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this ChangeOrderResponse.

        订单ID

        :param order_id: The order_id of this ChangeOrderResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def ret_code(self):
        r"""Gets the ret_code of this ChangeOrderResponse.

        变更状态码

        :return: The ret_code of this ChangeOrderResponse.
        :rtype: float
        """
        return self._ret_code

    @ret_code.setter
    def ret_code(self, ret_code):
        r"""Sets the ret_code of this ChangeOrderResponse.

        变更状态码

        :param ret_code: The ret_code of this ChangeOrderResponse.
        :type ret_code: float
        """
        self._ret_code = ret_code

    @property
    def ret_msg(self):
        r"""Gets the ret_msg of this ChangeOrderResponse.

        变更信息

        :return: The ret_msg of this ChangeOrderResponse.
        :rtype: str
        """
        return self._ret_msg

    @ret_msg.setter
    def ret_msg(self, ret_msg):
        r"""Sets the ret_msg of this ChangeOrderResponse.

        变更信息

        :param ret_msg: The ret_msg of this ChangeOrderResponse.
        :type ret_msg: str
        """
        self._ret_msg = ret_msg

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
        if not isinstance(other, ChangeOrderResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
