# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBridgesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bridges': 'list[BridgeResponse]',
        'page': 'Page'
    }

    attribute_map = {
        'bridges': 'bridges',
        'page': 'page'
    }

    def __init__(self, bridges=None, page=None):
        r"""ListBridgesResponse

        The model defined in huaweicloud sdk

        :param bridges: 网桥列表。
        :type bridges: list[:class:`huaweicloudsdkiotda.v5.BridgeResponse`]
        :param page: 
        :type page: :class:`huaweicloudsdkiotda.v5.Page`
        """
        
        super(ListBridgesResponse, self).__init__()

        self._bridges = None
        self._page = None
        self.discriminator = None

        if bridges is not None:
            self.bridges = bridges
        if page is not None:
            self.page = page

    @property
    def bridges(self):
        r"""Gets the bridges of this ListBridgesResponse.

        网桥列表。

        :return: The bridges of this ListBridgesResponse.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.BridgeResponse`]
        """
        return self._bridges

    @bridges.setter
    def bridges(self, bridges):
        r"""Sets the bridges of this ListBridgesResponse.

        网桥列表。

        :param bridges: The bridges of this ListBridgesResponse.
        :type bridges: list[:class:`huaweicloudsdkiotda.v5.BridgeResponse`]
        """
        self._bridges = bridges

    @property
    def page(self):
        r"""Gets the page of this ListBridgesResponse.

        :return: The page of this ListBridgesResponse.
        :rtype: :class:`huaweicloudsdkiotda.v5.Page`
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListBridgesResponse.

        :param page: The page of this ListBridgesResponse.
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
        if not isinstance(other, ListBridgesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
