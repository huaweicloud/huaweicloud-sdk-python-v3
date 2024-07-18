# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVpnServerRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_client_token')

    openapi_types = {
        'p2c_vgw_id': 'str',
        'x_client_token': 'str',
        'body': 'CreateServerRequestBody'
    }

    attribute_map = {
        'p2c_vgw_id': 'p2c_vgw_id',
        'x_client_token': 'X-Client-Token',
        'body': 'body'
    }

    def __init__(self, p2c_vgw_id=None, x_client_token=None, body=None):
        """CreateVpnServerRequest

        The model defined in huaweicloud sdk

        :param p2c_vgw_id: P2C VPN网关实例ID
        :type p2c_vgw_id: str
        :param x_client_token: 幂等性标识
        :type x_client_token: str
        :param body: Body of the CreateVpnServerRequest
        :type body: :class:`huaweicloudsdkvpn.v5.CreateServerRequestBody`
        """
        
        

        self._p2c_vgw_id = None
        self._x_client_token = None
        self._body = None
        self.discriminator = None

        self.p2c_vgw_id = p2c_vgw_id
        if x_client_token is not None:
            self.x_client_token = x_client_token
        if body is not None:
            self.body = body

    @property
    def p2c_vgw_id(self):
        """Gets the p2c_vgw_id of this CreateVpnServerRequest.

        P2C VPN网关实例ID

        :return: The p2c_vgw_id of this CreateVpnServerRequest.
        :rtype: str
        """
        return self._p2c_vgw_id

    @p2c_vgw_id.setter
    def p2c_vgw_id(self, p2c_vgw_id):
        """Sets the p2c_vgw_id of this CreateVpnServerRequest.

        P2C VPN网关实例ID

        :param p2c_vgw_id: The p2c_vgw_id of this CreateVpnServerRequest.
        :type p2c_vgw_id: str
        """
        self._p2c_vgw_id = p2c_vgw_id

    @property
    def x_client_token(self):
        """Gets the x_client_token of this CreateVpnServerRequest.

        幂等性标识

        :return: The x_client_token of this CreateVpnServerRequest.
        :rtype: str
        """
        return self._x_client_token

    @x_client_token.setter
    def x_client_token(self, x_client_token):
        """Sets the x_client_token of this CreateVpnServerRequest.

        幂等性标识

        :param x_client_token: The x_client_token of this CreateVpnServerRequest.
        :type x_client_token: str
        """
        self._x_client_token = x_client_token

    @property
    def body(self):
        """Gets the body of this CreateVpnServerRequest.

        :return: The body of this CreateVpnServerRequest.
        :rtype: :class:`huaweicloudsdkvpn.v5.CreateServerRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateVpnServerRequest.

        :param body: The body of this CreateVpnServerRequest.
        :type body: :class:`huaweicloudsdkvpn.v5.CreateServerRequestBody`
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
        if not isinstance(other, CreateVpnServerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
