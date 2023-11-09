# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVpnConnectionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpn_connection_id': 'str',
        'body': 'UpdateVpnConnectionRequestBody'
    }

    attribute_map = {
        'vpn_connection_id': 'vpn_connection_id',
        'body': 'body'
    }

    def __init__(self, vpn_connection_id=None, body=None):
        """UpdateVpnConnectionRequest

        The model defined in huaweicloud sdk

        :param vpn_connection_id: vpn连接ID
        :type vpn_connection_id: str
        :param body: Body of the UpdateVpnConnectionRequest
        :type body: :class:`huaweicloudsdkvpn.v5.UpdateVpnConnectionRequestBody`
        """
        
        

        self._vpn_connection_id = None
        self._body = None
        self.discriminator = None

        self.vpn_connection_id = vpn_connection_id
        if body is not None:
            self.body = body

    @property
    def vpn_connection_id(self):
        """Gets the vpn_connection_id of this UpdateVpnConnectionRequest.

        vpn连接ID

        :return: The vpn_connection_id of this UpdateVpnConnectionRequest.
        :rtype: str
        """
        return self._vpn_connection_id

    @vpn_connection_id.setter
    def vpn_connection_id(self, vpn_connection_id):
        """Sets the vpn_connection_id of this UpdateVpnConnectionRequest.

        vpn连接ID

        :param vpn_connection_id: The vpn_connection_id of this UpdateVpnConnectionRequest.
        :type vpn_connection_id: str
        """
        self._vpn_connection_id = vpn_connection_id

    @property
    def body(self):
        """Gets the body of this UpdateVpnConnectionRequest.

        :return: The body of this UpdateVpnConnectionRequest.
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateVpnConnectionRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateVpnConnectionRequest.

        :param body: The body of this UpdateVpnConnectionRequest.
        :type body: :class:`huaweicloudsdkvpn.v5.UpdateVpnConnectionRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateVpnConnectionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
