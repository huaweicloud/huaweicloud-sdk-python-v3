# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVpnConnectionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpn_connection': 'CreateVpnConnectionRequestBodyContent'
    }

    attribute_map = {
        'vpn_connection': 'vpn_connection'
    }

    def __init__(self, vpn_connection=None):
        """CreateVpnConnectionRequestBody

        The model defined in huaweicloud sdk

        :param vpn_connection: 
        :type vpn_connection: :class:`huaweicloudsdkvpn.v5.CreateVpnConnectionRequestBodyContent`
        """
        
        

        self._vpn_connection = None
        self.discriminator = None

        self.vpn_connection = vpn_connection

    @property
    def vpn_connection(self):
        """Gets the vpn_connection of this CreateVpnConnectionRequestBody.

        :return: The vpn_connection of this CreateVpnConnectionRequestBody.
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateVpnConnectionRequestBodyContent`
        """
        return self._vpn_connection

    @vpn_connection.setter
    def vpn_connection(self, vpn_connection):
        """Sets the vpn_connection of this CreateVpnConnectionRequestBody.

        :param vpn_connection: The vpn_connection of this CreateVpnConnectionRequestBody.
        :type vpn_connection: :class:`huaweicloudsdkvpn.v5.CreateVpnConnectionRequestBodyContent`
        """
        self._vpn_connection = vpn_connection

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
        if not isinstance(other, CreateVpnConnectionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
