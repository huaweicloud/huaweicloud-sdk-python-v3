# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigsGetBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'origin_request_header': 'list[OriginRequestHeader]',
        'http_response_header': 'list[HttpResponseHeader]',
        'url_auth': 'UrlAuthGetBody',
        'https': 'HttpGetBody'
    }

    attribute_map = {
        'origin_request_header': 'origin_request_header',
        'http_response_header': 'http_response_header',
        'url_auth': 'url_auth',
        'https': 'https'
    }

    def __init__(self, origin_request_header=None, http_response_header=None, url_auth=None, https=None):
        """ConfigsGetBody - a model defined in huaweicloud sdk"""
        
        

        self._origin_request_header = None
        self._http_response_header = None
        self._url_auth = None
        self._https = None
        self.discriminator = None

        if origin_request_header is not None:
            self.origin_request_header = origin_request_header
        if http_response_header is not None:
            self.http_response_header = http_response_header
        if url_auth is not None:
            self.url_auth = url_auth
        if https is not None:
            self.https = https

    @property
    def origin_request_header(self):
        """Gets the origin_request_header of this ConfigsGetBody.

        回源请求头配置

        :return: The origin_request_header of this ConfigsGetBody.
        :rtype: list[OriginRequestHeader]
        """
        return self._origin_request_header

    @origin_request_header.setter
    def origin_request_header(self, origin_request_header):
        """Sets the origin_request_header of this ConfigsGetBody.

        回源请求头配置

        :param origin_request_header: The origin_request_header of this ConfigsGetBody.
        :type: list[OriginRequestHeader]
        """
        self._origin_request_header = origin_request_header

    @property
    def http_response_header(self):
        """Gets the http_response_header of this ConfigsGetBody.

        http header配置

        :return: The http_response_header of this ConfigsGetBody.
        :rtype: list[HttpResponseHeader]
        """
        return self._http_response_header

    @http_response_header.setter
    def http_response_header(self, http_response_header):
        """Sets the http_response_header of this ConfigsGetBody.

        http header配置

        :param http_response_header: The http_response_header of this ConfigsGetBody.
        :type: list[HttpResponseHeader]
        """
        self._http_response_header = http_response_header

    @property
    def url_auth(self):
        """Gets the url_auth of this ConfigsGetBody.


        :return: The url_auth of this ConfigsGetBody.
        :rtype: UrlAuthGetBody
        """
        return self._url_auth

    @url_auth.setter
    def url_auth(self, url_auth):
        """Sets the url_auth of this ConfigsGetBody.


        :param url_auth: The url_auth of this ConfigsGetBody.
        :type: UrlAuthGetBody
        """
        self._url_auth = url_auth

    @property
    def https(self):
        """Gets the https of this ConfigsGetBody.


        :return: The https of this ConfigsGetBody.
        :rtype: HttpGetBody
        """
        return self._https

    @https.setter
    def https(self, https):
        """Sets the https of this ConfigsGetBody.


        :param https: The https of this ConfigsGetBody.
        :type: HttpGetBody
        """
        self._https = https

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
        if not isinstance(other, ConfigsGetBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
