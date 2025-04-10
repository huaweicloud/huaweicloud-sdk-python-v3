# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Spec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'engine_id': 'str',
        'spec_type': 'str',
        'cluster': 'str',
        'cluster_id': 'str',
        'cluster_nodes': 'SpecClusterNode',
        'flavor': 'str',
        'region': 'str',
        'version': 'str',
        'extend_param': 'str'
    }

    attribute_map = {
        'id': 'id',
        'engine_id': 'engineId',
        'spec_type': 'specType',
        'cluster': 'cluster',
        'cluster_id': 'clusterId',
        'cluster_nodes': 'clusterNodes',
        'flavor': 'flavor',
        'region': 'region',
        'version': 'version',
        'extend_param': 'extendParam'
    }

    def __init__(self, id=None, engine_id=None, spec_type=None, cluster=None, cluster_id=None, cluster_nodes=None, flavor=None, region=None, version=None, extend_param=None):
        r"""Spec

        The model defined in huaweicloud sdk

        :param id: 微服务引擎CCE规格ID
        :type id: int
        :param engine_id: 微服务引擎ID
        :type engine_id: str
        :param spec_type: 微服务引擎的集群部署类型
        :type spec_type: str
        :param cluster: 微服务引擎的CCE集群信息，目前为null
        :type cluster: str
        :param cluster_id: 微服务引擎的CCE集群ID
        :type cluster_id: str
        :param cluster_nodes: 
        :type cluster_nodes: :class:`huaweicloudsdkcse.v1.SpecClusterNode`
        :param flavor: 微服务引擎的CCE集群规格
        :type flavor: str
        :param region: 微服务引擎的CCE集群所在region
        :type region: str
        :param version: 微服务引擎的CCE集群版本
        :type version: str
        :param extend_param: 微服务引擎的CCE集群附加参数
        :type extend_param: str
        """
        
        

        self._id = None
        self._engine_id = None
        self._spec_type = None
        self._cluster = None
        self._cluster_id = None
        self._cluster_nodes = None
        self._flavor = None
        self._region = None
        self._version = None
        self._extend_param = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if engine_id is not None:
            self.engine_id = engine_id
        if spec_type is not None:
            self.spec_type = spec_type
        if cluster is not None:
            self.cluster = cluster
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_nodes is not None:
            self.cluster_nodes = cluster_nodes
        if flavor is not None:
            self.flavor = flavor
        if region is not None:
            self.region = region
        if version is not None:
            self.version = version
        if extend_param is not None:
            self.extend_param = extend_param

    @property
    def id(self):
        r"""Gets the id of this Spec.

        微服务引擎CCE规格ID

        :return: The id of this Spec.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Spec.

        微服务引擎CCE规格ID

        :param id: The id of this Spec.
        :type id: int
        """
        self._id = id

    @property
    def engine_id(self):
        r"""Gets the engine_id of this Spec.

        微服务引擎ID

        :return: The engine_id of this Spec.
        :rtype: str
        """
        return self._engine_id

    @engine_id.setter
    def engine_id(self, engine_id):
        r"""Sets the engine_id of this Spec.

        微服务引擎ID

        :param engine_id: The engine_id of this Spec.
        :type engine_id: str
        """
        self._engine_id = engine_id

    @property
    def spec_type(self):
        r"""Gets the spec_type of this Spec.

        微服务引擎的集群部署类型

        :return: The spec_type of this Spec.
        :rtype: str
        """
        return self._spec_type

    @spec_type.setter
    def spec_type(self, spec_type):
        r"""Sets the spec_type of this Spec.

        微服务引擎的集群部署类型

        :param spec_type: The spec_type of this Spec.
        :type spec_type: str
        """
        self._spec_type = spec_type

    @property
    def cluster(self):
        r"""Gets the cluster of this Spec.

        微服务引擎的CCE集群信息，目前为null

        :return: The cluster of this Spec.
        :rtype: str
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        r"""Sets the cluster of this Spec.

        微服务引擎的CCE集群信息，目前为null

        :param cluster: The cluster of this Spec.
        :type cluster: str
        """
        self._cluster = cluster

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this Spec.

        微服务引擎的CCE集群ID

        :return: The cluster_id of this Spec.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this Spec.

        微服务引擎的CCE集群ID

        :param cluster_id: The cluster_id of this Spec.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_nodes(self):
        r"""Gets the cluster_nodes of this Spec.

        :return: The cluster_nodes of this Spec.
        :rtype: :class:`huaweicloudsdkcse.v1.SpecClusterNode`
        """
        return self._cluster_nodes

    @cluster_nodes.setter
    def cluster_nodes(self, cluster_nodes):
        r"""Sets the cluster_nodes of this Spec.

        :param cluster_nodes: The cluster_nodes of this Spec.
        :type cluster_nodes: :class:`huaweicloudsdkcse.v1.SpecClusterNode`
        """
        self._cluster_nodes = cluster_nodes

    @property
    def flavor(self):
        r"""Gets the flavor of this Spec.

        微服务引擎的CCE集群规格

        :return: The flavor of this Spec.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this Spec.

        微服务引擎的CCE集群规格

        :param flavor: The flavor of this Spec.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def region(self):
        r"""Gets the region of this Spec.

        微服务引擎的CCE集群所在region

        :return: The region of this Spec.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this Spec.

        微服务引擎的CCE集群所在region

        :param region: The region of this Spec.
        :type region: str
        """
        self._region = region

    @property
    def version(self):
        r"""Gets the version of this Spec.

        微服务引擎的CCE集群版本

        :return: The version of this Spec.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this Spec.

        微服务引擎的CCE集群版本

        :param version: The version of this Spec.
        :type version: str
        """
        self._version = version

    @property
    def extend_param(self):
        r"""Gets the extend_param of this Spec.

        微服务引擎的CCE集群附加参数

        :return: The extend_param of this Spec.
        :rtype: str
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        r"""Sets the extend_param of this Spec.

        微服务引擎的CCE集群附加参数

        :param extend_param: The extend_param of this Spec.
        :type extend_param: str
        """
        self._extend_param = extend_param

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
        if not isinstance(other, Spec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
