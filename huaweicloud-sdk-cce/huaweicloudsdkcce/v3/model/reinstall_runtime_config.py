# coding: utf-8

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
        'container_base_size': 'int',
        'runtime': 'Runtime'
    }

    attribute_map = {
        'docker_base_size': 'dockerBaseSize',
        'container_base_size': 'containerBaseSize',
        'runtime': 'runtime'
    }

    def __init__(self, docker_base_size=None, container_base_size=None, runtime=None):
        r"""ReinstallRuntimeConfig

        The model defined in huaweicloud sdk

        :param docker_base_size: **参数解释**: 节点上单容器的可用磁盘空间大小（已废弃，请优先使用containerBaseSize参数），单位G。  不配置该值或值为0时将使用默认值，Devicemapper模式下默认值为10；OverlayFS模式默认不限制单容器可用空间大小，且dockerBaseSize设置仅在新版本集群的EulerOS[/HCEOS2.0](tag:hws,hws_hk,ctc,cmcc)节点上生效。  CCE节点容器运行时空间配置请参考[数据盘空间分配说明](cce_01_0341.xml)。  Devicemapper模式下建议dockerBaseSize配置不超过80G，设置过大时可能会导致容器运行时初始化时间过长而启动失败，若对容器磁盘大小有特殊要求，可考虑使用挂载外部或本地存储方式代替。 **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及
        :type docker_base_size: int
        :param container_base_size: **参数解释**： 节点上单容器的可用磁盘空间大小，单位G。 &gt; - 更新节点池时，不支持更新此参数 &gt; - 不配置该值或值为0时将使用默认值，OverlayFS模式默认不限制单容器可用空间大小；Devicemapper模式下默认值为10，且containerBaseSize设置仅在新版本集群（v1.23.14-r0/v1.25.9-r0/v1.27.6-r0/v1.28.4-r0及以上）的EulerOS[/HCEOS2.0](tag:hws,hws_hk,ctc,cmcc)节点上生效。           &gt; - CCE节点容器运行时空间配置请参考[数据盘空间分配说明](cce_01_0341.xml)。        &gt; - Devicemapper模式下建议containerBaseSize配置不超过80G，设置过大时可能会导致容器运行时初始化时间过长而启动失败，若对容器磁盘大小有特殊要求，可考虑使用挂载外部或本地存储方式代替；Devicemapper模式在新版中仅有共池裸机使用，已逐步废弃。  **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type container_base_size: int
        :param runtime: 
        :type runtime: :class:`huaweicloudsdkcce.v3.Runtime`
        """
        
        

        self._docker_base_size = None
        self._container_base_size = None
        self._runtime = None
        self.discriminator = None

        if docker_base_size is not None:
            self.docker_base_size = docker_base_size
        if container_base_size is not None:
            self.container_base_size = container_base_size
        if runtime is not None:
            self.runtime = runtime

    @property
    def docker_base_size(self):
        r"""Gets the docker_base_size of this ReinstallRuntimeConfig.

        **参数解释**: 节点上单容器的可用磁盘空间大小（已废弃，请优先使用containerBaseSize参数），单位G。  不配置该值或值为0时将使用默认值，Devicemapper模式下默认值为10；OverlayFS模式默认不限制单容器可用空间大小，且dockerBaseSize设置仅在新版本集群的EulerOS[/HCEOS2.0](tag:hws,hws_hk,ctc,cmcc)节点上生效。  CCE节点容器运行时空间配置请参考[数据盘空间分配说明](cce_01_0341.xml)。  Devicemapper模式下建议dockerBaseSize配置不超过80G，设置过大时可能会导致容器运行时初始化时间过长而启动失败，若对容器磁盘大小有特殊要求，可考虑使用挂载外部或本地存储方式代替。 **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及

        :return: The docker_base_size of this ReinstallRuntimeConfig.
        :rtype: int
        """
        return self._docker_base_size

    @docker_base_size.setter
    def docker_base_size(self, docker_base_size):
        r"""Sets the docker_base_size of this ReinstallRuntimeConfig.

        **参数解释**: 节点上单容器的可用磁盘空间大小（已废弃，请优先使用containerBaseSize参数），单位G。  不配置该值或值为0时将使用默认值，Devicemapper模式下默认值为10；OverlayFS模式默认不限制单容器可用空间大小，且dockerBaseSize设置仅在新版本集群的EulerOS[/HCEOS2.0](tag:hws,hws_hk,ctc,cmcc)节点上生效。  CCE节点容器运行时空间配置请参考[数据盘空间分配说明](cce_01_0341.xml)。  Devicemapper模式下建议dockerBaseSize配置不超过80G，设置过大时可能会导致容器运行时初始化时间过长而启动失败，若对容器磁盘大小有特殊要求，可考虑使用挂载外部或本地存储方式代替。 **约束限制**: 不涉及 **取值范围**: 不涉及 **默认取值**: 不涉及

        :param docker_base_size: The docker_base_size of this ReinstallRuntimeConfig.
        :type docker_base_size: int
        """
        self._docker_base_size = docker_base_size

    @property
    def container_base_size(self):
        r"""Gets the container_base_size of this ReinstallRuntimeConfig.

        **参数解释**： 节点上单容器的可用磁盘空间大小，单位G。 > - 更新节点池时，不支持更新此参数 > - 不配置该值或值为0时将使用默认值，OverlayFS模式默认不限制单容器可用空间大小；Devicemapper模式下默认值为10，且containerBaseSize设置仅在新版本集群（v1.23.14-r0/v1.25.9-r0/v1.27.6-r0/v1.28.4-r0及以上）的EulerOS[/HCEOS2.0](tag:hws,hws_hk,ctc,cmcc)节点上生效。           > - CCE节点容器运行时空间配置请参考[数据盘空间分配说明](cce_01_0341.xml)。        > - Devicemapper模式下建议containerBaseSize配置不超过80G，设置过大时可能会导致容器运行时初始化时间过长而启动失败，若对容器磁盘大小有特殊要求，可考虑使用挂载外部或本地存储方式代替；Devicemapper模式在新版中仅有共池裸机使用，已逐步废弃。  **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The container_base_size of this ReinstallRuntimeConfig.
        :rtype: int
        """
        return self._container_base_size

    @container_base_size.setter
    def container_base_size(self, container_base_size):
        r"""Sets the container_base_size of this ReinstallRuntimeConfig.

        **参数解释**： 节点上单容器的可用磁盘空间大小，单位G。 > - 更新节点池时，不支持更新此参数 > - 不配置该值或值为0时将使用默认值，OverlayFS模式默认不限制单容器可用空间大小；Devicemapper模式下默认值为10，且containerBaseSize设置仅在新版本集群（v1.23.14-r0/v1.25.9-r0/v1.27.6-r0/v1.28.4-r0及以上）的EulerOS[/HCEOS2.0](tag:hws,hws_hk,ctc,cmcc)节点上生效。           > - CCE节点容器运行时空间配置请参考[数据盘空间分配说明](cce_01_0341.xml)。        > - Devicemapper模式下建议containerBaseSize配置不超过80G，设置过大时可能会导致容器运行时初始化时间过长而启动失败，若对容器磁盘大小有特殊要求，可考虑使用挂载外部或本地存储方式代替；Devicemapper模式在新版中仅有共池裸机使用，已逐步废弃。  **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param container_base_size: The container_base_size of this ReinstallRuntimeConfig.
        :type container_base_size: int
        """
        self._container_base_size = container_base_size

    @property
    def runtime(self):
        r"""Gets the runtime of this ReinstallRuntimeConfig.

        :return: The runtime of this ReinstallRuntimeConfig.
        :rtype: :class:`huaweicloudsdkcce.v3.Runtime`
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        r"""Sets the runtime of this ReinstallRuntimeConfig.

        :param runtime: The runtime of this ReinstallRuntimeConfig.
        :type runtime: :class:`huaweicloudsdkcce.v3.Runtime`
        """
        self._runtime = runtime

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
        if not isinstance(other, ReinstallRuntimeConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
