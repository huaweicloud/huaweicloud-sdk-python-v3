# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebTamperEventContainerInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'image_name': 'str',
        'image_version': 'str',
        'container_id': 'str',
        'container_name': 'str',
        'pod_name': 'str',
        'pod_ip': 'str',
        'namespace': 'str',
        'cluster_id': 'str',
        'cluster_name': 'str'
    }

    attribute_map = {
        'image_name': 'image_name',
        'image_version': 'image_version',
        'container_id': 'container_id',
        'container_name': 'container_name',
        'pod_name': 'pod_name',
        'pod_ip': 'pod_ip',
        'namespace': 'namespace',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name'
    }

    def __init__(self, image_name=None, image_version=None, container_id=None, container_name=None, pod_name=None, pod_ip=None, namespace=None, cluster_id=None, cluster_name=None):
        r"""WebTamperEventContainerInfo

        The model defined in huaweicloud sdk

        :param image_name: **参数解释**： 镜像名称 **取值范围**： 字符长度1-256位 
        :type image_name: str
        :param image_version: **参数解释**： 镜像版本 **取值范围**： 字符长度1-256位 
        :type image_version: str
        :param container_id: **参数解释**： 容器ID **取值范围**： 字符长度1-256位 
        :type container_id: str
        :param container_name: **参数解释**： 容器名称 **取值范围**： 字符长度1-256位 
        :type container_name: str
        :param pod_name: **参数解释**： pod name **取值范围**： 字符长度1-256位 
        :type pod_name: str
        :param pod_ip: **参数解释**： pod ip **取值范围**： 字符长度1-256位 
        :type pod_ip: str
        :param namespace: **参数解释**： 命名空间 **取值范围**： 字符长度1-256位 
        :type namespace: str
        :param cluster_id: **参数解释**： 集群ID **取值范围**： 字符长度1-128位 
        :type cluster_id: str
        :param cluster_name: **参数解释**： 集群名称 **取值范围**： 字符长度1-256位 
        :type cluster_name: str
        """
        
        

        self._image_name = None
        self._image_version = None
        self._container_id = None
        self._container_name = None
        self._pod_name = None
        self._pod_ip = None
        self._namespace = None
        self._cluster_id = None
        self._cluster_name = None
        self.discriminator = None

        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if container_id is not None:
            self.container_id = container_id
        if container_name is not None:
            self.container_name = container_name
        if pod_name is not None:
            self.pod_name = pod_name
        if pod_ip is not None:
            self.pod_ip = pod_ip
        if namespace is not None:
            self.namespace = namespace
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name

    @property
    def image_name(self):
        r"""Gets the image_name of this WebTamperEventContainerInfo.

        **参数解释**： 镜像名称 **取值范围**： 字符长度1-256位 

        :return: The image_name of this WebTamperEventContainerInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this WebTamperEventContainerInfo.

        **参数解释**： 镜像名称 **取值范围**： 字符长度1-256位 

        :param image_name: The image_name of this WebTamperEventContainerInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this WebTamperEventContainerInfo.

        **参数解释**： 镜像版本 **取值范围**： 字符长度1-256位 

        :return: The image_version of this WebTamperEventContainerInfo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this WebTamperEventContainerInfo.

        **参数解释**： 镜像版本 **取值范围**： 字符长度1-256位 

        :param image_version: The image_version of this WebTamperEventContainerInfo.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def container_id(self):
        r"""Gets the container_id of this WebTamperEventContainerInfo.

        **参数解释**： 容器ID **取值范围**： 字符长度1-256位 

        :return: The container_id of this WebTamperEventContainerInfo.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this WebTamperEventContainerInfo.

        **参数解释**： 容器ID **取值范围**： 字符长度1-256位 

        :param container_id: The container_id of this WebTamperEventContainerInfo.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def container_name(self):
        r"""Gets the container_name of this WebTamperEventContainerInfo.

        **参数解释**： 容器名称 **取值范围**： 字符长度1-256位 

        :return: The container_name of this WebTamperEventContainerInfo.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this WebTamperEventContainerInfo.

        **参数解释**： 容器名称 **取值范围**： 字符长度1-256位 

        :param container_name: The container_name of this WebTamperEventContainerInfo.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def pod_name(self):
        r"""Gets the pod_name of this WebTamperEventContainerInfo.

        **参数解释**： pod name **取值范围**： 字符长度1-256位 

        :return: The pod_name of this WebTamperEventContainerInfo.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        r"""Sets the pod_name of this WebTamperEventContainerInfo.

        **参数解释**： pod name **取值范围**： 字符长度1-256位 

        :param pod_name: The pod_name of this WebTamperEventContainerInfo.
        :type pod_name: str
        """
        self._pod_name = pod_name

    @property
    def pod_ip(self):
        r"""Gets the pod_ip of this WebTamperEventContainerInfo.

        **参数解释**： pod ip **取值范围**： 字符长度1-256位 

        :return: The pod_ip of this WebTamperEventContainerInfo.
        :rtype: str
        """
        return self._pod_ip

    @pod_ip.setter
    def pod_ip(self, pod_ip):
        r"""Sets the pod_ip of this WebTamperEventContainerInfo.

        **参数解释**： pod ip **取值范围**： 字符长度1-256位 

        :param pod_ip: The pod_ip of this WebTamperEventContainerInfo.
        :type pod_ip: str
        """
        self._pod_ip = pod_ip

    @property
    def namespace(self):
        r"""Gets the namespace of this WebTamperEventContainerInfo.

        **参数解释**： 命名空间 **取值范围**： 字符长度1-256位 

        :return: The namespace of this WebTamperEventContainerInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this WebTamperEventContainerInfo.

        **参数解释**： 命名空间 **取值范围**： 字符长度1-256位 

        :param namespace: The namespace of this WebTamperEventContainerInfo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this WebTamperEventContainerInfo.

        **参数解释**： 集群ID **取值范围**： 字符长度1-128位 

        :return: The cluster_id of this WebTamperEventContainerInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this WebTamperEventContainerInfo.

        **参数解释**： 集群ID **取值范围**： 字符长度1-128位 

        :param cluster_id: The cluster_id of this WebTamperEventContainerInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this WebTamperEventContainerInfo.

        **参数解释**： 集群名称 **取值范围**： 字符长度1-256位 

        :return: The cluster_name of this WebTamperEventContainerInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this WebTamperEventContainerInfo.

        **参数解释**： 集群名称 **取值范围**： 字符长度1-256位 

        :param cluster_name: The cluster_name of this WebTamperEventContainerInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

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
        if not isinstance(other, WebTamperEventContainerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
