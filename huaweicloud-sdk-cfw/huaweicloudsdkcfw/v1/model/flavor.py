# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Flavor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'int',
        'eip_count': 'int',
        'vpc_count': 'int',
        'bandwidth': 'int',
        'log_storage': 'int',
        'default_bandwidth': 'int',
        'default_eip_count': 'int',
        'default_log_storage': 'int',
        'default_vpc_count': 'int'
    }

    attribute_map = {
        'version': 'version',
        'eip_count': 'eip_count',
        'vpc_count': 'vpc_count',
        'bandwidth': 'bandwidth',
        'log_storage': 'log_storage',
        'default_bandwidth': 'default_bandwidth',
        'default_eip_count': 'default_eip_count',
        'default_log_storage': 'default_log_storage',
        'default_vpc_count': 'default_vpc_count'
    }

    def __init__(self, version=None, eip_count=None, vpc_count=None, bandwidth=None, log_storage=None, default_bandwidth=None, default_eip_count=None, default_log_storage=None, default_vpc_count=None):
        """Flavor

        The model defined in huaweicloud sdk

        :param version: 防火墙版本，0：标准版，1：专业版，2：铂金版，3：基础版，购买时，当防火墙“charge_mode”为“postPaid”时，仅支持专业版。“charge_mode”为“prePaid”时，支持标准版、专业版。
        :type version: int
        :param eip_count: eip数量
        :type eip_count: int
        :param vpc_count: vpc数量
        :type vpc_count: int
        :param bandwidth: 带宽
        :type bandwidth: int
        :param log_storage: 日志存储
        :type log_storage: int
        :param default_bandwidth: 默认防火墙带宽
        :type default_bandwidth: int
        :param default_eip_count: 默认eip数
        :type default_eip_count: int
        :param default_log_storage: 默认日志存储
        :type default_log_storage: int
        :param default_vpc_count: 默认vpc数
        :type default_vpc_count: int
        """
        
        

        self._version = None
        self._eip_count = None
        self._vpc_count = None
        self._bandwidth = None
        self._log_storage = None
        self._default_bandwidth = None
        self._default_eip_count = None
        self._default_log_storage = None
        self._default_vpc_count = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if eip_count is not None:
            self.eip_count = eip_count
        if vpc_count is not None:
            self.vpc_count = vpc_count
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if log_storage is not None:
            self.log_storage = log_storage
        if default_bandwidth is not None:
            self.default_bandwidth = default_bandwidth
        if default_eip_count is not None:
            self.default_eip_count = default_eip_count
        if default_log_storage is not None:
            self.default_log_storage = default_log_storage
        if default_vpc_count is not None:
            self.default_vpc_count = default_vpc_count

    @property
    def version(self):
        """Gets the version of this Flavor.

        防火墙版本，0：标准版，1：专业版，2：铂金版，3：基础版，购买时，当防火墙“charge_mode”为“postPaid”时，仅支持专业版。“charge_mode”为“prePaid”时，支持标准版、专业版。

        :return: The version of this Flavor.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Flavor.

        防火墙版本，0：标准版，1：专业版，2：铂金版，3：基础版，购买时，当防火墙“charge_mode”为“postPaid”时，仅支持专业版。“charge_mode”为“prePaid”时，支持标准版、专业版。

        :param version: The version of this Flavor.
        :type version: int
        """
        self._version = version

    @property
    def eip_count(self):
        """Gets the eip_count of this Flavor.

        eip数量

        :return: The eip_count of this Flavor.
        :rtype: int
        """
        return self._eip_count

    @eip_count.setter
    def eip_count(self, eip_count):
        """Sets the eip_count of this Flavor.

        eip数量

        :param eip_count: The eip_count of this Flavor.
        :type eip_count: int
        """
        self._eip_count = eip_count

    @property
    def vpc_count(self):
        """Gets the vpc_count of this Flavor.

        vpc数量

        :return: The vpc_count of this Flavor.
        :rtype: int
        """
        return self._vpc_count

    @vpc_count.setter
    def vpc_count(self, vpc_count):
        """Sets the vpc_count of this Flavor.

        vpc数量

        :param vpc_count: The vpc_count of this Flavor.
        :type vpc_count: int
        """
        self._vpc_count = vpc_count

    @property
    def bandwidth(self):
        """Gets the bandwidth of this Flavor.

        带宽

        :return: The bandwidth of this Flavor.
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this Flavor.

        带宽

        :param bandwidth: The bandwidth of this Flavor.
        :type bandwidth: int
        """
        self._bandwidth = bandwidth

    @property
    def log_storage(self):
        """Gets the log_storage of this Flavor.

        日志存储

        :return: The log_storage of this Flavor.
        :rtype: int
        """
        return self._log_storage

    @log_storage.setter
    def log_storage(self, log_storage):
        """Sets the log_storage of this Flavor.

        日志存储

        :param log_storage: The log_storage of this Flavor.
        :type log_storage: int
        """
        self._log_storage = log_storage

    @property
    def default_bandwidth(self):
        """Gets the default_bandwidth of this Flavor.

        默认防火墙带宽

        :return: The default_bandwidth of this Flavor.
        :rtype: int
        """
        return self._default_bandwidth

    @default_bandwidth.setter
    def default_bandwidth(self, default_bandwidth):
        """Sets the default_bandwidth of this Flavor.

        默认防火墙带宽

        :param default_bandwidth: The default_bandwidth of this Flavor.
        :type default_bandwidth: int
        """
        self._default_bandwidth = default_bandwidth

    @property
    def default_eip_count(self):
        """Gets the default_eip_count of this Flavor.

        默认eip数

        :return: The default_eip_count of this Flavor.
        :rtype: int
        """
        return self._default_eip_count

    @default_eip_count.setter
    def default_eip_count(self, default_eip_count):
        """Sets the default_eip_count of this Flavor.

        默认eip数

        :param default_eip_count: The default_eip_count of this Flavor.
        :type default_eip_count: int
        """
        self._default_eip_count = default_eip_count

    @property
    def default_log_storage(self):
        """Gets the default_log_storage of this Flavor.

        默认日志存储

        :return: The default_log_storage of this Flavor.
        :rtype: int
        """
        return self._default_log_storage

    @default_log_storage.setter
    def default_log_storage(self, default_log_storage):
        """Sets the default_log_storage of this Flavor.

        默认日志存储

        :param default_log_storage: The default_log_storage of this Flavor.
        :type default_log_storage: int
        """
        self._default_log_storage = default_log_storage

    @property
    def default_vpc_count(self):
        """Gets the default_vpc_count of this Flavor.

        默认vpc数

        :return: The default_vpc_count of this Flavor.
        :rtype: int
        """
        return self._default_vpc_count

    @default_vpc_count.setter
    def default_vpc_count(self, default_vpc_count):
        """Sets the default_vpc_count of this Flavor.

        默认vpc数

        :param default_vpc_count: The default_vpc_count of this Flavor.
        :type default_vpc_count: int
        """
        self._default_vpc_count = default_vpc_count

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
        if not isinstance(other, Flavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
