# coding: utf-8

import re
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
        'cloud_connection_route': 'CloudConnectionRoute',
        'request_id': 'str'
    }

    attribute_map = {
        'cloud_connection_route': 'cloud_connection_route',
        'request_id': 'request_id'
    }

    def __init__(self, cloud_connection_route=None, request_id=None):
        """ShowCloudConnectionRoutesResponse

        The model defined in huaweicloud sdk

        :param cloud_connection_route: 
        :type cloud_connection_route: :class:`huaweicloudsdkcc.v3.CloudConnectionRoute`
        :param request_id: 请求ID。
        :type request_id: str
        """
        
        super(ShowCloudConnectionRoutesResponse, self).__init__()

        self._cloud_connection_route = None
        self._request_id = None
        self.discriminator = None

        if cloud_connection_route is not None:
            self.cloud_connection_route = cloud_connection_route
        if request_id is not None:
            self.request_id = request_id

    @property
    def cloud_connection_route(self):
        """Gets the cloud_connection_route of this ShowCloudConnectionRoutesResponse.

        :return: The cloud_connection_route of this ShowCloudConnectionRoutesResponse.
        :rtype: :class:`huaweicloudsdkcc.v3.CloudConnectionRoute`
        """
        return self._cloud_connection_route

    @cloud_connection_route.setter
    def cloud_connection_route(self, cloud_connection_route):
        """Sets the cloud_connection_route of this ShowCloudConnectionRoutesResponse.

        :param cloud_connection_route: The cloud_connection_route of this ShowCloudConnectionRoutesResponse.
        :type cloud_connection_route: :class:`huaweicloudsdkcc.v3.CloudConnectionRoute`
        """
        self._cloud_connection_route = cloud_connection_route

    @property
    def request_id(self):
        """Gets the request_id of this ShowCloudConnectionRoutesResponse.

        请求ID。

        :return: The request_id of this ShowCloudConnectionRoutesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ShowCloudConnectionRoutesResponse.

        请求ID。

        :param request_id: The request_id of this ShowCloudConnectionRoutesResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
