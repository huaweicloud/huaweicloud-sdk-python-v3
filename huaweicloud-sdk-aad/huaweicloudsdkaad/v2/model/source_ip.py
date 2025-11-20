# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SourceIp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_center': 'str',
        'isp': 'str',
        'ip': 'list[str]'
    }

    attribute_map = {
        'data_center': 'data_center',
        'isp': 'isp',
        'ip': 'ip'
    }

    def __init__(self, data_center=None, isp=None, ip=None):
        r"""SourceIp

        The model defined in huaweicloud sdk

        :param data_center: 数据中心
        :type data_center: str
        :param isp: 线路
        :type isp: str
        :param ip: 实例ip
        :type ip: list[str]
        """
        
        

        self._data_center = None
        self._isp = None
        self._ip = None
        self.discriminator = None

        if data_center is not None:
            self.data_center = data_center
        if isp is not None:
            self.isp = isp
        if ip is not None:
            self.ip = ip

    @property
    def data_center(self):
        r"""Gets the data_center of this SourceIp.

        数据中心

        :return: The data_center of this SourceIp.
        :rtype: str
        """
        return self._data_center

    @data_center.setter
    def data_center(self, data_center):
        r"""Sets the data_center of this SourceIp.

        数据中心

        :param data_center: The data_center of this SourceIp.
        :type data_center: str
        """
        self._data_center = data_center

    @property
    def isp(self):
        r"""Gets the isp of this SourceIp.

        线路

        :return: The isp of this SourceIp.
        :rtype: str
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        r"""Sets the isp of this SourceIp.

        线路

        :param isp: The isp of this SourceIp.
        :type isp: str
        """
        self._isp = isp

    @property
    def ip(self):
        r"""Gets the ip of this SourceIp.

        实例ip

        :return: The ip of this SourceIp.
        :rtype: list[str]
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this SourceIp.

        实例ip

        :param ip: The ip of this SourceIp.
        :type ip: list[str]
        """
        self._ip = ip

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
        if not isinstance(other, SourceIp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
