# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReinstallRuntimeConfig:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'docker_base_size': 'int',
        'runtime': 'Runtime'
    }

    attribute_map = {
        'docker_base_size': 'dockerBaseSize',
        'runtime': 'runtime'
    }

    def __init__(self, docker_base_size=None, runtime=None):
        """ReinstallRuntimeConfig - a model defined in huaweicloud sdk"""
        
        

        self._docker_base_size = None
        self._runtime = None
        self.discriminator = None

        if docker_base_size is not None:
            self.docker_base_size = docker_base_size
        if runtime is not None:
            self.runtime = runtime

    @property
    def docker_base_size(self):
        """Gets the docker_base_size of this ReinstallRuntimeConfig.

        Device mapper模式下，节点上Docker单容器的可用磁盘空间大小，OverlayFS模式(CCE Turbo集群中CentOS 7.6和Ubuntu 18.04节点，以及混合集群中Ubuntu 18.04节点)下不支持此字段。Device mapper模式下建议dockerBaseSize配置不超过80G，设置过大时可能会导致docker初始化时间过长而启动失败，若对容器磁盘大小有特殊要求，可考虑使用挂载外部或本地存储方式代替。 

        :return: The docker_base_size of this ReinstallRuntimeConfig.
        :rtype: int
        """
        return self._docker_base_size

    @docker_base_size.setter
    def docker_base_size(self, docker_base_size):
        """Sets the docker_base_size of this ReinstallRuntimeConfig.

        Device mapper模式下，节点上Docker单容器的可用磁盘空间大小，OverlayFS模式(CCE Turbo集群中CentOS 7.6和Ubuntu 18.04节点，以及混合集群中Ubuntu 18.04节点)下不支持此字段。Device mapper模式下建议dockerBaseSize配置不超过80G，设置过大时可能会导致docker初始化时间过长而启动失败，若对容器磁盘大小有特殊要求，可考虑使用挂载外部或本地存储方式代替。 

        :param docker_base_size: The docker_base_size of this ReinstallRuntimeConfig.
        :type: int
        """
        self._docker_base_size = docker_base_size

    @property
    def runtime(self):
        """Gets the runtime of this ReinstallRuntimeConfig.


        :return: The runtime of this ReinstallRuntimeConfig.
        :rtype: Runtime
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this ReinstallRuntimeConfig.


        :param runtime: The runtime of this ReinstallRuntimeConfig.
        :type: Runtime
        """
        self._runtime = runtime

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
        if not isinstance(other, ReinstallRuntimeConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
