# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDeviceProxiesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'device_proxies': 'list[QueryDeviceProxySimplify]',
        'page': 'Page'
    }

    attribute_map = {
        'device_proxies': 'device_proxies',
        'page': 'page'
    }

    def __init__(self, device_proxies=None, page=None):
        r"""ListDeviceProxiesResponse

        The model defined in huaweicloud sdk

        :param device_proxies: 代理设备列表
        :type device_proxies: list[:class:`huaweicloudsdkiotda.v5.QueryDeviceProxySimplify`]
        :param page: 
        :type page: :class:`huaweicloudsdkiotda.v5.Page`
        """
        
        super(ListDeviceProxiesResponse, self).__init__()

        self._device_proxies = None
        self._page = None
        self.discriminator = None

        if device_proxies is not None:
            self.device_proxies = device_proxies
        if page is not None:
            self.page = page

    @property
    def device_proxies(self):
        r"""Gets the device_proxies of this ListDeviceProxiesResponse.

        代理设备列表

        :return: The device_proxies of this ListDeviceProxiesResponse.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.QueryDeviceProxySimplify`]
        """
        return self._device_proxies

    @device_proxies.setter
    def device_proxies(self, device_proxies):
        r"""Sets the device_proxies of this ListDeviceProxiesResponse.

        代理设备列表

        :param device_proxies: The device_proxies of this ListDeviceProxiesResponse.
        :type device_proxies: list[:class:`huaweicloudsdkiotda.v5.QueryDeviceProxySimplify`]
        """
        self._device_proxies = device_proxies

    @property
    def page(self):
        r"""Gets the page of this ListDeviceProxiesResponse.

        :return: The page of this ListDeviceProxiesResponse.
        :rtype: :class:`huaweicloudsdkiotda.v5.Page`
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListDeviceProxiesResponse.

        :param page: The page of this ListDeviceProxiesResponse.
        :type page: :class:`huaweicloudsdkiotda.v5.Page`
        """
        self._page = page

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
        if not isinstance(other, ListDeviceProxiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
