# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebTamperProtectionContainerResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'container_id': 'str',
        'container_name': 'str',
        'image_name': 'str',
        'image_version': 'str',
        'pod_name': 'str',
        'pod_ip': 'str',
        'namespace': 'str',
        'all_directory_nums': 'int',
        'protected_directory_nums': 'int',
        'host_info': 'WebTamperEventHostInfo',
        'cluster_info': 'WebTamperEventClusterInfo'
    }

    attribute_map = {
        'status': 'status',
        'container_id': 'container_id',
        'container_name': 'container_name',
        'image_name': 'image_name',
        'image_version': 'image_version',
        'pod_name': 'pod_name',
        'pod_ip': 'pod_ip',
        'namespace': 'namespace',
        'all_directory_nums': 'all_directory_nums',
        'protected_directory_nums': 'protected_directory_nums',
        'host_info': 'host_info',
        'cluster_info': 'cluster_info'
    }

    def __init__(self, status=None, container_id=None, container_name=None, image_name=None, image_version=None, pod_name=None, pod_ip=None, namespace=None, all_directory_nums=None, protected_directory_nums=None, host_info=None, cluster_info=None):
        r"""WebTamperProtectionContainerResponseInfo

        The model defined in huaweicloud sdk

        :param status: description: |   **参数解释**:   防护状态   **取值范围**:   - protected：防护中   - partial_protected：部分防护   - protect_failed：防护失败 
        :type status: str
        :param container_id: **参数解释**： 容器ID **取值范围**： 字符长度1-256位 
        :type container_id: str
        :param container_name: **参数解释**： 容器名称 **取值范围**： 字符长度1-256位 
        :type container_name: str
        :param image_name: **参数解释**： 镜像名称 **取值范围**： 字符长度1-256位 
        :type image_name: str
        :param image_version: **参数解释**： 镜像版本 **取值范围**： 字符长度1-256位 
        :type image_version: str
        :param pod_name: **参数解释**： pod name **取值范围**： 字符长度1-256位 
        :type pod_name: str
        :param pod_ip: **参数解释**： pod ip **取值范围**： 字符长度1-256位 
        :type pod_ip: str
        :param namespace: **参数解释**： 命名空间 **取值范围**： 字符长度1-256位 
        :type namespace: str
        :param all_directory_nums: **参数解释**: 防护总目录数量 **取值范围**: 最小值0，最大值2147483647 
        :type all_directory_nums: int
        :param protected_directory_nums: **参数解释**: 防护成功数量 **取值范围**: 最小值0，最大值2147483647 
        :type protected_directory_nums: int
        :param host_info: 
        :type host_info: :class:`huaweicloudsdkhss.v5.WebTamperEventHostInfo`
        :param cluster_info: 
        :type cluster_info: :class:`huaweicloudsdkhss.v5.WebTamperEventClusterInfo`
        """
        
        

        self._status = None
        self._container_id = None
        self._container_name = None
        self._image_name = None
        self._image_version = None
        self._pod_name = None
        self._pod_ip = None
        self._namespace = None
        self._all_directory_nums = None
        self._protected_directory_nums = None
        self._host_info = None
        self._cluster_info = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if container_id is not None:
            self.container_id = container_id
        if container_name is not None:
            self.container_name = container_name
        if image_name is not None:
            self.image_name = image_name
        if image_version is not None:
            self.image_version = image_version
        if pod_name is not None:
            self.pod_name = pod_name
        if pod_ip is not None:
            self.pod_ip = pod_ip
        if namespace is not None:
            self.namespace = namespace
        if all_directory_nums is not None:
            self.all_directory_nums = all_directory_nums
        if protected_directory_nums is not None:
            self.protected_directory_nums = protected_directory_nums
        if host_info is not None:
            self.host_info = host_info
        if cluster_info is not None:
            self.cluster_info = cluster_info

    @property
    def status(self):
        r"""Gets the status of this WebTamperProtectionContainerResponseInfo.

        description: |   **参数解释**:   防护状态   **取值范围**:   - protected：防护中   - partial_protected：部分防护   - protect_failed：防护失败 

        :return: The status of this WebTamperProtectionContainerResponseInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this WebTamperProtectionContainerResponseInfo.

        description: |   **参数解释**:   防护状态   **取值范围**:   - protected：防护中   - partial_protected：部分防护   - protect_failed：防护失败 

        :param status: The status of this WebTamperProtectionContainerResponseInfo.
        :type status: str
        """
        self._status = status

    @property
    def container_id(self):
        r"""Gets the container_id of this WebTamperProtectionContainerResponseInfo.

        **参数解释**： 容器ID **取值范围**： 字符长度1-256位 

        :return: The container_id of this WebTamperProtectionContainerResponseInfo.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this WebTamperProtectionContainerResponseInfo.

        **参数解释**： 容器ID **取值范围**： 字符长度1-256位 

        :param container_id: The container_id of this WebTamperProtectionContainerResponseInfo.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def container_name(self):
        r"""Gets the container_name of this WebTamperProtectionContainerResponseInfo.

        **参数解释**： 容器名称 **取值范围**： 字符长度1-256位 

        :return: The container_name of this WebTamperProtectionContainerResponseInfo.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this WebTamperProtectionContainerResponseInfo.

        **参数解释**： 容器名称 **取值范围**： 字符长度1-256位 

        :param container_name: The container_name of this WebTamperProtectionContainerResponseInfo.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def image_name(self):
        r"""Gets the image_name of this WebTamperProtectionContainerResponseInfo.

        **参数解释**： 镜像名称 **取值范围**： 字符长度1-256位 

        :return: The image_name of this WebTamperProtectionContainerResponseInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this WebTamperProtectionContainerResponseInfo.

        **参数解释**： 镜像名称 **取值范围**： 字符长度1-256位 

        :param image_name: The image_name of this WebTamperProtectionContainerResponseInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def image_version(self):
        r"""Gets the image_version of this WebTamperProtectionContainerResponseInfo.

        **参数解释**： 镜像版本 **取值范围**： 字符长度1-256位 

        :return: The image_version of this WebTamperProtectionContainerResponseInfo.
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        r"""Sets the image_version of this WebTamperProtectionContainerResponseInfo.

        **参数解释**： 镜像版本 **取值范围**： 字符长度1-256位 

        :param image_version: The image_version of this WebTamperProtectionContainerResponseInfo.
        :type image_version: str
        """
        self._image_version = image_version

    @property
    def pod_name(self):
        r"""Gets the pod_name of this WebTamperProtectionContainerResponseInfo.

        **参数解释**： pod name **取值范围**： 字符长度1-256位 

        :return: The pod_name of this WebTamperProtectionContainerResponseInfo.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        r"""Sets the pod_name of this WebTamperProtectionContainerResponseInfo.

        **参数解释**： pod name **取值范围**： 字符长度1-256位 

        :param pod_name: The pod_name of this WebTamperProtectionContainerResponseInfo.
        :type pod_name: str
        """
        self._pod_name = pod_name

    @property
    def pod_ip(self):
        r"""Gets the pod_ip of this WebTamperProtectionContainerResponseInfo.

        **参数解释**： pod ip **取值范围**： 字符长度1-256位 

        :return: The pod_ip of this WebTamperProtectionContainerResponseInfo.
        :rtype: str
        """
        return self._pod_ip

    @pod_ip.setter
    def pod_ip(self, pod_ip):
        r"""Sets the pod_ip of this WebTamperProtectionContainerResponseInfo.

        **参数解释**： pod ip **取值范围**： 字符长度1-256位 

        :param pod_ip: The pod_ip of this WebTamperProtectionContainerResponseInfo.
        :type pod_ip: str
        """
        self._pod_ip = pod_ip

    @property
    def namespace(self):
        r"""Gets the namespace of this WebTamperProtectionContainerResponseInfo.

        **参数解释**： 命名空间 **取值范围**： 字符长度1-256位 

        :return: The namespace of this WebTamperProtectionContainerResponseInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this WebTamperProtectionContainerResponseInfo.

        **参数解释**： 命名空间 **取值范围**： 字符长度1-256位 

        :param namespace: The namespace of this WebTamperProtectionContainerResponseInfo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def all_directory_nums(self):
        r"""Gets the all_directory_nums of this WebTamperProtectionContainerResponseInfo.

        **参数解释**: 防护总目录数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The all_directory_nums of this WebTamperProtectionContainerResponseInfo.
        :rtype: int
        """
        return self._all_directory_nums

    @all_directory_nums.setter
    def all_directory_nums(self, all_directory_nums):
        r"""Sets the all_directory_nums of this WebTamperProtectionContainerResponseInfo.

        **参数解释**: 防护总目录数量 **取值范围**: 最小值0，最大值2147483647 

        :param all_directory_nums: The all_directory_nums of this WebTamperProtectionContainerResponseInfo.
        :type all_directory_nums: int
        """
        self._all_directory_nums = all_directory_nums

    @property
    def protected_directory_nums(self):
        r"""Gets the protected_directory_nums of this WebTamperProtectionContainerResponseInfo.

        **参数解释**: 防护成功数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The protected_directory_nums of this WebTamperProtectionContainerResponseInfo.
        :rtype: int
        """
        return self._protected_directory_nums

    @protected_directory_nums.setter
    def protected_directory_nums(self, protected_directory_nums):
        r"""Sets the protected_directory_nums of this WebTamperProtectionContainerResponseInfo.

        **参数解释**: 防护成功数量 **取值范围**: 最小值0，最大值2147483647 

        :param protected_directory_nums: The protected_directory_nums of this WebTamperProtectionContainerResponseInfo.
        :type protected_directory_nums: int
        """
        self._protected_directory_nums = protected_directory_nums

    @property
    def host_info(self):
        r"""Gets the host_info of this WebTamperProtectionContainerResponseInfo.

        :return: The host_info of this WebTamperProtectionContainerResponseInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.WebTamperEventHostInfo`
        """
        return self._host_info

    @host_info.setter
    def host_info(self, host_info):
        r"""Sets the host_info of this WebTamperProtectionContainerResponseInfo.

        :param host_info: The host_info of this WebTamperProtectionContainerResponseInfo.
        :type host_info: :class:`huaweicloudsdkhss.v5.WebTamperEventHostInfo`
        """
        self._host_info = host_info

    @property
    def cluster_info(self):
        r"""Gets the cluster_info of this WebTamperProtectionContainerResponseInfo.

        :return: The cluster_info of this WebTamperProtectionContainerResponseInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.WebTamperEventClusterInfo`
        """
        return self._cluster_info

    @cluster_info.setter
    def cluster_info(self, cluster_info):
        r"""Sets the cluster_info of this WebTamperProtectionContainerResponseInfo.

        :param cluster_info: The cluster_info of this WebTamperProtectionContainerResponseInfo.
        :type cluster_info: :class:`huaweicloudsdkhss.v5.WebTamperEventClusterInfo`
        """
        self._cluster_info = cluster_info

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
        if not isinstance(other, WebTamperProtectionContainerResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
