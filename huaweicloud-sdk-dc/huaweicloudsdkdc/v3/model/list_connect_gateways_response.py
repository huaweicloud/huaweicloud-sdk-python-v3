# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConnectGatewaysResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'connect_gateways': 'list[ConnectGatewayResponse]',
        'total_count': 'int',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'request_id': 'request_id',
        'connect_gateways': 'connect_gateways',
        'total_count': 'total_count',
        'page_info': 'page_info'
    }

    def __init__(self, request_id=None, connect_gateways=None, total_count=None, page_info=None):
        """ListConnectGatewaysResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求ID
        :type request_id: str
        :param connect_gateways: 
        :type connect_gateways: list[:class:`huaweicloudsdkdc.v3.ConnectGatewayResponse`]
        :param total_count: 总记录数。
        :type total_count: int
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkdc.v3.PageInfo`
        """
        
        super(ListConnectGatewaysResponse, self).__init__()

        self._request_id = None
        self._connect_gateways = None
        self._total_count = None
        self._page_info = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if connect_gateways is not None:
            self.connect_gateways = connect_gateways
        if total_count is not None:
            self.total_count = total_count
        if page_info is not None:
            self.page_info = page_info

    @property
    def request_id(self):
        """Gets the request_id of this ListConnectGatewaysResponse.

        请求ID

        :return: The request_id of this ListConnectGatewaysResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListConnectGatewaysResponse.

        请求ID

        :param request_id: The request_id of this ListConnectGatewaysResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def connect_gateways(self):
        """Gets the connect_gateways of this ListConnectGatewaysResponse.

        :return: The connect_gateways of this ListConnectGatewaysResponse.
        :rtype: list[:class:`huaweicloudsdkdc.v3.ConnectGatewayResponse`]
        """
        return self._connect_gateways

    @connect_gateways.setter
    def connect_gateways(self, connect_gateways):
        """Sets the connect_gateways of this ListConnectGatewaysResponse.

        :param connect_gateways: The connect_gateways of this ListConnectGatewaysResponse.
        :type connect_gateways: list[:class:`huaweicloudsdkdc.v3.ConnectGatewayResponse`]
        """
        self._connect_gateways = connect_gateways

    @property
    def total_count(self):
        """Gets the total_count of this ListConnectGatewaysResponse.

        总记录数。

        :return: The total_count of this ListConnectGatewaysResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListConnectGatewaysResponse.

        总记录数。

        :param total_count: The total_count of this ListConnectGatewaysResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def page_info(self):
        """Gets the page_info of this ListConnectGatewaysResponse.

        :return: The page_info of this ListConnectGatewaysResponse.
        :rtype: :class:`huaweicloudsdkdc.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListConnectGatewaysResponse.

        :param page_info: The page_info of this ListConnectGatewaysResponse.
        :type page_info: :class:`huaweicloudsdkdc.v3.PageInfo`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListConnectGatewaysResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
