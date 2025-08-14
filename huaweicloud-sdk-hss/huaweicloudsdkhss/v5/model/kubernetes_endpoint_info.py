# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KubernetesEndpointInfo:

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
        'service_name': 'str',
        'namespace': 'str',
        'creation_timestamp': 'int',
        'cluster_name': 'str',
        'cluster_type': 'str',
        'association_service': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'service_name': 'service_name',
        'namespace': 'namespace',
        'creation_timestamp': 'creation_timestamp',
        'cluster_name': 'cluster_name',
        'cluster_type': 'cluster_type',
        'association_service': 'association_service'
    }

    def __init__(self, id=None, name=None, service_name=None, namespace=None, creation_timestamp=None, cluster_name=None, cluster_type=None, association_service=None):
        r"""KubernetesEndpointInfo

        The model defined in huaweicloud sdk

        :param id: id
        :type id: str
        :param name: 端点名称
        :type name: str
        :param service_name: 服务名称
        :type service_name: str
        :param namespace: 命名空间
        :type namespace: str
        :param creation_timestamp: 创建时间戳
        :type creation_timestamp: int
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param cluster_type: 集群类型，包含以下几种： - k8s：原生集群 - cce：CCE集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群
        :type cluster_type: str
        :param association_service: 是否关联服务
        :type association_service: bool
        """
        
        

        self._id = None
        self._name = None
        self._service_name = None
        self._namespace = None
        self._creation_timestamp = None
        self._cluster_name = None
        self._cluster_type = None
        self._association_service = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if service_name is not None:
            self.service_name = service_name
        if namespace is not None:
            self.namespace = namespace
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if association_service is not None:
            self.association_service = association_service

    @property
    def id(self):
        r"""Gets the id of this KubernetesEndpointInfo.

        id

        :return: The id of this KubernetesEndpointInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this KubernetesEndpointInfo.

        id

        :param id: The id of this KubernetesEndpointInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this KubernetesEndpointInfo.

        端点名称

        :return: The name of this KubernetesEndpointInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this KubernetesEndpointInfo.

        端点名称

        :param name: The name of this KubernetesEndpointInfo.
        :type name: str
        """
        self._name = name

    @property
    def service_name(self):
        r"""Gets the service_name of this KubernetesEndpointInfo.

        服务名称

        :return: The service_name of this KubernetesEndpointInfo.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this KubernetesEndpointInfo.

        服务名称

        :param service_name: The service_name of this KubernetesEndpointInfo.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def namespace(self):
        r"""Gets the namespace of this KubernetesEndpointInfo.

        命名空间

        :return: The namespace of this KubernetesEndpointInfo.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this KubernetesEndpointInfo.

        命名空间

        :param namespace: The namespace of this KubernetesEndpointInfo.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def creation_timestamp(self):
        r"""Gets the creation_timestamp of this KubernetesEndpointInfo.

        创建时间戳

        :return: The creation_timestamp of this KubernetesEndpointInfo.
        :rtype: int
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        r"""Sets the creation_timestamp of this KubernetesEndpointInfo.

        创建时间戳

        :param creation_timestamp: The creation_timestamp of this KubernetesEndpointInfo.
        :type creation_timestamp: int
        """
        self._creation_timestamp = creation_timestamp

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this KubernetesEndpointInfo.

        集群名称

        :return: The cluster_name of this KubernetesEndpointInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this KubernetesEndpointInfo.

        集群名称

        :param cluster_name: The cluster_name of this KubernetesEndpointInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this KubernetesEndpointInfo.

        集群类型，包含以下几种： - k8s：原生集群 - cce：CCE集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群

        :return: The cluster_type of this KubernetesEndpointInfo.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this KubernetesEndpointInfo.

        集群类型，包含以下几种： - k8s：原生集群 - cce：CCE集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群

        :param cluster_type: The cluster_type of this KubernetesEndpointInfo.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def association_service(self):
        r"""Gets the association_service of this KubernetesEndpointInfo.

        是否关联服务

        :return: The association_service of this KubernetesEndpointInfo.
        :rtype: bool
        """
        return self._association_service

    @association_service.setter
    def association_service(self, association_service):
        r"""Sets the association_service of this KubernetesEndpointInfo.

        是否关联服务

        :param association_service: The association_service of this KubernetesEndpointInfo.
        :type association_service: bool
        """
        self._association_service = association_service

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
        if not isinstance(other, KubernetesEndpointInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
