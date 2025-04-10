# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpQueryCfwFlowLogsResponseDTODataRecords:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bytes': 'float',
        'direction': 'str',
        'packets': 'int',
        'start_time': 'int',
        'end_time': 'int',
        'log_id': 'str',
        'src_ip': 'str',
        'src_port': 'int',
        'dst_ip': 'str',
        'app': 'str',
        'dst_port': 'int',
        'protocol': 'str',
        'dst_host': 'str',
        'dst_region_id': 'str',
        'dst_region_name': 'str',
        'src_region_id': 'str',
        'src_region_name': 'str',
        'dst_province_id': 'str',
        'dst_province_name': 'str',
        'dst_city_id': 'str',
        'dst_city_name': 'str',
        'src_province_id': 'str',
        'src_province_name': 'str',
        'src_city_id': 'str',
        'src_city_name': 'str'
    }

    attribute_map = {
        'bytes': 'bytes',
        'direction': 'direction',
        'packets': 'packets',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'log_id': 'log_id',
        'src_ip': 'src_ip',
        'src_port': 'src_port',
        'dst_ip': 'dst_ip',
        'app': 'app',
        'dst_port': 'dst_port',
        'protocol': 'protocol',
        'dst_host': 'dst_host',
        'dst_region_id': 'dst_region_id',
        'dst_region_name': 'dst_region_name',
        'src_region_id': 'src_region_id',
        'src_region_name': 'src_region_name',
        'dst_province_id': 'dst_province_id',
        'dst_province_name': 'dst_province_name',
        'dst_city_id': 'dst_city_id',
        'dst_city_name': 'dst_city_name',
        'src_province_id': 'src_province_id',
        'src_province_name': 'src_province_name',
        'src_city_id': 'src_city_id',
        'src_city_name': 'src_city_name'
    }

    def __init__(self, bytes=None, direction=None, packets=None, start_time=None, end_time=None, log_id=None, src_ip=None, src_port=None, dst_ip=None, app=None, dst_port=None, protocol=None, dst_host=None, dst_region_id=None, dst_region_name=None, src_region_id=None, src_region_name=None, dst_province_id=None, dst_province_name=None, dst_city_id=None, dst_city_name=None, src_province_id=None, src_province_name=None, src_city_id=None, src_city_name=None):
        r"""HttpQueryCfwFlowLogsResponseDTODataRecords

        The model defined in huaweicloud sdk

        :param bytes: 字节
        :type bytes: float
        :param direction: 方向，有内到外（in2out）和外到内（out2in）两种
        :type direction: str
        :param packets: 字节包数
        :type packets: int
        :param start_time: 开始时间，以毫秒为单位的时间戳，如1718936272648
        :type start_time: int
        :param end_time: 结束时间，以毫秒为单位的时间戳，如1718936272648
        :type end_time: int
        :param log_id: 文档ID
        :type log_id: str
        :param src_ip: 源IP
        :type src_ip: str
        :param src_port: 源端口
        :type src_port: int
        :param dst_ip: 目的IP
        :type dst_ip: str
        :param app: 规则应用类型包括：“HTTP”，\&quot;HTTPS\&quot;，\&quot;TLS1\&quot;，“DNS”，“SSH”，“MYSQL”，“SMTP”，“RDP”，“RDPS”，“VNC”，“POP3”，“IMAP4”，“SMTPS”，“POP3S”，“FTPS”，“ANY”,“BGP”等。
        :type app: str
        :param dst_port: 目的端口
        :type dst_port: int
        :param protocol: 协议类型:TCP为6,UDP为17,ICMP为1,ICMPV6为58,ANY为-1,手动类型不为空，自动类型为空
        :type protocol: str
        :param dst_host: 目标主机
        :type dst_host: str
        :param dst_region_id: 目的地域id
        :type dst_region_id: str
        :param dst_region_name: 目的地域名称
        :type dst_region_name: str
        :param src_region_id: 源地域id
        :type src_region_id: str
        :param src_region_name: 源地域名称
        :type src_region_name: str
        :param dst_province_id: 目的省份id
        :type dst_province_id: str
        :param dst_province_name: 目的省份名称
        :type dst_province_name: str
        :param dst_city_id: 目的城市id
        :type dst_city_id: str
        :param dst_city_name: 目的城市名称
        :type dst_city_name: str
        :param src_province_id: 源省份id
        :type src_province_id: str
        :param src_province_name: 源省份名称
        :type src_province_name: str
        :param src_city_id: 源城市id
        :type src_city_id: str
        :param src_city_name: 源城市名称
        :type src_city_name: str
        """
        
        

        self._bytes = None
        self._direction = None
        self._packets = None
        self._start_time = None
        self._end_time = None
        self._log_id = None
        self._src_ip = None
        self._src_port = None
        self._dst_ip = None
        self._app = None
        self._dst_port = None
        self._protocol = None
        self._dst_host = None
        self._dst_region_id = None
        self._dst_region_name = None
        self._src_region_id = None
        self._src_region_name = None
        self._dst_province_id = None
        self._dst_province_name = None
        self._dst_city_id = None
        self._dst_city_name = None
        self._src_province_id = None
        self._src_province_name = None
        self._src_city_id = None
        self._src_city_name = None
        self.discriminator = None

        if bytes is not None:
            self.bytes = bytes
        if direction is not None:
            self.direction = direction
        if packets is not None:
            self.packets = packets
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if log_id is not None:
            self.log_id = log_id
        if src_ip is not None:
            self.src_ip = src_ip
        if src_port is not None:
            self.src_port = src_port
        if dst_ip is not None:
            self.dst_ip = dst_ip
        if app is not None:
            self.app = app
        if dst_port is not None:
            self.dst_port = dst_port
        if protocol is not None:
            self.protocol = protocol
        if dst_host is not None:
            self.dst_host = dst_host
        if dst_region_id is not None:
            self.dst_region_id = dst_region_id
        if dst_region_name is not None:
            self.dst_region_name = dst_region_name
        if src_region_id is not None:
            self.src_region_id = src_region_id
        if src_region_name is not None:
            self.src_region_name = src_region_name
        if dst_province_id is not None:
            self.dst_province_id = dst_province_id
        if dst_province_name is not None:
            self.dst_province_name = dst_province_name
        if dst_city_id is not None:
            self.dst_city_id = dst_city_id
        if dst_city_name is not None:
            self.dst_city_name = dst_city_name
        if src_province_id is not None:
            self.src_province_id = src_province_id
        if src_province_name is not None:
            self.src_province_name = src_province_name
        if src_city_id is not None:
            self.src_city_id = src_city_id
        if src_city_name is not None:
            self.src_city_name = src_city_name

    @property
    def bytes(self):
        r"""Gets the bytes of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        字节

        :return: The bytes of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :rtype: float
        """
        return self._bytes

    @bytes.setter
    def bytes(self, bytes):
        r"""Sets the bytes of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        字节

        :param bytes: The bytes of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :type bytes: float
        """
        self._bytes = bytes

    @property
    def direction(self):
        r"""Gets the direction of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        方向，有内到外（in2out）和外到内（out2in）两种

        :return: The direction of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        r"""Sets the direction of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        方向，有内到外（in2out）和外到内（out2in）两种

        :param direction: The direction of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :type direction: str
        """
        self._direction = direction

    @property
    def packets(self):
        r"""Gets the packets of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        字节包数

        :return: The packets of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :rtype: int
        """
        return self._packets

    @packets.setter
    def packets(self, packets):
        r"""Sets the packets of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        字节包数

        :param packets: The packets of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :type packets: int
        """
        self._packets = packets

    @property
    def start_time(self):
        r"""Gets the start_time of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        开始时间，以毫秒为单位的时间戳，如1718936272648

        :return: The start_time of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        开始时间，以毫秒为单位的时间戳，如1718936272648

        :param start_time: The start_time of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        结束时间，以毫秒为单位的时间戳，如1718936272648

        :return: The end_time of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        结束时间，以毫秒为单位的时间戳，如1718936272648

        :param end_time: The end_time of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def log_id(self):
        r"""Gets the log_id of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        文档ID

        :return: The log_id of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._log_id

    @log_id.setter
    def log_id(self, log_id):
        r"""Sets the log_id of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        文档ID

        :param log_id: The log_id of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :type log_id: str
        """
        self._log_id = log_id

    @property
    def src_ip(self):
        r"""Gets the src_ip of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        源IP

        :return: The src_ip of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._src_ip

    @src_ip.setter
    def src_ip(self, src_ip):
        r"""Sets the src_ip of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        源IP

        :param src_ip: The src_ip of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :type src_ip: str
        """
        self._src_ip = src_ip

    @property
    def src_port(self):
        r"""Gets the src_port of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        源端口

        :return: The src_port of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :rtype: int
        """
        return self._src_port

    @src_port.setter
    def src_port(self, src_port):
        r"""Sets the src_port of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        源端口

        :param src_port: The src_port of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :type src_port: int
        """
        self._src_port = src_port

    @property
    def dst_ip(self):
        r"""Gets the dst_ip of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        目的IP

        :return: The dst_ip of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._dst_ip

    @dst_ip.setter
    def dst_ip(self, dst_ip):
        r"""Sets the dst_ip of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        目的IP

        :param dst_ip: The dst_ip of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :type dst_ip: str
        """
        self._dst_ip = dst_ip

    @property
    def app(self):
        r"""Gets the app of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        规则应用类型包括：“HTTP”，\"HTTPS\"，\"TLS1\"，“DNS”，“SSH”，“MYSQL”，“SMTP”，“RDP”，“RDPS”，“VNC”，“POP3”，“IMAP4”，“SMTPS”，“POP3S”，“FTPS”，“ANY”,“BGP”等。

        :return: The app of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        规则应用类型包括：“HTTP”，\"HTTPS\"，\"TLS1\"，“DNS”，“SSH”，“MYSQL”，“SMTP”，“RDP”，“RDPS”，“VNC”，“POP3”，“IMAP4”，“SMTPS”，“POP3S”，“FTPS”，“ANY”,“BGP”等。

        :param app: The app of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :type app: str
        """
        self._app = app

    @property
    def dst_port(self):
        r"""Gets the dst_port of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        目的端口

        :return: The dst_port of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :rtype: int
        """
        return self._dst_port

    @dst_port.setter
    def dst_port(self, dst_port):
        r"""Sets the dst_port of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        目的端口

        :param dst_port: The dst_port of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :type dst_port: int
        """
        self._dst_port = dst_port

    @property
    def protocol(self):
        r"""Gets the protocol of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        协议类型:TCP为6,UDP为17,ICMP为1,ICMPV6为58,ANY为-1,手动类型不为空，自动类型为空

        :return: The protocol of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        协议类型:TCP为6,UDP为17,ICMP为1,ICMPV6为58,ANY为-1,手动类型不为空，自动类型为空

        :param protocol: The protocol of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def dst_host(self):
        r"""Gets the dst_host of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        目标主机

        :return: The dst_host of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._dst_host

    @dst_host.setter
    def dst_host(self, dst_host):
        r"""Sets the dst_host of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        目标主机

        :param dst_host: The dst_host of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :type dst_host: str
        """
        self._dst_host = dst_host

    @property
    def dst_region_id(self):
        r"""Gets the dst_region_id of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        目的地域id

        :return: The dst_region_id of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._dst_region_id

    @dst_region_id.setter
    def dst_region_id(self, dst_region_id):
        r"""Sets the dst_region_id of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        目的地域id

        :param dst_region_id: The dst_region_id of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :type dst_region_id: str
        """
        self._dst_region_id = dst_region_id

    @property
    def dst_region_name(self):
        r"""Gets the dst_region_name of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        目的地域名称

        :return: The dst_region_name of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._dst_region_name

    @dst_region_name.setter
    def dst_region_name(self, dst_region_name):
        r"""Sets the dst_region_name of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        目的地域名称

        :param dst_region_name: The dst_region_name of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :type dst_region_name: str
        """
        self._dst_region_name = dst_region_name

    @property
    def src_region_id(self):
        r"""Gets the src_region_id of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        源地域id

        :return: The src_region_id of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._src_region_id

    @src_region_id.setter
    def src_region_id(self, src_region_id):
        r"""Sets the src_region_id of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        源地域id

        :param src_region_id: The src_region_id of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :type src_region_id: str
        """
        self._src_region_id = src_region_id

    @property
    def src_region_name(self):
        r"""Gets the src_region_name of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        源地域名称

        :return: The src_region_name of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._src_region_name

    @src_region_name.setter
    def src_region_name(self, src_region_name):
        r"""Sets the src_region_name of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        源地域名称

        :param src_region_name: The src_region_name of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :type src_region_name: str
        """
        self._src_region_name = src_region_name

    @property
    def dst_province_id(self):
        r"""Gets the dst_province_id of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        目的省份id

        :return: The dst_province_id of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._dst_province_id

    @dst_province_id.setter
    def dst_province_id(self, dst_province_id):
        r"""Sets the dst_province_id of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        目的省份id

        :param dst_province_id: The dst_province_id of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :type dst_province_id: str
        """
        self._dst_province_id = dst_province_id

    @property
    def dst_province_name(self):
        r"""Gets the dst_province_name of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        目的省份名称

        :return: The dst_province_name of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._dst_province_name

    @dst_province_name.setter
    def dst_province_name(self, dst_province_name):
        r"""Sets the dst_province_name of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        目的省份名称

        :param dst_province_name: The dst_province_name of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :type dst_province_name: str
        """
        self._dst_province_name = dst_province_name

    @property
    def dst_city_id(self):
        r"""Gets the dst_city_id of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        目的城市id

        :return: The dst_city_id of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._dst_city_id

    @dst_city_id.setter
    def dst_city_id(self, dst_city_id):
        r"""Sets the dst_city_id of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        目的城市id

        :param dst_city_id: The dst_city_id of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :type dst_city_id: str
        """
        self._dst_city_id = dst_city_id

    @property
    def dst_city_name(self):
        r"""Gets the dst_city_name of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        目的城市名称

        :return: The dst_city_name of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._dst_city_name

    @dst_city_name.setter
    def dst_city_name(self, dst_city_name):
        r"""Sets the dst_city_name of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        目的城市名称

        :param dst_city_name: The dst_city_name of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :type dst_city_name: str
        """
        self._dst_city_name = dst_city_name

    @property
    def src_province_id(self):
        r"""Gets the src_province_id of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        源省份id

        :return: The src_province_id of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._src_province_id

    @src_province_id.setter
    def src_province_id(self, src_province_id):
        r"""Sets the src_province_id of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        源省份id

        :param src_province_id: The src_province_id of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :type src_province_id: str
        """
        self._src_province_id = src_province_id

    @property
    def src_province_name(self):
        r"""Gets the src_province_name of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        源省份名称

        :return: The src_province_name of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._src_province_name

    @src_province_name.setter
    def src_province_name(self, src_province_name):
        r"""Sets the src_province_name of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        源省份名称

        :param src_province_name: The src_province_name of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :type src_province_name: str
        """
        self._src_province_name = src_province_name

    @property
    def src_city_id(self):
        r"""Gets the src_city_id of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        源城市id

        :return: The src_city_id of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._src_city_id

    @src_city_id.setter
    def src_city_id(self, src_city_id):
        r"""Sets the src_city_id of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        源城市id

        :param src_city_id: The src_city_id of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :type src_city_id: str
        """
        self._src_city_id = src_city_id

    @property
    def src_city_name(self):
        r"""Gets the src_city_name of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        源城市名称

        :return: The src_city_name of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :rtype: str
        """
        return self._src_city_name

    @src_city_name.setter
    def src_city_name(self, src_city_name):
        r"""Sets the src_city_name of this HttpQueryCfwFlowLogsResponseDTODataRecords.

        源城市名称

        :param src_city_name: The src_city_name of this HttpQueryCfwFlowLogsResponseDTODataRecords.
        :type src_city_name: str
        """
        self._src_city_name = src_city_name

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
        if not isinstance(other, HttpQueryCfwFlowLogsResponseDTODataRecords):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
