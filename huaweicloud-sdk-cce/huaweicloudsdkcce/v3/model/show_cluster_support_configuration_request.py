# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterSupportConfigurationRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_type': 'str',
        'cluster_version': 'str',
        'cluster_id': 'str',
        'network_mode': 'str'
    }

    attribute_map = {
        'cluster_type': 'clusterType',
        'cluster_version': 'clusterVersion',
        'cluster_id': 'clusterID',
        'network_mode': 'networkMode'
    }

    def __init__(self, cluster_type=None, cluster_version=None, cluster_id=None, network_mode=None):
        r"""ShowClusterSupportConfigurationRequest

        The model defined in huaweicloud sdk

        :param cluster_type: **参数解释**： 该参数用于过滤集群架构 **约束限制**： 不涉及 **取值范围**： - ARM64: 仅获取鲲鹏集群支持的配置项  **默认取值**： 不涉及
        :type cluster_type: str
        :param cluster_version: **参数解释**： 该参数用于获取指定集群版本支持的配置项 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type cluster_version: str
        :param cluster_id: **参数解释**： 该参数用于获取指定集群支持的配置项 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及
        :type cluster_id: str
        :param network_mode: **参数解释**： 该参数用于过滤掉集群网络模型相关配置项 **约束限制**： 不涉及 **取值范围**： - eni: 过滤掉云原生网络2.0模型相关配置  **默认取值**： 不涉及
        :type network_mode: str
        """
        
        

        self._cluster_type = None
        self._cluster_version = None
        self._cluster_id = None
        self._network_mode = None
        self.discriminator = None

        if cluster_type is not None:
            self.cluster_type = cluster_type
        if cluster_version is not None:
            self.cluster_version = cluster_version
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if network_mode is not None:
            self.network_mode = network_mode

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this ShowClusterSupportConfigurationRequest.

        **参数解释**： 该参数用于过滤集群架构 **约束限制**： 不涉及 **取值范围**： - ARM64: 仅获取鲲鹏集群支持的配置项  **默认取值**： 不涉及

        :return: The cluster_type of this ShowClusterSupportConfigurationRequest.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this ShowClusterSupportConfigurationRequest.

        **参数解释**： 该参数用于过滤集群架构 **约束限制**： 不涉及 **取值范围**： - ARM64: 仅获取鲲鹏集群支持的配置项  **默认取值**： 不涉及

        :param cluster_type: The cluster_type of this ShowClusterSupportConfigurationRequest.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def cluster_version(self):
        r"""Gets the cluster_version of this ShowClusterSupportConfigurationRequest.

        **参数解释**： 该参数用于获取指定集群版本支持的配置项 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The cluster_version of this ShowClusterSupportConfigurationRequest.
        :rtype: str
        """
        return self._cluster_version

    @cluster_version.setter
    def cluster_version(self, cluster_version):
        r"""Sets the cluster_version of this ShowClusterSupportConfigurationRequest.

        **参数解释**： 该参数用于获取指定集群版本支持的配置项 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param cluster_version: The cluster_version of this ShowClusterSupportConfigurationRequest.
        :type cluster_version: str
        """
        self._cluster_version = cluster_version

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShowClusterSupportConfigurationRequest.

        **参数解释**： 该参数用于获取指定集群支持的配置项 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :return: The cluster_id of this ShowClusterSupportConfigurationRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShowClusterSupportConfigurationRequest.

        **参数解释**： 该参数用于获取指定集群支持的配置项 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及

        :param cluster_id: The cluster_id of this ShowClusterSupportConfigurationRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def network_mode(self):
        r"""Gets the network_mode of this ShowClusterSupportConfigurationRequest.

        **参数解释**： 该参数用于过滤掉集群网络模型相关配置项 **约束限制**： 不涉及 **取值范围**： - eni: 过滤掉云原生网络2.0模型相关配置  **默认取值**： 不涉及

        :return: The network_mode of this ShowClusterSupportConfigurationRequest.
        :rtype: str
        """
        return self._network_mode

    @network_mode.setter
    def network_mode(self, network_mode):
        r"""Sets the network_mode of this ShowClusterSupportConfigurationRequest.

        **参数解释**： 该参数用于过滤掉集群网络模型相关配置项 **约束限制**： 不涉及 **取值范围**： - eni: 过滤掉云原生网络2.0模型相关配置  **默认取值**： 不涉及

        :param network_mode: The network_mode of this ShowClusterSupportConfigurationRequest.
        :type network_mode: str
        """
        self._network_mode = network_mode

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
        if not isinstance(other, ShowClusterSupportConfigurationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
