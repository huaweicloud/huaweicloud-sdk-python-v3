# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNatGatewaysResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nat_gateways': 'list[NatGatewayResponseBody]'
    }

    attribute_map = {
        'nat_gateways': 'nat_gateways'
    }

    def __init__(self, nat_gateways=None):
        """ListNatGatewaysResponse

        The model defined in huaweicloud sdk

        :param nat_gateways: 查询公网NAT网关实例列表的响应体。 详见NatGateway字段说明。
        :type nat_gateways: list[:class:`huaweicloudsdknat.v2.NatGatewayResponseBody`]
        """
        
        super(ListNatGatewaysResponse, self).__init__()

        self._nat_gateways = None
        self.discriminator = None

        if nat_gateways is not None:
            self.nat_gateways = nat_gateways

    @property
    def nat_gateways(self):
        """Gets the nat_gateways of this ListNatGatewaysResponse.

        查询公网NAT网关实例列表的响应体。 详见NatGateway字段说明。

        :return: The nat_gateways of this ListNatGatewaysResponse.
        :rtype: list[:class:`huaweicloudsdknat.v2.NatGatewayResponseBody`]
        """
        return self._nat_gateways

    @nat_gateways.setter
    def nat_gateways(self, nat_gateways):
        """Sets the nat_gateways of this ListNatGatewaysResponse.

        查询公网NAT网关实例列表的响应体。 详见NatGateway字段说明。

        :param nat_gateways: The nat_gateways of this ListNatGatewaysResponse.
        :type nat_gateways: list[:class:`huaweicloudsdknat.v2.NatGatewayResponseBody`]
        """
        self._nat_gateways = nat_gateways

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
        if not isinstance(other, ListNatGatewaysResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
