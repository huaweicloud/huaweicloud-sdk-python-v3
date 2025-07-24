# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeShareChargeModeV2Response(SdkResponse):

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
        r"""ChangeShareChargeModeV2Response

        The model defined in huaweicloud sdk

        :param order_ids: 转包周期生成的订单数组
        :type order_ids: list[str]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ChangeShareChargeModeV2Response, self).__init__()

        self._order_ids = None
        self._x_request_id = None
        self.discriminator = None

        if order_ids is not None:
            self.order_ids = order_ids
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def order_ids(self):
        r"""Gets the order_ids of this ChangeShareChargeModeV2Response.

        转包周期生成的订单数组

        :return: The order_ids of this ChangeShareChargeModeV2Response.
        :rtype: list[str]
        """
        return self._order_ids

    @order_ids.setter
    def order_ids(self, order_ids):
        r"""Sets the order_ids of this ChangeShareChargeModeV2Response.

        转包周期生成的订单数组

        :param order_ids: The order_ids of this ChangeShareChargeModeV2Response.
        :type order_ids: list[str]
        """
        self._order_ids = order_ids

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ChangeShareChargeModeV2Response.

        :return: The x_request_id of this ChangeShareChargeModeV2Response.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ChangeShareChargeModeV2Response.

        :param x_request_id: The x_request_id of this ChangeShareChargeModeV2Response.
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
        if not isinstance(other, ChangeShareChargeModeV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
