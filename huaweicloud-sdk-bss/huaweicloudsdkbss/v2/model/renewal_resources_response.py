# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RenewalResourcesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'order_ids': 'list[str]'
    }

    attribute_map = {
        'order_ids': 'order_ids'
    }

    def __init__(self, order_ids=None):
        """RenewalResourcesResponse

        The model defined in huaweicloud sdk

        :param order_ids: 续订资源生成的订单ID的列表。
        :type order_ids: list[str]
        """
        
        super(RenewalResourcesResponse, self).__init__()

        self._order_ids = None
        self.discriminator = None

        if order_ids is not None:
            self.order_ids = order_ids

    @property
    def order_ids(self):
        """Gets the order_ids of this RenewalResourcesResponse.

        续订资源生成的订单ID的列表。

        :return: The order_ids of this RenewalResourcesResponse.
        :rtype: list[str]
        """
        return self._order_ids

    @order_ids.setter
    def order_ids(self, order_ids):
        """Sets the order_ids of this RenewalResourcesResponse.

        续订资源生成的订单ID的列表。

        :param order_ids: The order_ids of this RenewalResourcesResponse.
        :type order_ids: list[str]
        """
        self._order_ids = order_ids

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
        if not isinstance(other, RenewalResourcesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
