# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConnectionMonitorResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connection_monitor': 'ConnectionMonitorInfo',
        'request_id': 'str'
    }

    attribute_map = {
        'connection_monitor': 'connection_monitor',
        'request_id': 'request_id'
    }

    def __init__(self, connection_monitor=None, request_id=None):
        """ShowConnectionMonitorResponse

        The model defined in huaweicloud sdk

        :param connection_monitor: 
        :type connection_monitor: :class:`huaweicloudsdkvpn.v5.ConnectionMonitorInfo`
        :param request_id: 请求id
        :type request_id: str
        """
        
        super(ShowConnectionMonitorResponse, self).__init__()

        self._connection_monitor = None
        self._request_id = None
        self.discriminator = None

        if connection_monitor is not None:
            self.connection_monitor = connection_monitor
        if request_id is not None:
            self.request_id = request_id

    @property
    def connection_monitor(self):
        """Gets the connection_monitor of this ShowConnectionMonitorResponse.

        :return: The connection_monitor of this ShowConnectionMonitorResponse.
        :rtype: :class:`huaweicloudsdkvpn.v5.ConnectionMonitorInfo`
        """
        return self._connection_monitor

    @connection_monitor.setter
    def connection_monitor(self, connection_monitor):
        """Sets the connection_monitor of this ShowConnectionMonitorResponse.

        :param connection_monitor: The connection_monitor of this ShowConnectionMonitorResponse.
        :type connection_monitor: :class:`huaweicloudsdkvpn.v5.ConnectionMonitorInfo`
        """
        self._connection_monitor = connection_monitor

    @property
    def request_id(self):
        """Gets the request_id of this ShowConnectionMonitorResponse.

        请求id

        :return: The request_id of this ShowConnectionMonitorResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ShowConnectionMonitorResponse.

        请求id

        :param request_id: The request_id of this ShowConnectionMonitorResponse.
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
        if not isinstance(other, ShowConnectionMonitorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
