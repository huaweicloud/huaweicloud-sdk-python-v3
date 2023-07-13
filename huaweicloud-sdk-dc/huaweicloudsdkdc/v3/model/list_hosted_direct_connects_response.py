# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHostedDirectConnectsResponse(SdkResponse):

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
        'hosted_connects': 'list[HostedDirectConnect]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'request_id': 'request_id',
        'hosted_connects': 'hosted_connects',
        'page_info': 'page_info'
    }

    def __init__(self, request_id=None, hosted_connects=None, page_info=None):
        """ListHostedDirectConnectsResponse

        The model defined in huaweicloud sdk

        :param request_id: 本次操作的请求ID
        :type request_id: str
        :param hosted_connects: 
        :type hosted_connects: list[:class:`huaweicloudsdkdc.v3.HostedDirectConnect`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkdc.v3.PageInfo`
        """
        
        super(ListHostedDirectConnectsResponse, self).__init__()

        self._request_id = None
        self._hosted_connects = None
        self._page_info = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if hosted_connects is not None:
            self.hosted_connects = hosted_connects
        if page_info is not None:
            self.page_info = page_info

    @property
    def request_id(self):
        """Gets the request_id of this ListHostedDirectConnectsResponse.

        本次操作的请求ID

        :return: The request_id of this ListHostedDirectConnectsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListHostedDirectConnectsResponse.

        本次操作的请求ID

        :param request_id: The request_id of this ListHostedDirectConnectsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def hosted_connects(self):
        """Gets the hosted_connects of this ListHostedDirectConnectsResponse.

        :return: The hosted_connects of this ListHostedDirectConnectsResponse.
        :rtype: list[:class:`huaweicloudsdkdc.v3.HostedDirectConnect`]
        """
        return self._hosted_connects

    @hosted_connects.setter
    def hosted_connects(self, hosted_connects):
        """Sets the hosted_connects of this ListHostedDirectConnectsResponse.

        :param hosted_connects: The hosted_connects of this ListHostedDirectConnectsResponse.
        :type hosted_connects: list[:class:`huaweicloudsdkdc.v3.HostedDirectConnect`]
        """
        self._hosted_connects = hosted_connects

    @property
    def page_info(self):
        """Gets the page_info of this ListHostedDirectConnectsResponse.

        :return: The page_info of this ListHostedDirectConnectsResponse.
        :rtype: :class:`huaweicloudsdkdc.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListHostedDirectConnectsResponse.

        :param page_info: The page_info of this ListHostedDirectConnectsResponse.
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
        if not isinstance(other, ListHostedDirectConnectsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
