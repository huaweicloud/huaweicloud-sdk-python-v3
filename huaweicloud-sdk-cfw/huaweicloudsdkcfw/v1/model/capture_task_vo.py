# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CaptureTaskVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'capture_size': 'str',
        'created_date': 'str',
        'dest_address': 'str',
        'dest_address_type': 'int',
        'dest_port': 'str',
        'duration': 'int',
        'is_deleted': 'int',
        'max_packets': 'int',
        'modified_date': 'str',
        'name': 'str',
        'protocol': 'int',
        'remaining_days': 'int',
        'source_address': 'str',
        'source_address_type': 'int',
        'source_port': 'str',
        'status': 'int',
        'task_id': 'str'
    }

    attribute_map = {
        'capture_size': 'capture_size',
        'created_date': 'created_date',
        'dest_address': 'dest_address',
        'dest_address_type': 'dest_address_type',
        'dest_port': 'dest_port',
        'duration': 'duration',
        'is_deleted': 'is_deleted',
        'max_packets': 'max_packets',
        'modified_date': 'modified_date',
        'name': 'name',
        'protocol': 'protocol',
        'remaining_days': 'remaining_days',
        'source_address': 'source_address',
        'source_address_type': 'source_address_type',
        'source_port': 'source_port',
        'status': 'status',
        'task_id': 'task_id'
    }

    def __init__(self, capture_size=None, created_date=None, dest_address=None, dest_address_type=None, dest_port=None, duration=None, is_deleted=None, max_packets=None, modified_date=None, name=None, protocol=None, remaining_days=None, source_address=None, source_address_type=None, source_port=None, status=None, task_id=None):
        r"""CaptureTaskVO

        The model defined in huaweicloud sdk

        :param capture_size: 抓包大小,如500kb,500mb
        :type capture_size: str
        :param created_date: 抓包创建时间,如2024/08/31 10:17:30
        :type created_date: str
        :param dest_address: 目的地址
        :type dest_address: str
        :param dest_address_type: 目的地址类型0 ipv4，1 ipv6
        :type dest_address_type: int
        :param dest_port: 目的端口
        :type dest_port: str
        :param duration: 抓包时长，以分钟为单位
        :type duration: int
        :param is_deleted: 是否被删除，0否 1是
        :type is_deleted: int
        :param max_packets: 最大抓包数，以个为单位
        :type max_packets: int
        :param modified_date: 修改日期,如2024/08/31 10:17:30
        :type modified_date: str
        :param name: 抓包任务名称
        :type name: str
        :param protocol: 协议类型:TCP为6，UDP为17，ICMP为1，ICMPV6为58，ANY为-1，手动类型不为空，自动类型为空
        :type protocol: int
        :param remaining_days: 剩余保留天数
        :type remaining_days: int
        :param source_address: 源地址
        :type source_address: str
        :param source_address_type: 源地址类型0 ipv4，1 ipv6
        :type source_address_type: int
        :param source_port: 源端口
        :type source_port: str
        :param status: 抓包任务状态，如成功（1），运行中（2），已截止（4），截止中（5）
        :type status: int
        :param task_id: 抓包任务id
        :type task_id: str
        """
        
        

        self._capture_size = None
        self._created_date = None
        self._dest_address = None
        self._dest_address_type = None
        self._dest_port = None
        self._duration = None
        self._is_deleted = None
        self._max_packets = None
        self._modified_date = None
        self._name = None
        self._protocol = None
        self._remaining_days = None
        self._source_address = None
        self._source_address_type = None
        self._source_port = None
        self._status = None
        self._task_id = None
        self.discriminator = None

        if capture_size is not None:
            self.capture_size = capture_size
        if created_date is not None:
            self.created_date = created_date
        if dest_address is not None:
            self.dest_address = dest_address
        if dest_address_type is not None:
            self.dest_address_type = dest_address_type
        if dest_port is not None:
            self.dest_port = dest_port
        if duration is not None:
            self.duration = duration
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if max_packets is not None:
            self.max_packets = max_packets
        if modified_date is not None:
            self.modified_date = modified_date
        if name is not None:
            self.name = name
        if protocol is not None:
            self.protocol = protocol
        if remaining_days is not None:
            self.remaining_days = remaining_days
        if source_address is not None:
            self.source_address = source_address
        if source_address_type is not None:
            self.source_address_type = source_address_type
        if source_port is not None:
            self.source_port = source_port
        if status is not None:
            self.status = status
        if task_id is not None:
            self.task_id = task_id

    @property
    def capture_size(self):
        r"""Gets the capture_size of this CaptureTaskVO.

        抓包大小,如500kb,500mb

        :return: The capture_size of this CaptureTaskVO.
        :rtype: str
        """
        return self._capture_size

    @capture_size.setter
    def capture_size(self, capture_size):
        r"""Sets the capture_size of this CaptureTaskVO.

        抓包大小,如500kb,500mb

        :param capture_size: The capture_size of this CaptureTaskVO.
        :type capture_size: str
        """
        self._capture_size = capture_size

    @property
    def created_date(self):
        r"""Gets the created_date of this CaptureTaskVO.

        抓包创建时间,如2024/08/31 10:17:30

        :return: The created_date of this CaptureTaskVO.
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this CaptureTaskVO.

        抓包创建时间,如2024/08/31 10:17:30

        :param created_date: The created_date of this CaptureTaskVO.
        :type created_date: str
        """
        self._created_date = created_date

    @property
    def dest_address(self):
        r"""Gets the dest_address of this CaptureTaskVO.

        目的地址

        :return: The dest_address of this CaptureTaskVO.
        :rtype: str
        """
        return self._dest_address

    @dest_address.setter
    def dest_address(self, dest_address):
        r"""Sets the dest_address of this CaptureTaskVO.

        目的地址

        :param dest_address: The dest_address of this CaptureTaskVO.
        :type dest_address: str
        """
        self._dest_address = dest_address

    @property
    def dest_address_type(self):
        r"""Gets the dest_address_type of this CaptureTaskVO.

        目的地址类型0 ipv4，1 ipv6

        :return: The dest_address_type of this CaptureTaskVO.
        :rtype: int
        """
        return self._dest_address_type

    @dest_address_type.setter
    def dest_address_type(self, dest_address_type):
        r"""Sets the dest_address_type of this CaptureTaskVO.

        目的地址类型0 ipv4，1 ipv6

        :param dest_address_type: The dest_address_type of this CaptureTaskVO.
        :type dest_address_type: int
        """
        self._dest_address_type = dest_address_type

    @property
    def dest_port(self):
        r"""Gets the dest_port of this CaptureTaskVO.

        目的端口

        :return: The dest_port of this CaptureTaskVO.
        :rtype: str
        """
        return self._dest_port

    @dest_port.setter
    def dest_port(self, dest_port):
        r"""Sets the dest_port of this CaptureTaskVO.

        目的端口

        :param dest_port: The dest_port of this CaptureTaskVO.
        :type dest_port: str
        """
        self._dest_port = dest_port

    @property
    def duration(self):
        r"""Gets the duration of this CaptureTaskVO.

        抓包时长，以分钟为单位

        :return: The duration of this CaptureTaskVO.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this CaptureTaskVO.

        抓包时长，以分钟为单位

        :param duration: The duration of this CaptureTaskVO.
        :type duration: int
        """
        self._duration = duration

    @property
    def is_deleted(self):
        r"""Gets the is_deleted of this CaptureTaskVO.

        是否被删除，0否 1是

        :return: The is_deleted of this CaptureTaskVO.
        :rtype: int
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        r"""Sets the is_deleted of this CaptureTaskVO.

        是否被删除，0否 1是

        :param is_deleted: The is_deleted of this CaptureTaskVO.
        :type is_deleted: int
        """
        self._is_deleted = is_deleted

    @property
    def max_packets(self):
        r"""Gets the max_packets of this CaptureTaskVO.

        最大抓包数，以个为单位

        :return: The max_packets of this CaptureTaskVO.
        :rtype: int
        """
        return self._max_packets

    @max_packets.setter
    def max_packets(self, max_packets):
        r"""Sets the max_packets of this CaptureTaskVO.

        最大抓包数，以个为单位

        :param max_packets: The max_packets of this CaptureTaskVO.
        :type max_packets: int
        """
        self._max_packets = max_packets

    @property
    def modified_date(self):
        r"""Gets the modified_date of this CaptureTaskVO.

        修改日期,如2024/08/31 10:17:30

        :return: The modified_date of this CaptureTaskVO.
        :rtype: str
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        r"""Sets the modified_date of this CaptureTaskVO.

        修改日期,如2024/08/31 10:17:30

        :param modified_date: The modified_date of this CaptureTaskVO.
        :type modified_date: str
        """
        self._modified_date = modified_date

    @property
    def name(self):
        r"""Gets the name of this CaptureTaskVO.

        抓包任务名称

        :return: The name of this CaptureTaskVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CaptureTaskVO.

        抓包任务名称

        :param name: The name of this CaptureTaskVO.
        :type name: str
        """
        self._name = name

    @property
    def protocol(self):
        r"""Gets the protocol of this CaptureTaskVO.

        协议类型:TCP为6，UDP为17，ICMP为1，ICMPV6为58，ANY为-1，手动类型不为空，自动类型为空

        :return: The protocol of this CaptureTaskVO.
        :rtype: int
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this CaptureTaskVO.

        协议类型:TCP为6，UDP为17，ICMP为1，ICMPV6为58，ANY为-1，手动类型不为空，自动类型为空

        :param protocol: The protocol of this CaptureTaskVO.
        :type protocol: int
        """
        self._protocol = protocol

    @property
    def remaining_days(self):
        r"""Gets the remaining_days of this CaptureTaskVO.

        剩余保留天数

        :return: The remaining_days of this CaptureTaskVO.
        :rtype: int
        """
        return self._remaining_days

    @remaining_days.setter
    def remaining_days(self, remaining_days):
        r"""Sets the remaining_days of this CaptureTaskVO.

        剩余保留天数

        :param remaining_days: The remaining_days of this CaptureTaskVO.
        :type remaining_days: int
        """
        self._remaining_days = remaining_days

    @property
    def source_address(self):
        r"""Gets the source_address of this CaptureTaskVO.

        源地址

        :return: The source_address of this CaptureTaskVO.
        :rtype: str
        """
        return self._source_address

    @source_address.setter
    def source_address(self, source_address):
        r"""Sets the source_address of this CaptureTaskVO.

        源地址

        :param source_address: The source_address of this CaptureTaskVO.
        :type source_address: str
        """
        self._source_address = source_address

    @property
    def source_address_type(self):
        r"""Gets the source_address_type of this CaptureTaskVO.

        源地址类型0 ipv4，1 ipv6

        :return: The source_address_type of this CaptureTaskVO.
        :rtype: int
        """
        return self._source_address_type

    @source_address_type.setter
    def source_address_type(self, source_address_type):
        r"""Sets the source_address_type of this CaptureTaskVO.

        源地址类型0 ipv4，1 ipv6

        :param source_address_type: The source_address_type of this CaptureTaskVO.
        :type source_address_type: int
        """
        self._source_address_type = source_address_type

    @property
    def source_port(self):
        r"""Gets the source_port of this CaptureTaskVO.

        源端口

        :return: The source_port of this CaptureTaskVO.
        :rtype: str
        """
        return self._source_port

    @source_port.setter
    def source_port(self, source_port):
        r"""Sets the source_port of this CaptureTaskVO.

        源端口

        :param source_port: The source_port of this CaptureTaskVO.
        :type source_port: str
        """
        self._source_port = source_port

    @property
    def status(self):
        r"""Gets the status of this CaptureTaskVO.

        抓包任务状态，如成功（1），运行中（2），已截止（4），截止中（5）

        :return: The status of this CaptureTaskVO.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CaptureTaskVO.

        抓包任务状态，如成功（1），运行中（2），已截止（4），截止中（5）

        :param status: The status of this CaptureTaskVO.
        :type status: int
        """
        self._status = status

    @property
    def task_id(self):
        r"""Gets the task_id of this CaptureTaskVO.

        抓包任务id

        :return: The task_id of this CaptureTaskVO.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this CaptureTaskVO.

        抓包任务id

        :param task_id: The task_id of this CaptureTaskVO.
        :type task_id: str
        """
        self._task_id = task_id

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
        if not isinstance(other, CaptureTaskVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
