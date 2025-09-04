# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHarmonySoftBusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'harmony_soft_buses': 'list[HarmonySoftBusResponseDTO]',
        'page': 'Page'
    }

    attribute_map = {
        'harmony_soft_buses': 'harmony_soft_buses',
        'page': 'page'
    }

    def __init__(self, harmony_soft_buses=None, page=None):
        r"""ListHarmonySoftBusResponse

        The model defined in huaweicloud sdk

        :param harmony_soft_buses: 设备组信息列表。
        :type harmony_soft_buses: list[:class:`huaweicloudsdkiotda.v5.HarmonySoftBusResponseDTO`]
        :param page: 
        :type page: :class:`huaweicloudsdkiotda.v5.Page`
        """
        
        super(ListHarmonySoftBusResponse, self).__init__()

        self._harmony_soft_buses = None
        self._page = None
        self.discriminator = None

        if harmony_soft_buses is not None:
            self.harmony_soft_buses = harmony_soft_buses
        if page is not None:
            self.page = page

    @property
    def harmony_soft_buses(self):
        r"""Gets the harmony_soft_buses of this ListHarmonySoftBusResponse.

        设备组信息列表。

        :return: The harmony_soft_buses of this ListHarmonySoftBusResponse.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.HarmonySoftBusResponseDTO`]
        """
        return self._harmony_soft_buses

    @harmony_soft_buses.setter
    def harmony_soft_buses(self, harmony_soft_buses):
        r"""Sets the harmony_soft_buses of this ListHarmonySoftBusResponse.

        设备组信息列表。

        :param harmony_soft_buses: The harmony_soft_buses of this ListHarmonySoftBusResponse.
        :type harmony_soft_buses: list[:class:`huaweicloudsdkiotda.v5.HarmonySoftBusResponseDTO`]
        """
        self._harmony_soft_buses = harmony_soft_buses

    @property
    def page(self):
        r"""Gets the page of this ListHarmonySoftBusResponse.

        :return: The page of this ListHarmonySoftBusResponse.
        :rtype: :class:`huaweicloudsdkiotda.v5.Page`
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListHarmonySoftBusResponse.

        :param page: The page of this ListHarmonySoftBusResponse.
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
        if not isinstance(other, ListHarmonySoftBusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
