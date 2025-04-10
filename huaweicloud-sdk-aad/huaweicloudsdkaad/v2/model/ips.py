# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Ips:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ip_id': 'str',
        'ip': 'str',
        'isp': 'str',
        'data_center': 'str',
        'foreign_switch_status': 'int',
        'udp_switch_status': 'int'
    }

    attribute_map = {
        'ip_id': 'ip_id',
        'ip': 'ip',
        'isp': 'isp',
        'data_center': 'data_center',
        'foreign_switch_status': 'foreign_switch_status',
        'udp_switch_status': 'udp_switch_status'
    }

    def __init__(self, ip_id=None, ip=None, isp=None, data_center=None, foreign_switch_status=None, udp_switch_status=None):
        r"""Ips

        The model defined in huaweicloud sdk

        :param ip_id: ip id
        :type ip_id: str
        :param ip: ip
        :type ip: str
        :param isp: 线路
        :type isp: str
        :param data_center: 数据中心
        :type data_center: str
        :param foreign_switch_status: 海外区域封禁状态 0-关闭 1-开启
        :type foreign_switch_status: int
        :param udp_switch_status: UDP协议禁用 0-关闭 1-开启
        :type udp_switch_status: int
        """
        
        

        self._ip_id = None
        self._ip = None
        self._isp = None
        self._data_center = None
        self._foreign_switch_status = None
        self._udp_switch_status = None
        self.discriminator = None

        if ip_id is not None:
            self.ip_id = ip_id
        if ip is not None:
            self.ip = ip
        if isp is not None:
            self.isp = isp
        if data_center is not None:
            self.data_center = data_center
        if foreign_switch_status is not None:
            self.foreign_switch_status = foreign_switch_status
        if udp_switch_status is not None:
            self.udp_switch_status = udp_switch_status

    @property
    def ip_id(self):
        r"""Gets the ip_id of this Ips.

        ip id

        :return: The ip_id of this Ips.
        :rtype: str
        """
        return self._ip_id

    @ip_id.setter
    def ip_id(self, ip_id):
        r"""Sets the ip_id of this Ips.

        ip id

        :param ip_id: The ip_id of this Ips.
        :type ip_id: str
        """
        self._ip_id = ip_id

    @property
    def ip(self):
        r"""Gets the ip of this Ips.

        ip

        :return: The ip of this Ips.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this Ips.

        ip

        :param ip: The ip of this Ips.
        :type ip: str
        """
        self._ip = ip

    @property
    def isp(self):
        r"""Gets the isp of this Ips.

        线路

        :return: The isp of this Ips.
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        r"""Sets the isp of this Ips.

        线路

        :param isp: The isp of this Ips.
        :type isp: str
        """
        self._isp = isp

    @property
    def data_center(self):
        r"""Gets the data_center of this Ips.

        数据中心

        :return: The data_center of this Ips.
        :rtype: str
        """
        return self._data_center

    @data_center.setter
    def data_center(self, data_center):
        r"""Sets the data_center of this Ips.

        数据中心

        :param data_center: The data_center of this Ips.
        :type data_center: str
        """
        self._data_center = data_center

    @property
    def foreign_switch_status(self):
        r"""Gets the foreign_switch_status of this Ips.

        海外区域封禁状态 0-关闭 1-开启

        :return: The foreign_switch_status of this Ips.
        :rtype: int
        """
        return self._foreign_switch_status

    @foreign_switch_status.setter
    def foreign_switch_status(self, foreign_switch_status):
        r"""Sets the foreign_switch_status of this Ips.

        海外区域封禁状态 0-关闭 1-开启

        :param foreign_switch_status: The foreign_switch_status of this Ips.
        :type foreign_switch_status: int
        """
        self._foreign_switch_status = foreign_switch_status

    @property
    def udp_switch_status(self):
        r"""Gets the udp_switch_status of this Ips.

        UDP协议禁用 0-关闭 1-开启

        :return: The udp_switch_status of this Ips.
        :rtype: int
        """
        return self._udp_switch_status

    @udp_switch_status.setter
    def udp_switch_status(self, udp_switch_status):
        r"""Sets the udp_switch_status of this Ips.

        UDP协议禁用 0-关闭 1-开启

        :param udp_switch_status: The udp_switch_status of this Ips.
        :type udp_switch_status: int
        """
        self._udp_switch_status = udp_switch_status

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
        if not isinstance(other, Ips):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
