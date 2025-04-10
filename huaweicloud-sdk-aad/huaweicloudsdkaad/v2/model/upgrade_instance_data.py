# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeInstanceData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'basic_bandwidth': 'str',
        'elastic_bandwidth': 'str',
        'service_bandwidth': 'int',
        'port_num': 'int',
        'bind_domain_num': 'int',
        'elastic_service_bandwidth_type': 'int',
        'elastic_service_bandwidth': 'int',
        'basic_qps': 'int'
    }

    attribute_map = {
        'basic_bandwidth': 'basic_bandwidth',
        'elastic_bandwidth': 'elastic_bandwidth',
        'service_bandwidth': 'service_bandwidth',
        'port_num': 'port_num',
        'bind_domain_num': 'bind_domain_num',
        'elastic_service_bandwidth_type': 'elastic_service_bandwidth_type',
        'elastic_service_bandwidth': 'elastic_service_bandwidth',
        'basic_qps': 'basic_qps'
    }

    def __init__(self, basic_bandwidth=None, elastic_bandwidth=None, service_bandwidth=None, port_num=None, bind_domain_num=None, elastic_service_bandwidth_type=None, elastic_service_bandwidth=None, basic_qps=None):
        r"""UpgradeInstanceData

        The model defined in huaweicloud sdk

        :param basic_bandwidth: 保底带宽(G)
        :type basic_bandwidth: str
        :param elastic_bandwidth: 弹性带宽(G)
        :type elastic_bandwidth: str
        :param service_bandwidth: 业务带宽
        :type service_bandwidth: int
        :param port_num: 端口数
        :type port_num: int
        :param bind_domain_num: 域名数
        :type bind_domain_num: int
        :param elastic_service_bandwidth_type: 弹性业务带宽,0-关闭，3-月95
        :type elastic_service_bandwidth_type: int
        :param elastic_service_bandwidth: 弹性业务带宽增加值
        :type elastic_service_bandwidth: int
        :param basic_qps: 业务QPS(如果实例没购买过QPS，需要在页面上升级一次规格开通QPS，之后才可以通过接口修改规格)
        :type basic_qps: int
        """
        
        

        self._basic_bandwidth = None
        self._elastic_bandwidth = None
        self._service_bandwidth = None
        self._port_num = None
        self._bind_domain_num = None
        self._elastic_service_bandwidth_type = None
        self._elastic_service_bandwidth = None
        self._basic_qps = None
        self.discriminator = None

        if basic_bandwidth is not None:
            self.basic_bandwidth = basic_bandwidth
        if elastic_bandwidth is not None:
            self.elastic_bandwidth = elastic_bandwidth
        if service_bandwidth is not None:
            self.service_bandwidth = service_bandwidth
        if port_num is not None:
            self.port_num = port_num
        if bind_domain_num is not None:
            self.bind_domain_num = bind_domain_num
        if elastic_service_bandwidth_type is not None:
            self.elastic_service_bandwidth_type = elastic_service_bandwidth_type
        if elastic_service_bandwidth is not None:
            self.elastic_service_bandwidth = elastic_service_bandwidth
        if basic_qps is not None:
            self.basic_qps = basic_qps

    @property
    def basic_bandwidth(self):
        r"""Gets the basic_bandwidth of this UpgradeInstanceData.

        保底带宽(G)

        :return: The basic_bandwidth of this UpgradeInstanceData.
        :rtype: str
        """
        return self._basic_bandwidth

    @basic_bandwidth.setter
    def basic_bandwidth(self, basic_bandwidth):
        r"""Sets the basic_bandwidth of this UpgradeInstanceData.

        保底带宽(G)

        :param basic_bandwidth: The basic_bandwidth of this UpgradeInstanceData.
        :type basic_bandwidth: str
        """
        self._basic_bandwidth = basic_bandwidth

    @property
    def elastic_bandwidth(self):
        r"""Gets the elastic_bandwidth of this UpgradeInstanceData.

        弹性带宽(G)

        :return: The elastic_bandwidth of this UpgradeInstanceData.
        :rtype: str
        """
        return self._elastic_bandwidth

    @elastic_bandwidth.setter
    def elastic_bandwidth(self, elastic_bandwidth):
        r"""Sets the elastic_bandwidth of this UpgradeInstanceData.

        弹性带宽(G)

        :param elastic_bandwidth: The elastic_bandwidth of this UpgradeInstanceData.
        :type elastic_bandwidth: str
        """
        self._elastic_bandwidth = elastic_bandwidth

    @property
    def service_bandwidth(self):
        r"""Gets the service_bandwidth of this UpgradeInstanceData.

        业务带宽

        :return: The service_bandwidth of this UpgradeInstanceData.
        :rtype: int
        """
        return self._service_bandwidth

    @service_bandwidth.setter
    def service_bandwidth(self, service_bandwidth):
        r"""Sets the service_bandwidth of this UpgradeInstanceData.

        业务带宽

        :param service_bandwidth: The service_bandwidth of this UpgradeInstanceData.
        :type service_bandwidth: int
        """
        self._service_bandwidth = service_bandwidth

    @property
    def port_num(self):
        r"""Gets the port_num of this UpgradeInstanceData.

        端口数

        :return: The port_num of this UpgradeInstanceData.
        :rtype: int
        """
        return self._port_num

    @port_num.setter
    def port_num(self, port_num):
        r"""Sets the port_num of this UpgradeInstanceData.

        端口数

        :param port_num: The port_num of this UpgradeInstanceData.
        :type port_num: int
        """
        self._port_num = port_num

    @property
    def bind_domain_num(self):
        r"""Gets the bind_domain_num of this UpgradeInstanceData.

        域名数

        :return: The bind_domain_num of this UpgradeInstanceData.
        :rtype: int
        """
        return self._bind_domain_num

    @bind_domain_num.setter
    def bind_domain_num(self, bind_domain_num):
        r"""Sets the bind_domain_num of this UpgradeInstanceData.

        域名数

        :param bind_domain_num: The bind_domain_num of this UpgradeInstanceData.
        :type bind_domain_num: int
        """
        self._bind_domain_num = bind_domain_num

    @property
    def elastic_service_bandwidth_type(self):
        r"""Gets the elastic_service_bandwidth_type of this UpgradeInstanceData.

        弹性业务带宽,0-关闭，3-月95

        :return: The elastic_service_bandwidth_type of this UpgradeInstanceData.
        :rtype: int
        """
        return self._elastic_service_bandwidth_type

    @elastic_service_bandwidth_type.setter
    def elastic_service_bandwidth_type(self, elastic_service_bandwidth_type):
        r"""Sets the elastic_service_bandwidth_type of this UpgradeInstanceData.

        弹性业务带宽,0-关闭，3-月95

        :param elastic_service_bandwidth_type: The elastic_service_bandwidth_type of this UpgradeInstanceData.
        :type elastic_service_bandwidth_type: int
        """
        self._elastic_service_bandwidth_type = elastic_service_bandwidth_type

    @property
    def elastic_service_bandwidth(self):
        r"""Gets the elastic_service_bandwidth of this UpgradeInstanceData.

        弹性业务带宽增加值

        :return: The elastic_service_bandwidth of this UpgradeInstanceData.
        :rtype: int
        """
        return self._elastic_service_bandwidth

    @elastic_service_bandwidth.setter
    def elastic_service_bandwidth(self, elastic_service_bandwidth):
        r"""Sets the elastic_service_bandwidth of this UpgradeInstanceData.

        弹性业务带宽增加值

        :param elastic_service_bandwidth: The elastic_service_bandwidth of this UpgradeInstanceData.
        :type elastic_service_bandwidth: int
        """
        self._elastic_service_bandwidth = elastic_service_bandwidth

    @property
    def basic_qps(self):
        r"""Gets the basic_qps of this UpgradeInstanceData.

        业务QPS(如果实例没购买过QPS，需要在页面上升级一次规格开通QPS，之后才可以通过接口修改规格)

        :return: The basic_qps of this UpgradeInstanceData.
        :rtype: int
        """
        return self._basic_qps

    @basic_qps.setter
    def basic_qps(self, basic_qps):
        r"""Sets the basic_qps of this UpgradeInstanceData.

        业务QPS(如果实例没购买过QPS，需要在页面上升级一次规格开通QPS，之后才可以通过接口修改规格)

        :param basic_qps: The basic_qps of this UpgradeInstanceData.
        :type basic_qps: int
        """
        self._basic_qps = basic_qps

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
        if not isinstance(other, UpgradeInstanceData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
