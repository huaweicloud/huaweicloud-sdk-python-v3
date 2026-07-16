# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DockerLvmConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'docker_thin_pool': 'int',
        'kubernetes_lv': 'int',
        'docker_disk_type': 'str',
        'lv_type': 'str'
    }

    attribute_map = {
        'docker_thin_pool': 'dockerThinPool',
        'kubernetes_lv': 'kubernetesLV',
        'docker_disk_type': 'dockerDiskType',
        'lv_type': 'lvType'
    }

    def __init__(self, docker_thin_pool=None, kubernetes_lv=None, docker_disk_type=None, lv_type=None):
        r"""DockerLvmConfig

        The model defined in huaweicloud sdk

        :param docker_thin_pool: **参数解释**： 资源池节点Docker盘占数据盘的百分比。例如Docker盘大小占用数据盘20%，该参数值为20。 **取值范围**： 不涉及。
        :type docker_thin_pool: int
        :param kubernetes_lv: **参数解释**： 资源池节点上kubelet占数据盘的百分比。例如Docker盘大小占用数据盘20%，该参数值为20。 **取值范围**： 不涉及。
        :type kubernetes_lv: int
        :param docker_disk_type: **参数解释**： 磁盘类型。 **取值范围**： 可选值如下： - evs：云硬盘 - ssd：本地SSD硬盘
        :type docker_disk_type: str
        :param lv_type: **参数解释**： LVM写入模式。 **取值范围**： 可选值如下： - striped：条带模式，使用多块磁盘组成条带模式，能够提升磁盘性能 - linear：线性模式
        :type lv_type: str
        """
        
        

        self._docker_thin_pool = None
        self._kubernetes_lv = None
        self._docker_disk_type = None
        self._lv_type = None
        self.discriminator = None

        self.docker_thin_pool = docker_thin_pool
        self.kubernetes_lv = kubernetes_lv
        self.docker_disk_type = docker_disk_type
        if lv_type is not None:
            self.lv_type = lv_type

    @property
    def docker_thin_pool(self):
        r"""Gets the docker_thin_pool of this DockerLvmConfig.

        **参数解释**： 资源池节点Docker盘占数据盘的百分比。例如Docker盘大小占用数据盘20%，该参数值为20。 **取值范围**： 不涉及。

        :return: The docker_thin_pool of this DockerLvmConfig.
        :rtype: int
        """
        return self._docker_thin_pool

    @docker_thin_pool.setter
    def docker_thin_pool(self, docker_thin_pool):
        r"""Sets the docker_thin_pool of this DockerLvmConfig.

        **参数解释**： 资源池节点Docker盘占数据盘的百分比。例如Docker盘大小占用数据盘20%，该参数值为20。 **取值范围**： 不涉及。

        :param docker_thin_pool: The docker_thin_pool of this DockerLvmConfig.
        :type docker_thin_pool: int
        """
        self._docker_thin_pool = docker_thin_pool

    @property
    def kubernetes_lv(self):
        r"""Gets the kubernetes_lv of this DockerLvmConfig.

        **参数解释**： 资源池节点上kubelet占数据盘的百分比。例如Docker盘大小占用数据盘20%，该参数值为20。 **取值范围**： 不涉及。

        :return: The kubernetes_lv of this DockerLvmConfig.
        :rtype: int
        """
        return self._kubernetes_lv

    @kubernetes_lv.setter
    def kubernetes_lv(self, kubernetes_lv):
        r"""Sets the kubernetes_lv of this DockerLvmConfig.

        **参数解释**： 资源池节点上kubelet占数据盘的百分比。例如Docker盘大小占用数据盘20%，该参数值为20。 **取值范围**： 不涉及。

        :param kubernetes_lv: The kubernetes_lv of this DockerLvmConfig.
        :type kubernetes_lv: int
        """
        self._kubernetes_lv = kubernetes_lv

    @property
    def docker_disk_type(self):
        r"""Gets the docker_disk_type of this DockerLvmConfig.

        **参数解释**： 磁盘类型。 **取值范围**： 可选值如下： - evs：云硬盘 - ssd：本地SSD硬盘

        :return: The docker_disk_type of this DockerLvmConfig.
        :rtype: str
        """
        return self._docker_disk_type

    @docker_disk_type.setter
    def docker_disk_type(self, docker_disk_type):
        r"""Sets the docker_disk_type of this DockerLvmConfig.

        **参数解释**： 磁盘类型。 **取值范围**： 可选值如下： - evs：云硬盘 - ssd：本地SSD硬盘

        :param docker_disk_type: The docker_disk_type of this DockerLvmConfig.
        :type docker_disk_type: str
        """
        self._docker_disk_type = docker_disk_type

    @property
    def lv_type(self):
        r"""Gets the lv_type of this DockerLvmConfig.

        **参数解释**： LVM写入模式。 **取值范围**： 可选值如下： - striped：条带模式，使用多块磁盘组成条带模式，能够提升磁盘性能 - linear：线性模式

        :return: The lv_type of this DockerLvmConfig.
        :rtype: str
        """
        return self._lv_type

    @lv_type.setter
    def lv_type(self, lv_type):
        r"""Sets the lv_type of this DockerLvmConfig.

        **参数解释**： LVM写入模式。 **取值范围**： 可选值如下： - striped：条带模式，使用多块磁盘组成条带模式，能够提升磁盘性能 - linear：线性模式

        :param lv_type: The lv_type of this DockerLvmConfig.
        :type lv_type: str
        """
        self._lv_type = lv_type

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
        if not isinstance(other, DockerLvmConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
