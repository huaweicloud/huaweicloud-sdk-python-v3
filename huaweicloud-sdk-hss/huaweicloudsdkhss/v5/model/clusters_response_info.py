# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClustersResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'cluster_name': 'str',
        'cluster_type': 'str',
        'version': 'str',
        'mode': 'str',
        'namespace_num': 'int',
        'policy_num': 'int',
        'protection_status': 'bool'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'cluster_type': 'cluster_type',
        'version': 'version',
        'mode': 'mode',
        'namespace_num': 'namespace_num',
        'policy_num': 'policy_num',
        'protection_status': 'protection_status'
    }

    def __init__(self, cluster_id=None, cluster_name=None, cluster_type=None, version=None, mode=None, namespace_num=None, policy_num=None, protection_status=None):
        r"""ClustersResponseInfo

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID
        :type cluster_id: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param cluster_type: 集群类型:   - cce：cce集群   - k8s：k8s集群    - ali：阿里云集群   - tencent：腾讯云集群   - azure：微软云集群   - aws：亚马逊集群   - self_built_hw：华为云自建集群   - self_built_idc：IDC自建集群
        :type cluster_type: str
        :param version: 集群版本
        :type version: str
        :param mode: 网络模型:   - overlay_l2：容器隧道网络   - vpc-router：VPC网络   - eni：云原生网络2.0   - native-network：K8S原生网络
        :type mode: str
        :param namespace_num: 命名空间数
        :type namespace_num: int
        :param policy_num: 策略数量
        :type policy_num: int
        :param protection_status: 防护状态：true、false
        :type protection_status: bool
        """
        
        

        self._cluster_id = None
        self._cluster_name = None
        self._cluster_type = None
        self._version = None
        self._mode = None
        self._namespace_num = None
        self._policy_num = None
        self._protection_status = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if version is not None:
            self.version = version
        if mode is not None:
            self.mode = mode
        if namespace_num is not None:
            self.namespace_num = namespace_num
        if policy_num is not None:
            self.policy_num = policy_num
        if protection_status is not None:
            self.protection_status = protection_status

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ClustersResponseInfo.

        集群ID

        :return: The cluster_id of this ClustersResponseInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ClustersResponseInfo.

        集群ID

        :param cluster_id: The cluster_id of this ClustersResponseInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ClustersResponseInfo.

        集群名称

        :return: The cluster_name of this ClustersResponseInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ClustersResponseInfo.

        集群名称

        :param cluster_name: The cluster_name of this ClustersResponseInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this ClustersResponseInfo.

        集群类型:   - cce：cce集群   - k8s：k8s集群    - ali：阿里云集群   - tencent：腾讯云集群   - azure：微软云集群   - aws：亚马逊集群   - self_built_hw：华为云自建集群   - self_built_idc：IDC自建集群

        :return: The cluster_type of this ClustersResponseInfo.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this ClustersResponseInfo.

        集群类型:   - cce：cce集群   - k8s：k8s集群    - ali：阿里云集群   - tencent：腾讯云集群   - azure：微软云集群   - aws：亚马逊集群   - self_built_hw：华为云自建集群   - self_built_idc：IDC自建集群

        :param cluster_type: The cluster_type of this ClustersResponseInfo.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def version(self):
        r"""Gets the version of this ClustersResponseInfo.

        集群版本

        :return: The version of this ClustersResponseInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ClustersResponseInfo.

        集群版本

        :param version: The version of this ClustersResponseInfo.
        :type version: str
        """
        self._version = version

    @property
    def mode(self):
        r"""Gets the mode of this ClustersResponseInfo.

        网络模型:   - overlay_l2：容器隧道网络   - vpc-router：VPC网络   - eni：云原生网络2.0   - native-network：K8S原生网络

        :return: The mode of this ClustersResponseInfo.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this ClustersResponseInfo.

        网络模型:   - overlay_l2：容器隧道网络   - vpc-router：VPC网络   - eni：云原生网络2.0   - native-network：K8S原生网络

        :param mode: The mode of this ClustersResponseInfo.
        :type mode: str
        """
        self._mode = mode

    @property
    def namespace_num(self):
        r"""Gets the namespace_num of this ClustersResponseInfo.

        命名空间数

        :return: The namespace_num of this ClustersResponseInfo.
        :rtype: int
        """
        return self._namespace_num

    @namespace_num.setter
    def namespace_num(self, namespace_num):
        r"""Sets the namespace_num of this ClustersResponseInfo.

        命名空间数

        :param namespace_num: The namespace_num of this ClustersResponseInfo.
        :type namespace_num: int
        """
        self._namespace_num = namespace_num

    @property
    def policy_num(self):
        r"""Gets the policy_num of this ClustersResponseInfo.

        策略数量

        :return: The policy_num of this ClustersResponseInfo.
        :rtype: int
        """
        return self._policy_num

    @policy_num.setter
    def policy_num(self, policy_num):
        r"""Sets the policy_num of this ClustersResponseInfo.

        策略数量

        :param policy_num: The policy_num of this ClustersResponseInfo.
        :type policy_num: int
        """
        self._policy_num = policy_num

    @property
    def protection_status(self):
        r"""Gets the protection_status of this ClustersResponseInfo.

        防护状态：true、false

        :return: The protection_status of this ClustersResponseInfo.
        :rtype: bool
        """
        return self._protection_status

    @protection_status.setter
    def protection_status(self, protection_status):
        r"""Sets the protection_status of this ClustersResponseInfo.

        防护状态：true、false

        :param protection_status: The protection_status of this ClustersResponseInfo.
        :type protection_status: bool
        """
        self._protection_status = protection_status

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
        if not isinstance(other, ClustersResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
