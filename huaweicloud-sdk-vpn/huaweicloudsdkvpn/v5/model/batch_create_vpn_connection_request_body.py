# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateVpnConnectionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpn_connections': 'list[CreateVpnConnectionRequestBodyContent]'
    }

    attribute_map = {
        'vpn_connections': 'vpn_connections'
    }

    def __init__(self, vpn_connections=None):
        r"""BatchCreateVpnConnectionRequestBody

        The model defined in huaweicloud sdk

        :param vpn_connections: 
        :type vpn_connections: list[:class:`huaweicloudsdkvpn.v5.CreateVpnConnectionRequestBodyContent`]
        """
        
        

        self._vpn_connections = None
        self.discriminator = None

        self.vpn_connections = vpn_connections

    @property
    def vpn_connections(self):
        r"""Gets the vpn_connections of this BatchCreateVpnConnectionRequestBody.

        :return: The vpn_connections of this BatchCreateVpnConnectionRequestBody.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.CreateVpnConnectionRequestBodyContent`]
        """
        return self._vpn_connections

    @vpn_connections.setter
    def vpn_connections(self, vpn_connections):
        r"""Sets the vpn_connections of this BatchCreateVpnConnectionRequestBody.

        :param vpn_connections: The vpn_connections of this BatchCreateVpnConnectionRequestBody.
        :type vpn_connections: list[:class:`huaweicloudsdkvpn.v5.CreateVpnConnectionRequestBodyContent`]
        """
        self._vpn_connections = vpn_connections

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
        if not isinstance(other, BatchCreateVpnConnectionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
