# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCloudConnectionRoutesResponse(SdkResponse):

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
        'cloud_connection_route': 'CloudConnectionRoute'
    }

    attribute_map = {
        'request_id': 'request_id',
        'cloud_connection_route': 'cloud_connection_route'
    }

    def __init__(self, request_id=None, cloud_connection_route=None):
        r"""ShowCloudConnectionRoutesResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求ID。
        :type request_id: str
        :param cloud_connection_route: 
        :type cloud_connection_route: :class:`huaweicloudsdkcc.v3.CloudConnectionRoute`
        """
        
        super(ShowCloudConnectionRoutesResponse, self).__init__()

        self._request_id = None
        self._cloud_connection_route = None
        self.discriminator = None

        self.request_id = request_id
        self.cloud_connection_route = cloud_connection_route

    @property
    def request_id(self):
        r"""Gets the request_id of this ShowCloudConnectionRoutesResponse.

        请求ID。

        :return: The request_id of this ShowCloudConnectionRoutesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ShowCloudConnectionRoutesResponse.

        请求ID。

        :param request_id: The request_id of this ShowCloudConnectionRoutesResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def cloud_connection_route(self):
        r"""Gets the cloud_connection_route of this ShowCloudConnectionRoutesResponse.

        :return: The cloud_connection_route of this ShowCloudConnectionRoutesResponse.
        :rtype: :class:`huaweicloudsdkcc.v3.CloudConnectionRoute`
        """
        return self._cloud_connection_route

    @cloud_connection_route.setter
    def cloud_connection_route(self, cloud_connection_route):
        r"""Sets the cloud_connection_route of this ShowCloudConnectionRoutesResponse.

        :param cloud_connection_route: The cloud_connection_route of this ShowCloudConnectionRoutesResponse.
        :type cloud_connection_route: :class:`huaweicloudsdkcc.v3.CloudConnectionRoute`
        """
        self._cloud_connection_route = cloud_connection_route

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
        if not isinstance(other, ShowCloudConnectionRoutesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
