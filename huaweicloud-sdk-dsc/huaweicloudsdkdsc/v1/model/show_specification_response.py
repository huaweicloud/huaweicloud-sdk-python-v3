# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSpecificationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'order_infos': 'list[ProductOrderInfo]'
    }

    attribute_map = {
        'order_infos': 'orderInfos'
    }

    def __init__(self, order_infos=None):
        """ShowSpecificationResponse

        The model defined in huaweicloud sdk

        :param order_infos: 订单列表
        :type order_infos: list[:class:`huaweicloudsdkdsc.v1.ProductOrderInfo`]
        """
        
        super(ShowSpecificationResponse, self).__init__()

        self._order_infos = None
        self.discriminator = None

        if order_infos is not None:
            self.order_infos = order_infos

    @property
    def order_infos(self):
        """Gets the order_infos of this ShowSpecificationResponse.

        订单列表

        :return: The order_infos of this ShowSpecificationResponse.
        :rtype: list[:class:`huaweicloudsdkdsc.v1.ProductOrderInfo`]
        """
        return self._order_infos

    @order_infos.setter
    def order_infos(self, order_infos):
        """Sets the order_infos of this ShowSpecificationResponse.

        订单列表

        :param order_infos: The order_infos of this ShowSpecificationResponse.
        :type order_infos: list[:class:`huaweicloudsdkdsc.v1.ProductOrderInfo`]
        """
        self._order_infos = order_infos

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
        if not isinstance(other, ShowSpecificationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
