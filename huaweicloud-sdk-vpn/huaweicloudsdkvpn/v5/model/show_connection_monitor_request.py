# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConnectionMonitorRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connection_monitor_id': 'str'
    }

    attribute_map = {
        'connection_monitor_id': 'connection_monitor_id'
    }

    def __init__(self, connection_monitor_id=None):
        """ShowConnectionMonitorRequest

        The model defined in huaweicloud sdk

        :param connection_monitor_id: VPN连接监控的ID
        :type connection_monitor_id: str
        """
        
        

        self._connection_monitor_id = None
        self.discriminator = None

        self.connection_monitor_id = connection_monitor_id

    @property
    def connection_monitor_id(self):
        """Gets the connection_monitor_id of this ShowConnectionMonitorRequest.

        VPN连接监控的ID

        :return: The connection_monitor_id of this ShowConnectionMonitorRequest.
        :rtype: str
        """
        return self._connection_monitor_id

    @connection_monitor_id.setter
    def connection_monitor_id(self, connection_monitor_id):
        """Sets the connection_monitor_id of this ShowConnectionMonitorRequest.

        VPN连接监控的ID

        :param connection_monitor_id: The connection_monitor_id of this ShowConnectionMonitorRequest.
        :type connection_monitor_id: str
        """
        self._connection_monitor_id = connection_monitor_id

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
        if not isinstance(other, ShowConnectionMonitorRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
