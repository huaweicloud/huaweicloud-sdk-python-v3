# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCgwsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'customer_gateways': 'list[ResponseCustomerGateway]',
        'total_count': 'int',
        'page_info': 'PageInfo',
        'request_id': 'str'
    }

    attribute_map = {
        'customer_gateways': 'customer_gateways',
        'total_count': 'total_count',
        'page_info': 'page_info',
        'request_id': 'request_id'
    }

    def __init__(self, customer_gateways=None, total_count=None, page_info=None, request_id=None):
        """ListCgwsResponse

        The model defined in huaweicloud sdk

        :param customer_gateways: 对端网关信息
        :type customer_gateways: list[:class:`huaweicloudsdkvpn.v5.ResponseCustomerGateway`]
        :param total_count: 租户下对端网关总数
        :type total_count: int
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkvpn.v5.PageInfo`
        :param request_id: 请求id
        :type request_id: str
        """
        
        super(ListCgwsResponse, self).__init__()

        self._customer_gateways = None
        self._total_count = None
        self._page_info = None
        self._request_id = None
        self.discriminator = None

        if customer_gateways is not None:
            self.customer_gateways = customer_gateways
        if total_count is not None:
            self.total_count = total_count
        if page_info is not None:
            self.page_info = page_info
        if request_id is not None:
            self.request_id = request_id

    @property
    def customer_gateways(self):
        """Gets the customer_gateways of this ListCgwsResponse.

        对端网关信息

        :return: The customer_gateways of this ListCgwsResponse.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.ResponseCustomerGateway`]
        """
        return self._customer_gateways

    @customer_gateways.setter
    def customer_gateways(self, customer_gateways):
        """Sets the customer_gateways of this ListCgwsResponse.

        对端网关信息

        :param customer_gateways: The customer_gateways of this ListCgwsResponse.
        :type customer_gateways: list[:class:`huaweicloudsdkvpn.v5.ResponseCustomerGateway`]
        """
        self._customer_gateways = customer_gateways

    @property
    def total_count(self):
        """Gets the total_count of this ListCgwsResponse.

        租户下对端网关总数

        :return: The total_count of this ListCgwsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListCgwsResponse.

        租户下对端网关总数

        :param total_count: The total_count of this ListCgwsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def page_info(self):
        """Gets the page_info of this ListCgwsResponse.

        :return: The page_info of this ListCgwsResponse.
        :rtype: :class:`huaweicloudsdkvpn.v5.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListCgwsResponse.

        :param page_info: The page_info of this ListCgwsResponse.
        :type page_info: :class:`huaweicloudsdkvpn.v5.PageInfo`
        """
        self._page_info = page_info

    @property
    def request_id(self):
        """Gets the request_id of this ListCgwsResponse.

        请求id

        :return: The request_id of this ListCgwsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListCgwsResponse.

        请求id

        :param request_id: The request_id of this ListCgwsResponse.
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
        if not isinstance(other, ListCgwsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
