# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConnectionMonitorsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connection_monitors': 'list[ConnectionMonitorInfo]',
        'request_id': 'str'
    }

    attribute_map = {
        'connection_monitors': 'connection_monitors',
        'request_id': 'request_id'
    }

    def __init__(self, connection_monitors=None, request_id=None):
        """ListConnectionMonitorsResponse

        The model defined in huaweicloud sdk

        :param connection_monitors: 
        :type connection_monitors: list[:class:`huaweicloudsdkvpn.v5.ConnectionMonitorInfo`]
        :param request_id: 请求id
        :type request_id: str
        """
        
        super(ListConnectionMonitorsResponse, self).__init__()

        self._connection_monitors = None
        self._request_id = None
        self.discriminator = None

        if connection_monitors is not None:
            self.connection_monitors = connection_monitors
        if request_id is not None:
            self.request_id = request_id

    @property
    def connection_monitors(self):
        """Gets the connection_monitors of this ListConnectionMonitorsResponse.

        :return: The connection_monitors of this ListConnectionMonitorsResponse.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.ConnectionMonitorInfo`]
        """
        return self._connection_monitors

    @connection_monitors.setter
    def connection_monitors(self, connection_monitors):
        """Sets the connection_monitors of this ListConnectionMonitorsResponse.

        :param connection_monitors: The connection_monitors of this ListConnectionMonitorsResponse.
        :type connection_monitors: list[:class:`huaweicloudsdkvpn.v5.ConnectionMonitorInfo`]
        """
        self._connection_monitors = connection_monitors

    @property
    def request_id(self):
        """Gets the request_id of this ListConnectionMonitorsResponse.

        请求id

        :return: The request_id of this ListConnectionMonitorsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListConnectionMonitorsResponse.

        请求id

        :param request_id: The request_id of this ListConnectionMonitorsResponse.
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
        if not isinstance(other, ListConnectionMonitorsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
