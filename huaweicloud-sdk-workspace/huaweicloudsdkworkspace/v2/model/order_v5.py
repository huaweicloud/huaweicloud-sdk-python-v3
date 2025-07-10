# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrderV5:

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
        'order_status': 'int',
        'result': 'str',
        'result_code': 'str',
        'result_msg': 'str'
    }

    attribute_map = {
        'order_id': 'order_id',
        'order_status': 'order_status',
        'result': 'result',
        'result_code': 'result_code',
        'result_msg': 'result_msg'
    }

    def __init__(self, order_id=None, order_status=None, result=None, result_code=None, result_msg=None):
        r"""OrderV5

        The model defined in huaweicloud sdk

        :param order_id: 订单id。
        :type order_id: str
        :param order_status: 订单状态:0:初始化; 1:待审核; 2:待退款; 3:处理中; 4:已取消; 5:已完成; 6:待支付; 7:补偿中; 8:待审批; 9:待确认; 10:待发货; 11:待收货; 12:待上门取货; 13:换新中; 14:待商家收货。
        :type order_status: int
        :param result: 结果，SUCCESS:成功； FAIL：失败。
        :type result: str
        :param result_code: result&#x3D;FAIL时，必填，表示该订单失败原因。
        :type result_code: str
        :param result_msg: 失败信息，和result_code结对出现。
        :type result_msg: str
        """
        
        

        self._order_id = None
        self._order_status = None
        self._result = None
        self._result_code = None
        self._result_msg = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        if order_status is not None:
            self.order_status = order_status
        if result is not None:
            self.result = result
        if result_code is not None:
            self.result_code = result_code
        if result_msg is not None:
            self.result_msg = result_msg

    @property
    def order_id(self):
        r"""Gets the order_id of this OrderV5.

        订单id。

        :return: The order_id of this OrderV5.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this OrderV5.

        订单id。

        :param order_id: The order_id of this OrderV5.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def order_status(self):
        r"""Gets the order_status of this OrderV5.

        订单状态:0:初始化; 1:待审核; 2:待退款; 3:处理中; 4:已取消; 5:已完成; 6:待支付; 7:补偿中; 8:待审批; 9:待确认; 10:待发货; 11:待收货; 12:待上门取货; 13:换新中; 14:待商家收货。

        :return: The order_status of this OrderV5.
        :rtype: int
        """
        return self._order_status

    @order_status.setter
    def order_status(self, order_status):
        r"""Sets the order_status of this OrderV5.

        订单状态:0:初始化; 1:待审核; 2:待退款; 3:处理中; 4:已取消; 5:已完成; 6:待支付; 7:补偿中; 8:待审批; 9:待确认; 10:待发货; 11:待收货; 12:待上门取货; 13:换新中; 14:待商家收货。

        :param order_status: The order_status of this OrderV5.
        :type order_status: int
        """
        self._order_status = order_status

    @property
    def result(self):
        r"""Gets the result of this OrderV5.

        结果，SUCCESS:成功； FAIL：失败。

        :return: The result of this OrderV5.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this OrderV5.

        结果，SUCCESS:成功； FAIL：失败。

        :param result: The result of this OrderV5.
        :type result: str
        """
        self._result = result

    @property
    def result_code(self):
        r"""Gets the result_code of this OrderV5.

        result=FAIL时，必填，表示该订单失败原因。

        :return: The result_code of this OrderV5.
        :rtype: str
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code):
        r"""Sets the result_code of this OrderV5.

        result=FAIL时，必填，表示该订单失败原因。

        :param result_code: The result_code of this OrderV5.
        :type result_code: str
        """
        self._result_code = result_code

    @property
    def result_msg(self):
        r"""Gets the result_msg of this OrderV5.

        失败信息，和result_code结对出现。

        :return: The result_msg of this OrderV5.
        :rtype: str
        """
        return self._result_msg

    @result_msg.setter
    def result_msg(self, result_msg):
        r"""Sets the result_msg of this OrderV5.

        失败信息，和result_code结对出现。

        :param result_msg: The result_msg of this OrderV5.
        :type result_msg: str
        """
        self._result_msg = result_msg

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
        if not isinstance(other, OrderV5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
