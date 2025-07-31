# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKubernetesServiceInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'endpoint_name': 'str',
        'namespace': 'str',
        'creation_timestamp': 'int',
        'cluster_name': 'str',
        'labels': 'str',
        'type': 'str',
        'cluster_ip': 'str',
        'selector': 'str',
        'session_affinity': 'str',
        'service_port_list': 'list[KubernetesServicePortInfo]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'endpoint_name': 'endpoint_name',
        'namespace': 'namespace',
        'creation_timestamp': 'creation_timestamp',
        'cluster_name': 'cluster_name',
        'labels': 'labels',
        'type': 'type',
        'cluster_ip': 'cluster_ip',
        'selector': 'selector',
        'session_affinity': 'session_affinity',
        'service_port_list': 'service_port_list'
    }

    def __init__(self, id=None, name=None, endpoint_name=None, namespace=None, creation_timestamp=None, cluster_name=None, labels=None, type=None, cluster_ip=None, selector=None, session_affinity=None, service_port_list=None):
        r"""ShowKubernetesServiceInfoResponse

        The model defined in huaweicloud sdk

        :param id: 服务ID
        :type id: str
        :param name: 服务名称
        :type name: str
        :param endpoint_name: 端点名称
        :type endpoint_name: str
        :param namespace: 命名空间
        :type namespace: str
        :param creation_timestamp: 创建时间戳
        :type creation_timestamp: int
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param labels: 标签
        :type labels: str
        :param type: 服务类型（访问方式）
        :type type: str
        :param cluster_ip: 集群IP
        :type cluster_ip: str
        :param selector: 选择器
        :type selector: str
        :param session_affinity: 会话亲和性
        :type session_affinity: str
        :param service_port_list: Service关联端口列表
        :type service_port_list: list[:class:`huaweicloudsdkhss.v5.KubernetesServicePortInfo`]
        """
        
        super(ShowKubernetesServiceInfoResponse, self).__init__()

        self._id = None
        self._name = None
        self._endpoint_name = None
        self._namespace = None
        self._creation_timestamp = None
        self._cluster_name = None
        self._labels = None
        self._type = None
        self._cluster_ip = None
        self._selector = None
        self._session_affinity = None
        self._service_port_list = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if endpoint_name is not None:
            self.endpoint_name = endpoint_name
        if namespace is not None:
            self.namespace = namespace
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if labels is not None:
            self.labels = labels
        if type is not None:
            self.type = type
        if cluster_ip is not None:
            self.cluster_ip = cluster_ip
        if selector is not None:
            self.selector = selector
        if session_affinity is not None:
            self.session_affinity = session_affinity
        if service_port_list is not None:
            self.service_port_list = service_port_list

    @property
    def id(self):
        r"""Gets the id of this ShowKubernetesServiceInfoResponse.

        服务ID

        :return: The id of this ShowKubernetesServiceInfoResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowKubernetesServiceInfoResponse.

        服务ID

        :param id: The id of this ShowKubernetesServiceInfoResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowKubernetesServiceInfoResponse.

        服务名称

        :return: The name of this ShowKubernetesServiceInfoResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowKubernetesServiceInfoResponse.

        服务名称

        :param name: The name of this ShowKubernetesServiceInfoResponse.
        :type name: str
        """
        self._name = name

    @property
    def endpoint_name(self):
        r"""Gets the endpoint_name of this ShowKubernetesServiceInfoResponse.

        端点名称

        :return: The endpoint_name of this ShowKubernetesServiceInfoResponse.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        r"""Sets the endpoint_name of this ShowKubernetesServiceInfoResponse.

        端点名称

        :param endpoint_name: The endpoint_name of this ShowKubernetesServiceInfoResponse.
        :type endpoint_name: str
        """
        self._endpoint_name = endpoint_name

    @property
    def namespace(self):
        r"""Gets the namespace of this ShowKubernetesServiceInfoResponse.

        命名空间

        :return: The namespace of this ShowKubernetesServiceInfoResponse.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ShowKubernetesServiceInfoResponse.

        命名空间

        :param namespace: The namespace of this ShowKubernetesServiceInfoResponse.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def creation_timestamp(self):
        r"""Gets the creation_timestamp of this ShowKubernetesServiceInfoResponse.

        创建时间戳

        :return: The creation_timestamp of this ShowKubernetesServiceInfoResponse.
        :rtype: int
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        r"""Sets the creation_timestamp of this ShowKubernetesServiceInfoResponse.

        创建时间戳

        :param creation_timestamp: The creation_timestamp of this ShowKubernetesServiceInfoResponse.
        :type creation_timestamp: int
        """
        self._creation_timestamp = creation_timestamp

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ShowKubernetesServiceInfoResponse.

        集群名称

        :return: The cluster_name of this ShowKubernetesServiceInfoResponse.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ShowKubernetesServiceInfoResponse.

        集群名称

        :param cluster_name: The cluster_name of this ShowKubernetesServiceInfoResponse.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def labels(self):
        r"""Gets the labels of this ShowKubernetesServiceInfoResponse.

        标签

        :return: The labels of this ShowKubernetesServiceInfoResponse.
        :rtype: str
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ShowKubernetesServiceInfoResponse.

        标签

        :param labels: The labels of this ShowKubernetesServiceInfoResponse.
        :type labels: str
        """
        self._labels = labels

    @property
    def type(self):
        r"""Gets the type of this ShowKubernetesServiceInfoResponse.

        服务类型（访问方式）

        :return: The type of this ShowKubernetesServiceInfoResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowKubernetesServiceInfoResponse.

        服务类型（访问方式）

        :param type: The type of this ShowKubernetesServiceInfoResponse.
        :type type: str
        """
        self._type = type

    @property
    def cluster_ip(self):
        r"""Gets the cluster_ip of this ShowKubernetesServiceInfoResponse.

        集群IP

        :return: The cluster_ip of this ShowKubernetesServiceInfoResponse.
        :rtype: str
        """
        return self._cluster_ip

    @cluster_ip.setter
    def cluster_ip(self, cluster_ip):
        r"""Sets the cluster_ip of this ShowKubernetesServiceInfoResponse.

        集群IP

        :param cluster_ip: The cluster_ip of this ShowKubernetesServiceInfoResponse.
        :type cluster_ip: str
        """
        self._cluster_ip = cluster_ip

    @property
    def selector(self):
        r"""Gets the selector of this ShowKubernetesServiceInfoResponse.

        选择器

        :return: The selector of this ShowKubernetesServiceInfoResponse.
        :rtype: str
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        r"""Sets the selector of this ShowKubernetesServiceInfoResponse.

        选择器

        :param selector: The selector of this ShowKubernetesServiceInfoResponse.
        :type selector: str
        """
        self._selector = selector

    @property
    def session_affinity(self):
        r"""Gets the session_affinity of this ShowKubernetesServiceInfoResponse.

        会话亲和性

        :return: The session_affinity of this ShowKubernetesServiceInfoResponse.
        :rtype: str
        """
        return self._session_affinity

    @session_affinity.setter
    def session_affinity(self, session_affinity):
        r"""Sets the session_affinity of this ShowKubernetesServiceInfoResponse.

        会话亲和性

        :param session_affinity: The session_affinity of this ShowKubernetesServiceInfoResponse.
        :type session_affinity: str
        """
        self._session_affinity = session_affinity

    @property
    def service_port_list(self):
        r"""Gets the service_port_list of this ShowKubernetesServiceInfoResponse.

        Service关联端口列表

        :return: The service_port_list of this ShowKubernetesServiceInfoResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.KubernetesServicePortInfo`]
        """
        return self._service_port_list

    @service_port_list.setter
    def service_port_list(self, service_port_list):
        r"""Sets the service_port_list of this ShowKubernetesServiceInfoResponse.

        Service关联端口列表

        :param service_port_list: The service_port_list of this ShowKubernetesServiceInfoResponse.
        :type service_port_list: list[:class:`huaweicloudsdkhss.v5.KubernetesServicePortInfo`]
        """
        self._service_port_list = service_port_list

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
        if not isinstance(other, ShowKubernetesServiceInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
