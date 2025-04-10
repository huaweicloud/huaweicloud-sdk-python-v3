# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetworkCheckInfoRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_connectivity': 'bool',
        'destination_connectivity': 'bool',
        'network_delay': 'float',
        'network_jitter': 'float',
        'migration_speed': 'float',
        'loss_percentage': 'float',
        'cpu_usage': 'float',
        'mem_usage': 'float',
        'evaluation_result': 'str'
    }

    attribute_map = {
        'domain_connectivity': 'domain_connectivity',
        'destination_connectivity': 'destination_connectivity',
        'network_delay': 'network_delay',
        'network_jitter': 'network_jitter',
        'migration_speed': 'migration_speed',
        'loss_percentage': 'loss_percentage',
        'cpu_usage': 'cpu_usage',
        'mem_usage': 'mem_usage',
        'evaluation_result': 'evaluation_result'
    }

    def __init__(self, domain_connectivity=None, destination_connectivity=None, network_delay=None, network_jitter=None, migration_speed=None, loss_percentage=None, cpu_usage=None, mem_usage=None, evaluation_result=None):
        r"""NetworkCheckInfoRequestBody

        The model defined in huaweicloud sdk

        :param domain_connectivity: 域名连通性
        :type domain_connectivity: bool
        :param destination_connectivity: 目的端连通性
        :type destination_connectivity: bool
        :param network_delay: 网络时延
        :type network_delay: float
        :param network_jitter: 网络抖动
        :type network_jitter: float
        :param migration_speed: 带宽
        :type migration_speed: float
        :param loss_percentage: 丢包
        :type loss_percentage: float
        :param cpu_usage: CPU占用
        :type cpu_usage: float
        :param mem_usage: 内存占用
        :type mem_usage: float
        :param evaluation_result: 评估结果
        :type evaluation_result: str
        """
        
        

        self._domain_connectivity = None
        self._destination_connectivity = None
        self._network_delay = None
        self._network_jitter = None
        self._migration_speed = None
        self._loss_percentage = None
        self._cpu_usage = None
        self._mem_usage = None
        self._evaluation_result = None
        self.discriminator = None

        if domain_connectivity is not None:
            self.domain_connectivity = domain_connectivity
        if destination_connectivity is not None:
            self.destination_connectivity = destination_connectivity
        self.network_delay = network_delay
        self.network_jitter = network_jitter
        self.migration_speed = migration_speed
        self.loss_percentage = loss_percentage
        self.cpu_usage = cpu_usage
        self.mem_usage = mem_usage
        self.evaluation_result = evaluation_result

    @property
    def domain_connectivity(self):
        r"""Gets the domain_connectivity of this NetworkCheckInfoRequestBody.

        域名连通性

        :return: The domain_connectivity of this NetworkCheckInfoRequestBody.
        :rtype: bool
        """
        return self._domain_connectivity

    @domain_connectivity.setter
    def domain_connectivity(self, domain_connectivity):
        r"""Sets the domain_connectivity of this NetworkCheckInfoRequestBody.

        域名连通性

        :param domain_connectivity: The domain_connectivity of this NetworkCheckInfoRequestBody.
        :type domain_connectivity: bool
        """
        self._domain_connectivity = domain_connectivity

    @property
    def destination_connectivity(self):
        r"""Gets the destination_connectivity of this NetworkCheckInfoRequestBody.

        目的端连通性

        :return: The destination_connectivity of this NetworkCheckInfoRequestBody.
        :rtype: bool
        """
        return self._destination_connectivity

    @destination_connectivity.setter
    def destination_connectivity(self, destination_connectivity):
        r"""Sets the destination_connectivity of this NetworkCheckInfoRequestBody.

        目的端连通性

        :param destination_connectivity: The destination_connectivity of this NetworkCheckInfoRequestBody.
        :type destination_connectivity: bool
        """
        self._destination_connectivity = destination_connectivity

    @property
    def network_delay(self):
        r"""Gets the network_delay of this NetworkCheckInfoRequestBody.

        网络时延

        :return: The network_delay of this NetworkCheckInfoRequestBody.
        :rtype: float
        """
        return self._network_delay

    @network_delay.setter
    def network_delay(self, network_delay):
        r"""Sets the network_delay of this NetworkCheckInfoRequestBody.

        网络时延

        :param network_delay: The network_delay of this NetworkCheckInfoRequestBody.
        :type network_delay: float
        """
        self._network_delay = network_delay

    @property
    def network_jitter(self):
        r"""Gets the network_jitter of this NetworkCheckInfoRequestBody.

        网络抖动

        :return: The network_jitter of this NetworkCheckInfoRequestBody.
        :rtype: float
        """
        return self._network_jitter

    @network_jitter.setter
    def network_jitter(self, network_jitter):
        r"""Sets the network_jitter of this NetworkCheckInfoRequestBody.

        网络抖动

        :param network_jitter: The network_jitter of this NetworkCheckInfoRequestBody.
        :type network_jitter: float
        """
        self._network_jitter = network_jitter

    @property
    def migration_speed(self):
        r"""Gets the migration_speed of this NetworkCheckInfoRequestBody.

        带宽

        :return: The migration_speed of this NetworkCheckInfoRequestBody.
        :rtype: float
        """
        return self._migration_speed

    @migration_speed.setter
    def migration_speed(self, migration_speed):
        r"""Sets the migration_speed of this NetworkCheckInfoRequestBody.

        带宽

        :param migration_speed: The migration_speed of this NetworkCheckInfoRequestBody.
        :type migration_speed: float
        """
        self._migration_speed = migration_speed

    @property
    def loss_percentage(self):
        r"""Gets the loss_percentage of this NetworkCheckInfoRequestBody.

        丢包

        :return: The loss_percentage of this NetworkCheckInfoRequestBody.
        :rtype: float
        """
        return self._loss_percentage

    @loss_percentage.setter
    def loss_percentage(self, loss_percentage):
        r"""Sets the loss_percentage of this NetworkCheckInfoRequestBody.

        丢包

        :param loss_percentage: The loss_percentage of this NetworkCheckInfoRequestBody.
        :type loss_percentage: float
        """
        self._loss_percentage = loss_percentage

    @property
    def cpu_usage(self):
        r"""Gets the cpu_usage of this NetworkCheckInfoRequestBody.

        CPU占用

        :return: The cpu_usage of this NetworkCheckInfoRequestBody.
        :rtype: float
        """
        return self._cpu_usage

    @cpu_usage.setter
    def cpu_usage(self, cpu_usage):
        r"""Sets the cpu_usage of this NetworkCheckInfoRequestBody.

        CPU占用

        :param cpu_usage: The cpu_usage of this NetworkCheckInfoRequestBody.
        :type cpu_usage: float
        """
        self._cpu_usage = cpu_usage

    @property
    def mem_usage(self):
        r"""Gets the mem_usage of this NetworkCheckInfoRequestBody.

        内存占用

        :return: The mem_usage of this NetworkCheckInfoRequestBody.
        :rtype: float
        """
        return self._mem_usage

    @mem_usage.setter
    def mem_usage(self, mem_usage):
        r"""Sets the mem_usage of this NetworkCheckInfoRequestBody.

        内存占用

        :param mem_usage: The mem_usage of this NetworkCheckInfoRequestBody.
        :type mem_usage: float
        """
        self._mem_usage = mem_usage

    @property
    def evaluation_result(self):
        r"""Gets the evaluation_result of this NetworkCheckInfoRequestBody.

        评估结果

        :return: The evaluation_result of this NetworkCheckInfoRequestBody.
        :rtype: str
        """
        return self._evaluation_result

    @evaluation_result.setter
    def evaluation_result(self, evaluation_result):
        r"""Sets the evaluation_result of this NetworkCheckInfoRequestBody.

        评估结果

        :param evaluation_result: The evaluation_result of this NetworkCheckInfoRequestBody.
        :type evaluation_result: str
        """
        self._evaluation_result = evaluation_result

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
        if not isinstance(other, NetworkCheckInfoRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
