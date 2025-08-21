# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOutputInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cidr_whitelist': 'list[str]',
        'destination': 'str',
        'name': 'str',
        'encryption': 'FlowSourceDecryption',
        'output_status': 'str',
        'listener_address': 'str',
        'port': 'int',
        'protocol': 'str',
        'stream_id': 'str',
        'description': 'str',
        'min_latency': 'int',
        'health_status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'cidr_whitelist': 'cidr_whitelist',
        'destination': 'destination',
        'name': 'name',
        'encryption': 'encryption',
        'output_status': 'output_status',
        'listener_address': 'listener_address',
        'port': 'port',
        'protocol': 'protocol',
        'stream_id': 'stream_id',
        'description': 'description',
        'min_latency': 'min_latency',
        'health_status': 'health_status',
        'type': 'type'
    }

    def __init__(self, cidr_whitelist=None, destination=None, name=None, encryption=None, output_status=None, listener_address=None, port=None, protocol=None, stream_id=None, description=None, min_latency=None, health_status=None, type=None):
        r"""ShowOutputInfoResponse

        The model defined in huaweicloud sdk

        :param cidr_whitelist: ip白名单，最大20条ip白名单
        :type cidr_whitelist: list[str]
        :param destination: 推流地址，支持ip和域名，最大值64
        :type destination: str
        :param name: output名称，有效字符：大小写字母，数字，中划线，下划线;且只能以字母开头
        :type name: str
        :param encryption: 
        :type encryption: :class:`huaweicloudsdklive.v1.FlowSourceDecryption`
        :param output_status: 输出状态，ENABLED：启用，DISABLED：禁用
        :type output_status: str
        :param listener_address: srt-listener模式，监听地址，不支持修改
        :type listener_address: str
        :param port: 端口，如果ssrt-listener为监听端口，那么srt-caller为对端端口
        :type port: int
        :param protocol: 协议，srt-caller，srt-listener
        :type protocol: str
        :param stream_id: srt-caller模式支持设置streamid
        :type stream_id: str
        :param description: 输出描述
        :type description: str
        :param min_latency: 最小时延，单位毫秒，默认值2000，最小值10，最大值15000
        :type min_latency: int
        :param health_status: 转推流状态，CONNECTED：转推中，DISCONNECTED：转推中断
        :type health_status: str
        :param type: 输出类型
        :type type: str
        """
        
        super(ShowOutputInfoResponse, self).__init__()

        self._cidr_whitelist = None
        self._destination = None
        self._name = None
        self._encryption = None
        self._output_status = None
        self._listener_address = None
        self._port = None
        self._protocol = None
        self._stream_id = None
        self._description = None
        self._min_latency = None
        self._health_status = None
        self._type = None
        self.discriminator = None

        if cidr_whitelist is not None:
            self.cidr_whitelist = cidr_whitelist
        if destination is not None:
            self.destination = destination
        if name is not None:
            self.name = name
        if encryption is not None:
            self.encryption = encryption
        if output_status is not None:
            self.output_status = output_status
        if listener_address is not None:
            self.listener_address = listener_address
        if port is not None:
            self.port = port
        if protocol is not None:
            self.protocol = protocol
        if stream_id is not None:
            self.stream_id = stream_id
        if description is not None:
            self.description = description
        if min_latency is not None:
            self.min_latency = min_latency
        if health_status is not None:
            self.health_status = health_status
        if type is not None:
            self.type = type

    @property
    def cidr_whitelist(self):
        r"""Gets the cidr_whitelist of this ShowOutputInfoResponse.

        ip白名单，最大20条ip白名单

        :return: The cidr_whitelist of this ShowOutputInfoResponse.
        :rtype: list[str]
        """
        return self._cidr_whitelist

    @cidr_whitelist.setter
    def cidr_whitelist(self, cidr_whitelist):
        r"""Sets the cidr_whitelist of this ShowOutputInfoResponse.

        ip白名单，最大20条ip白名单

        :param cidr_whitelist: The cidr_whitelist of this ShowOutputInfoResponse.
        :type cidr_whitelist: list[str]
        """
        self._cidr_whitelist = cidr_whitelist

    @property
    def destination(self):
        r"""Gets the destination of this ShowOutputInfoResponse.

        推流地址，支持ip和域名，最大值64

        :return: The destination of this ShowOutputInfoResponse.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        r"""Sets the destination of this ShowOutputInfoResponse.

        推流地址，支持ip和域名，最大值64

        :param destination: The destination of this ShowOutputInfoResponse.
        :type destination: str
        """
        self._destination = destination

    @property
    def name(self):
        r"""Gets the name of this ShowOutputInfoResponse.

        output名称，有效字符：大小写字母，数字，中划线，下划线;且只能以字母开头

        :return: The name of this ShowOutputInfoResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowOutputInfoResponse.

        output名称，有效字符：大小写字母，数字，中划线，下划线;且只能以字母开头

        :param name: The name of this ShowOutputInfoResponse.
        :type name: str
        """
        self._name = name

    @property
    def encryption(self):
        r"""Gets the encryption of this ShowOutputInfoResponse.

        :return: The encryption of this ShowOutputInfoResponse.
        :rtype: :class:`huaweicloudsdklive.v1.FlowSourceDecryption`
        """
        return self._encryption

    @encryption.setter
    def encryption(self, encryption):
        r"""Sets the encryption of this ShowOutputInfoResponse.

        :param encryption: The encryption of this ShowOutputInfoResponse.
        :type encryption: :class:`huaweicloudsdklive.v1.FlowSourceDecryption`
        """
        self._encryption = encryption

    @property
    def output_status(self):
        r"""Gets the output_status of this ShowOutputInfoResponse.

        输出状态，ENABLED：启用，DISABLED：禁用

        :return: The output_status of this ShowOutputInfoResponse.
        :rtype: str
        """
        return self._output_status

    @output_status.setter
    def output_status(self, output_status):
        r"""Sets the output_status of this ShowOutputInfoResponse.

        输出状态，ENABLED：启用，DISABLED：禁用

        :param output_status: The output_status of this ShowOutputInfoResponse.
        :type output_status: str
        """
        self._output_status = output_status

    @property
    def listener_address(self):
        r"""Gets the listener_address of this ShowOutputInfoResponse.

        srt-listener模式，监听地址，不支持修改

        :return: The listener_address of this ShowOutputInfoResponse.
        :rtype: str
        """
        return self._listener_address

    @listener_address.setter
    def listener_address(self, listener_address):
        r"""Sets the listener_address of this ShowOutputInfoResponse.

        srt-listener模式，监听地址，不支持修改

        :param listener_address: The listener_address of this ShowOutputInfoResponse.
        :type listener_address: str
        """
        self._listener_address = listener_address

    @property
    def port(self):
        r"""Gets the port of this ShowOutputInfoResponse.

        端口，如果ssrt-listener为监听端口，那么srt-caller为对端端口

        :return: The port of this ShowOutputInfoResponse.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this ShowOutputInfoResponse.

        端口，如果ssrt-listener为监听端口，那么srt-caller为对端端口

        :param port: The port of this ShowOutputInfoResponse.
        :type port: int
        """
        self._port = port

    @property
    def protocol(self):
        r"""Gets the protocol of this ShowOutputInfoResponse.

        协议，srt-caller，srt-listener

        :return: The protocol of this ShowOutputInfoResponse.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this ShowOutputInfoResponse.

        协议，srt-caller，srt-listener

        :param protocol: The protocol of this ShowOutputInfoResponse.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def stream_id(self):
        r"""Gets the stream_id of this ShowOutputInfoResponse.

        srt-caller模式支持设置streamid

        :return: The stream_id of this ShowOutputInfoResponse.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        r"""Sets the stream_id of this ShowOutputInfoResponse.

        srt-caller模式支持设置streamid

        :param stream_id: The stream_id of this ShowOutputInfoResponse.
        :type stream_id: str
        """
        self._stream_id = stream_id

    @property
    def description(self):
        r"""Gets the description of this ShowOutputInfoResponse.

        输出描述

        :return: The description of this ShowOutputInfoResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowOutputInfoResponse.

        输出描述

        :param description: The description of this ShowOutputInfoResponse.
        :type description: str
        """
        self._description = description

    @property
    def min_latency(self):
        r"""Gets the min_latency of this ShowOutputInfoResponse.

        最小时延，单位毫秒，默认值2000，最小值10，最大值15000

        :return: The min_latency of this ShowOutputInfoResponse.
        :rtype: int
        """
        return self._min_latency

    @min_latency.setter
    def min_latency(self, min_latency):
        r"""Sets the min_latency of this ShowOutputInfoResponse.

        最小时延，单位毫秒，默认值2000，最小值10，最大值15000

        :param min_latency: The min_latency of this ShowOutputInfoResponse.
        :type min_latency: int
        """
        self._min_latency = min_latency

    @property
    def health_status(self):
        r"""Gets the health_status of this ShowOutputInfoResponse.

        转推流状态，CONNECTED：转推中，DISCONNECTED：转推中断

        :return: The health_status of this ShowOutputInfoResponse.
        :rtype: str
        """
        return self._health_status

    @health_status.setter
    def health_status(self, health_status):
        r"""Sets the health_status of this ShowOutputInfoResponse.

        转推流状态，CONNECTED：转推中，DISCONNECTED：转推中断

        :param health_status: The health_status of this ShowOutputInfoResponse.
        :type health_status: str
        """
        self._health_status = health_status

    @property
    def type(self):
        r"""Gets the type of this ShowOutputInfoResponse.

        输出类型

        :return: The type of this ShowOutputInfoResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowOutputInfoResponse.

        输出类型

        :param type: The type of this ShowOutputInfoResponse.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ShowOutputInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
