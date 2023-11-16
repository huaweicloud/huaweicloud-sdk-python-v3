# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceIpInfo:

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
        'basic_bandwidth': 'int',
        'elastic_bandwidth': 'int',
        'ip_status': 'int'
    }

    attribute_map = {
        'ip_id': 'ip_id',
        'ip': 'ip',
        'basic_bandwidth': 'basic_bandwidth',
        'elastic_bandwidth': 'elastic_bandwidth',
        'ip_status': 'ip_status'
    }

    def __init__(self, ip_id=None, ip=None, basic_bandwidth=None, elastic_bandwidth=None, ip_status=None):
        """InstanceIpInfo

        The model defined in huaweicloud sdk

        :param ip_id: IP ID
        :type ip_id: str
        :param ip: IP
        :type ip: str
        :param basic_bandwidth: 保底带宽
        :type basic_bandwidth: int
        :param elastic_bandwidth: 弹性带宽
        :type elastic_bandwidth: int
        :param ip_status: IP状态
        :type ip_status: int
        """
        
        

        self._ip_id = None
        self._ip = None
        self._basic_bandwidth = None
        self._elastic_bandwidth = None
        self._ip_status = None
        self.discriminator = None

        if ip_id is not None:
            self.ip_id = ip_id
        if ip is not None:
            self.ip = ip
        if basic_bandwidth is not None:
            self.basic_bandwidth = basic_bandwidth
        if elastic_bandwidth is not None:
            self.elastic_bandwidth = elastic_bandwidth
        if ip_status is not None:
            self.ip_status = ip_status

    @property
    def ip_id(self):
        """Gets the ip_id of this InstanceIpInfo.

        IP ID

        :return: The ip_id of this InstanceIpInfo.
        :rtype: str
        """
        return self._ip_id

    @ip_id.setter
    def ip_id(self, ip_id):
        """Sets the ip_id of this InstanceIpInfo.

        IP ID

        :param ip_id: The ip_id of this InstanceIpInfo.
        :type ip_id: str
        """
        self._ip_id = ip_id

    @property
    def ip(self):
        """Gets the ip of this InstanceIpInfo.

        IP

        :return: The ip of this InstanceIpInfo.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this InstanceIpInfo.

        IP

        :param ip: The ip of this InstanceIpInfo.
        :type ip: str
        """
        self._ip = ip

    @property
    def basic_bandwidth(self):
        """Gets the basic_bandwidth of this InstanceIpInfo.

        保底带宽

        :return: The basic_bandwidth of this InstanceIpInfo.
        :rtype: int
        """
        return self._basic_bandwidth

    @basic_bandwidth.setter
    def basic_bandwidth(self, basic_bandwidth):
        """Sets the basic_bandwidth of this InstanceIpInfo.

        保底带宽

        :param basic_bandwidth: The basic_bandwidth of this InstanceIpInfo.
        :type basic_bandwidth: int
        """
        self._basic_bandwidth = basic_bandwidth

    @property
    def elastic_bandwidth(self):
        """Gets the elastic_bandwidth of this InstanceIpInfo.

        弹性带宽

        :return: The elastic_bandwidth of this InstanceIpInfo.
        :rtype: int
        """
        return self._elastic_bandwidth

    @elastic_bandwidth.setter
    def elastic_bandwidth(self, elastic_bandwidth):
        """Sets the elastic_bandwidth of this InstanceIpInfo.

        弹性带宽

        :param elastic_bandwidth: The elastic_bandwidth of this InstanceIpInfo.
        :type elastic_bandwidth: int
        """
        self._elastic_bandwidth = elastic_bandwidth

    @property
    def ip_status(self):
        """Gets the ip_status of this InstanceIpInfo.

        IP状态

        :return: The ip_status of this InstanceIpInfo.
        :rtype: int
        """
        return self._ip_status

    @ip_status.setter
    def ip_status(self, ip_status):
        """Sets the ip_status of this InstanceIpInfo.

        IP状态

        :param ip_status: The ip_status of this InstanceIpInfo.
        :type ip_status: int
        """
        self._ip_status = ip_status

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
        if not isinstance(other, InstanceIpInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
