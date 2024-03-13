# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFirewallRequest:

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
        'x_client_token': 'str',
        'x_trace_id': 'str',
        'body': 'CreateFirewallReq'
    }

    attribute_map = {
        'x_client_token': 'X-Client-Token',
        'x_trace_id': 'X-Trace-Id',
        'body': 'body'
    }

    def __init__(self, x_client_token=None, x_trace_id=None, body=None):
        """CreateFirewallRequest

        The model defined in huaweicloud sdk

        :param x_client_token: 保证客户端请求幂等性的标识。  该标识为32位UUID格式，由客户端生成，且需确保不同请求之间该标识具有唯一性。
        :type x_client_token: str
        :param x_trace_id: 
        :type x_trace_id: str
        :param body: Body of the CreateFirewallRequest
        :type body: :class:`huaweicloudsdkcfw.v1.CreateFirewallReq`
        """
        
        

        self._x_client_token = None
        self._x_trace_id = None
        self._body = None
        self.discriminator = None

        if x_client_token is not None:
            self.x_client_token = x_client_token
        if x_trace_id is not None:
            self.x_trace_id = x_trace_id
        if body is not None:
            self.body = body

    @property
    def x_client_token(self):
        """Gets the x_client_token of this CreateFirewallRequest.

        保证客户端请求幂等性的标识。  该标识为32位UUID格式，由客户端生成，且需确保不同请求之间该标识具有唯一性。

        :return: The x_client_token of this CreateFirewallRequest.
        :rtype: str
        """
        return self._x_client_token

    @x_client_token.setter
    def x_client_token(self, x_client_token):
        """Sets the x_client_token of this CreateFirewallRequest.

        保证客户端请求幂等性的标识。  该标识为32位UUID格式，由客户端生成，且需确保不同请求之间该标识具有唯一性。

        :param x_client_token: The x_client_token of this CreateFirewallRequest.
        :type x_client_token: str
        """
        self._x_client_token = x_client_token

    @property
    def x_trace_id(self):
        """Gets the x_trace_id of this CreateFirewallRequest.

        :return: The x_trace_id of this CreateFirewallRequest.
        :rtype: str
        """
        return self._x_trace_id

    @x_trace_id.setter
    def x_trace_id(self, x_trace_id):
        """Sets the x_trace_id of this CreateFirewallRequest.

        :param x_trace_id: The x_trace_id of this CreateFirewallRequest.
        :type x_trace_id: str
        """
        self._x_trace_id = x_trace_id

    @property
    def body(self):
        """Gets the body of this CreateFirewallRequest.

        :return: The body of this CreateFirewallRequest.
        :rtype: :class:`huaweicloudsdkcfw.v1.CreateFirewallReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateFirewallRequest.

        :param body: The body of this CreateFirewallRequest.
        :type body: :class:`huaweicloudsdkcfw.v1.CreateFirewallReq`
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
        if not isinstance(other, CreateFirewallRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
