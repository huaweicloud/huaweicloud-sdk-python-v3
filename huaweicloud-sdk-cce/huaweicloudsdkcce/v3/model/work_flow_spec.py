# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkFlowSpec:

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
        'cluster_version': 'str',
        'target_version': 'str'
    }

    attribute_map = {
        'cluster_id': 'clusterID',
        'cluster_version': 'clusterVersion',
        'target_version': 'targetVersion'
    }

    def __init__(self, cluster_id=None, cluster_version=None, target_version=None):
        r"""WorkFlowSpec

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID，资源唯一标识，创建成功后自动生成，填写无效
        :type cluster_id: str
        :param cluster_version: 本次集群升级的当前版本 
        :type cluster_version: str
        :param target_version: 本次集群升级的目标版本 
        :type target_version: str
        """
        
        

        self._cluster_id = None
        self._cluster_version = None
        self._target_version = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_version is not None:
            self.cluster_version = cluster_version
        self.target_version = target_version

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this WorkFlowSpec.

        集群ID，资源唯一标识，创建成功后自动生成，填写无效

        :return: The cluster_id of this WorkFlowSpec.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this WorkFlowSpec.

        集群ID，资源唯一标识，创建成功后自动生成，填写无效

        :param cluster_id: The cluster_id of this WorkFlowSpec.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_version(self):
        r"""Gets the cluster_version of this WorkFlowSpec.

        本次集群升级的当前版本 

        :return: The cluster_version of this WorkFlowSpec.
        :rtype: str
        """
        return self._cluster_version

    @cluster_version.setter
    def cluster_version(self, cluster_version):
        r"""Sets the cluster_version of this WorkFlowSpec.

        本次集群升级的当前版本 

        :param cluster_version: The cluster_version of this WorkFlowSpec.
        :type cluster_version: str
        """
        self._cluster_version = cluster_version

    @property
    def target_version(self):
        r"""Gets the target_version of this WorkFlowSpec.

        本次集群升级的目标版本 

        :return: The target_version of this WorkFlowSpec.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        r"""Sets the target_version of this WorkFlowSpec.

        本次集群升级的目标版本 

        :param target_version: The target_version of this WorkFlowSpec.
        :type target_version: str
        """
        self._target_version = target_version

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
        if not isinstance(other, WorkFlowSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
