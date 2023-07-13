# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDirectConnectsResponse(SdkResponse):

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
        'direct_connects': 'list[DirectConnect]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'request_id': 'request_id',
        'direct_connects': 'direct_connects',
        'page_info': 'page_info'
    }

    def __init__(self, request_id=None, direct_connects=None, page_info=None):
        """ListDirectConnectsResponse

        The model defined in huaweicloud sdk

        :param request_id: 操作请求ID
        :type request_id: str
        :param direct_connects: 物理专线对象列表
        :type direct_connects: list[:class:`huaweicloudsdkdc.v3.DirectConnect`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkdc.v3.PageInfo`
        """
        
        super(ListDirectConnectsResponse, self).__init__()

        self._request_id = None
        self._direct_connects = None
        self._page_info = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if direct_connects is not None:
            self.direct_connects = direct_connects
        if page_info is not None:
            self.page_info = page_info

    @property
    def request_id(self):
        """Gets the request_id of this ListDirectConnectsResponse.

        操作请求ID

        :return: The request_id of this ListDirectConnectsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListDirectConnectsResponse.

        操作请求ID

        :param request_id: The request_id of this ListDirectConnectsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def direct_connects(self):
        """Gets the direct_connects of this ListDirectConnectsResponse.

        物理专线对象列表

        :return: The direct_connects of this ListDirectConnectsResponse.
        :rtype: list[:class:`huaweicloudsdkdc.v3.DirectConnect`]
        """
        return self._direct_connects

    @direct_connects.setter
    def direct_connects(self, direct_connects):
        """Sets the direct_connects of this ListDirectConnectsResponse.

        物理专线对象列表

        :param direct_connects: The direct_connects of this ListDirectConnectsResponse.
        :type direct_connects: list[:class:`huaweicloudsdkdc.v3.DirectConnect`]
        """
        self._direct_connects = direct_connects

    @property
    def page_info(self):
        """Gets the page_info of this ListDirectConnectsResponse.

        :return: The page_info of this ListDirectConnectsResponse.
        :rtype: :class:`huaweicloudsdkdc.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListDirectConnectsResponse.

        :param page_info: The page_info of this ListDirectConnectsResponse.
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
        if not isinstance(other, ListDirectConnectsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
