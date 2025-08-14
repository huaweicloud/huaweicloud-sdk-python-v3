# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_name': 'str',
        'cluster_id': 'str',
        'cluster_version': 'str',
        'protect_status': 'str',
        'policy_num': 'int',
        'cluster_status': 'str',
        'cluster_type': 'str'
    }

    attribute_map = {
        'cluster_name': 'cluster_name',
        'cluster_id': 'cluster_id',
        'cluster_version': 'cluster_version',
        'protect_status': 'protect_status',
        'policy_num': 'policy_num',
        'cluster_status': 'cluster_status',
        'cluster_type': 'cluster_type'
    }

    def __init__(self, cluster_name=None, cluster_id=None, cluster_version=None, protect_status=None, policy_num=None, cluster_status=None, cluster_type=None):
        r"""ClusterResponseInfo

        The model defined in huaweicloud sdk

        :param cluster_name: 集群名称
        :type cluster_name: str
        :param cluster_id: 集群ID
        :type cluster_id: str
        :param cluster_version: 集群版本
        :type cluster_version: str
        :param protect_status: 防护状态 - unprotected - plugin error - protected with policy - deploy policy failed - protected without policy - uninstall failed - uninstall
        :type protect_status: str
        :param policy_num: 策略数量
        :type policy_num: int
        :param cluster_status: 集群运行状态 - Available - Unavailable
        :type cluster_status: str
        :param cluster_type: 集群类型，包含以下几种： - k8s：原生集群 - cce：CCE集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群
        :type cluster_type: str
        """
        
        

        self._cluster_name = None
        self._cluster_id = None
        self._cluster_version = None
        self._protect_status = None
        self._policy_num = None
        self._cluster_status = None
        self._cluster_type = None
        self.discriminator = None

        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_version is not None:
            self.cluster_version = cluster_version
        if protect_status is not None:
            self.protect_status = protect_status
        if policy_num is not None:
            self.policy_num = policy_num
        if cluster_status is not None:
            self.cluster_status = cluster_status
        if cluster_type is not None:
            self.cluster_type = cluster_type

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ClusterResponseInfo.

        集群名称

        :return: The cluster_name of this ClusterResponseInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ClusterResponseInfo.

        集群名称

        :param cluster_name: The cluster_name of this ClusterResponseInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ClusterResponseInfo.

        集群ID

        :return: The cluster_id of this ClusterResponseInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ClusterResponseInfo.

        集群ID

        :param cluster_id: The cluster_id of this ClusterResponseInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_version(self):
        r"""Gets the cluster_version of this ClusterResponseInfo.

        集群版本

        :return: The cluster_version of this ClusterResponseInfo.
        :rtype: str
        """
        return self._cluster_version

    @cluster_version.setter
    def cluster_version(self, cluster_version):
        r"""Sets the cluster_version of this ClusterResponseInfo.

        集群版本

        :param cluster_version: The cluster_version of this ClusterResponseInfo.
        :type cluster_version: str
        """
        self._cluster_version = cluster_version

    @property
    def protect_status(self):
        r"""Gets the protect_status of this ClusterResponseInfo.

        防护状态 - unprotected - plugin error - protected with policy - deploy policy failed - protected without policy - uninstall failed - uninstall

        :return: The protect_status of this ClusterResponseInfo.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this ClusterResponseInfo.

        防护状态 - unprotected - plugin error - protected with policy - deploy policy failed - protected without policy - uninstall failed - uninstall

        :param protect_status: The protect_status of this ClusterResponseInfo.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def policy_num(self):
        r"""Gets the policy_num of this ClusterResponseInfo.

        策略数量

        :return: The policy_num of this ClusterResponseInfo.
        :rtype: int
        """
        return self._policy_num

    @policy_num.setter
    def policy_num(self, policy_num):
        r"""Sets the policy_num of this ClusterResponseInfo.

        策略数量

        :param policy_num: The policy_num of this ClusterResponseInfo.
        :type policy_num: int
        """
        self._policy_num = policy_num

    @property
    def cluster_status(self):
        r"""Gets the cluster_status of this ClusterResponseInfo.

        集群运行状态 - Available - Unavailable

        :return: The cluster_status of this ClusterResponseInfo.
        :rtype: str
        """
        return self._cluster_status

    @cluster_status.setter
    def cluster_status(self, cluster_status):
        r"""Sets the cluster_status of this ClusterResponseInfo.

        集群运行状态 - Available - Unavailable

        :param cluster_status: The cluster_status of this ClusterResponseInfo.
        :type cluster_status: str
        """
        self._cluster_status = cluster_status

    @property
    def cluster_type(self):
        r"""Gets the cluster_type of this ClusterResponseInfo.

        集群类型，包含以下几种： - k8s：原生集群 - cce：CCE集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群

        :return: The cluster_type of this ClusterResponseInfo.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        r"""Sets the cluster_type of this ClusterResponseInfo.

        集群类型，包含以下几种： - k8s：原生集群 - cce：CCE集群 - ali：阿里云集群 - tencent：腾讯云集群 - azure：微软云集群 - aws：亚马逊集群 - self_built_hw：华为云自建集群 - self_built_idc：IDC自建集群

        :param cluster_type: The cluster_type of this ClusterResponseInfo.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

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
        if not isinstance(other, ClusterResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
