# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulAffectImageContainersResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'container_name': 'str',
        'container_id': 'str',
        'cluster_name': 'str',
        'cluster_id': 'str',
        'host_name': 'str',
        'public_ip': 'str',
        'private_ip': 'str',
        'pod_name': 'str',
        'pod_id': 'str',
        'namespace': 'str'
    }

    attribute_map = {
        'container_name': 'container_name',
        'container_id': 'container_id',
        'cluster_name': 'cluster_name',
        'cluster_id': 'cluster_id',
        'host_name': 'host_name',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'pod_name': 'pod_name',
        'pod_id': 'pod_id',
        'namespace': 'namespace'
    }

    def __init__(self, container_name=None, container_id=None, cluster_name=None, cluster_id=None, host_name=None, public_ip=None, private_ip=None, pod_name=None, pod_id=None, namespace=None):
        r"""VulAffectImageContainersResponseInfo

        The model defined in huaweicloud sdk

        :param container_name: 容器名称
        :type container_name: str
        :param container_id: 容器ID
        :type container_id: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param cluster_id: 集群ID
        :type cluster_id: str
        :param host_name: 节点名称
        :type host_name: str
        :param public_ip: 公网IP
        :type public_ip: str
        :param private_ip: 私网IP
        :type private_ip: str
        :param pod_name: pod名称
        :type pod_name: str
        :param pod_id: pod id
        :type pod_id: str
        :param namespace: 命名空间
        :type namespace: str
        """
        
        

        self._container_name = None
        self._container_id = None
        self._cluster_name = None
        self._cluster_id = None
        self._host_name = None
        self._public_ip = None
        self._private_ip = None
        self._pod_name = None
        self._pod_id = None
        self._namespace = None
        self.discriminator = None

        if container_name is not None:
            self.container_name = container_name
        if container_id is not None:
            self.container_id = container_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if host_name is not None:
            self.host_name = host_name
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if pod_name is not None:
            self.pod_name = pod_name
        if pod_id is not None:
            self.pod_id = pod_id
        if namespace is not None:
            self.namespace = namespace

    @property
    def container_name(self):
        r"""Gets the container_name of this VulAffectImageContainersResponseInfo.

        容器名称

        :return: The container_name of this VulAffectImageContainersResponseInfo.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this VulAffectImageContainersResponseInfo.

        容器名称

        :param container_name: The container_name of this VulAffectImageContainersResponseInfo.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def container_id(self):
        r"""Gets the container_id of this VulAffectImageContainersResponseInfo.

        容器ID

        :return: The container_id of this VulAffectImageContainersResponseInfo.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this VulAffectImageContainersResponseInfo.

        容器ID

        :param container_id: The container_id of this VulAffectImageContainersResponseInfo.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this VulAffectImageContainersResponseInfo.

        集群名称

        :return: The cluster_name of this VulAffectImageContainersResponseInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this VulAffectImageContainersResponseInfo.

        集群名称

        :param cluster_name: The cluster_name of this VulAffectImageContainersResponseInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this VulAffectImageContainersResponseInfo.

        集群ID

        :return: The cluster_id of this VulAffectImageContainersResponseInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this VulAffectImageContainersResponseInfo.

        集群ID

        :param cluster_id: The cluster_id of this VulAffectImageContainersResponseInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def host_name(self):
        r"""Gets the host_name of this VulAffectImageContainersResponseInfo.

        节点名称

        :return: The host_name of this VulAffectImageContainersResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this VulAffectImageContainersResponseInfo.

        节点名称

        :param host_name: The host_name of this VulAffectImageContainersResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def public_ip(self):
        r"""Gets the public_ip of this VulAffectImageContainersResponseInfo.

        公网IP

        :return: The public_ip of this VulAffectImageContainersResponseInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this VulAffectImageContainersResponseInfo.

        公网IP

        :param public_ip: The public_ip of this VulAffectImageContainersResponseInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this VulAffectImageContainersResponseInfo.

        私网IP

        :return: The private_ip of this VulAffectImageContainersResponseInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this VulAffectImageContainersResponseInfo.

        私网IP

        :param private_ip: The private_ip of this VulAffectImageContainersResponseInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def pod_name(self):
        r"""Gets the pod_name of this VulAffectImageContainersResponseInfo.

        pod名称

        :return: The pod_name of this VulAffectImageContainersResponseInfo.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        r"""Sets the pod_name of this VulAffectImageContainersResponseInfo.

        pod名称

        :param pod_name: The pod_name of this VulAffectImageContainersResponseInfo.
        :type pod_name: str
        """
        self._pod_name = pod_name

    @property
    def pod_id(self):
        r"""Gets the pod_id of this VulAffectImageContainersResponseInfo.

        pod id

        :return: The pod_id of this VulAffectImageContainersResponseInfo.
        :rtype: str
        """
        return self._pod_id

    @pod_id.setter
    def pod_id(self, pod_id):
        r"""Sets the pod_id of this VulAffectImageContainersResponseInfo.

        pod id

        :param pod_id: The pod_id of this VulAffectImageContainersResponseInfo.
        :type pod_id: str
        """
        self._pod_id = pod_id

    @property
    def namespace(self):
        r"""Gets the namespace of this VulAffectImageContainersResponseInfo.

        命名空间

        :return: The namespace of this VulAffectImageContainersResponseInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this VulAffectImageContainersResponseInfo.

        命名空间

        :param namespace: The namespace of this VulAffectImageContainersResponseInfo.
        :type namespace: str
        """
        self._namespace = namespace

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
        if not isinstance(other, VulAffectImageContainersResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
