# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloudServiceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_num': 'int',
        'resource_num': 'int',
        'resource_distribution': 'ResourceDistribution'
    }

    attribute_map = {
        'service_num': 'service_num',
        'resource_num': 'resource_num',
        'resource_distribution': 'resource_distribution'
    }

    def __init__(self, service_num=None, resource_num=None, resource_distribution=None):
        r"""CloudServiceInfo

        The model defined in huaweicloud sdk

        :param service_num: 当前租户开通的云原生密码服务数量（只统计白名单服务情况）
        :type service_num: int
        :param resource_num: 当前租户云原生密码服务的资源实例总和
        :type resource_num: int
        :param resource_distribution: 
        :type resource_distribution: :class:`huaweicloudsdkcpcs.v1.ResourceDistribution`
        """
        
        

        self._service_num = None
        self._resource_num = None
        self._resource_distribution = None
        self.discriminator = None

        self.service_num = service_num
        self.resource_num = resource_num
        self.resource_distribution = resource_distribution

    @property
    def service_num(self):
        r"""Gets the service_num of this CloudServiceInfo.

        当前租户开通的云原生密码服务数量（只统计白名单服务情况）

        :return: The service_num of this CloudServiceInfo.
        :rtype: int
        """
        return self._service_num

    @service_num.setter
    def service_num(self, service_num):
        r"""Sets the service_num of this CloudServiceInfo.

        当前租户开通的云原生密码服务数量（只统计白名单服务情况）

        :param service_num: The service_num of this CloudServiceInfo.
        :type service_num: int
        """
        self._service_num = service_num

    @property
    def resource_num(self):
        r"""Gets the resource_num of this CloudServiceInfo.

        当前租户云原生密码服务的资源实例总和

        :return: The resource_num of this CloudServiceInfo.
        :rtype: int
        """
        return self._resource_num

    @resource_num.setter
    def resource_num(self, resource_num):
        r"""Sets the resource_num of this CloudServiceInfo.

        当前租户云原生密码服务的资源实例总和

        :param resource_num: The resource_num of this CloudServiceInfo.
        :type resource_num: int
        """
        self._resource_num = resource_num

    @property
    def resource_distribution(self):
        r"""Gets the resource_distribution of this CloudServiceInfo.

        :return: The resource_distribution of this CloudServiceInfo.
        :rtype: :class:`huaweicloudsdkcpcs.v1.ResourceDistribution`
        """
        return self._resource_distribution

    @resource_distribution.setter
    def resource_distribution(self, resource_distribution):
        r"""Sets the resource_distribution of this CloudServiceInfo.

        :param resource_distribution: The resource_distribution of this CloudServiceInfo.
        :type resource_distribution: :class:`huaweicloudsdkcpcs.v1.ResourceDistribution`
        """
        self._resource_distribution = resource_distribution

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
        if not isinstance(other, CloudServiceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
