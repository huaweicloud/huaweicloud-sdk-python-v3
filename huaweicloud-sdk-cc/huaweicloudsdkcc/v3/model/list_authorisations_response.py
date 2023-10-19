# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAuthorisationsResponse(SdkResponse):

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
        'page_info': 'PageInfo',
        'authorisations': 'list[Authorisation]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'page_info': 'page_info',
        'authorisations': 'authorisations'
    }

    def __init__(self, request_id=None, page_info=None, authorisations=None):
        """ListAuthorisationsResponse

        The model defined in huaweicloud sdk

        :param request_id: 资源ID标识符。
        :type request_id: str
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkcc.v3.PageInfo`
        :param authorisations: 授权实例列表。
        :type authorisations: list[:class:`huaweicloudsdkcc.v3.Authorisation`]
        """
        
        super(ListAuthorisationsResponse, self).__init__()

        self._request_id = None
        self._page_info = None
        self._authorisations = None
        self.discriminator = None

        self.request_id = request_id
        if page_info is not None:
            self.page_info = page_info
        self.authorisations = authorisations

    @property
    def request_id(self):
        """Gets the request_id of this ListAuthorisationsResponse.

        资源ID标识符。

        :return: The request_id of this ListAuthorisationsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListAuthorisationsResponse.

        资源ID标识符。

        :param request_id: The request_id of this ListAuthorisationsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def page_info(self):
        """Gets the page_info of this ListAuthorisationsResponse.

        :return: The page_info of this ListAuthorisationsResponse.
        :rtype: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListAuthorisationsResponse.

        :param page_info: The page_info of this ListAuthorisationsResponse.
        :type page_info: :class:`huaweicloudsdkcc.v3.PageInfo`
        """
        self._page_info = page_info

    @property
    def authorisations(self):
        """Gets the authorisations of this ListAuthorisationsResponse.

        授权实例列表。

        :return: The authorisations of this ListAuthorisationsResponse.
        :rtype: list[:class:`huaweicloudsdkcc.v3.Authorisation`]
        """
        return self._authorisations

    @authorisations.setter
    def authorisations(self, authorisations):
        """Sets the authorisations of this ListAuthorisationsResponse.

        授权实例列表。

        :param authorisations: The authorisations of this ListAuthorisationsResponse.
        :type authorisations: list[:class:`huaweicloudsdkcc.v3.Authorisation`]
        """
        self._authorisations = authorisations

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
        if not isinstance(other, ListAuthorisationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
