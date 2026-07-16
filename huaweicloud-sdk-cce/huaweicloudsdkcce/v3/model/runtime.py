# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Runtime:

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
        'runtime_class': 'str'
    }

    attribute_map = {
        'name': 'name',
        'runtime_class': 'runtimeClass'
    }

    def __init__(self, name=None, runtime_class=None):
        r"""Runtime

        The model defined in huaweicloud sdk

        :param name: 容器运行时，默认场景： - v1.25以下集群：默认为\&quot;docker\&quot; - v1.25及以上集群，随操作系统变化，默认的容器运行时不同：操作系统为EulerOS 2.5[、EulerOS 2.8](tag:hws,hws_hk)的节点默认为\&quot;docker\&quot;，其余操作系统的节点默认为\&quot;containerd\&quot; 
        :type name: str
        :param runtime_class: **参数解释**： 容器运行时子类别。 **约束限制**： 仅CCE Turbo集群下弹性云服务器-物理机类型节点且上级运行时为containerd场景支持使用安全运行时。 **取值范围**： - runc: 普通运行时。 - kata: 安全运行时，需配套c6、c7系列弹性云服务器-物理机，支持的操作系统为EulerOS 2.10。 - kuasar-vmm: 安全运行时v2，支持kc2、ki2、c7、ac8h系列弹性服务器-物理机，配套操作系统为HCE 2.0，集群版本需为v1.28.15-r70、v1.29.15-r30、v1.30.14-r30、v1.31.10-r30、v1.32.6-r30、v1.33.5-r20或以上版本。  **默认取值**： runc
        :type runtime_class: str
        """
        
        

        self._name = None
        self._runtime_class = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if runtime_class is not None:
            self.runtime_class = runtime_class

    @property
    def name(self):
        r"""Gets the name of this Runtime.

        容器运行时，默认场景： - v1.25以下集群：默认为\"docker\" - v1.25及以上集群，随操作系统变化，默认的容器运行时不同：操作系统为EulerOS 2.5[、EulerOS 2.8](tag:hws,hws_hk)的节点默认为\"docker\"，其余操作系统的节点默认为\"containerd\" 

        :return: The name of this Runtime.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Runtime.

        容器运行时，默认场景： - v1.25以下集群：默认为\"docker\" - v1.25及以上集群，随操作系统变化，默认的容器运行时不同：操作系统为EulerOS 2.5[、EulerOS 2.8](tag:hws,hws_hk)的节点默认为\"docker\"，其余操作系统的节点默认为\"containerd\" 

        :param name: The name of this Runtime.
        :type name: str
        """
        self._name = name

    @property
    def runtime_class(self):
        r"""Gets the runtime_class of this Runtime.

        **参数解释**： 容器运行时子类别。 **约束限制**： 仅CCE Turbo集群下弹性云服务器-物理机类型节点且上级运行时为containerd场景支持使用安全运行时。 **取值范围**： - runc: 普通运行时。 - kata: 安全运行时，需配套c6、c7系列弹性云服务器-物理机，支持的操作系统为EulerOS 2.10。 - kuasar-vmm: 安全运行时v2，支持kc2、ki2、c7、ac8h系列弹性服务器-物理机，配套操作系统为HCE 2.0，集群版本需为v1.28.15-r70、v1.29.15-r30、v1.30.14-r30、v1.31.10-r30、v1.32.6-r30、v1.33.5-r20或以上版本。  **默认取值**： runc

        :return: The runtime_class of this Runtime.
        :rtype: str
        """
        return self._runtime_class

    @runtime_class.setter
    def runtime_class(self, runtime_class):
        r"""Sets the runtime_class of this Runtime.

        **参数解释**： 容器运行时子类别。 **约束限制**： 仅CCE Turbo集群下弹性云服务器-物理机类型节点且上级运行时为containerd场景支持使用安全运行时。 **取值范围**： - runc: 普通运行时。 - kata: 安全运行时，需配套c6、c7系列弹性云服务器-物理机，支持的操作系统为EulerOS 2.10。 - kuasar-vmm: 安全运行时v2，支持kc2、ki2、c7、ac8h系列弹性服务器-物理机，配套操作系统为HCE 2.0，集群版本需为v1.28.15-r70、v1.29.15-r30、v1.30.14-r30、v1.31.10-r30、v1.32.6-r30、v1.33.5-r20或以上版本。  **默认取值**： runc

        :param runtime_class: The runtime_class of this Runtime.
        :type runtime_class: str
        """
        self._runtime_class = runtime_class

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Runtime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
