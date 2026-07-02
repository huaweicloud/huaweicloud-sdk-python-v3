# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SaInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'source_ip_cidr': 'str',
        'dest_ip_cidr': 'str',
        'packets_sent': 'float',
        'packets_recv': 'float',
        'traffic_sent': 'float',
        'traffic_recv': 'float',
        'collected_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'source_ip_cidr': 'source_ip_cidr',
        'dest_ip_cidr': 'dest_ip_cidr',
        'packets_sent': 'packets_sent',
        'packets_recv': 'packets_recv',
        'traffic_sent': 'traffic_sent',
        'traffic_recv': 'traffic_recv',
        'collected_at': 'collected_at'
    }

    def __init__(self, id=None, source_ip_cidr=None, dest_ip_cidr=None, packets_sent=None, packets_recv=None, traffic_sent=None, traffic_recv=None, collected_at=None):
        r"""SaInfo

        The model defined in huaweicloud sdk

        :param id: 网段协商ID
        :type id: str
        :param source_ip_cidr: 源IP网段
        :type source_ip_cidr: str
        :param dest_ip_cidr: 目的IP网段
        :type dest_ip_cidr: str
        :param packets_sent: 发送包
        :type packets_sent: float
        :param packets_recv: 接收包
        :type packets_recv: float
        :param traffic_sent: 发送流量(Byte)
        :type traffic_sent: float
        :param traffic_recv: 接收流量(Byte)
        :type traffic_recv: float
        :param collected_at: 数据收集时间
        :type collected_at: datetime
        """
        
        

        self._id = None
        self._source_ip_cidr = None
        self._dest_ip_cidr = None
        self._packets_sent = None
        self._packets_recv = None
        self._traffic_sent = None
        self._traffic_recv = None
        self._collected_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if source_ip_cidr is not None:
            self.source_ip_cidr = source_ip_cidr
        if dest_ip_cidr is not None:
            self.dest_ip_cidr = dest_ip_cidr
        if packets_sent is not None:
            self.packets_sent = packets_sent
        if packets_recv is not None:
            self.packets_recv = packets_recv
        if traffic_sent is not None:
            self.traffic_sent = traffic_sent
        if traffic_recv is not None:
            self.traffic_recv = traffic_recv
        if collected_at is not None:
            self.collected_at = collected_at

    @property
    def id(self):
        r"""Gets the id of this SaInfo.

        网段协商ID

        :return: The id of this SaInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SaInfo.

        网段协商ID

        :param id: The id of this SaInfo.
        :type id: str
        """
        self._id = id

    @property
    def source_ip_cidr(self):
        r"""Gets the source_ip_cidr of this SaInfo.

        源IP网段

        :return: The source_ip_cidr of this SaInfo.
        :rtype: str
        """
        return self._source_ip_cidr

    @source_ip_cidr.setter
    def source_ip_cidr(self, source_ip_cidr):
        r"""Sets the source_ip_cidr of this SaInfo.

        源IP网段

        :param source_ip_cidr: The source_ip_cidr of this SaInfo.
        :type source_ip_cidr: str
        """
        self._source_ip_cidr = source_ip_cidr

    @property
    def dest_ip_cidr(self):
        r"""Gets the dest_ip_cidr of this SaInfo.

        目的IP网段

        :return: The dest_ip_cidr of this SaInfo.
        :rtype: str
        """
        return self._dest_ip_cidr

    @dest_ip_cidr.setter
    def dest_ip_cidr(self, dest_ip_cidr):
        r"""Sets the dest_ip_cidr of this SaInfo.

        目的IP网段

        :param dest_ip_cidr: The dest_ip_cidr of this SaInfo.
        :type dest_ip_cidr: str
        """
        self._dest_ip_cidr = dest_ip_cidr

    @property
    def packets_sent(self):
        r"""Gets the packets_sent of this SaInfo.

        发送包

        :return: The packets_sent of this SaInfo.
        :rtype: float
        """
        return self._packets_sent

    @packets_sent.setter
    def packets_sent(self, packets_sent):
        r"""Sets the packets_sent of this SaInfo.

        发送包

        :param packets_sent: The packets_sent of this SaInfo.
        :type packets_sent: float
        """
        self._packets_sent = packets_sent

    @property
    def packets_recv(self):
        r"""Gets the packets_recv of this SaInfo.

        接收包

        :return: The packets_recv of this SaInfo.
        :rtype: float
        """
        return self._packets_recv

    @packets_recv.setter
    def packets_recv(self, packets_recv):
        r"""Sets the packets_recv of this SaInfo.

        接收包

        :param packets_recv: The packets_recv of this SaInfo.
        :type packets_recv: float
        """
        self._packets_recv = packets_recv

    @property
    def traffic_sent(self):
        r"""Gets the traffic_sent of this SaInfo.

        发送流量(Byte)

        :return: The traffic_sent of this SaInfo.
        :rtype: float
        """
        return self._traffic_sent

    @traffic_sent.setter
    def traffic_sent(self, traffic_sent):
        r"""Sets the traffic_sent of this SaInfo.

        发送流量(Byte)

        :param traffic_sent: The traffic_sent of this SaInfo.
        :type traffic_sent: float
        """
        self._traffic_sent = traffic_sent

    @property
    def traffic_recv(self):
        r"""Gets the traffic_recv of this SaInfo.

        接收流量(Byte)

        :return: The traffic_recv of this SaInfo.
        :rtype: float
        """
        return self._traffic_recv

    @traffic_recv.setter
    def traffic_recv(self, traffic_recv):
        r"""Sets the traffic_recv of this SaInfo.

        接收流量(Byte)

        :param traffic_recv: The traffic_recv of this SaInfo.
        :type traffic_recv: float
        """
        self._traffic_recv = traffic_recv

    @property
    def collected_at(self):
        r"""Gets the collected_at of this SaInfo.

        数据收集时间

        :return: The collected_at of this SaInfo.
        :rtype: datetime
        """
        return self._collected_at

    @collected_at.setter
    def collected_at(self, collected_at):
        r"""Sets the collected_at of this SaInfo.

        数据收集时间

        :param collected_at: The collected_at of this SaInfo.
        :type collected_at: datetime
        """
        self._collected_at = collected_at

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
