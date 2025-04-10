# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CCEClusterInfo:

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
        'cluster_platform_type': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'cluster_platform_type': 'cluster_platform_type'
    }

    def __init__(self, cluster_id=None, cluster_name=None, cluster_platform_type=None):
        r"""CCEClusterInfo

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID
        :type cluster_id: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param cluster_platform_type: 集群CPU架构类型：X86（VirtualMachine），ARM（ARM64）
        :type cluster_platform_type: str
        """
        
        

        self._cluster_id = None
        self._cluster_name = None
        self._cluster_platform_type = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.cluster_platform_type = cluster_platform_type

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this CCEClusterInfo.

        集群ID

        :return: The cluster_id of this CCEClusterInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this CCEClusterInfo.

        集群ID

        :param cluster_id: The cluster_id of this CCEClusterInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this CCEClusterInfo.

        集群名称

        :return: The cluster_name of this CCEClusterInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this CCEClusterInfo.

        集群名称

        :param cluster_name: The cluster_name of this CCEClusterInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_platform_type(self):
        r"""Gets the cluster_platform_type of this CCEClusterInfo.

        集群CPU架构类型：X86（VirtualMachine），ARM（ARM64）

        :return: The cluster_platform_type of this CCEClusterInfo.
        :rtype: str
        """
        return self._cluster_platform_type

    @cluster_platform_type.setter
    def cluster_platform_type(self, cluster_platform_type):
        r"""Sets the cluster_platform_type of this CCEClusterInfo.

        集群CPU架构类型：X86（VirtualMachine），ARM（ARM64）

        :param cluster_platform_type: The cluster_platform_type of this CCEClusterInfo.
        :type cluster_platform_type: str
        """
        self._cluster_platform_type = cluster_platform_type

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
        if not isinstance(other, CCEClusterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
