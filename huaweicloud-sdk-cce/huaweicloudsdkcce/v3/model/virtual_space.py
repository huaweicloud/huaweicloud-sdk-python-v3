# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VirtualSpace:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'size': 'str',
        'lvm_config': 'LVMConfig',
        'runtime_config': 'RuntimeConfig'
    }

    attribute_map = {
        'name': 'name',
        'size': 'size',
        'lvm_config': 'lvmConfig',
        'runtime_config': 'runtimeConfig'
    }

    def __init__(self, name=None, size=None, lvm_config=None, runtime_config=None):
        """VirtualSpace

        The model defined in huaweicloud sdk

        :param name: virtualSpace的名称，当前仅支持三种类型：kubernetes、runtime、user。 - kubernetes：k8s空间配置，需配置lvmConfig； - runtime：运行时空间配置，需配置runtimeConfig； - user：用户空间配置，需配置lvmConfig 
        :type name: str
        :param size: virtualSpace的大小，仅支持整数百分比。例如：90%。 &gt;一个group中所有virtualSpace的百分比之和不得超过100% 
        :type size: str
        :param lvm_config: 
        :type lvm_config: :class:`huaweicloudsdkcce.v3.LVMConfig`
        :param runtime_config: 
        :type runtime_config: :class:`huaweicloudsdkcce.v3.RuntimeConfig`
        """
        
        

        self._name = None
        self._size = None
        self._lvm_config = None
        self._runtime_config = None
        self.discriminator = None

        self.name = name
        self.size = size
        if lvm_config is not None:
            self.lvm_config = lvm_config
        if runtime_config is not None:
            self.runtime_config = runtime_config

    @property
    def name(self):
        """Gets the name of this VirtualSpace.

        virtualSpace的名称，当前仅支持三种类型：kubernetes、runtime、user。 - kubernetes：k8s空间配置，需配置lvmConfig； - runtime：运行时空间配置，需配置runtimeConfig； - user：用户空间配置，需配置lvmConfig 

        :return: The name of this VirtualSpace.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VirtualSpace.

        virtualSpace的名称，当前仅支持三种类型：kubernetes、runtime、user。 - kubernetes：k8s空间配置，需配置lvmConfig； - runtime：运行时空间配置，需配置runtimeConfig； - user：用户空间配置，需配置lvmConfig 

        :param name: The name of this VirtualSpace.
        :type name: str
        """
        self._name = name

    @property
    def size(self):
        """Gets the size of this VirtualSpace.

        virtualSpace的大小，仅支持整数百分比。例如：90%。 >一个group中所有virtualSpace的百分比之和不得超过100% 

        :return: The size of this VirtualSpace.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this VirtualSpace.

        virtualSpace的大小，仅支持整数百分比。例如：90%。 >一个group中所有virtualSpace的百分比之和不得超过100% 

        :param size: The size of this VirtualSpace.
        :type size: str
        """
        self._size = size

    @property
    def lvm_config(self):
        """Gets the lvm_config of this VirtualSpace.

        :return: The lvm_config of this VirtualSpace.
        :rtype: :class:`huaweicloudsdkcce.v3.LVMConfig`
        """
        return self._lvm_config

    @lvm_config.setter
    def lvm_config(self, lvm_config):
        """Sets the lvm_config of this VirtualSpace.

        :param lvm_config: The lvm_config of this VirtualSpace.
        :type lvm_config: :class:`huaweicloudsdkcce.v3.LVMConfig`
        """
        self._lvm_config = lvm_config

    @property
    def runtime_config(self):
        """Gets the runtime_config of this VirtualSpace.

        :return: The runtime_config of this VirtualSpace.
        :rtype: :class:`huaweicloudsdkcce.v3.RuntimeConfig`
        """
        return self._runtime_config

    @runtime_config.setter
    def runtime_config(self, runtime_config):
        """Sets the runtime_config of this VirtualSpace.

        :param runtime_config: The runtime_config of this VirtualSpace.
        :type runtime_config: :class:`huaweicloudsdkcce.v3.RuntimeConfig`
        """
        self._runtime_config = runtime_config

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
        if not isinstance(other, VirtualSpace):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
