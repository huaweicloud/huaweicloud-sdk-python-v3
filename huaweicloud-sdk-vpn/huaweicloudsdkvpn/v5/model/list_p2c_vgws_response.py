# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListP2cVgwsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'p2c_vpn_gateways': 'list[ShowResponseP2cVgw]',
        'request_id': 'str'
    }

    attribute_map = {
        'p2c_vpn_gateways': 'p2c_vpn_gateways',
        'request_id': 'request_id'
    }

    def __init__(self, p2c_vpn_gateways=None, request_id=None):
        """ListP2cVgwsResponse

        The model defined in huaweicloud sdk

        :param p2c_vpn_gateways: 网关信息
        :type p2c_vpn_gateways: list[:class:`huaweicloudsdkvpn.v5.ShowResponseP2cVgw`]
        :param request_id: 请求ID
        :type request_id: str
        """
        
        super(ListP2cVgwsResponse, self).__init__()

        self._p2c_vpn_gateways = None
        self._request_id = None
        self.discriminator = None

        if p2c_vpn_gateways is not None:
            self.p2c_vpn_gateways = p2c_vpn_gateways
        if request_id is not None:
            self.request_id = request_id

    @property
    def p2c_vpn_gateways(self):
        """Gets the p2c_vpn_gateways of this ListP2cVgwsResponse.

        网关信息

        :return: The p2c_vpn_gateways of this ListP2cVgwsResponse.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.ShowResponseP2cVgw`]
        """
        return self._p2c_vpn_gateways

    @p2c_vpn_gateways.setter
    def p2c_vpn_gateways(self, p2c_vpn_gateways):
        """Sets the p2c_vpn_gateways of this ListP2cVgwsResponse.

        网关信息

        :param p2c_vpn_gateways: The p2c_vpn_gateways of this ListP2cVgwsResponse.
        :type p2c_vpn_gateways: list[:class:`huaweicloudsdkvpn.v5.ShowResponseP2cVgw`]
        """
        self._p2c_vpn_gateways = p2c_vpn_gateways

    @property
    def request_id(self):
        """Gets the request_id of this ListP2cVgwsResponse.

        请求ID

        :return: The request_id of this ListP2cVgwsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListP2cVgwsResponse.

        请求ID

        :param request_id: The request_id of this ListP2cVgwsResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, ListP2cVgwsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
