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
        'log_storage': 'int'
    }

    attribute_map = {
        'version': 'version',
        'eip_count': 'eip_count',
        'vpc_count': 'vpc_count',
        'bandwidth': 'bandwidth',
        'log_storage': 'log_storage'
    }

    def __init__(self, version=None, eip_count=None, vpc_count=None, bandwidth=None, log_storage=None):
        """Flavor

        The model defined in huaweicloud sdk

        :param version: 防火墙版本，0：标准版，1：专业版，2：铂金版，3：基础版
        :type version: int
        :param eip_count: eip数量
        :type eip_count: int
        :param vpc_count: vpc数量
        :type vpc_count: int
        :param bandwidth: 带宽
        :type bandwidth: int
        :param log_storage: 日志存储
        :type log_storage: int
        """
        
        

        self._version = None
        self._eip_count = None
        self._vpc_count = None
        self._bandwidth = None
        self._log_storage = None
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

    @property
    def version(self):
        """Gets the version of this Flavor.

        防火墙版本，0：标准版，1：专业版，2：铂金版，3：基础版

        :return: The version of this Flavor.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Flavor.

        防火墙版本，0：标准版，1：专业版，2：铂金版，3：基础版

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
