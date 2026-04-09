# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeDemand2PeriodResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'order_ids': 'list[str]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'order_ids': 'order_ids',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, order_ids=None, x_request_id=None):
        r"""ChangeDemand2PeriodResponse

        The model defined in huaweicloud sdk

        :param order_ids: **参数解释**: 订单ID的集合。
        :type order_ids: list[str]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._order_ids = None
        self._x_request_id = None
        self.discriminator = None

        if order_ids is not None:
            self.order_ids = order_ids
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def order_ids(self):
        r"""Gets the order_ids of this ChangeDemand2PeriodResponse.

        **参数解释**: 订单ID的集合。

        :return: The order_ids of this ChangeDemand2PeriodResponse.
        :rtype: list[str]
        """
        return self._order_ids

    @order_ids.setter
    def order_ids(self, order_ids):
        r"""Sets the order_ids of this ChangeDemand2PeriodResponse.

        **参数解释**: 订单ID的集合。

        :param order_ids: The order_ids of this ChangeDemand2PeriodResponse.
        :type order_ids: list[str]
        """
        self._order_ids = order_ids

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ChangeDemand2PeriodResponse.

        :return: The x_request_id of this ChangeDemand2PeriodResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ChangeDemand2PeriodResponse.

        :param x_request_id: The x_request_id of this ChangeDemand2PeriodResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ChangeDemand2PeriodResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ChangeDemand2PeriodResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
