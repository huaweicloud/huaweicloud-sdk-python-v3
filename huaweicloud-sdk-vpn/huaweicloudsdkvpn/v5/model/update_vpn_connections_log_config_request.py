# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVpnConnectionsLogConfigRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'p2c_vgw_id': 'str',
        'body': 'UpdateVpnLogConfigRequestBody'
    }

    attribute_map = {
        'p2c_vgw_id': 'p2c_vgw_id',
        'body': 'body'
    }

    def __init__(self, p2c_vgw_id=None, body=None):
        r"""UpdateVpnConnectionsLogConfigRequest

        The model defined in huaweicloud sdk

        :param p2c_vgw_id: P2C VPN网关实例ID
        :type p2c_vgw_id: str
        :param body: Body of the UpdateVpnConnectionsLogConfigRequest
        :type body: :class:`huaweicloudsdkvpn.v5.UpdateVpnLogConfigRequestBody`
        """
        
        

        self._p2c_vgw_id = None
        self._body = None
        self.discriminator = None

        self.p2c_vgw_id = p2c_vgw_id
        if body is not None:
            self.body = body

    @property
    def p2c_vgw_id(self):
        r"""Gets the p2c_vgw_id of this UpdateVpnConnectionsLogConfigRequest.

        P2C VPN网关实例ID

        :return: The p2c_vgw_id of this UpdateVpnConnectionsLogConfigRequest.
        :rtype: str
        """
        return self._p2c_vgw_id

    @p2c_vgw_id.setter
    def p2c_vgw_id(self, p2c_vgw_id):
        r"""Sets the p2c_vgw_id of this UpdateVpnConnectionsLogConfigRequest.

        P2C VPN网关实例ID

        :param p2c_vgw_id: The p2c_vgw_id of this UpdateVpnConnectionsLogConfigRequest.
        :type p2c_vgw_id: str
        """
        self._p2c_vgw_id = p2c_vgw_id

    @property
    def body(self):
        r"""Gets the body of this UpdateVpnConnectionsLogConfigRequest.

        :return: The body of this UpdateVpnConnectionsLogConfigRequest.
        :rtype: :class:`huaweicloudsdkvpn.v5.UpdateVpnLogConfigRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateVpnConnectionsLogConfigRequest.

        :param body: The body of this UpdateVpnConnectionsLogConfigRequest.
        :type body: :class:`huaweicloudsdkvpn.v5.UpdateVpnLogConfigRequestBody`
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
        if not isinstance(other, UpdateVpnConnectionsLogConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
