# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DDosStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'floating_ip_id': 'str',
        'floating_ip_address': 'str',
        'network_type': 'str',
        'status': 'str',
        'blackhole_endtime': 'int',
        'protect_type': 'str',
        'traffic_threshold': 'int',
        'http_threshold': 'int'
    }

    attribute_map = {
        'floating_ip_id': 'floating_ip_id',
        'floating_ip_address': 'floating_ip_address',
        'network_type': 'network_type',
        'status': 'status',
        'blackhole_endtime': 'blackhole_endtime',
        'protect_type': 'protect_type',
        'traffic_threshold': 'traffic_threshold',
        'http_threshold': 'http_threshold'
    }

    def __init__(self, floating_ip_id=None, floating_ip_address=None, network_type=None, status=None, blackhole_endtime=None, protect_type=None, traffic_threshold=None, http_threshold=None):
        """DDosStatus

        The model defined in huaweicloud sdk

        :param floating_ip_id: EIP的ID
        :type floating_ip_id: str
        :param floating_ip_address: 浮动IP地址
        :type floating_ip_address: str
        :param network_type: EIP所属类型，可选范围： - EIP：未绑定到ECS的EIP或绑定到ECS的EIP - ELB：绑定到ELB的EIP
        :type network_type: str
        :param status: 防护状态，可选范围： - normal：表示正常 - configging：表示设置中 - notConfig：表示未设置 - packetcleaning：表示清洗 - packetdropping：表示黑洞
        :type status: str
        :param blackhole_endtime: 黑洞结束时间
        :type blackhole_endtime: int
        :param protect_type: 防护类型
        :type protect_type: str
        :param traffic_threshold: 流量阈值
        :type traffic_threshold: int
        :param http_threshold: http流量阈值
        :type http_threshold: int
        """
        
        

        self._floating_ip_id = None
        self._floating_ip_address = None
        self._network_type = None
        self._status = None
        self._blackhole_endtime = None
        self._protect_type = None
        self._traffic_threshold = None
        self._http_threshold = None
        self.discriminator = None

        self.floating_ip_id = floating_ip_id
        self.floating_ip_address = floating_ip_address
        self.network_type = network_type
        self.status = status
        self.blackhole_endtime = blackhole_endtime
        self.protect_type = protect_type
        self.traffic_threshold = traffic_threshold
        self.http_threshold = http_threshold

    @property
    def floating_ip_id(self):
        """Gets the floating_ip_id of this DDosStatus.

        EIP的ID

        :return: The floating_ip_id of this DDosStatus.
        :rtype: str
        """
        return self._floating_ip_id

    @floating_ip_id.setter
    def floating_ip_id(self, floating_ip_id):
        """Sets the floating_ip_id of this DDosStatus.

        EIP的ID

        :param floating_ip_id: The floating_ip_id of this DDosStatus.
        :type floating_ip_id: str
        """
        self._floating_ip_id = floating_ip_id

    @property
    def floating_ip_address(self):
        """Gets the floating_ip_address of this DDosStatus.

        浮动IP地址

        :return: The floating_ip_address of this DDosStatus.
        :rtype: str
        """
        return self._floating_ip_address

    @floating_ip_address.setter
    def floating_ip_address(self, floating_ip_address):
        """Sets the floating_ip_address of this DDosStatus.

        浮动IP地址

        :param floating_ip_address: The floating_ip_address of this DDosStatus.
        :type floating_ip_address: str
        """
        self._floating_ip_address = floating_ip_address

    @property
    def network_type(self):
        """Gets the network_type of this DDosStatus.

        EIP所属类型，可选范围： - EIP：未绑定到ECS的EIP或绑定到ECS的EIP - ELB：绑定到ELB的EIP

        :return: The network_type of this DDosStatus.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """Sets the network_type of this DDosStatus.

        EIP所属类型，可选范围： - EIP：未绑定到ECS的EIP或绑定到ECS的EIP - ELB：绑定到ELB的EIP

        :param network_type: The network_type of this DDosStatus.
        :type network_type: str
        """
        self._network_type = network_type

    @property
    def status(self):
        """Gets the status of this DDosStatus.

        防护状态，可选范围： - normal：表示正常 - configging：表示设置中 - notConfig：表示未设置 - packetcleaning：表示清洗 - packetdropping：表示黑洞

        :return: The status of this DDosStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DDosStatus.

        防护状态，可选范围： - normal：表示正常 - configging：表示设置中 - notConfig：表示未设置 - packetcleaning：表示清洗 - packetdropping：表示黑洞

        :param status: The status of this DDosStatus.
        :type status: str
        """
        self._status = status

    @property
    def blackhole_endtime(self):
        """Gets the blackhole_endtime of this DDosStatus.

        黑洞结束时间

        :return: The blackhole_endtime of this DDosStatus.
        :rtype: int
        """
        return self._blackhole_endtime

    @blackhole_endtime.setter
    def blackhole_endtime(self, blackhole_endtime):
        """Sets the blackhole_endtime of this DDosStatus.

        黑洞结束时间

        :param blackhole_endtime: The blackhole_endtime of this DDosStatus.
        :type blackhole_endtime: int
        """
        self._blackhole_endtime = blackhole_endtime

    @property
    def protect_type(self):
        """Gets the protect_type of this DDosStatus.

        防护类型

        :return: The protect_type of this DDosStatus.
        :rtype: str
        """
        return self._protect_type

    @protect_type.setter
    def protect_type(self, protect_type):
        """Sets the protect_type of this DDosStatus.

        防护类型

        :param protect_type: The protect_type of this DDosStatus.
        :type protect_type: str
        """
        self._protect_type = protect_type

    @property
    def traffic_threshold(self):
        """Gets the traffic_threshold of this DDosStatus.

        流量阈值

        :return: The traffic_threshold of this DDosStatus.
        :rtype: int
        """
        return self._traffic_threshold

    @traffic_threshold.setter
    def traffic_threshold(self, traffic_threshold):
        """Sets the traffic_threshold of this DDosStatus.

        流量阈值

        :param traffic_threshold: The traffic_threshold of this DDosStatus.
        :type traffic_threshold: int
        """
        self._traffic_threshold = traffic_threshold

    @property
    def http_threshold(self):
        """Gets the http_threshold of this DDosStatus.

        http流量阈值

        :return: The http_threshold of this DDosStatus.
        :rtype: int
        """
        return self._http_threshold

    @http_threshold.setter
    def http_threshold(self, http_threshold):
        """Sets the http_threshold of this DDosStatus.

        http流量阈值

        :param http_threshold: The http_threshold of this DDosStatus.
        :type http_threshold: int
        """
        self._http_threshold = http_threshold

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
        if not isinstance(other, DDosStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
