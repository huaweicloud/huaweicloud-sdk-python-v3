# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPrivateNatsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'gateways': 'list[PrivateNat]',
        'request_id': 'str',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'gateways': 'gateways',
        'request_id': 'request_id',
        'page_info': 'page_info'
    }

    def __init__(self, gateways=None, request_id=None, page_info=None):
        r"""ListPrivateNatsResponse

        The model defined in huaweicloud sdk

        :param gateways: 查询私网NAT网关实例列表的响应体。 详见PrivateNat字段说明。
        :type gateways: list[:class:`huaweicloudsdknat.v2.PrivateNat`]
        :param request_id: 请求ID。
        :type request_id: str
        :param page_info: 
        :type page_info: :class:`huaweicloudsdknat.v2.PageInfo`
        """
        
        super(ListPrivateNatsResponse, self).__init__()

        self._gateways = None
        self._request_id = None
        self._page_info = None
        self.discriminator = None

        if gateways is not None:
            self.gateways = gateways
        if request_id is not None:
            self.request_id = request_id
        if page_info is not None:
            self.page_info = page_info

    @property
    def gateways(self):
        r"""Gets the gateways of this ListPrivateNatsResponse.

        查询私网NAT网关实例列表的响应体。 详见PrivateNat字段说明。

        :return: The gateways of this ListPrivateNatsResponse.
        :rtype: list[:class:`huaweicloudsdknat.v2.PrivateNat`]
        """
        return self._gateways

    @gateways.setter
    def gateways(self, gateways):
        r"""Sets the gateways of this ListPrivateNatsResponse.

        查询私网NAT网关实例列表的响应体。 详见PrivateNat字段说明。

        :param gateways: The gateways of this ListPrivateNatsResponse.
        :type gateways: list[:class:`huaweicloudsdknat.v2.PrivateNat`]
        """
        self._gateways = gateways

    @property
    def request_id(self):
        r"""Gets the request_id of this ListPrivateNatsResponse.

        请求ID。

        :return: The request_id of this ListPrivateNatsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListPrivateNatsResponse.

        请求ID。

        :param request_id: The request_id of this ListPrivateNatsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def page_info(self):
        r"""Gets the page_info of this ListPrivateNatsResponse.

        :return: The page_info of this ListPrivateNatsResponse.
        :rtype: :class:`huaweicloudsdknat.v2.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListPrivateNatsResponse.

        :param page_info: The page_info of this ListPrivateNatsResponse.
        :type page_info: :class:`huaweicloudsdknat.v2.PageInfo`
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
        if not isinstance(other, ListPrivateNatsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
