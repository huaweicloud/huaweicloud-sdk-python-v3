# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlowSource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_listener_address': 'str',
        'source_listener_port': 'int',
        'stream_id': 'str',
        'min_latency': 'int',
        'cidr_whitelist': 'list[str]',
        'description': 'str',
        'protocol': 'str',
        'name': 'str',
        'decryption': 'FlowSourceDecryption'
    }

    attribute_map = {
        'source_listener_address': 'source_listener_address',
        'source_listener_port': 'source_listener_port',
        'stream_id': 'stream_id',
        'min_latency': 'min_latency',
        'cidr_whitelist': 'cidr_whitelist',
        'description': 'description',
        'protocol': 'protocol',
        'name': 'name',
        'decryption': 'decryption'
    }

    def __init__(self, source_listener_address=None, source_listener_port=None, stream_id=None, min_latency=None, cidr_whitelist=None, description=None, protocol=None, name=None, decryption=None):
        r"""FlowSource

        The model defined in huaweicloud sdk

        :param source_listener_address: 拉流地址
        :type source_listener_address: str
        :param source_listener_port: 拉流端口，2077/2088不可选
        :type source_listener_port: int
        :param stream_id: srt拉流streamid
        :type stream_id: str
        :param min_latency: 最小时延，单位ms
        :type min_latency: int
        :param cidr_whitelist: 推流CIDR IP白名单列表
        :type cidr_whitelist: list[str]
        :param description: 描述
        :type description: str
        :param protocol: 协议，srt-caller，srt-listener
        :type protocol: str
        :param name: 入流资源名称
        :type name: str
        :param decryption: 
        :type decryption: :class:`huaweicloudsdklive.v1.FlowSourceDecryption`
        """
        
        

        self._source_listener_address = None
        self._source_listener_port = None
        self._stream_id = None
        self._min_latency = None
        self._cidr_whitelist = None
        self._description = None
        self._protocol = None
        self._name = None
        self._decryption = None
        self.discriminator = None

        if source_listener_address is not None:
            self.source_listener_address = source_listener_address
        if source_listener_port is not None:
            self.source_listener_port = source_listener_port
        if stream_id is not None:
            self.stream_id = stream_id
        if min_latency is not None:
            self.min_latency = min_latency
        if cidr_whitelist is not None:
            self.cidr_whitelist = cidr_whitelist
        if description is not None:
            self.description = description
        self.protocol = protocol
        self.name = name
        if decryption is not None:
            self.decryption = decryption

    @property
    def source_listener_address(self):
        r"""Gets the source_listener_address of this FlowSource.

        拉流地址

        :return: The source_listener_address of this FlowSource.
        :rtype: str
        """
        return self._source_listener_address

    @source_listener_address.setter
    def source_listener_address(self, source_listener_address):
        r"""Sets the source_listener_address of this FlowSource.

        拉流地址

        :param source_listener_address: The source_listener_address of this FlowSource.
        :type source_listener_address: str
        """
        self._source_listener_address = source_listener_address

    @property
    def source_listener_port(self):
        r"""Gets the source_listener_port of this FlowSource.

        拉流端口，2077/2088不可选

        :return: The source_listener_port of this FlowSource.
        :rtype: int
        """
        return self._source_listener_port

    @source_listener_port.setter
    def source_listener_port(self, source_listener_port):
        r"""Sets the source_listener_port of this FlowSource.

        拉流端口，2077/2088不可选

        :param source_listener_port: The source_listener_port of this FlowSource.
        :type source_listener_port: int
        """
        self._source_listener_port = source_listener_port

    @property
    def stream_id(self):
        r"""Gets the stream_id of this FlowSource.

        srt拉流streamid

        :return: The stream_id of this FlowSource.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        r"""Sets the stream_id of this FlowSource.

        srt拉流streamid

        :param stream_id: The stream_id of this FlowSource.
        :type stream_id: str
        """
        self._stream_id = stream_id

    @property
    def min_latency(self):
        r"""Gets the min_latency of this FlowSource.

        最小时延，单位ms

        :return: The min_latency of this FlowSource.
        :rtype: int
        """
        return self._min_latency

    @min_latency.setter
    def min_latency(self, min_latency):
        r"""Sets the min_latency of this FlowSource.

        最小时延，单位ms

        :param min_latency: The min_latency of this FlowSource.
        :type min_latency: int
        """
        self._min_latency = min_latency

    @property
    def cidr_whitelist(self):
        r"""Gets the cidr_whitelist of this FlowSource.

        推流CIDR IP白名单列表

        :return: The cidr_whitelist of this FlowSource.
        :rtype: list[str]
        """
        return self._cidr_whitelist

    @cidr_whitelist.setter
    def cidr_whitelist(self, cidr_whitelist):
        r"""Sets the cidr_whitelist of this FlowSource.

        推流CIDR IP白名单列表

        :param cidr_whitelist: The cidr_whitelist of this FlowSource.
        :type cidr_whitelist: list[str]
        """
        self._cidr_whitelist = cidr_whitelist

    @property
    def description(self):
        r"""Gets the description of this FlowSource.

        描述

        :return: The description of this FlowSource.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this FlowSource.

        描述

        :param description: The description of this FlowSource.
        :type description: str
        """
        self._description = description

    @property
    def protocol(self):
        r"""Gets the protocol of this FlowSource.

        协议，srt-caller，srt-listener

        :return: The protocol of this FlowSource.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this FlowSource.

        协议，srt-caller，srt-listener

        :param protocol: The protocol of this FlowSource.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def name(self):
        r"""Gets the name of this FlowSource.

        入流资源名称

        :return: The name of this FlowSource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this FlowSource.

        入流资源名称

        :param name: The name of this FlowSource.
        :type name: str
        """
        self._name = name

    @property
    def decryption(self):
        r"""Gets the decryption of this FlowSource.

        :return: The decryption of this FlowSource.
        :rtype: :class:`huaweicloudsdklive.v1.FlowSourceDecryption`
        """
        return self._decryption

    @decryption.setter
    def decryption(self, decryption):
        r"""Sets the decryption of this FlowSource.

        :param decryption: The decryption of this FlowSource.
        :type decryption: :class:`huaweicloudsdklive.v1.FlowSourceDecryption`
        """
        self._decryption = decryption

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
        if not isinstance(other, FlowSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
