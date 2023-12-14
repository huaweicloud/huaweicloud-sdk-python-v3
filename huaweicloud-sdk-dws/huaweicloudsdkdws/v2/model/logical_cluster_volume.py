# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogicalClusterVolume:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'logical_cluster_name': 'str',
        'usage': 'str',
        'total': 'str',
        'percent': 'str'
    }

    attribute_map = {
        'logical_cluster_name': 'logical_cluster_name',
        'usage': 'usage',
        'total': 'total',
        'percent': 'percent'
    }

    def __init__(self, logical_cluster_name=None, usage=None, total=None, percent=None):
        """LogicalClusterVolume

        The model defined in huaweicloud sdk

        :param logical_cluster_name: 逻辑集群名称
        :type logical_cluster_name: str
        :param usage: 磁盘使用量
        :type usage: str
        :param total: 磁盘总量
        :type total: str
        :param percent: 磁盘使用比例
        :type percent: str
        """
        
        

        self._logical_cluster_name = None
        self._usage = None
        self._total = None
        self._percent = None
        self.discriminator = None

        if logical_cluster_name is not None:
            self.logical_cluster_name = logical_cluster_name
        if usage is not None:
            self.usage = usage
        if total is not None:
            self.total = total
        if percent is not None:
            self.percent = percent

    @property
    def logical_cluster_name(self):
        """Gets the logical_cluster_name of this LogicalClusterVolume.

        逻辑集群名称

        :return: The logical_cluster_name of this LogicalClusterVolume.
        :rtype: str
        """
        return self._logical_cluster_name

    @logical_cluster_name.setter
    def logical_cluster_name(self, logical_cluster_name):
        """Sets the logical_cluster_name of this LogicalClusterVolume.

        逻辑集群名称

        :param logical_cluster_name: The logical_cluster_name of this LogicalClusterVolume.
        :type logical_cluster_name: str
        """
        self._logical_cluster_name = logical_cluster_name

    @property
    def usage(self):
        """Gets the usage of this LogicalClusterVolume.

        磁盘使用量

        :return: The usage of this LogicalClusterVolume.
        :rtype: str
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this LogicalClusterVolume.

        磁盘使用量

        :param usage: The usage of this LogicalClusterVolume.
        :type usage: str
        """
        self._usage = usage

    @property
    def total(self):
        """Gets the total of this LogicalClusterVolume.

        磁盘总量

        :return: The total of this LogicalClusterVolume.
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this LogicalClusterVolume.

        磁盘总量

        :param total: The total of this LogicalClusterVolume.
        :type total: str
        """
        self._total = total

    @property
    def percent(self):
        """Gets the percent of this LogicalClusterVolume.

        磁盘使用比例

        :return: The percent of this LogicalClusterVolume.
        :rtype: str
        """
        return self._percent

    @percent.setter
    def percent(self, percent):
        """Sets the percent of this LogicalClusterVolume.

        磁盘使用比例

        :param percent: The percent of this LogicalClusterVolume.
        :type percent: str
        """
        self._percent = percent

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
        if not isinstance(other, LogicalClusterVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
