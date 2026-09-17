# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Nic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eth': 'str',
        'ip': 'str',
        'mask_len': 'int'
    }

    attribute_map = {
        'eth': 'eth',
        'ip': 'ip',
        'mask_len': 'mask_len'
    }

    def __init__(self, eth=None, ip=None, mask_len=None):
        r"""Nic

        The model defined in huaweicloud sdk

        :param eth: 网卡信息，如eth0,eth1
        :type eth: str
        :param ip: 网卡ip
        :type ip: str
        :param mask_len: 子网掩码的位数
        :type mask_len: int
        """
        
        

        self._eth = None
        self._ip = None
        self._mask_len = None
        self.discriminator = None

        if eth is not None:
            self.eth = eth
        if ip is not None:
            self.ip = ip
        if mask_len is not None:
            self.mask_len = mask_len

    @property
    def eth(self):
        r"""Gets the eth of this Nic.

        网卡信息，如eth0,eth1

        :return: The eth of this Nic.
        :rtype: str
        """
        return self._eth

    @eth.setter
    def eth(self, eth):
        r"""Sets the eth of this Nic.

        网卡信息，如eth0,eth1

        :param eth: The eth of this Nic.
        :type eth: str
        """
        self._eth = eth

    @property
    def ip(self):
        r"""Gets the ip of this Nic.

        网卡ip

        :return: The ip of this Nic.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this Nic.

        网卡ip

        :param ip: The ip of this Nic.
        :type ip: str
        """
        self._ip = ip

    @property
    def mask_len(self):
        r"""Gets the mask_len of this Nic.

        子网掩码的位数

        :return: The mask_len of this Nic.
        :rtype: int
        """
        return self._mask_len

    @mask_len.setter
    def mask_len(self, mask_len):
        r"""Sets the mask_len of this Nic.

        子网掩码的位数

        :param mask_len: The mask_len of this Nic.
        :type mask_len: int
        """
        self._mask_len = mask_len

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
        if not isinstance(other, Nic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
