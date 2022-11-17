# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEndpointConnectionsDescResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connections': 'list[ConnectionEndpoints]'
    }

    attribute_map = {
        'connections': 'connections'
    }

    def __init__(self, connections=None):
        """UpdateEndpointConnectionsDescResponse

        The model defined in huaweicloud sdk

        :param connections: 连接列表
        :type connections: list[:class:`huaweicloudsdkvpcep.v1.ConnectionEndpoints`]
        """
        
        super(UpdateEndpointConnectionsDescResponse, self).__init__()

        self._connections = None
        self.discriminator = None

        if connections is not None:
            self.connections = connections

    @property
    def connections(self):
        """Gets the connections of this UpdateEndpointConnectionsDescResponse.

        连接列表

        :return: The connections of this UpdateEndpointConnectionsDescResponse.
        :rtype: list[:class:`huaweicloudsdkvpcep.v1.ConnectionEndpoints`]
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        """Sets the connections of this UpdateEndpointConnectionsDescResponse.

        连接列表

        :param connections: The connections of this UpdateEndpointConnectionsDescResponse.
        :type connections: list[:class:`huaweicloudsdkvpcep.v1.ConnectionEndpoints`]
        """
        self._connections = connections

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
        if not isinstance(other, UpdateEndpointConnectionsDescResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
