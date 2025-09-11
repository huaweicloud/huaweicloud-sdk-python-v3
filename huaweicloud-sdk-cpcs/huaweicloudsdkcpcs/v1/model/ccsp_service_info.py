# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CcspServiceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_num': 'int',
        'instance_num': 'int',
        'instance_quota': 'int',
        'instance_distribution': 'InstanceDistribution'
    }

    attribute_map = {
        'cluster_num': 'cluster_num',
        'instance_num': 'instance_num',
        'instance_quota': 'instance_quota',
        'instance_distribution': 'instance_distribution'
    }

    def __init__(self, cluster_num=None, instance_num=None, instance_quota=None, instance_distribution=None):
        r"""CcspServiceInfo

        The model defined in huaweicloud sdk

        :param cluster_num: 当前租户拥有的密码服务集群数量
        :type cluster_num: int
        :param instance_num: 当前租户拥有的密码服务实例数量
        :type instance_num: int
        :param instance_quota: 当前租户的可创建的密码服务实例配额数
        :type instance_quota: int
        :param instance_distribution: 
        :type instance_distribution: :class:`huaweicloudsdkcpcs.v1.InstanceDistribution`
        """
        
        

        self._cluster_num = None
        self._instance_num = None
        self._instance_quota = None
        self._instance_distribution = None
        self.discriminator = None

        self.cluster_num = cluster_num
        self.instance_num = instance_num
        self.instance_quota = instance_quota
        self.instance_distribution = instance_distribution

    @property
    def cluster_num(self):
        r"""Gets the cluster_num of this CcspServiceInfo.

        当前租户拥有的密码服务集群数量

        :return: The cluster_num of this CcspServiceInfo.
        :rtype: int
        """
        return self._cluster_num

    @cluster_num.setter
    def cluster_num(self, cluster_num):
        r"""Sets the cluster_num of this CcspServiceInfo.

        当前租户拥有的密码服务集群数量

        :param cluster_num: The cluster_num of this CcspServiceInfo.
        :type cluster_num: int
        """
        self._cluster_num = cluster_num

    @property
    def instance_num(self):
        r"""Gets the instance_num of this CcspServiceInfo.

        当前租户拥有的密码服务实例数量

        :return: The instance_num of this CcspServiceInfo.
        :rtype: int
        """
        return self._instance_num

    @instance_num.setter
    def instance_num(self, instance_num):
        r"""Sets the instance_num of this CcspServiceInfo.

        当前租户拥有的密码服务实例数量

        :param instance_num: The instance_num of this CcspServiceInfo.
        :type instance_num: int
        """
        self._instance_num = instance_num

    @property
    def instance_quota(self):
        r"""Gets the instance_quota of this CcspServiceInfo.

        当前租户的可创建的密码服务实例配额数

        :return: The instance_quota of this CcspServiceInfo.
        :rtype: int
        """
        return self._instance_quota

    @instance_quota.setter
    def instance_quota(self, instance_quota):
        r"""Sets the instance_quota of this CcspServiceInfo.

        当前租户的可创建的密码服务实例配额数

        :param instance_quota: The instance_quota of this CcspServiceInfo.
        :type instance_quota: int
        """
        self._instance_quota = instance_quota

    @property
    def instance_distribution(self):
        r"""Gets the instance_distribution of this CcspServiceInfo.

        :return: The instance_distribution of this CcspServiceInfo.
        :rtype: :class:`huaweicloudsdkcpcs.v1.InstanceDistribution`
        """
        return self._instance_distribution

    @instance_distribution.setter
    def instance_distribution(self, instance_distribution):
        r"""Sets the instance_distribution of this CcspServiceInfo.

        :param instance_distribution: The instance_distribution of this CcspServiceInfo.
        :type instance_distribution: :class:`huaweicloudsdkcpcs.v1.InstanceDistribution`
        """
        self._instance_distribution = instance_distribution

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
        if not isinstance(other, CcspServiceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
