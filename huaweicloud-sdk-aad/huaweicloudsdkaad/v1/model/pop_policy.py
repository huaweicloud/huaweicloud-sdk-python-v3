# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PopPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'block_location': 'list[str]',
        'block_protocol': 'list[str]',
        'bw_list': 'Bw',
        'connection_protection': 'bool',
        'connection_protection_list': 'list[str]',
        'fingerprint_count': 'int',
        'port_block_count': 'int',
        'watermark_count': 'int',
        'if_exist_traffic': 'bool',
        'pop': 'str'
    }

    attribute_map = {
        'block_location': 'block_location',
        'block_protocol': 'block_protocol',
        'bw_list': 'bw_list',
        'connection_protection': 'connection_protection',
        'connection_protection_list': 'connection_protection_list',
        'fingerprint_count': 'fingerprint_count',
        'port_block_count': 'port_block_count',
        'watermark_count': 'watermark_count',
        'if_exist_traffic': 'if_exist_traffic',
        'pop': 'pop'
    }

    def __init__(self, block_location=None, block_protocol=None, bw_list=None, connection_protection=None, connection_protection_list=None, fingerprint_count=None, port_block_count=None, watermark_count=None, if_exist_traffic=None, pop=None):
        r"""PopPolicy

        The model defined in huaweicloud sdk

        :param block_location: 位置封禁列表
        :type block_location: list[str]
        :param block_protocol: 协议封禁列表
        :type block_protocol: list[str]
        :param bw_list: 
        :type bw_list: :class:`huaweicloudsdkaad.v1.Bw`
        :param connection_protection: 是否开启连接防护
        :type connection_protection: bool
        :param connection_protection_list: 连接防护列表
        :type connection_protection_list: list[str]
        :param fingerprint_count: 指纹数
        :type fingerprint_count: int
        :param port_block_count: 端口封禁数
        :type port_block_count: int
        :param watermark_count: 水印数
        :type watermark_count: int
        :param if_exist_traffic: 是否存在流量
        :type if_exist_traffic: bool
        :param pop: 固定值ALL
        :type pop: str
        """
        
        

        self._block_location = None
        self._block_protocol = None
        self._bw_list = None
        self._connection_protection = None
        self._connection_protection_list = None
        self._fingerprint_count = None
        self._port_block_count = None
        self._watermark_count = None
        self._if_exist_traffic = None
        self._pop = None
        self.discriminator = None

        self.block_location = block_location
        self.block_protocol = block_protocol
        self.bw_list = bw_list
        self.connection_protection = connection_protection
        self.connection_protection_list = connection_protection_list
        self.fingerprint_count = fingerprint_count
        self.port_block_count = port_block_count
        self.watermark_count = watermark_count
        self.if_exist_traffic = if_exist_traffic
        self.pop = pop

    @property
    def block_location(self):
        r"""Gets the block_location of this PopPolicy.

        位置封禁列表

        :return: The block_location of this PopPolicy.
        :rtype: list[str]
        """
        return self._block_location

    @block_location.setter
    def block_location(self, block_location):
        r"""Sets the block_location of this PopPolicy.

        位置封禁列表

        :param block_location: The block_location of this PopPolicy.
        :type block_location: list[str]
        """
        self._block_location = block_location

    @property
    def block_protocol(self):
        r"""Gets the block_protocol of this PopPolicy.

        协议封禁列表

        :return: The block_protocol of this PopPolicy.
        :rtype: list[str]
        """
        return self._block_protocol

    @block_protocol.setter
    def block_protocol(self, block_protocol):
        r"""Sets the block_protocol of this PopPolicy.

        协议封禁列表

        :param block_protocol: The block_protocol of this PopPolicy.
        :type block_protocol: list[str]
        """
        self._block_protocol = block_protocol

    @property
    def bw_list(self):
        r"""Gets the bw_list of this PopPolicy.

        :return: The bw_list of this PopPolicy.
        :rtype: :class:`huaweicloudsdkaad.v1.Bw`
        """
        return self._bw_list

    @bw_list.setter
    def bw_list(self, bw_list):
        r"""Sets the bw_list of this PopPolicy.

        :param bw_list: The bw_list of this PopPolicy.
        :type bw_list: :class:`huaweicloudsdkaad.v1.Bw`
        """
        self._bw_list = bw_list

    @property
    def connection_protection(self):
        r"""Gets the connection_protection of this PopPolicy.

        是否开启连接防护

        :return: The connection_protection of this PopPolicy.
        :rtype: bool
        """
        return self._connection_protection

    @connection_protection.setter
    def connection_protection(self, connection_protection):
        r"""Sets the connection_protection of this PopPolicy.

        是否开启连接防护

        :param connection_protection: The connection_protection of this PopPolicy.
        :type connection_protection: bool
        """
        self._connection_protection = connection_protection

    @property
    def connection_protection_list(self):
        r"""Gets the connection_protection_list of this PopPolicy.

        连接防护列表

        :return: The connection_protection_list of this PopPolicy.
        :rtype: list[str]
        """
        return self._connection_protection_list

    @connection_protection_list.setter
    def connection_protection_list(self, connection_protection_list):
        r"""Sets the connection_protection_list of this PopPolicy.

        连接防护列表

        :param connection_protection_list: The connection_protection_list of this PopPolicy.
        :type connection_protection_list: list[str]
        """
        self._connection_protection_list = connection_protection_list

    @property
    def fingerprint_count(self):
        r"""Gets the fingerprint_count of this PopPolicy.

        指纹数

        :return: The fingerprint_count of this PopPolicy.
        :rtype: int
        """
        return self._fingerprint_count

    @fingerprint_count.setter
    def fingerprint_count(self, fingerprint_count):
        r"""Sets the fingerprint_count of this PopPolicy.

        指纹数

        :param fingerprint_count: The fingerprint_count of this PopPolicy.
        :type fingerprint_count: int
        """
        self._fingerprint_count = fingerprint_count

    @property
    def port_block_count(self):
        r"""Gets the port_block_count of this PopPolicy.

        端口封禁数

        :return: The port_block_count of this PopPolicy.
        :rtype: int
        """
        return self._port_block_count

    @port_block_count.setter
    def port_block_count(self, port_block_count):
        r"""Sets the port_block_count of this PopPolicy.

        端口封禁数

        :param port_block_count: The port_block_count of this PopPolicy.
        :type port_block_count: int
        """
        self._port_block_count = port_block_count

    @property
    def watermark_count(self):
        r"""Gets the watermark_count of this PopPolicy.

        水印数

        :return: The watermark_count of this PopPolicy.
        :rtype: int
        """
        return self._watermark_count

    @watermark_count.setter
    def watermark_count(self, watermark_count):
        r"""Sets the watermark_count of this PopPolicy.

        水印数

        :param watermark_count: The watermark_count of this PopPolicy.
        :type watermark_count: int
        """
        self._watermark_count = watermark_count

    @property
    def if_exist_traffic(self):
        r"""Gets the if_exist_traffic of this PopPolicy.

        是否存在流量

        :return: The if_exist_traffic of this PopPolicy.
        :rtype: bool
        """
        return self._if_exist_traffic

    @if_exist_traffic.setter
    def if_exist_traffic(self, if_exist_traffic):
        r"""Sets the if_exist_traffic of this PopPolicy.

        是否存在流量

        :param if_exist_traffic: The if_exist_traffic of this PopPolicy.
        :type if_exist_traffic: bool
        """
        self._if_exist_traffic = if_exist_traffic

    @property
    def pop(self):
        r"""Gets the pop of this PopPolicy.

        固定值ALL

        :return: The pop of this PopPolicy.
        :rtype: str
        """
        return self._pop

    @pop.setter
    def pop(self, pop):
        r"""Sets the pop of this PopPolicy.

        固定值ALL

        :param pop: The pop of this PopPolicy.
        :type pop: str
        """
        self._pop = pop

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
        if not isinstance(other, PopPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
