# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisassociateSiteNetworkBandwidthResponse(SdkResponse):

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
        'site_connection': 'SiteConnection'
    }

    attribute_map = {
        'request_id': 'request_id',
        'site_connection': 'site_connection'
    }

    def __init__(self, request_id=None, site_connection=None):
        r"""DisassociateSiteNetworkBandwidthResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求ID。
        :type request_id: str
        :param site_connection: 
        :type site_connection: :class:`huaweicloudsdkcc.v3.SiteConnection`
        """
        
        super(DisassociateSiteNetworkBandwidthResponse, self).__init__()

        self._request_id = None
        self._site_connection = None
        self.discriminator = None

        self.request_id = request_id
        self.site_connection = site_connection

    @property
    def request_id(self):
        r"""Gets the request_id of this DisassociateSiteNetworkBandwidthResponse.

        请求ID。

        :return: The request_id of this DisassociateSiteNetworkBandwidthResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this DisassociateSiteNetworkBandwidthResponse.

        请求ID。

        :param request_id: The request_id of this DisassociateSiteNetworkBandwidthResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def site_connection(self):
        r"""Gets the site_connection of this DisassociateSiteNetworkBandwidthResponse.

        :return: The site_connection of this DisassociateSiteNetworkBandwidthResponse.
        :rtype: :class:`huaweicloudsdkcc.v3.SiteConnection`
        """
        return self._site_connection

    @site_connection.setter
    def site_connection(self, site_connection):
        r"""Sets the site_connection of this DisassociateSiteNetworkBandwidthResponse.

        :param site_connection: The site_connection of this DisassociateSiteNetworkBandwidthResponse.
        :type site_connection: :class:`huaweicloudsdkcc.v3.SiteConnection`
        """
        self._site_connection = site_connection

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
        if not isinstance(other, DisassociateSiteNetworkBandwidthResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
