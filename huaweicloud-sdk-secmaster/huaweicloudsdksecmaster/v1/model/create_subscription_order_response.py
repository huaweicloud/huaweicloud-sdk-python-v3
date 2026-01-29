# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSubscriptionOrderResponse(SdkResponse):

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
        'order_status': 'int'
    }

    attribute_map = {
        'order_id': 'order_id',
        'order_status': 'order_status'
    }

    def __init__(self, order_id=None, order_status=None):
        r"""CreateSubscriptionOrderResponse

        The model defined in huaweicloud sdk

        :param order_id: 创建或变更订单ID，只有scene为PREPAID时返回有此数据
        :type order_id: str
        :param order_status: 订单更新状态，1：变更订单成功，5，订单变更失败
        :type order_status: int
        """
        
        super().__init__()

        self._order_id = None
        self._order_status = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        if order_status is not None:
            self.order_status = order_status

    @property
    def order_id(self):
        r"""Gets the order_id of this CreateSubscriptionOrderResponse.

        创建或变更订单ID，只有scene为PREPAID时返回有此数据

        :return: The order_id of this CreateSubscriptionOrderResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this CreateSubscriptionOrderResponse.

        创建或变更订单ID，只有scene为PREPAID时返回有此数据

        :param order_id: The order_id of this CreateSubscriptionOrderResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def order_status(self):
        r"""Gets the order_status of this CreateSubscriptionOrderResponse.

        订单更新状态，1：变更订单成功，5，订单变更失败

        :return: The order_status of this CreateSubscriptionOrderResponse.
        :rtype: int
        """
        return self._order_status

    @order_status.setter
    def order_status(self, order_status):
        r"""Sets the order_status of this CreateSubscriptionOrderResponse.

        订单更新状态，1：变更订单成功，5，订单变更失败

        :param order_status: The order_status of this CreateSubscriptionOrderResponse.
        :type order_status: int
        """
        self._order_status = order_status

    def to_dict(self):
        import warnings
        warnings.warn("CreateSubscriptionOrderResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateSubscriptionOrderResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
