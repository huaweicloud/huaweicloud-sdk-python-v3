# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApplicationEndpointsResponse(SdkResponse):

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
        'next_page_flag': 'bool',
        'endpoints': 'list[ApplicationEndpoint]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'next_page_flag': 'next_page_flag',
        'endpoints': 'endpoints'
    }

    def __init__(self, request_id=None, next_page_flag=None, endpoints=None):
        """ListApplicationEndpointsResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求的唯一标识ID。
        :type request_id: str
        :param next_page_flag: 是否有下一页标识。
        :type next_page_flag: bool
        :param endpoints: Application_endpoint结构体数。
        :type endpoints: list[:class:`huaweicloudsdksmn.v2.ApplicationEndpoint`]
        """
        
        super(ListApplicationEndpointsResponse, self).__init__()

        self._request_id = None
        self._next_page_flag = None
        self._endpoints = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if next_page_flag is not None:
            self.next_page_flag = next_page_flag
        if endpoints is not None:
            self.endpoints = endpoints

    @property
    def request_id(self):
        """Gets the request_id of this ListApplicationEndpointsResponse.

        请求的唯一标识ID。

        :return: The request_id of this ListApplicationEndpointsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListApplicationEndpointsResponse.

        请求的唯一标识ID。

        :param request_id: The request_id of this ListApplicationEndpointsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def next_page_flag(self):
        """Gets the next_page_flag of this ListApplicationEndpointsResponse.

        是否有下一页标识。

        :return: The next_page_flag of this ListApplicationEndpointsResponse.
        :rtype: bool
        """
        return self._next_page_flag

    @next_page_flag.setter
    def next_page_flag(self, next_page_flag):
        """Sets the next_page_flag of this ListApplicationEndpointsResponse.

        是否有下一页标识。

        :param next_page_flag: The next_page_flag of this ListApplicationEndpointsResponse.
        :type next_page_flag: bool
        """
        self._next_page_flag = next_page_flag

    @property
    def endpoints(self):
        """Gets the endpoints of this ListApplicationEndpointsResponse.

        Application_endpoint结构体数。

        :return: The endpoints of this ListApplicationEndpointsResponse.
        :rtype: list[:class:`huaweicloudsdksmn.v2.ApplicationEndpoint`]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """Sets the endpoints of this ListApplicationEndpointsResponse.

        Application_endpoint结构体数。

        :param endpoints: The endpoints of this ListApplicationEndpointsResponse.
        :type endpoints: list[:class:`huaweicloudsdksmn.v2.ApplicationEndpoint`]
        """
        self._endpoints = endpoints

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
        if not isinstance(other, ListApplicationEndpointsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
