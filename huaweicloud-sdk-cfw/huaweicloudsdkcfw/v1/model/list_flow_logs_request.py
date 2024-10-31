# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlowLogsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fw_instance_id': 'str',
        'direction': 'str',
        'log_type': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'src_ip': 'str',
        'src_port': 'int',
        'dst_ip': 'str',
        'dst_port': 'int',
        'protocol': 'str',
        'app': 'str',
        'log_id': 'str',
        'next_date': 'int',
        'offset': 'int',
        'limit': 'int',
        'enterprise_project_id': 'str',
        'dst_host': 'str',
        'src_region_name': 'str',
        'dst_region_name': 'str',
        'src_province_name': 'str',
        'dst_province_name': 'str',
        'src_city_name': 'str',
        'dst_city_name': 'str'
    }

    attribute_map = {
        'fw_instance_id': 'fw_instance_id',
        'direction': 'direction',
        'log_type': 'log_type',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'src_ip': 'src_ip',
        'src_port': 'src_port',
        'dst_ip': 'dst_ip',
        'dst_port': 'dst_port',
        'protocol': 'protocol',
        'app': 'app',
        'log_id': 'log_id',
        'next_date': 'next_date',
        'offset': 'offset',
        'limit': 'limit',
        'enterprise_project_id': 'enterprise_project_id',
        'dst_host': 'dst_host',
        'src_region_name': 'src_region_name',
        'dst_region_name': 'dst_region_name',
        'src_province_name': 'src_province_name',
        'dst_province_name': 'dst_province_name',
        'src_city_name': 'src_city_name',
        'dst_city_name': 'dst_city_name'
    }

    def __init__(self, fw_instance_id=None, direction=None, log_type=None, start_time=None, end_time=None, src_ip=None, src_port=None, dst_ip=None, dst_port=None, protocol=None, app=None, log_id=None, next_date=None, offset=None, limit=None, enterprise_project_id=None, dst_host=None, src_region_name=None, dst_region_name=None, src_province_name=None, dst_province_name=None, src_city_name=None, dst_city_name=None):
        """ListFlowLogsRequest

        The model defined in huaweicloud sdk

        :param fw_instance_id: 防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取
        :type fw_instance_id: str
        :param direction: 方向，包含in2out，out2in
        :type direction: str
        :param log_type: 日志类型包括：internet，vpc，nat
        :type log_type: str
        :param start_time: 开始时间，以毫秒为单位的时间戳，如1718936272648
        :type start_time: int
        :param end_time: 结束时间，以毫秒为单位的时间戳，如1718936272648
        :type end_time: int
        :param src_ip: 源IP
        :type src_ip: str
        :param src_port: 源端口
        :type src_port: int
        :param dst_ip: 目的IP
        :type dst_ip: str
        :param dst_port: 目的端口
        :type dst_port: int
        :param protocol: 协议类型，包含TCP, UDP,ICMP,ICMPV6等。
        :type protocol: str
        :param app: 规则应用类型包括：“HTTP”，\&quot;HTTPS\&quot;，\&quot;TLS1\&quot;，“DNS”，“SSH”，“MYSQL”，“SMTP”，“RDP”，“RDPS”，“VNC”，“POP3”，“IMAP4”，“SMTPS”，“POP3S”，“FTPS”，“ANY”,“BGP”等。
        :type app: str
        :param log_id: 文档ID,第一页为空，其他页不为空，其他页可取上一次查询最后一条数据的log_id
        :type log_id: str
        :param next_date: 下个日期，当是第一页时为空，不是第一页时不为空，其他页可取上一次查询最后一条数据的start_time
        :type next_date: int
        :param offset: 偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于0，首页时为空，非首页时不为空
        :type offset: int
        :param limit: 每页显示个数，范围为1-1024
        :type limit: int
        :param enterprise_project_id: 企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0
        :type enterprise_project_id: str
        :param dst_host: 目的主机
        :type dst_host: str
        :param src_region_name: 源region名称
        :type src_region_name: str
        :param dst_region_name: 目的region名称
        :type dst_region_name: str
        :param src_province_name: 源省份名称
        :type src_province_name: str
        :param dst_province_name: 目的省份名称
        :type dst_province_name: str
        :param src_city_name: 源城市名称
        :type src_city_name: str
        :param dst_city_name: 目的城市名称
        :type dst_city_name: str
        """
        
        

        self._fw_instance_id = None
        self._direction = None
        self._log_type = None
        self._start_time = None
        self._end_time = None
        self._src_ip = None
        self._src_port = None
        self._dst_ip = None
        self._dst_port = None
        self._protocol = None
        self._app = None
        self._log_id = None
        self._next_date = None
        self._offset = None
        self._limit = None
        self._enterprise_project_id = None
        self._dst_host = None
        self._src_region_name = None
        self._dst_region_name = None
        self._src_province_name = None
        self._dst_province_name = None
        self._src_city_name = None
        self._dst_city_name = None
        self.discriminator = None

        self.fw_instance_id = fw_instance_id
        if direction is not None:
            self.direction = direction
        if log_type is not None:
            self.log_type = log_type
        self.start_time = start_time
        self.end_time = end_time
        if src_ip is not None:
            self.src_ip = src_ip
        if src_port is not None:
            self.src_port = src_port
        if dst_ip is not None:
            self.dst_ip = dst_ip
        if dst_port is not None:
            self.dst_port = dst_port
        if protocol is not None:
            self.protocol = protocol
        if app is not None:
            self.app = app
        if log_id is not None:
            self.log_id = log_id
        if next_date is not None:
            self.next_date = next_date
        if offset is not None:
            self.offset = offset
        self.limit = limit
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if dst_host is not None:
            self.dst_host = dst_host
        if src_region_name is not None:
            self.src_region_name = src_region_name
        if dst_region_name is not None:
            self.dst_region_name = dst_region_name
        if src_province_name is not None:
            self.src_province_name = src_province_name
        if dst_province_name is not None:
            self.dst_province_name = dst_province_name
        if src_city_name is not None:
            self.src_city_name = src_city_name
        if dst_city_name is not None:
            self.dst_city_name = dst_city_name

    @property
    def fw_instance_id(self):
        """Gets the fw_instance_id of this ListFlowLogsRequest.

        防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :return: The fw_instance_id of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        """Sets the fw_instance_id of this ListFlowLogsRequest.

        防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :param fw_instance_id: The fw_instance_id of this ListFlowLogsRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def direction(self):
        """Gets the direction of this ListFlowLogsRequest.

        方向，包含in2out，out2in

        :return: The direction of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this ListFlowLogsRequest.

        方向，包含in2out，out2in

        :param direction: The direction of this ListFlowLogsRequest.
        :type direction: str
        """
        self._direction = direction

    @property
    def log_type(self):
        """Gets the log_type of this ListFlowLogsRequest.

        日志类型包括：internet，vpc，nat

        :return: The log_type of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        """Sets the log_type of this ListFlowLogsRequest.

        日志类型包括：internet，vpc，nat

        :param log_type: The log_type of this ListFlowLogsRequest.
        :type log_type: str
        """
        self._log_type = log_type

    @property
    def start_time(self):
        """Gets the start_time of this ListFlowLogsRequest.

        开始时间，以毫秒为单位的时间戳，如1718936272648

        :return: The start_time of this ListFlowLogsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListFlowLogsRequest.

        开始时间，以毫秒为单位的时间戳，如1718936272648

        :param start_time: The start_time of this ListFlowLogsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListFlowLogsRequest.

        结束时间，以毫秒为单位的时间戳，如1718936272648

        :return: The end_time of this ListFlowLogsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListFlowLogsRequest.

        结束时间，以毫秒为单位的时间戳，如1718936272648

        :param end_time: The end_time of this ListFlowLogsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def src_ip(self):
        """Gets the src_ip of this ListFlowLogsRequest.

        源IP

        :return: The src_ip of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._src_ip

    @src_ip.setter
    def src_ip(self, src_ip):
        """Sets the src_ip of this ListFlowLogsRequest.

        源IP

        :param src_ip: The src_ip of this ListFlowLogsRequest.
        :type src_ip: str
        """
        self._src_ip = src_ip

    @property
    def src_port(self):
        """Gets the src_port of this ListFlowLogsRequest.

        源端口

        :return: The src_port of this ListFlowLogsRequest.
        :rtype: int
        """
        return self._src_port

    @src_port.setter
    def src_port(self, src_port):
        """Sets the src_port of this ListFlowLogsRequest.

        源端口

        :param src_port: The src_port of this ListFlowLogsRequest.
        :type src_port: int
        """
        self._src_port = src_port

    @property
    def dst_ip(self):
        """Gets the dst_ip of this ListFlowLogsRequest.

        目的IP

        :return: The dst_ip of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._dst_ip

    @dst_ip.setter
    def dst_ip(self, dst_ip):
        """Sets the dst_ip of this ListFlowLogsRequest.

        目的IP

        :param dst_ip: The dst_ip of this ListFlowLogsRequest.
        :type dst_ip: str
        """
        self._dst_ip = dst_ip

    @property
    def dst_port(self):
        """Gets the dst_port of this ListFlowLogsRequest.

        目的端口

        :return: The dst_port of this ListFlowLogsRequest.
        :rtype: int
        """
        return self._dst_port

    @dst_port.setter
    def dst_port(self, dst_port):
        """Sets the dst_port of this ListFlowLogsRequest.

        目的端口

        :param dst_port: The dst_port of this ListFlowLogsRequest.
        :type dst_port: int
        """
        self._dst_port = dst_port

    @property
    def protocol(self):
        """Gets the protocol of this ListFlowLogsRequest.

        协议类型，包含TCP, UDP,ICMP,ICMPV6等。

        :return: The protocol of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ListFlowLogsRequest.

        协议类型，包含TCP, UDP,ICMP,ICMPV6等。

        :param protocol: The protocol of this ListFlowLogsRequest.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def app(self):
        """Gets the app of this ListFlowLogsRequest.

        规则应用类型包括：“HTTP”，\"HTTPS\"，\"TLS1\"，“DNS”，“SSH”，“MYSQL”，“SMTP”，“RDP”，“RDPS”，“VNC”，“POP3”，“IMAP4”，“SMTPS”，“POP3S”，“FTPS”，“ANY”,“BGP”等。

        :return: The app of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this ListFlowLogsRequest.

        规则应用类型包括：“HTTP”，\"HTTPS\"，\"TLS1\"，“DNS”，“SSH”，“MYSQL”，“SMTP”，“RDP”，“RDPS”，“VNC”，“POP3”，“IMAP4”，“SMTPS”，“POP3S”，“FTPS”，“ANY”,“BGP”等。

        :param app: The app of this ListFlowLogsRequest.
        :type app: str
        """
        self._app = app

    @property
    def log_id(self):
        """Gets the log_id of this ListFlowLogsRequest.

        文档ID,第一页为空，其他页不为空，其他页可取上一次查询最后一条数据的log_id

        :return: The log_id of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._log_id

    @log_id.setter
    def log_id(self, log_id):
        """Sets the log_id of this ListFlowLogsRequest.

        文档ID,第一页为空，其他页不为空，其他页可取上一次查询最后一条数据的log_id

        :param log_id: The log_id of this ListFlowLogsRequest.
        :type log_id: str
        """
        self._log_id = log_id

    @property
    def next_date(self):
        """Gets the next_date of this ListFlowLogsRequest.

        下个日期，当是第一页时为空，不是第一页时不为空，其他页可取上一次查询最后一条数据的start_time

        :return: The next_date of this ListFlowLogsRequest.
        :rtype: int
        """
        return self._next_date

    @next_date.setter
    def next_date(self, next_date):
        """Sets the next_date of this ListFlowLogsRequest.

        下个日期，当是第一页时为空，不是第一页时不为空，其他页可取上一次查询最后一条数据的start_time

        :param next_date: The next_date of this ListFlowLogsRequest.
        :type next_date: int
        """
        self._next_date = next_date

    @property
    def offset(self):
        """Gets the offset of this ListFlowLogsRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于0，首页时为空，非首页时不为空

        :return: The offset of this ListFlowLogsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListFlowLogsRequest.

        偏移量：指定返回记录的开始位置，必须为数字，取值范围为大于0，首页时为空，非首页时不为空

        :param offset: The offset of this ListFlowLogsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListFlowLogsRequest.

        每页显示个数，范围为1-1024

        :return: The limit of this ListFlowLogsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListFlowLogsRequest.

        每页显示个数，范围为1-1024

        :param limit: The limit of this ListFlowLogsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListFlowLogsRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :return: The enterprise_project_id of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListFlowLogsRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :param enterprise_project_id: The enterprise_project_id of this ListFlowLogsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def dst_host(self):
        """Gets the dst_host of this ListFlowLogsRequest.

        目的主机

        :return: The dst_host of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._dst_host

    @dst_host.setter
    def dst_host(self, dst_host):
        """Sets the dst_host of this ListFlowLogsRequest.

        目的主机

        :param dst_host: The dst_host of this ListFlowLogsRequest.
        :type dst_host: str
        """
        self._dst_host = dst_host

    @property
    def src_region_name(self):
        """Gets the src_region_name of this ListFlowLogsRequest.

        源region名称

        :return: The src_region_name of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._src_region_name

    @src_region_name.setter
    def src_region_name(self, src_region_name):
        """Sets the src_region_name of this ListFlowLogsRequest.

        源region名称

        :param src_region_name: The src_region_name of this ListFlowLogsRequest.
        :type src_region_name: str
        """
        self._src_region_name = src_region_name

    @property
    def dst_region_name(self):
        """Gets the dst_region_name of this ListFlowLogsRequest.

        目的region名称

        :return: The dst_region_name of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._dst_region_name

    @dst_region_name.setter
    def dst_region_name(self, dst_region_name):
        """Sets the dst_region_name of this ListFlowLogsRequest.

        目的region名称

        :param dst_region_name: The dst_region_name of this ListFlowLogsRequest.
        :type dst_region_name: str
        """
        self._dst_region_name = dst_region_name

    @property
    def src_province_name(self):
        """Gets the src_province_name of this ListFlowLogsRequest.

        源省份名称

        :return: The src_province_name of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._src_province_name

    @src_province_name.setter
    def src_province_name(self, src_province_name):
        """Sets the src_province_name of this ListFlowLogsRequest.

        源省份名称

        :param src_province_name: The src_province_name of this ListFlowLogsRequest.
        :type src_province_name: str
        """
        self._src_province_name = src_province_name

    @property
    def dst_province_name(self):
        """Gets the dst_province_name of this ListFlowLogsRequest.

        目的省份名称

        :return: The dst_province_name of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._dst_province_name

    @dst_province_name.setter
    def dst_province_name(self, dst_province_name):
        """Sets the dst_province_name of this ListFlowLogsRequest.

        目的省份名称

        :param dst_province_name: The dst_province_name of this ListFlowLogsRequest.
        :type dst_province_name: str
        """
        self._dst_province_name = dst_province_name

    @property
    def src_city_name(self):
        """Gets the src_city_name of this ListFlowLogsRequest.

        源城市名称

        :return: The src_city_name of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._src_city_name

    @src_city_name.setter
    def src_city_name(self, src_city_name):
        """Sets the src_city_name of this ListFlowLogsRequest.

        源城市名称

        :param src_city_name: The src_city_name of this ListFlowLogsRequest.
        :type src_city_name: str
        """
        self._src_city_name = src_city_name

    @property
    def dst_city_name(self):
        """Gets the dst_city_name of this ListFlowLogsRequest.

        目的城市名称

        :return: The dst_city_name of this ListFlowLogsRequest.
        :rtype: str
        """
        return self._dst_city_name

    @dst_city_name.setter
    def dst_city_name(self, dst_city_name):
        """Sets the dst_city_name of this ListFlowLogsRequest.

        目的城市名称

        :param dst_city_name: The dst_city_name of this ListFlowLogsRequest.
        :type dst_city_name: str
        """
        self._dst_city_name = dst_city_name

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
        if not isinstance(other, ListFlowLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
