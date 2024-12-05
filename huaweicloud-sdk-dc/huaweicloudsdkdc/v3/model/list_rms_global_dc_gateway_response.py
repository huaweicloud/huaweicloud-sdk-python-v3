# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRmsGlobalDcGatewayResponse(SdkResponse):

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
        'global_dc_gateways': 'list[RmsListGlobalDcGateways]',
        'page_info': 'PageInfo',
        'x_request_id': 'str'
    }

    attribute_map = {
        'request_id': 'request_id',
        'global_dc_gateways': 'global_dc_gateways',
        'page_info': 'page_info',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, request_id=None, global_dc_gateways=None, page_info=None, x_request_id=None):
        """ListRmsGlobalDcGatewayResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求ID
        :type request_id: str
        :param global_dc_gateways: 全球接入网关
        :type global_dc_gateways: list[:class:`huaweicloudsdkdc.v3.RmsListGlobalDcGateways`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkdc.v3.PageInfo`
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListRmsGlobalDcGatewayResponse, self).__init__()

        self._request_id = None
        self._global_dc_gateways = None
        self._page_info = None
        self._x_request_id = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if global_dc_gateways is not None:
            self.global_dc_gateways = global_dc_gateways
        if page_info is not None:
            self.page_info = page_info
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def request_id(self):
        """Gets the request_id of this ListRmsGlobalDcGatewayResponse.

        请求ID

        :return: The request_id of this ListRmsGlobalDcGatewayResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListRmsGlobalDcGatewayResponse.

        请求ID

        :param request_id: The request_id of this ListRmsGlobalDcGatewayResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def global_dc_gateways(self):
        """Gets the global_dc_gateways of this ListRmsGlobalDcGatewayResponse.

        全球接入网关

        :return: The global_dc_gateways of this ListRmsGlobalDcGatewayResponse.
        :rtype: list[:class:`huaweicloudsdkdc.v3.RmsListGlobalDcGateways`]
        """
        return self._global_dc_gateways

    @global_dc_gateways.setter
    def global_dc_gateways(self, global_dc_gateways):
        """Sets the global_dc_gateways of this ListRmsGlobalDcGatewayResponse.

        全球接入网关

        :param global_dc_gateways: The global_dc_gateways of this ListRmsGlobalDcGatewayResponse.
        :type global_dc_gateways: list[:class:`huaweicloudsdkdc.v3.RmsListGlobalDcGateways`]
        """
        self._global_dc_gateways = global_dc_gateways

    @property
    def page_info(self):
        """Gets the page_info of this ListRmsGlobalDcGatewayResponse.

        :return: The page_info of this ListRmsGlobalDcGatewayResponse.
        :rtype: :class:`huaweicloudsdkdc.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListRmsGlobalDcGatewayResponse.

        :param page_info: The page_info of this ListRmsGlobalDcGatewayResponse.
        :type page_info: :class:`huaweicloudsdkdc.v3.PageInfo`
        """
        self._page_info = page_info

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ListRmsGlobalDcGatewayResponse.

        :return: The x_request_id of this ListRmsGlobalDcGatewayResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ListRmsGlobalDcGatewayResponse.

        :param x_request_id: The x_request_id of this ListRmsGlobalDcGatewayResponse.
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
        if not isinstance(other, ListRmsGlobalDcGatewayResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
