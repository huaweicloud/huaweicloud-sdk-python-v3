# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateServerInterfaceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_id': 'str',
        'port_id': 'str',
        'body': 'UpdateNicInfoRequestBody'
    }

    attribute_map = {
        'server_id': 'server_id',
        'port_id': 'port_id',
        'body': 'body'
    }

    def __init__(self, server_id=None, port_id=None, body=None):
        r"""UpdateServerInterfaceRequest

        The model defined in huaweicloud sdk

        :param server_id: 云服务器ID。
        :type server_id: str
        :param port_id: The network card ID of the cloud server.
        :type port_id: str
        :param body: Body of the UpdateServerInterfaceRequest
        :type body: :class:`huaweicloudsdkecs.v2.UpdateNicInfoRequestBody`
        """
        
        

        self._server_id = None
        self._port_id = None
        self._body = None
        self.discriminator = None

        self.server_id = server_id
        self.port_id = port_id
        if body is not None:
            self.body = body

    @property
    def server_id(self):
        r"""Gets the server_id of this UpdateServerInterfaceRequest.

        云服务器ID。

        :return: The server_id of this UpdateServerInterfaceRequest.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this UpdateServerInterfaceRequest.

        云服务器ID。

        :param server_id: The server_id of this UpdateServerInterfaceRequest.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def port_id(self):
        r"""Gets the port_id of this UpdateServerInterfaceRequest.

        The network card ID of the cloud server.

        :return: The port_id of this UpdateServerInterfaceRequest.
        :rtype: str
        """
        return self._port_id

    @port_id.setter
    def port_id(self, port_id):
        r"""Sets the port_id of this UpdateServerInterfaceRequest.

        The network card ID of the cloud server.

        :param port_id: The port_id of this UpdateServerInterfaceRequest.
        :type port_id: str
        """
        self._port_id = port_id

    @property
    def body(self):
        r"""Gets the body of this UpdateServerInterfaceRequest.

        :return: The body of this UpdateServerInterfaceRequest.
        :rtype: :class:`huaweicloudsdkecs.v2.UpdateNicInfoRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateServerInterfaceRequest.

        :param body: The body of this UpdateServerInterfaceRequest.
        :type body: :class:`huaweicloudsdkecs.v2.UpdateNicInfoRequestBody`
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
        if not isinstance(other, UpdateServerInterfaceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
