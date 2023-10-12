# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EsListenerResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protocol': 'str',
        'id': 'str',
        'name': 'str',
        'protocol_port': 'str',
        'ipgroup': 'EsIpgroupResource'
    }

    attribute_map = {
        'protocol': 'protocol',
        'id': 'id',
        'name': 'name',
        'protocol_port': 'protocol_port',
        'ipgroup': 'ipgroup'
    }

    def __init__(self, protocol=None, id=None, name=None, protocol_port=None, ipgroup=None):
        """EsListenerResponse

        The model defined in huaweicloud sdk

        :param protocol: 监听器的监听协议。
        :type protocol: str
        :param id: 监听器ID。
        :type id: str
        :param name: 监听器的名称。
        :type name: str
        :param protocol_port: 监听器的前端监听端口。
        :type protocol_port: str
        :param ipgroup: 
        :type ipgroup: :class:`huaweicloudsdkcss.v1.EsIpgroupResource`
        """
        
        

        self._protocol = None
        self._id = None
        self._name = None
        self._protocol_port = None
        self._ipgroup = None
        self.discriminator = None

        if protocol is not None:
            self.protocol = protocol
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if protocol_port is not None:
            self.protocol_port = protocol_port
        if ipgroup is not None:
            self.ipgroup = ipgroup

    @property
    def protocol(self):
        """Gets the protocol of this EsListenerResponse.

        监听器的监听协议。

        :return: The protocol of this EsListenerResponse.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this EsListenerResponse.

        监听器的监听协议。

        :param protocol: The protocol of this EsListenerResponse.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def id(self):
        """Gets the id of this EsListenerResponse.

        监听器ID。

        :return: The id of this EsListenerResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EsListenerResponse.

        监听器ID。

        :param id: The id of this EsListenerResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this EsListenerResponse.

        监听器的名称。

        :return: The name of this EsListenerResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EsListenerResponse.

        监听器的名称。

        :param name: The name of this EsListenerResponse.
        :type name: str
        """
        self._name = name

    @property
    def protocol_port(self):
        """Gets the protocol_port of this EsListenerResponse.

        监听器的前端监听端口。

        :return: The protocol_port of this EsListenerResponse.
        :rtype: str
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this EsListenerResponse.

        监听器的前端监听端口。

        :param protocol_port: The protocol_port of this EsListenerResponse.
        :type protocol_port: str
        """
        self._protocol_port = protocol_port

    @property
    def ipgroup(self):
        """Gets the ipgroup of this EsListenerResponse.

        :return: The ipgroup of this EsListenerResponse.
        :rtype: :class:`huaweicloudsdkcss.v1.EsIpgroupResource`
        """
        return self._ipgroup

    @ipgroup.setter
    def ipgroup(self, ipgroup):
        """Sets the ipgroup of this EsListenerResponse.

        :param ipgroup: The ipgroup of this EsListenerResponse.
        :type ipgroup: :class:`huaweicloudsdkcss.v1.EsIpgroupResource`
        """
        self._ipgroup = ipgroup

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
        if not isinstance(other, EsListenerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
