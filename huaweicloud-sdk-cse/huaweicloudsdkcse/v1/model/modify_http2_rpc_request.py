# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyHttp2RpcRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'gateway_id': 'str',
        'http2_rpc_id': 'str',
        'accept': 'str',
        'body': 'Http2Rpc'
    }

    attribute_map = {
        'gateway_id': 'gateway_id',
        'http2_rpc_id': 'http2Rpc_id',
        'accept': 'Accept',
        'body': 'body'
    }

    def __init__(self, gateway_id=None, http2_rpc_id=None, accept=None, body=None):
        """ModifyHttp2RpcRequest

        The model defined in huaweicloud sdk

        :param gateway_id: 网关实例id
        :type gateway_id: str
        :param http2_rpc_id: http2Rpc id
        :type http2_rpc_id: str
        :param accept: 该字段内容填为 \&quot;application/json\&quot;
        :type accept: str
        :param body: Body of the ModifyHttp2RpcRequest
        :type body: :class:`huaweicloudsdkcse.v1.Http2Rpc`
        """
        
        

        self._gateway_id = None
        self._http2_rpc_id = None
        self._accept = None
        self._body = None
        self.discriminator = None

        self.gateway_id = gateway_id
        self.http2_rpc_id = http2_rpc_id
        if accept is not None:
            self.accept = accept
        if body is not None:
            self.body = body

    @property
    def gateway_id(self):
        """Gets the gateway_id of this ModifyHttp2RpcRequest.

        网关实例id

        :return: The gateway_id of this ModifyHttp2RpcRequest.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """Sets the gateway_id of this ModifyHttp2RpcRequest.

        网关实例id

        :param gateway_id: The gateway_id of this ModifyHttp2RpcRequest.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

    @property
    def http2_rpc_id(self):
        """Gets the http2_rpc_id of this ModifyHttp2RpcRequest.

        http2Rpc id

        :return: The http2_rpc_id of this ModifyHttp2RpcRequest.
        :rtype: str
        """
        return self._http2_rpc_id

    @http2_rpc_id.setter
    def http2_rpc_id(self, http2_rpc_id):
        """Sets the http2_rpc_id of this ModifyHttp2RpcRequest.

        http2Rpc id

        :param http2_rpc_id: The http2_rpc_id of this ModifyHttp2RpcRequest.
        :type http2_rpc_id: str
        """
        self._http2_rpc_id = http2_rpc_id

    @property
    def accept(self):
        """Gets the accept of this ModifyHttp2RpcRequest.

        该字段内容填为 \"application/json\"

        :return: The accept of this ModifyHttp2RpcRequest.
        :rtype: str
        """
        return self._accept

    @accept.setter
    def accept(self, accept):
        """Sets the accept of this ModifyHttp2RpcRequest.

        该字段内容填为 \"application/json\"

        :param accept: The accept of this ModifyHttp2RpcRequest.
        :type accept: str
        """
        self._accept = accept

    @property
    def body(self):
        """Gets the body of this ModifyHttp2RpcRequest.

        :return: The body of this ModifyHttp2RpcRequest.
        :rtype: :class:`huaweicloudsdkcse.v1.Http2Rpc`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ModifyHttp2RpcRequest.

        :param body: The body of this ModifyHttp2RpcRequest.
        :type body: :class:`huaweicloudsdkcse.v1.Http2Rpc`
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
        if not isinstance(other, ModifyHttp2RpcRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
